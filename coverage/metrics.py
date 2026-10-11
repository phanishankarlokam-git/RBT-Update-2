"""
STEP 4 of the procedure: counting. Every level uses the same three numbers.

    TP (true positives)  = items found in BOTH the generated run and the answer set
    Precision            = TP / (number of items the generator produced)
    Recall               = TP / (number of items in the answer set)
    F1                   = 2 * Precision * Recall / (Precision + Recall)

What an "item" is changes with the level:

  L1 nodes     answer-set nodes vs generated nodes (after label matching)
  L2 arrows    answer-set "A leads to B" pairs vs generated "A leads to B" pairs,
               both reduced to the nodes the two graphs share (see graph.project)
  L3 tests     answer-set ROUTES vs generated TEST PATHS.
               Recall    = routes walked by at least one generated path / all routes
                           (a test case that no path can express counts as one route never walked)
               Precision = paths NEEDED / all generated paths. "Needed" = the smallest set of
                           generated paths that still walks every route the run walks.
                           Duplicates and paths that walk no route are not needed.
  L4 sparkles  recall only: how many of the expert decisions in the notes the run makes
"""
from itertools import combinations

import networkx as nx

from .graph import project
from .labels import similarity, contains_all, THRESHOLD
from . import checks as CK


def prf(tp_pred, n_pred, tp_ref, n_ref):
    """Precision, recall, F1. If the generator produced nothing at a level, precision is 0
    (not undefined), so an empty answer never looks better than a wrong one."""
    p = tp_pred / n_pred if n_pred else 0.0
    r = tp_ref / n_ref if n_ref else None
    if r is None or (p + r) == 0:
        f = 0.0 if r is not None else None
    else:
        f = 2 * p * r / (p + r)
    return {"precision": p, "recall": r, "f1": f}


# ------------------------------------------------------------------------- L1
def level1(ref, tg, meaning):
    lenient = meaning.mode == "lenient"
    items = [("node", n.id, n.label, n.artifact) for n in tg.nodes.values() if n.role == "concept"]
    if lenient:
        items += [("box", b.id, b.label, False) for b in tg.labelled_boxes()]
    ref_ids = [n.id for n in ref.concept_nodes()]
    rows, best = [], {}
    for kind, gid, label, art in items:
        ids, how, score = (meaning.of_node(gid) if kind == "node" else meaning.of_box(gid))
        rows.append(dict(kind=kind, id=gid, label=label, artifact=art, means=sorted(ids), how=how, score=score))
        for rid in ids:
            if rid not in best or score > best[rid][1]:
                best[rid] = (gid, score)
    credited = {g for g, _ in best.values()}
    for r in rows:
        r["credited"] = r["id"] in credited and bool(r["means"])
    res = prf(len(credited), len(items), len(best), len(ref_ids))
    res.update(tp=len(best), n_gen=len(items), n_ref=len(ref_ids),
               found=sorted(best), missing=[r for r in ref_ids if r not in best],
               artifacts=sum(1 for r in rows if r["artifact"]), rows=rows)
    return res


# ------------------------------------------------------------------------- L2
def level2(ref, tg, meaning):
    RG = ref.network(use_boxes=False)
    ref_pairs = project(RG, {n.id: {n.id} for n in ref.concept_nodes()})
    GG = tg.network(use_boxes=(meaning.mode == "lenient"))
    gen_pairs = project(GG, {g: meaning.of_network_node(g) for g in GG.nodes})
    tp = ref_pairs & gen_pairs
    res = prf(len(tp), len(gen_pairs), len(tp), len(ref_pairs))
    res.update(tp=len(tp), n_gen=len(gen_pairs), n_ref=len(ref_pairs),
               matched=sorted(tp), missing=sorted(ref_pairs - gen_pairs), extra=sorted(gen_pairs - ref_pairs))
    return res


# ------------------------------------------------------------------------- L3
def _label_ok(word, step, meaning):
    """Does a step carry the event/guard word? '(a | b)' accepts either wording.
    A question node ("OK or Cancel?") never carries a guard: it asks, it does not answer."""
    if step.question:
        return False
    alts = [w.strip() for w in word.strip("()").split("|") if w.strip()]
    for lab in step.labels:
        for w in alts:
            if similarity(w, lab) >= THRESHOLD or contains_all(w, lab):
                return True
        aw = meaning.alias_words(lab)
        if any("(" + w + ")" in aw for w in alts):
            return True
    return False


