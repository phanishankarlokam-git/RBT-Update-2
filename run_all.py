#!/usr/bin/env python3
"""
One command that produces every number in Update 2.

    python run_all.py                         # score everything, write results/
    python run_all.py --pptx Browser.pptx     # also check the answer-set files against the slides

What it does, requirement by requirement (B2, B5, ... B23):
  1. reads the answer set (data/answer_set/Bx.dot + Bx.yaml)
  2. reads every run it can find (data/runs/<source>/Bx/runN.dot + runN-TCs.txt)
  3. matches labels (strict and lenient), then
  4. counts L1 nodes, L2 arrows, L3 tests, L4 sparkles for each run, and
  5. writes results/summary.csv, results/summary.xlsx and one audit file per run.

It also scores the answer set against itself ("answer-set" rows): its own paths are
generated the way a path-coverage tool would do it. Those rows show the best score any
path-based generator could reach, because the graph is perfect.
"""
import argparse
import glob
import os
import re
import sys

import yaml

from coverage.answer_set import load as load_answer_set, check_against_pptx
from coverage.graph import load_dot, enumerate_paths
from coverage.paths import parse_paths, paths_from_enumeration
from coverage.mapping import Meaning, load_aliases
from coverage.metrics import level1, level2, level3, level4
from coverage import report

MODES = ("strict", "lenient")


def req_order(rid):
    return int(re.sub(r"\D", "", rid) or 0)


def score(ref, spec, tg, paths, aliases, judgements, rid, run_key):
    out = {}
    for mode in MODES:
        m = Meaning(ref, tg, mode, aliases, rid, run_key)
        out[mode] = (level1(ref, tg, m), level2(ref, tg, m), level3(spec, paths, m),
                     level4(ref, spec, tg, m, judgements, run_key))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default="results")
    ap.add_argument("--pptx", default=None, help="Browser.pptx, to check the answer-set files against the slides")
    args = ap.parse_args()

    ans_dir = os.path.join(args.data, "answer_set")
    os.makedirs(os.path.join(args.out, "audit"), exist_ok=True)
    aliases = load_aliases(os.path.join(args.data, "aliases.yaml"))
    jl = yaml.safe_load(open(os.path.join(args.data, "judgements.yaml"), encoding="utf-8")) or []
    judgements = {(j["requirement"], j["run"], j["sparkle"]): j for j in jl}

    rids = sorted((os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ans_dir, "B*.yaml"))), key=req_order)
    rows, profile = [], []
    for rid in rids:
        ref, spec = load_answer_set(ans_dir, rid)

        # the answer set scored against itself (perfect graph, paths enumerated automatically)
        base_paths = paths_from_enumeration(enumerate_paths(ref), ref)
        res = score(ref, spec, ref, base_paths, aliases, judgements, rid, "answer-set")
        for mode in MODES:
            rows.append(report.row_for(rid, "answer-set", "enumerated", mode, *res[mode]))
        report.write_audit(os.path.join(args.out, "audit", f"{rid}-answer-set.md"),
                           f"{rid}: the answer set scored against itself", ref, spec, ref, base_paths, res)

        tcs = spec["test_cases"]
        profile.append({
            "requirement": rid,
            "answer_nodes": res["strict"][0]["n_ref"],
            "answer_arrow_pairs": res["strict"][1]["n_ref"],
            "test_cases": len(tcs),
            "routes": res["strict"][2]["n_routes"],
            "relational_test_cases": len(res["strict"][2]["relational"]),
            "sparkles": len(spec["sparkles"]),
            "manual_sparkles": sum(1 for s in spec["sparkles"] if s["check"]["type"] == "manual"),
            "enumerated_paths": len(base_paths),
            "baseline_L3_recall": res["strict"][2]["recall"],
            "baseline_L3_precision": res["strict"][2]["precision"],
            "baseline_test_cases_covered": len(res["strict"][2]["tc_covered"]),
        })

        # every generated run found on disk
        for source in sorted(os.listdir(os.path.join(args.data, "runs"))):
            rdir = os.path.join(args.data, "runs", source, rid)
            if not os.path.isdir(rdir):
                continue
            for dot in sorted(glob.glob(os.path.join(rdir, "run*.dot")),
                              key=lambda p: int(re.sub(r"\D", "", os.path.basename(p)) or 0)):
                run = os.path.basename(dot)[:-4]
                tcs_path = os.path.join(rdir, f"{run}-TCs.txt")
                tg = load_dot(dot)
                text = open(tcs_path, encoding="utf-8").read() if os.path.exists(tcs_path) else ""
                paths = parse_paths(text, tg)
                key = f"{source}/{run}"
                res = score(ref, spec, tg, paths, aliases, judgements, rid, key)
                for mode in MODES:
                    rows.append(report.row_for(rid, source, run, mode, *res[mode]))
                report.write_audit(os.path.join(args.out, "audit", f"{rid}-{source}-{run}.md"),
                                   f"{rid}, {source} {run}", ref, spec, tg, paths, res)

    report.write_csv(rows, os.path.join(args.out, "summary.csv"))
    report.write_xlsx(rows, os.path.join(args.out, "summary.xlsx"))
    with open(os.path.join(args.out, "answer_set_profile.csv"), "w", encoding="utf-8") as f:
        f.write(",".join(profile[0].keys()) + "\n")
        for p in profile:
            f.write(",".join(str(round(v, 4) if isinstance(v, float) else v) for v in p.values()) + "\n")

    if args.pptx:
        diffs = check_against_pptx(args.pptx, ans_dir, rids)
        with open(os.path.join(args.out, "answer_set_check.txt"), "w", encoding="utf-8") as f:
            f.write("Differences between the answer-set files and Browser.pptx\n")
            f.write("\n".join(diffs) if diffs else "None: every shape and arrow label on the slides is encoded.")
            f.write("\n")
        print(f"answer-set check: {len(diffs)} difference(s), see {args.out}/answer_set_check.txt")

    print(f"{len(rows)} result rows for {len(rids)} requirements written to {args.out}/")
    for r in rows:
        if r["mode"] == "strict" and r["source"] != "pilot":
            print(f"  {r['requirement']:4} {r['source']:10} {r['run']:10} "
                  f"L1 F1 {report.pct(r['L1_f1']):>5}  L2 F1 {report.pct(r['L2_f1']):>5}  "
                  f"L3 R {report.pct(r['L3_recall']):>5} P {report.pct(r['L3_precision']):>5}  "
                  f"TC {r['test_cases_covered']}/{r['test_cases_total']}  L4 {r['L4_met']}/{r['L4_total']}")


if __name__ == "__main__":
    sys.exit(main())
