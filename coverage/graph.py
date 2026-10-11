"""
STEPS 1 and 2 of the procedure: reading a test graph from a Graphviz DOT file.

The same reader is used for the answer set and for generated runs, so both sides are
turned into the same kind of object before anything is compared.

What the reader keeps
---------------------
nodes   every node, with its label and a role:
          concept   an ordinary labelled node (a state, a decision, a component ...)
          start     an entry marker (a small point, or an unlabelled node nothing points to)
          bar       an unlabelled fork / join / choice bar
          terminal  a node labelled only "Start", "End", "Begin", "Finish" ... (notation, not content)
          note      a comment box (shape=note)
edges   every arrow, with its label and kind (transition, or composition in the answer set)
boxes   every Graphviz cluster ("subgraph cluster_x { ... }"), with its label and members
texts   free text that is not a node label (graph title, note boxes, box labels)
"""
import re
from dataclasses import dataclass, field

import networkx as nx
import pydot

from .labels import clean_text

TERMINAL_WORDS = {"start", "end", "begin", "finish", "stop", "initial", "final", "done", "exit point"}
ARTIFACT_RE = re.compile(r"cluster[\s_-]*\w*", re.I)


@dataclass
class Node:
    id: str
    label: str
    role: str                 # concept | start | bar | terminal | note
    shape: str = ""
    attrs: dict = field(default_factory=dict)
    artifact: bool = False    # a node called "cluster_0" etc. (a Graphviz leftover, see report)


@dataclass
class Edge:
    u: str
    v: str
    label: str = ""
    kind: str = "transition"  # transition | composition
    attrs: dict = field(default_factory=dict)


@dataclass
class Box:
    id: str
    label: str
    members: set = field(default_factory=set)     # all nodes inside, including nested boxes' nodes
    parent: str = None


@dataclass
class TestGraph:
    name: str
    nodes: dict
    edges: list
    boxes: dict
    texts: list
    source: str = ""

    # ------------------------------------------------------------------ helpers
    def concept_nodes(self):
        return [n for n in self.nodes.values() if n.role == "concept"]

    def labelled_boxes(self):
        return [b for b in self.boxes.values() if b.label.strip()]

    def boxes_of(self, node_id):
        """Boxes that contain node_id, outermost first."""
        found = [b for b in self.boxes.values() if node_id in b.members]
        found.sort(key=lambda b: len(b.members), reverse=True)
        return found

    def initial_nodes(self):
        """Where test paths start: targets of start markers, else nodes nothing points to."""
        starts = [n.id for n in self.nodes.values() if n.role == "start"]
        targets = [e.v for e in self.edges if e.u in starts]
        if targets:
            return list(dict.fromkeys(targets))
        indeg = {nid: 0 for nid in self.nodes}
        for e in self.edges:
            if e.u != e.v:
                indeg[e.v] = indeg.get(e.v, 0) + 1
        roots = [nid for nid, d in indeg.items() if d == 0 and self.nodes[nid].role != "note"]
        return roots or [next(iter(self.nodes))]

    def network(self, use_boxes):
        """A networkx MultiDiGraph of the test graph.

        use_boxes=False : boxes are ignored (strict reading).
        use_boxes=True  : each box becomes a node "box:<id>" that contains its members
                          (box -> member edges, kind=contain), and an arrow drawn from
                          outside a box to a node inside it is read as entering the box
                          first (as in UML composite states).
        """
        G = nx.MultiDiGraph()
        for n in self.nodes.values():
            if n.role != "note":
                G.add_node(n.id, role=n.role, label=n.label)
        for e in self.edges:
            if e.u not in G or e.v not in G:
                continue
            u, v = e.u, e.v
            if use_boxes:
                entering = [b for b in self.boxes_of(v) if u not in b.members]
                if entering:
                    v = "box:" + entering[0].id
            G.add_edge(u, v, label=e.label, kind=e.kind)
        if use_boxes:
            for b in self.boxes.values():
                G.add_node("box:" + b.id, role="concept" if b.label.strip() else "bar", label=b.label)
            for b in self.boxes.values():
                # direct members only: members not inside a smaller box of this box
                inner = [c for c in self.boxes.values() if c.parent == b.id]
                inner_members = set().union(*[c.members for c in inner]) if inner else set()
                for m in b.members - inner_members:
                    if m in G:
                        G.add_edge("box:" + b.id, m, label="", kind="contain")
                for c in inner:
                    G.add_edge("box:" + b.id, "box:" + c.id, label="", kind="contain")
        return G


# ---------------------------------------------------------------------- reading DOT
def _unquote(s):
    if s is None:
        return None
    s = str(s)
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        s = s[1:-1]
    if s.startswith("<") and s.endswith(">"):          # HTML-like label
        s = re.sub(r"<[^>]*>", " ", s[1:-1])
    return s.replace('\\"', '"').replace("\\n", " ").replace("\\l", " ").replace("\\r", " ").strip()


def _attrs(obj):
    return {k: _unquote(v) for k, v in (obj.get_attributes() or {}).items()}


