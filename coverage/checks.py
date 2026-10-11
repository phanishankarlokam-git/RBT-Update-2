"""
LEVEL 4: the "sparkles" (expert modelling decisions listed in the answer-set notes).

Each sparkle in data/answer_set/B*.yaml has a `check`: a small mechanical test that is
run on the generated graph. The check types are:

  concepts        the graph has a node for each listed answer-set node
  uses_term       some node label contains every word of the answer-set term (e.g. "HTML Display Zone")
  no_word         no node label contains this word (B11: "do NOT model Browser")
  fanout          some node or bar splits into at least `min` of the listed nodes
                  (optionally: right after an arrow/step carrying the word in `after`)
  fanin           some node or bar joins at least `min` of the listed nodes
                  (optionally: and then leads on to `then`)
  composition     at least `min` listed parts hang off one whole with composition notation
                  (a diamond arrow, or an arrow labelled contains/has/consists of ...);
                  in lenient mode a Graphviz box holding the parts also counts
  optional_child  a node for "other / optional / additional / extra" items is reachable from the whole
  label_has       the node for X has one of the given marks in its label (e.g. "<--")
  text_has        some text in the graph has a word from every listed group
  entry_states    the listed nodes are where the graph starts
  shared_target   exactly one node for X, and it is reached both after `after[0]` and `after[1]`
  converge        exactly one node for X, reached from both triggers in `after`
  precedes        X comes before the step carrying the word in `then`, never after it
  in_split        X is one branch of a split
  sequence        X is done before Y (an arrow path X -> ... -> Y, or a bar marked sequential)
  manual          judged by a person; the verdict and reason are in data/judgements.yaml
"""
from .labels import words, stem, is_exact, similarity, contains_all, clean_text, is_negated, THRESHOLD

COMPOSITION_WORDS = {"contain", "consist", "has", "have", "includ", "compos", "part", "compris", "made"}
OPTIONAL_MARKS = ["other", "optional", "additional", "extra"]


class Ctx:
    def __init__(self, ref, tg, meaning, mode, judgements, key):
        self.ref, self.tg, self.meaning, self.mode = ref, tg, meaning, mode
        self.G = tg.network(use_boxes=(mode == "lenient"))
        self.judgements, self.key = judgements, key
        self.mean = {g: meaning.of_network_node(g) for g in self.G.nodes}

    def nodes_for(self, rid):
        return [g for g, m in self.mean.items() if rid in m]

    def role(self, g):
        return self.G.nodes[g].get("role", "concept")

    def label(self, g):
        return self.G.nodes[g].get("label", "") or ""

    def succ(self, g):
        """Successors, looking through unlabelled bars and nodes that stand for nothing only once."""
        out = set()
        for w in self.G.successors(g):
            if w == g:
                continue
            out.add(w)
            if self.role(w) in ("bar", "start") or (not self.mean.get(w) and not self.label(w).strip()):
                out |= {x for x in self.G.successors(w) if x != w}
        return out

    def pred(self, g):
        out = set()
        for w in self.G.predecessors(g):
            if w == g:
                continue
            out.add(w)
            if self.role(w) in ("bar", "start") or (not self.mean.get(w) and not self.label(w).strip()):
                out |= {x for x in self.G.predecessors(w) if x != w}
        return out

    def reach(self, a, b):
        import networkx as nx
        return a in self.G and b in self.G and nx.has_path(self.G, a, b)

    def after_points(self, text):
        """Graph nodes that come right after something carrying `text` (an arrow label or a node label)."""
        pts = set()
        for u, v, d in self.G.edges(data=True):
            lab = d.get("label") or ""
            if lab and (similarity(text, lab) >= THRESHOLD or contains_all(text, lab)):
                pts.add(v)
        for g in self.G.nodes:
            lab = self.label(g)
            if lab and not lab.strip().endswith("?") and (similarity(text, lab) >= THRESHOLD or contains_all(text, lab)):
                pts.add(g)                     # a node that itself carries the word (e.g. "Click OK")
        return pts

    def all_texts(self):
        t = [self.label(g) for g in self.G.nodes] + list(self.tg.texts)
        t += [d.get("label") or "" for _, _, d in self.G.edges(data=True)]
        return [x for x in t if x]


