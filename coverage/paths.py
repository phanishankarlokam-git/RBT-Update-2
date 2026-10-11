"""
STEP 2 (second half): reading the generated test paths and laying them on the run's own graph.

A generated run gives two things: a graph (DOT) and a text list of "traversal paths".
The text is free-form, so each path line is read like this:

1. Take every numbered line ("1. A -> B -> C"). Markdown stars are removed.
2. Split it at the arrows. Labels that themselves contain an arrow (e.g. "File -> Open
   Selected") are protected first, so they are not cut in two.
3. Look up every piece in the run's own graph: a node label, a box (cluster) label or an
   arrow label. "X (via Y)" is read as "Y, then X".
4. Between two consecutive nodes, if the graph has a labelled arrow, that arrow label is
   added as a step, because it is part of what the path does (e.g. "launch browser").
5. Anything that cannot be found in the graph ("loop back") stays in the path as an
   unknown step, and the path is flagged as not valid for its own graph.
"""
import re
from dataclasses import dataclass, field

from .labels import clean_text, best_match, THRESHOLD

ARROW_SPLIT = re.compile(r"\s*(?:→|->|=>|⟶)\s*")
LINE_RE = re.compile(r"^\s*(?:[-*]\s*)?(\d+)\s*[.):]\s*(.+?)\s*$")
VIA_RE = re.compile(r"^(.*?)\s*\(\s*(?:via\s+)?(?:all\s+)?(.+?)\s*\)\s*$", re.I)


@dataclass
class Step:
    text: str
    kind: str                     # node | box | edge | unknown
    ref: object = None            # node id, box id, or None
    implicit: bool = False        # added from the graph, not written in the path
    labels: list = field(default_factory=list)
    question: bool = False        # a question node (diamond, or label ending in "?")


@dataclass
class TestPath:
    number: int
    raw: str
    steps: list
    problems: list = field(default_factory=list)

    @property
    def valid(self):
        return not self.problems

    def signature(self):
        return tuple((s.kind, s.ref if s.kind != "unknown" else clean_text(s.text))
                     for s in self.steps if not s.implicit)

    def pretty(self, tg=None):
        out = []
        for s in self.steps:
            if s.kind == "edge":
                out.append(f"({s.text})" if s.implicit else f"[{s.text}]")
            elif s.kind == "unknown":
                out.append(f"?{s.text}?")
            elif s.kind == "node" and tg is not None and not tg.nodes[s.ref].label.strip():
                out.append("[bar]")
            else:
                out.append(s.text)
        return " → ".join(out)


class _Lookup:
    def __init__(self, tg):
        self.tg = tg
        self.by_node = {}
        for n in tg.nodes.values():                       # labels first ...
            if n.role != "note" and n.label.strip():
                self.by_node.setdefault(clean_text(n.label), n.id)
        for n in tg.nodes.values():                       # ... then ids, as a fallback
            if n.role != "note":
                self.by_node.setdefault(clean_text(n.id), n.id)
        self.by_box = {clean_text(b.label): b.id for b in tg.boxes.values() if b.label.strip()}
        self.by_edge = {}
        for e in tg.edges:
            if e.label:
                self.by_edge.setdefault(clean_text(e.label), []).append(e)
        self.node_labels = {n.id: n.label for n in tg.nodes.values() if n.role in ("concept", "terminal")}

    def exact(self, text):
        c = clean_text(text)
        if not c:
            return None
        if c in self.by_node:
            nid = self.by_node[c]
            return Step(self.tg.nodes[nid].label, "node", nid)
        if c in self.by_box:
            bid = self.by_box[c]
            return Step(self.tg.boxes[bid].label, "box", bid)
        if c in self.by_edge:
            return Step(self.by_edge[c][0].label, "edge", None, labels=[self.by_edge[c][0].label])
        return None


def _members(tg, step):
    if step.kind == "node":
        return {step.ref}
    if step.kind == "box":
        return set(tg.boxes[step.ref].members)
    return set()


def _connected(tg, a, b):
    """True when the graph lets a path go from step a to step b in one move."""
    ma, mb = _members(tg, a), _members(tg, b)
    if a.kind == "box" and b.kind == "node" and b.ref in ma:
        return True                                    # from a box to one of its members
    return any(e.u in ma and e.v in mb for e in tg.edges)