def load_dot(path=None, text=None, name=None):
    """Read a DOT file (or DOT text) into a TestGraph."""
    if text is None:
        text = open(path, encoding="utf-8").read()
    graphs = pydot.graph_from_dot_data(text)
    if not graphs:
        raise ValueError(f"could not parse DOT: {path}")
    g = graphs[0]

    nodes, edges, boxes, texts = {}, [], {}, []
    node_defaults = {}

    def ensure(nid, attrs=None, inherited=None):
        nid = _unquote(nid)
        if nid in ("node", "edge", "graph") or nid is None:
            return None
        base = dict(node_defaults)
        base.update(inherited or {})
        if nid not in nodes:
            nodes[nid] = dict(base)
        if attrs:
            nodes[nid].update(attrs)
        return nid

    def walk(container, box_id, inherited):
        local_defaults = dict(inherited)
        for n in container.get_node_list():
            nm = _unquote(n.get_name())
            if nm == "node":
                local_defaults.update(_attrs(n))
                if box_id is None:
                    node_defaults.update(_attrs(n))
                continue
            if nm in ("edge", "graph"):
                continue
            nid = ensure(nm, _attrs(n), local_defaults)
            if box_id and nid:
                boxes[box_id].members.add(nid)
        for e in container.get_edge_list():
            src, dst = e.get_source(), e.get_destination()
            if not isinstance(src, str) or not isinstance(dst, str):
                continue                                   # a -> {b c} style, not used here
            u = ensure(src, None, local_defaults)
            v = ensure(dst, None, local_defaults)
            a = _attrs(e)
            edges.append(Edge(u, v, a.get("label", "") or "", a.get("kind", "transition") or "transition", a))
            if box_id:
                boxes[box_id].members.update([u, v])
        for sg in container.get_subgraph_list():
            sname = _unquote(sg.get_name()) or ""
            sa = _attrs(sg)
            if sname.lower().startswith("cluster"):
                bid = sname
                boxes[bid] = Box(bid, sa.get("label", "") or "", set(), box_id)
                if sa.get("label"):
                    texts.append(sa["label"])
                walk(sg, bid, local_defaults)
                if box_id:
                    boxes[box_id].members |= boxes[bid].members
            else:
                walk(sg, box_id, local_defaults)

    ga = _attrs(g)
    if ga.get("label"):
        texts.append(ga["label"])
    walk(g, None, {})

    indeg = {nid: 0 for nid in nodes}
    for e in edges:
        if e.u != e.v:
            indeg[e.v] += 1

    out = {}
    for nid, a in nodes.items():
        label = a.get("label")
        if label is None or label == "\\N":
            label = nid
        shape = (a.get("shape") or "").lower()
        kind = (a.get("kind") or "").lower()
        if kind in ("state", "decision"):
            role = "concept"
        elif kind in ("start", "bar", "note"):
            role = kind
        elif shape == "note":
            role = "note"
        elif shape == "point":
            role = "start" if indeg[nid] == 0 else "bar"
        elif not label.strip():
            role = "start" if indeg[nid] == 0 else "bar"
        elif clean_text(label) in TERMINAL_WORDS:
            role = "terminal"
        else:
            role = "concept"
        if role == "note":
            texts.append(label)
        artifact = bool(ARTIFACT_RE.fullmatch(nid.strip())) and role == "concept"
        out[nid] = Node(nid, label, role, shape, a, artifact)

    return TestGraph(name or (ga.get("requirement") or _unquote(g.get_name()) or ""), out, edges, boxes, texts,
                     source=text)


# ---------------------------------------------------------------------- projection
def project(G, meaning):
    """Reduce a graph to the concepts it shares with the answer set.

    meaning: dict node -> set of answer-set ids that node stands for (empty = none).
    Result: set of (a, b) pairs of answer-set ids, meaning "the graph goes from a to b,
    possibly passing through nodes that stand for nothing in the answer set".
    Self-pairs (a, a) are dropped.
    """
    pairs = set()
    for u in G.nodes:
        src = meaning.get(u) or set()
        if not src:
            continue
        seen, stack = {u}, [w for w in G.successors(u)]
        while stack:
            w = stack.pop()
            if w in seen:
                continue
            seen.add(w)
            dst = meaning.get(w) or set()
            if dst:
                for a in src:
                    for b in dst:
                        if a != b:
                            pairs.add((a, b))
            else:
                stack.extend(G.successors(w))
    return pairs


# ---------------------------------------------------------------------- path enumeration
def enumerate_paths(tg, use_boxes=False):
    """All paths from an initial node to a node with no way out.

    This is the usual way a test generator reaches "100% coverage": every branch is
    followed to its end, and a loop is walked once (the path stops when it comes back
    to a node it has already visited). Each path is a list of steps; a step is
    ("node", id) or ("edge", label).
    """
    G = tg.network(use_boxes)
    paths = []

    def dfs(node, visited, steps):
        outs = [(v, d) for _, v, d in G.out_edges(node, data=True)]
        if not outs:
            paths.append(list(steps))
            return
        for v, d in outs:
            add = []
            if d.get("label"):
                add.append(("edge", d["label"]))
            add.append(("node", v))
            if v in visited:
                paths.append(steps + add)
            else:
                dfs(v, visited | {v}, steps + add)

    for s in tg.initial_nodes():
        dfs(s, {s}, [("node", s)])
    return paths
