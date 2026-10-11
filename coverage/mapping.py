"""
STEP 3 (second half): what does each element of a generated graph stand for?

For every node, box (cluster) and arrow label of a generated run we decide which
answer-set node it stands for, using the label rule in labels.py.

Two modes are always reported side by side:

  strict   only the automatic word rule; boxes (clusters) are ignored.
  lenient  the same, plus
             - labelled boxes count as nodes (a box is read as a composite node), and
             - the alias list data/aliases.yaml: equivalences a person has checked and
               written down with a reason (e.g. "Dynamic Content Area" = "To Be Implemented").

The difference between the two modes shows how much of a score depends on human judgement.
"""
import fnmatch

import yaml

from .labels import best_match, clean_text, THRESHOLD


def load_aliases(path):
    try:
        data = yaml.safe_load(open(path, encoding="utf-8")) or []
    except FileNotFoundError:
        data = []
    return data


class Meaning:
    def __init__(self, ref_graph, run_graph, mode, aliases=(), requirement="", run_key=""):
        self.mode = mode
        self.ref_labels = {n.id: n.label for n in ref_graph.concept_nodes()}
        self.run = run_graph
        self.aliases = []
        if mode == "lenient":
            for a in aliases:
                if a.get("requirement") not in (requirement, "*"):
                    continue
                runs = a.get("runs", ["*"])
                if not any(fnmatch.fnmatch(run_key, r) for r in runs):
                    continue
                self.aliases.append(a)
        self._cache = {}

    # -------------------------------------------------------------- labels
    def of_label(self, text):
        """(set of answer-set ids, how, score) for a piece of text."""
        key = clean_text(text)
        if key in self._cache:
            return self._cache[key]
        res = (set(), "none", 0.0)
        for a in self.aliases:
            if clean_text(a["label"]) == key:
                ids = {m for m in a["means"] if not str(m).startswith("(")}
                res = (ids, "alias: " + a.get("reason", ""), 1.0)
                break
        else:
            rid, score, how = best_match(text, self.ref_labels, THRESHOLD)
            if rid is not None:
                res = ({rid}, how, score)
            else:
                res = (set(), how, score)
        self._cache[key] = res
        return res

    def alias_words(self, text):
        """Event/guard words an alias says this text stands for, e.g. '(do nothing)'."""
        key = clean_text(text)
        out = set()
        for a in self.aliases:
            if clean_text(a["label"]) == key:
                out |= {m for m in a["means"] if str(m).startswith("(")}
        return out

    # -------------------------------------------------------------- graph elements
    def of_node(self, node_id):
        n = self.run.nodes.get(node_id)
        if n is None or n.role != "concept":
            return set(), "not a concept node", 0.0
        return self.of_label(n.label)

    def of_box(self, box_id):
        if self.mode != "lenient":
            return set(), "boxes ignored in strict mode", 0.0
        b = self.run.boxes.get(box_id)
        if b is None or not b.label.strip():
            return set(), "unlabelled box", 0.0
        return self.of_label(b.label)

    def of_network_node(self, g_node):
        if str(g_node).startswith("box:"):
            return self.of_box(g_node[4:])[0]
        return self.of_node(g_node)[0]

    def of_step(self, step):
        if step.kind == "node":
            return self.of_node(step.ref)[0]
        if step.kind == "box":
            return self.of_box(step.ref)[0]
        out = set()                                  # arrow labels and unknown steps
        for lab in (step.labels or [step.text]):
            out |= self.of_label(lab)[0]
        return out
