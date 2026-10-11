"""
Builds the LaTeX tables used in the Update 2 report straight from results/summary.csv,
so no number in the report is typed by hand.

    python scripts/make_tables.py            (after python run_all.py)
"""
import csv
import os
import statistics as st
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results")
OUT = os.path.join(RES, "tables")
REQS = ["B2", "B5", "B7", "B11", "B12", "B15", "B16", "B19", "B20", "B23"]

rows = list(csv.DictReader(open(os.path.join(RES, "summary.csv"), encoding="utf-8")))
prof = {r["requirement"]: r for r in csv.DictReader(open(os.path.join(RES, "answer_set_profile.csv"), encoding="utf-8"))}


def get(rid, source, run, mode):
    for r in rows:
        if (r["requirement"], r["source"], r["run"], r["mode"]) == (rid, source, run, mode):
            return r
    raise KeyError((rid, source, run, mode))


def p(x):
    return f"{100 * float(x):.1f}"


def tex(t):
    """Escape text for LaTeX (and stop -- from turning into a dash)."""
    t = str(t)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                 ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\^{}")]:
        t = t.replace(a, b)
    t = t.replace("--", "-{}-").replace("<", r"\textless{}").replace(">", r"\textgreater{}")
    return t


def w(name, text):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(text)


# ------------------------------------------------------------ B2 official results
lines = []
for label, key in [("L1 nodes", "L1"), ("L2 arrows", "L2"), ("L3 tests", "L3")]:
    for mode in ("strict", "lenient"):
        cells = []
        for run in ("run1", "run2", "run3"):
            r = get("B2", "official", run, mode)
            cells.append(f"{p(r[key + '_recall'])} / {p(r[key + '_precision'])} / {p(r[key + '_f1'])}")
        lines.append(f"{label}, {mode} & " + " & ".join(cells) + r" \\")
for mode in ("strict", "lenient"):
    cells = []
    for run in ("run1", "run2", "run3"):
        r = get("B2", "official", run, mode)
        cells.append(f"{r['test_cases_covered']} of {r['test_cases_total']}")
    lines.append(f"Test cases covered, {mode} & " + " & ".join(cells) + r" \\")
for mode in ("strict", "lenient"):
    cells = []
    for run in ("run1", "run2", "run3"):
        r = get("B2", "official", run, mode)
        cells.append(f"{r['L4_met']} of {r['L4_total']} ({p(r['L4_recall'])})")
    lines.append(f"L4 sparkles, {mode} & " + " & ".join(cells) + r" \\")
cells = []
for run in ("run1", "run2", "run3"):
    r = get("B2", "official", run, "strict")
    cells.append(f"{r['L3_paths']} / {r['valid_paths']} / {r['duplicate_paths']}")
lines.append(r"\midrule" + "\nPaths (given / valid / repeated) & " + " & ".join(cells) + r" \\")
cells = []
for run in ("run1", "run2", "run3"):
    r = get("B2", "official", run, "strict")
    cells.append(f"{r['artifact_nodes']} of {r['L1_generated_nodes']}")
lines.append("Nodes named cluster\\_N & " + " & ".join(cells) + r" \\")
w("b2_results.tex", "\n".join(lines) + "\n")

# ------------------------------------------------------------ answer set scored against itself
lines = []
tot = [0, 0]
for rid in REQS:
    a = prof[rid]
    r = get(rid, "answer-set", "enumerated", "strict")
    tot[0] += int(r["test_cases_covered"])
    tot[1] += int(r["test_cases_total"])
    lines.append(f"{rid} & {a['answer_nodes']} & {a['answer_arrow_pairs']} & {a['test_cases']} & {a['routes']}"
                 f" & {a['enumerated_paths']} & {p(r['L3_recall'])} & {p(r['L3_precision'])}"
                 f" & {r['test_cases_covered']} of {r['test_cases_total']} \\\\")
lines.append(r"\midrule")
lines.append(f"All & & & {sum(int(prof[x]['test_cases']) for x in REQS)} & {sum(int(prof[x]['routes']) for x in REQS)} & "
             f"{sum(int(prof[x]['enumerated_paths']) for x in REQS)} & & & {tot[0]} of {tot[1]} \\\\")
w("answer_set.tex", "\n".join(lines) + "\n")