def route_hit(route, steps, step_means, meaning):
    """Does this path pass the route's checkpoints in order? Returns the step indexes used, or None.
    Each checkpoint must be passed by its own step, later than the step used for the checkpoint
    before it. (So one label, e.g. "Current Page = Previous Page", can never count both as the
    guard "previous page exists" and as the outcome node.)"""
    i, used = 0, []
    for cp in route:
        is_label = cp.startswith("(")
        found = None
        for j in range(i, len(steps)):
            if is_label and _label_ok(cp, steps[j], meaning):
                found = j
                break
            if not is_label and cp in step_means[j]:
                found = j
                break
        if found is None:
            return None
        used.append(found)
        i = found + 1
    return used


def minimal_cover(n_paths, covers, targets):
    """Smallest set of paths whose routes together include every route in `targets`.
    covers[i] = set of routes walked by path i. Exact search (the runs here are small)."""
    targets = set(targets)
    if not targets:
        return []
    useful = [i for i in range(n_paths) if covers.get(i)]
    for k in range(1, len(useful) + 1):
        for combo in combinations(useful, k):
            got = set()
            for i in combo:
                got |= covers[i]
            if targets <= got:
                return list(combo)
    return useful


def level3(spec, paths, meaning):
    """spec: the loaded answer-set YAML. paths: TestPath list."""
    routes, route_tcs = [], {}
    for tc in spec["test_cases"]:
        for rt in tc.get("routes", []):
            key = tuple(rt)
            if key not in route_tcs:
                routes.append(key)
                route_tcs[key] = []
            route_tcs[key].append(tc["id"])
    relational = [tc["id"] for tc in spec["test_cases"] if tc.get("type") == "relational"]

    step_means = [[meaning.of_step(s) for s in p.steps] for p in paths]
    hits = {}
    covers = {}
    for pi, p in enumerate(paths):
        for ri, rt in enumerate(routes):
            used = route_hit(rt, p.steps, step_means[pi], meaning)
            if used is not None:
                hits[(pi, ri)] = used
                covers.setdefault(pi, set()).add(ri)
    walked = set().union(*covers.values()) if covers else set()
    needed = minimal_cover(len(paths), covers, walked)
    n_units = len(routes) + len(relational)
    res = prf(len(needed), len(paths), len(walked), n_units)

    covered_tcs = [tc["id"] for tc in spec["test_cases"]
                   if tc.get("type") != "relational" and tc.get("routes")
                   and all(routes.index(tuple(rt)) in walked for rt in tc["routes"])]
    n_tc = len(spec["test_cases"])
    sigs = [p.signature() for p in paths]
    dups = sum(1 for i, sg in enumerate(sigs) if sg in sigs[:i])
    res.update(tp=len(walked), tp_paths=len(needed), n_gen=len(paths), n_ref=n_units,
               n_routes=len(routes), relational=relational,
               walked=[routes[r] for r in sorted(walked)],
               not_walked=[routes[r] for r in range(len(routes)) if r not in walked],
               needed=[paths[i].number for i in needed],
               path_routes={paths[i].number: [routes[r] for r in sorted(covers.get(i, set()))] for i in range(len(paths))},
               hits={(paths[a].number, routes[b]): u for (a, b), u in hits.items()},
               routes=routes, route_tcs=route_tcs,
               tc_covered=covered_tcs, tc_total=n_tc,
               tc_coverage=(len(covered_tcs) / n_tc if n_tc else None),
               n_valid=sum(1 for p in paths if p.valid), n_dup=dups, step_means=step_means)
    return res


# ------------------------------------------------------------------------- L4
def level4(ref, spec, tg, meaning, judgements, run_key):
    out = []
    for sp in spec["sparkles"]:
        jkey = (spec["id"], run_key, sp["id"])
        ctx = CK.Ctx(ref, tg, meaning, meaning.mode, judgements, jkey)
        ok, why = CK.run_check(sp["check"], ctx)
        out.append(dict(id=sp["id"], notes=sp["notes"], type=sp["check"]["type"], met=ok, why=why))
    n = len(out)
    met = sum(1 for o in out if o["met"])
    return {"recall": met / n if n else None, "met": met, "n": n, "rows": out}