def _fanout_nodes(c, targets, min_n):
    """Nodes that split: at least two different next nodes, together reaching >= min_n targets.
    (One next node that happens to stand for two things is not a split.)"""
    hits = []
    for g in c.G.nodes:
        reached, via = set(), set()
        for w in c.succ(g):
            got = c.mean.get(w, set()) & set(targets)
            if got:
                reached |= got
                via.add(w)
        if len(reached) >= min_n and len(via) >= 2:
            hits.append((g, reached))
    return hits


def run_check(check, c):
    t = check["type"]
    if t == "concepts":
        missing = [r for r in check["nodes"] if not c.nodes_for(r)]
        return (not missing), ("all present" if not missing else "missing: " + ", ".join(missing))
    if t == "uses_term":
        ids = check["node"] if isinstance(check["node"], list) else [check["node"]]
        bad = []
        for rid in ids:
            want = c.ref.nodes[rid].label
            if not any(contains_all(want, c.label(g)) for g in c.G.nodes if c.role(g) == "concept"):
                bad.append(want)
        return (not bad), ("term used" if not bad else "term not used: " + "; ".join(bad))
    if t == "exact_label":
        ids = check["node"] if isinstance(check["node"], list) else [check["node"]]
        bad = []
        for rid in ids:
            want = c.ref.nodes[rid].label
            if not any(is_exact(want, c.label(g)) for g in c.G.nodes if c.role(g) == "concept"):
                bad.append(want)
        return (not bad), ("same wording used" if not bad else "wording differs for: " + "; ".join(bad))
    if t == "no_word":
        w = stem(check["word"].lower())
        used = [c.label(g) for g in c.G.nodes if c.role(g) == "concept" and w in words(c.label(g))]
        return (not used), ("not used" if not used else "used in: " + "; ".join(used))
    if t == "fanout":
        hits = _fanout_nodes(c, check["targets"], check.get("min", 2))
        if check.get("after"):
            pts = c.after_points(check["after"])
            hits = [h for h in hits if h[0] in pts]
        if hits:
            g, reached = hits[0]
            return True, f"'{c.label(g) or '[bar]'}' splits into {sorted(reached)}"
        return False, "no split into the required nodes" + (f" after '{check['after']}'" if check.get("after") else "")
    if t == "fanin":
        srcs, min_n = set(check["sources"]), check.get("min", 2)
        for g in c.G.nodes:
            came, via = set(), set()
            for w in c.pred(g):
                got = c.mean.get(w, set()) & srcs
                if got:
                    came |= got
                    via.add(w)
            if len(came) >= min_n and len(via) >= 2:
                if check.get("then"):
                    goal = c.nodes_for(check["then"])
                    if not any(c.reach(g, x) for x in goal):
                        continue
                return True, f"'{c.label(g) or '[bar]'}' joins {sorted(came)}"
        return False, "no join of the required nodes" + (f" leading to {check['then']}" if check.get("then") else "")
    if t == "composition":
        parts, min_n = set(check["parts"]), check.get("min", 2)
        by_src = {}
        for u, v, d in c.G.edges(data=True):
            styled = d.get("kind") == "composition"
            e_attrs = {}
            for e in c.tg.edges:
                if e.u == u and e.v == v:
                    e_attrs = e.attrs
                    break
            if "diamond" in (e_attrs.get("arrowhead", "") + e_attrs.get("arrowtail", "")).lower():
                styled = True
            if words(d.get("label") or "") & {stem(x) for x in COMPOSITION_WORDS} or \
               any(x in (d.get("label") or "").lower() for x in ("contain", "consist", "part of", "has ")):
                styled = True
            if styled:
                by_src.setdefault(u, set()).update(c.mean.get(v, set()) & parts)
        for u, got in by_src.items():
            if len(got) >= min_n:
                return True, f"composition from '{c.label(u)}' to {sorted(got)}"
        if c.mode == "lenient":
            for b in c.tg.boxes.values():
                got = set()
                for m in b.members:
                    got |= c.mean.get(m, set()) & parts
                if len(got) >= min_n:
                    return True, f"box '{b.label or b.id}' holds {sorted(got)}"
        return False, "no composition notation around the parts" + (" (boxes not counted in strict mode)" if c.mode == "strict" else "")
    if t == "optional_child":
        roots = c.nodes_for(check["whole"]) or [g for g in c.tg.initial_nodes() if g in c.G]
        import networkx as nx
        reach = set()
        for r in roots:
            reach |= nx.descendants(c.G, r) | {r}
        marks = {stem(m) for m in OPTIONAL_MARKS}
        found = sorted((c.label(g) for g in reach if words(c.label(g)) & marks),
                       key=lambda lab: (is_negated(words(lab)), lab.lower()))
        if found:
            # Sorted so that the report is the same on every run; a positive label is shown first.
            return True, f"optional items modelled as '{found[0]}'"
        return False, "no node for other/optional items"
    if t == "label_has":
        bad = []
        for rid, marks in check["nodes"].items():
            gs = c.nodes_for(rid)
            if not any(any(mk.lower() in c.label(g).lower() for mk in marks) for g in gs):
                bad.append(rid)
        return (not bad), ("marks present" if not bad else "missing for: " + ", ".join(bad))
    if t == "text_has":
        texts = [x.lower() for x in c.all_texts()]
        for x in texts:
            if all(any(w in x for w in grp) for grp in check["all_of"]):
                return True, f"found in: '{x[:70]}'"
        return False, "no such annotation"
    if t == "entry_states":
        entries = set()
        for g in c.tg.initial_nodes():
            if g in c.G:
                entries.add(g)
                if c.role(g) in ("start", "terminal", "bar"):
                    entries |= set(c.G.successors(g))
        bad = [r for r in check["nodes"] if not any(g in entries for g in c.nodes_for(r))]
        return (not bad), ("both are start states" if not bad else "not a start state: " + ", ".join(bad))
    if t in ("shared_target", "converge"):
        gs = c.nodes_for(check["node"])
        if len(gs) != 1:
            return False, f"{len(gs)} nodes stand for {check['node']} (need exactly one)"
        g = gs[0]
        missing = [a for a in check["after"] if not any(c.reach(p, g) for p in c.after_points(a))]
        return (not missing), ("one shared node reached from all branches" if not missing else "not reached after: " + ", ".join(missing))
    if t == "precedes":
        firsts = c.nodes_for(check["first"])
        then_txt = check["then"].strip("()")
        thens = c.after_points(then_txt)
        if not firsts or not thens:
            return False, "one of the two steps is missing"
        fwd = any(c.reach(f, x) for f in firsts for x in thens)
        back = any(c.reach(x, f) for f in firsts for x in thens if x not in firsts)
        return (fwd and not back), ("check comes first" if fwd and not back else "order not as required")
    if t == "in_split":
        for g in c.G.nodes:
            s = c.succ(g)
            if len(s) >= 2 and any(check["node"] in c.mean.get(w, set()) for w in s):
                return True, f"'{c.label(g) or '[bar]'}' splits and one branch is {check['node']}"
        return False, f"{check['node']} is not a branch of a split"
    if t == "sequence":
        a, b = c.nodes_for(check["first"]), c.nodes_for(check["then"])
        if any(c.reach(x, y) for x in a for y in b):
            return True, "done one after the other"
        for e1 in c.tg.edges:
            n = c.tg.nodes.get(e1.u)
            if n and n.attrs.get("bar") == "seq":
                outs = {e.v: int(e.attrs.get("order", 0) or 0) for e in c.tg.edges if e.u == e1.u}
                ia = [outs[x] for x in a if x in outs]
                ib = [outs[x] for x in b if x in outs]
                if ia and ib and min(ia) < max(ib):
                    return True, "bar marked sequential, in the right order"
        return False, "no ordering between the two"
    if t == "manual":
        verdict = c.judgements.get(c.key)
        if verdict is None:
            return False, "not judged yet (counted as not met)"
        return bool(verdict["met"]), "manual: " + verdict.get("reason", "")
    raise ValueError("unknown check type " + t)