# ------------------------------------------------------------ pilot runs
lines = []
tots = {"strict": [0, 0, 0, 0], "lenient": [0, 0, 0, 0]}
for rid in REQS:
    cells = []
    per = {}
    for mode in ("strict", "lenient"):
        rs = [r for r in rows if r["requirement"] == rid and r["source"] == "pilot" and r["mode"] == mode]
        tc = sum(int(r["test_cases_covered"]) for r in rs), sum(int(r["test_cases_total"]) for r in rs)
        sp = sum(int(r["L4_met"]) for r in rs), sum(int(r["L4_total"]) for r in rs)
        per[mode] = dict(tc=tc, sp=sp,
                         rec=st.mean(float(r["L3_recall"]) for r in rs),
                         pre=st.mean(float(r["L3_precision"]) for r in rs),
                         n1=st.mean(float(r["L1_f1"]) for r in rs))
        t = tots[mode]
        t[0] += tc[0]; t[1] += tc[1]; t[2] += sp[0]; t[3] += sp[1]
    s, l = per["strict"], per["lenient"]
    base = get(rid, "answer-set", "enumerated", "strict")
    lines.append(f"{rid} & {p(s['n1'])} / {p(l['n1'])} & {p(s['rec'])} / {p(l['rec'])} & {p(s['pre'])} / {p(l['pre'])}"
                 f" & {s['tc'][0]} / {l['tc'][0]} of {s['tc'][1]} & {s['sp'][0]} / {l['sp'][0]} of {s['sp'][1]}"
                 f" & {int(base['test_cases_covered']) * 3} of {s['tc'][1]} \\\\")
lines.append(r"\midrule")
s, l = tots["strict"], tots["lenient"]
allb = sum(int(get(r, "answer-set", "enumerated", "strict")["test_cases_covered"]) * 3 for r in REQS)
lines.append(f"All 30 runs & & & & {s[0]} / {l[0]} of {s[1]} & {s[2]} / {l[2]} of {s[3]} & {allb} of {s[1]} \\\\")
w("pilot.tex", "\n".join(lines) + "\n")

# ------------------------------------------------------------ routes (appendix)
import re
lines = []
for rid in REQS:
    spec = yaml.safe_load(open(os.path.join(ROOT, "data", "answer_set", f"{rid}.yaml"), encoding="utf-8"))
    dot = open(os.path.join(ROOT, "data", "answer_set", f"{rid}.dot"), encoding="utf-8").read()
    labels = dict(re.findall(r'^\s*(\w+)\s+\[label="([^"]*)"', dot, re.M))
    first = True
    for tc in spec["test_cases"]:
        if tc.get("routes"):
            rts = r" \newline ".join(
                " $\\rightarrow$ ".join(
                    (r"\textit{" + tex(cp.replace(" | ", " or ")) + "}") if cp.startswith("(") else tex(labels.get(cp, cp))
                    for cp in rt) for rt in tc["routes"])
        else:
            rts = r"\textit{none: it compares two launches}"
        lines.append(f"{rid if first else ''} & {tc['id']} & {tc['type']} & {rts} \\\\")
        first = False
    lines.append(r"\midrule")
w("routes.tex", "\n".join(lines[:-1]) + "\n")

# ------------------------------------------------------------ reconciliation with Update 1
U1 = {  # values printed in Update 1, runs 1, 2, 3
    "L1s_r": [71.4, 71.4, 57.1], "L1s_p": [50.0, 55.6, 57.1],
    "L1l_r": [71.4, 100.0, 85.7], "L1l_p": [50.0, 63.6, 66.7],
    "L2r": [0.0, 100.0, 66.7], "L2p": [0.0, 42.9, 40.0],
    "L3r": [50.0, 50.0, 0.0], "L3p": [25.0, 10.0, 0.0], "L3f": [33.3, 16.7, 0.0],
    # Update 1 used the share of test cases covered (L3r) as the recall of its test-level F.
    "L4": [66.7, 66.7, 66.7],
}
R = {run: {m: get("B2", "official", run, m) for m in ("strict", "lenient")} for run in ("run1", "run2", "run3")}
runs = ("run1", "run2", "run3")
spec_rows = [
    ("Node recall, strict", "L1s_r", "strict", "L1_recall", "same"),
    ("Node precision, strict", "L1s_p", "strict", "L1_precision", "same"),
    ("Node recall, lenient", "L1l_r", "lenient", "L1_recall", "same"),
    ("Node precision, lenient", "L1l_p", "lenient", "L1_precision", "same"),
    ("Arrow recall", "L2r", "lenient", "L2_recall", "same"),
    ("Arrow precision", "L2p", "lenient", "L2_precision", "changed (a)"),
    ("Test cases covered", "L3r", "strict", "test_case_coverage", "same (b)"),
    ("Test recall used in $F$", "L3r", "strict", "L3_recall", "changed (c)"),
    ("Test precision", "L3p", "strict", "L3_precision", "changed (d)"),
    ("Test F-measure", "L3f", "strict", "L3_f1", "changed (e)"),
    ("Sparkles, strict", "L4", "strict", "L4_recall", "same"),
]
L = []
for label, uk, mode, col, note in spec_rows:
    cells = []
    for i, r in enumerate(runs):
        new_v = p(R[r][mode][col])
        old_v = f"{U1[uk][i]:.1f}"
        if new_v != old_v:
            new_v = r"\textbf{" + new_v + "}"
        cells += [old_v, new_v]
    L.append(label + " & " + " & ".join(cells) + f" & {note} \\\\")
w("reconcile.tex", "\n".join(L) + "\n")
