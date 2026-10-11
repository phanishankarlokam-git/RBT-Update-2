"""
Checks that the tool reproduces the B2 worked example in Update 2, number by number.
Run with:  python -m pytest tests/      (or simply: python tests/test_b2_worked_example.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from coverage.answer_set import load
from coverage.graph import load_dot, enumerate_paths
from coverage.paths import parse_paths, paths_from_enumeration
from coverage.mapping import Meaning, load_aliases
from coverage.metrics import level1, level2, level3, level4
from coverage.labels import similarity, words

DATA = os.path.join(ROOT, "data")


def run(i, mode):
    ref, spec = load(os.path.join(DATA, "answer_set"), "B2")
    d = os.path.join(DATA, "runs", "official", "B2")
    tg = load_dot(os.path.join(d, f"run{i}.dot"))
    paths = parse_paths(open(os.path.join(d, f"run{i}-TCs.txt"), encoding="utf-8").read(), tg)
    m = Meaning(ref, tg, mode, load_aliases(os.path.join(DATA, "aliases.yaml")), "B2", f"official/run{i}")
    return level1(ref, tg, m), level2(ref, tg, m), level3(spec, paths, m), level4(ref, spec, tg, m, {}, f"official/run{i}")


def close(a, b):
    return abs(a - b) < 0.001


def test_label_rule():
    assert words("Launching Browser") == words("launch browser")
    assert similarity("Launching Browser", "Browser") == 0.5
    assert similarity("No Current Page", "Current page") == 0.0          # negation guard
    assert similarity("Content Click Disabled", "Content Click Enabled") == 0.0  # opposites guard


def test_level1_matches_update1():
    # (recall, precision) strict and lenient, exactly as in Update 1
    expected = {1: ((5/7, 5/10), (5/7, 5/10)), 2: ((5/7, 5/9), (7/7, 7/11)), 3: ((4/7, 4/7), (6/7, 6/9))}
    for i, (s, l) in expected.items():
        r1s = run(i, "strict")[0]
        r1l = run(i, "lenient")[0]
        assert close(r1s["recall"], s[0]) and close(r1s["precision"], s[1]), i
        assert close(r1l["recall"], l[0]) and close(r1l["precision"], l[1]), i


def test_level2_lenient():
    expected = {1: (0.0, 0.0), 2: (1.0, 1.0), 3: (4/6, 1.0)}
    for i, (r, p) in expected.items():
        r2 = run(i, "lenient")[1]
        assert close(r2["recall"], r) and close(r2["precision"], p), i


def test_level3_worked_example():
    # run 1: 4 routes walked of 5 units, 4 of 4 paths needed
    r3 = run(1, "strict")[2]
    assert r3["tp"] == 4 and r3["n_ref"] == 5 and r3["tp_paths"] == 4 and r3["n_gen"] == 4
    assert close(r3["recall"], 0.8) and close(r3["precision"], 1.0) and close(r3["f1"], 8/9)
    # run 2: same 4 routes, but only 4 of its 10 paths are needed
    r3 = run(2, "strict")[2]
    assert r3["tp"] == 4 and r3["tp_paths"] == 4 and r3["n_gen"] == 10
    assert close(r3["precision"], 0.4) and close(r3["f1"], 2 * 0.4 * 0.8 / 1.2)
    assert r3["n_valid"] == 4 and r3["n_dup"] == 1
    # run 3: never reaches the launch, so no route
    r3 = run(3, "strict")[2]
    assert r3["tp"] == 0 and r3["tc_covered"] == []
    # test cases covered = Update 1's L3 recall
    assert run(1, "strict")[2]["tc_covered"] == ["T1"]
    assert run(2, "strict")[2]["tc_covered"] == ["T1"]


def test_level4():
    for i in (1, 2, 3):
        assert run(i, "strict")[3]["met"] == 2
        assert run(i, "lenient")[3]["met"] == 3


def test_answer_set_scores_itself_perfectly_on_L1_L2_L4():
    ref, spec = load(os.path.join(DATA, "answer_set"), "B2")
    m = Meaning(ref, ref, "strict", [], "B2", "answer-set")
    paths = paths_from_enumeration(enumerate_paths(ref), ref)
    assert level1(ref, ref, m)["f1"] == 1.0
    assert level2(ref, ref, m)["f1"] == 1.0
    assert level4(ref, spec, ref, m, {}, "answer-set")["met"] == 3
    assert close(level3(spec, paths, m)["recall"], 0.8)   # T2 compares two launches: no path can express it


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok ", name)
    print("all checks passed")
