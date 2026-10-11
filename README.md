<<<<<<< HEAD
# Coverage tool: generated test graphs vs. the answer set (Browser dataset)

This folder computes every number in Research Update 2. One command reproduces all of it.

## Run it

```
pip install -r requirements.txt
python run_all.py --pptx data/Browser.pptx   # scores every run, writes results/
python scripts/make_tables.py                # rebuilds the LaTeX tables used in the report
python tests/test_b2_worked_example.py       # checks the B2 worked example, number by number
```

Runs in a few seconds. Python 3.9 or newer.

## The procedure in five steps

| Step | What happens | Where |
|---|---|---|
| 1. Answer set into files | Each diagram in Browser.pptx is typed into `Bx.dot` (nodes, arrows, labels). The notes (requirement, logical test cases, sparkles) are copied word for word into `Bx.yaml`. Each logical test case is broken into routes. The program then checks the files against the slides automatically. | `data/answer_set/`, `coverage/answer_set.py` |
| 2. Each generated run into files | The run's graph as DOT (`runN.dot`) and its path list unchanged (`runN-TCs.txt`). The program reads each numbered path and lays it on the run's own graph. | `data/runs/<source>/Bx/`, `coverage/graph.py`, `coverage/paths.py` |
| 3. Match labels | Clean both labels, compare word sets (shared / all), match at 0.5 or when every answer-set word is present; never across a negation or an opposite pair. Strict = this rule only. Lenient = also Graphviz boxes as nodes and the reviewed list `data/aliases.yaml`. | `coverage/labels.py`, `coverage/mapping.py` |
| 4. Count | L1 nodes, L2 arrows, L3 tests (routes and paths), L4 sparkles. Precision = matched generated items / all generated items; recall = matched answer-set items / all answer-set items; F1 = 2PR/(P+R). | `coverage/metrics.py`, `coverage/checks.py` |
| 5. Report | `results/summary.csv` and `.xlsx` (every number), `results/audit/*.md` (every decision behind every number), `results/answer_set_check.txt`. | `coverage/report.py`, `run_all.py` |

## Words used

* **Route**: the checkpoints one test path must pass, in order: the start node (unless it is the neutral "Browser"), the event or guard words that tell this test case apart from the others, and the outcome nodes. A logical test case has one or more routes.
* **Walked**: a path walks a route when it passes all the route's checkpoints in order, each at a later
  step than the one before. A path is read as written in `TCs.txt`; whether it is possible in the run's
  own graph is reported separately and does not change what it walks.
* **Needed path**: a path that belongs to the smallest set of paths that still walks every route the run walks. Duplicates and paths that walk no route are not needed.
* **Test case covered**: all of its routes are walked.
* **Strict / lenient**: see Step 3.

## Folder layout

```
run_all.py                     one command for everything
coverage/                      the program (one file per step)
data/Browser.pptx              the answer set as given
data/answer_set/Bx.dot|yaml    Step 1 output, one pair per requirement (+ Bx.png renders)
data/runs/official/B2/         your three B2 OneShot runs: original PNG, re-typed DOT, TCs.txt
data/runs/pilot/Bx/            30 pilot runs: raw reply, DOT, paths, PNG; pilot_manifest.csv
data/pilot_prompt.txt          the prompt used for the pilot runs
data/aliases.yaml              reviewed matches (lenient mode only), each with a reason
data/judgements.yaml           the one sparkle judged by hand (B16 swimlane)
results/                       created by run_all.py
scripts/make_tables.py         LaTeX tables for the report
scripts/make_answer_set_yaml.py  how the YAML files were created from the slides
tests/                         the B2 worked example as automatic checks
```

## Adding new runs

Put `runN.dot` and `runN-TCs.txt` in `data/runs/<source>/<requirement>/` (for example
`data/runs/official/B20/run1.dot`) and run `python run_all.py` again. Nothing else changes.
If a run only exists as a picture, type its graph into DOT first and render it with
`dot -Tpng runN.dot -o check.png` to compare with the picture.
=======
# RBT-Update-2
>>>>>>> a44631b226e586f640f268fb04a3279de3c04e62