def parse_paths(text, tg):
    """Read the numbered paths in `text` and lay them on graph `tg`."""
    look = _Lookup(tg)
    arrowy = sorted({lab for lab in list(look.node_labels.values()) + [b.label for b in tg.boxes.values()]
                     + [e.label for e in tg.edges]
                     if lab and re.search(r"→|->|=>|>", lab)}, key=len, reverse=True)
    paths = []
    for line in (text or "").splitlines():
        line = line.replace("**", "").replace("`", "")
        m = LINE_RE.match(line)
        if not m:
            continue
        number, body = int(m.group(1)), m.group(2)
        protected = {}
        for i, lab in enumerate(arrowy):
            key = f"\x00{i}\x00"
            if lab in body:
                body = body.replace(lab, key)
                protected[key] = lab
        tokens = [t for t in ARROW_SPLIT.split(body)]
        steps, problems = [], []
        for tok in tokens:
            for key, lab in protected.items():
                tok = tok.replace(key, lab)
            tok = tok.strip().strip("*").strip()
            if not tok:
                continue
            st = look.exact(tok)
            if st:
                steps.append(st)
                continue
            vm = VIA_RE.match(tok)
            if vm:
                head, inner = look.exact(vm.group(1)), look.exact(vm.group(2))
                if head:
                    if inner:
                        steps.append(inner)
                    else:
                        problems.append(f"note '({vm.group(2)})' after '{vm.group(1)}' is not in the graph; ignored")
                    steps.append(head)
                    continue
            nid, score, how = best_match(tok, look.node_labels, THRESHOLD)
            if nid is not None:
                steps.append(Step(tg.nodes[nid].label, "node", nid))
                problems.append(f"step '{tok}' read as node '{tg.nodes[nid].label}' (similar wording, score {score:.2f})")
                continue
            steps.append(Step(tok, "unknown", None, labels=[tok]))
            problems.append(f"step '{tok}' is not a node or arrow of this graph")
        paths.append(_finish(TestPath(number, m.group(2), steps, problems), tg))
    return paths


def _finish(p, tg):
    """Add arrow labels between consecutive nodes and check each move exists in the graph."""
    out, prev = [], None
    pending_edge = None
    for st in p.steps:
        if st.kind == "edge":
            if prev is not None and not any(e.u in _members(tg, prev) and e.label and
                                            clean_text(e.label) == clean_text(st.text) for e in tg.edges):
                p.problems.append(f"arrow '{st.text}' does not leave '{prev.text}'")
            pending_edge = st
            out.append(st)
            continue
        if st.kind in ("node", "box"):
            if prev is not None:
                if not _connected(tg, prev, st):
                    p.problems.append(f"no arrow from '{prev.text}' to '{st.text}' in this graph")
                elif pending_edge is None:
                    labs = [e.label for e in tg.edges
                            if e.u in _members(tg, prev) and e.v in _members(tg, st) and e.label]
                    labs = list(dict.fromkeys(labs))
                    if labs:
                        out.append(Step(" / ".join(labs), "edge", None, implicit=True, labels=labs))
            out.append(st)
            prev, pending_edge = st, None
            continue
        out.append(st)                                  # unknown step
        pending_edge = None
    p.steps = out
    for s in p.steps:
        if not s.labels:
            s.labels = [s.text]
        s.question = _is_question(tg, s)
    return p


def _is_question(tg, step):
    if step.kind != "node":
        return False
    n = tg.nodes.get(step.ref)
    return bool(n) and (n.shape == "diamond" or n.label.strip().endswith("?"))


def paths_from_enumeration(raw_paths, tg):
    """Turn graph.enumerate_paths() output into TestPath objects (used for the answer-set baseline)."""
    out = []
    for i, rp in enumerate(raw_paths, 1):
        steps = []
        for kind, val in rp:
            if kind == "node":
                if val.startswith("box:"):
                    b = tg.boxes[val[4:]]
                    steps.append(Step(b.label, "box", b.id, labels=[b.label]))
                else:
                    n = tg.nodes[val]
                    steps.append(Step(n.label, "node", n.id, labels=[n.label]))
            else:
                steps.append(Step(val, "edge", None, labels=[val]))
        for st in steps:
            st.question = _is_question(tg, st)
        p = TestPath(i, "", steps, [])
        p.raw = p.pretty(tg)
        out.append(p)
    return out
