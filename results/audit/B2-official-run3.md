# B2, official run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 57.1 | 57.1 | 57.1 | 4 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 0.0 | 0.0 | 0.0 | 0 of 5 routes walked; 0 of 5 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 66.7 | | | 2 of 3 |
| L1 nodes | lenient | 85.7 | 66.7 | 75.0 | 6 of 7 answer-set nodes found; 9 generated nodes |
| L2 arrows | lenient | 66.7 | 100.0 | 80.0 | 4 of 6 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 0.0 | 0.0 | 0.0 | 0 of 5 routes walked; 0 of 5 paths needed; test cases covered 0/2 |
| L4 sparkles | lenient | 100.0 | | | 3 of 3 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main Screen | nothing | nothing | none | no |
| Main Menu Bar | Main Menu Bar | Main Menu Bar | exact | yes |
| Navigational Toolbar | Navigational Toolbar | Navigational Toolbar | exact | yes |
| Text Field for URL Entry | Text Field for URL Entry | Text Field for URL Entry | exact | yes |
| HTML Display Zone | HTML Display Zone | HTML Display Zone | exact | yes |
| cluster_0 (Graphviz leftover) | nothing | nothing | none | no |
| cluster_1 (Graphviz leftover) | nothing | nothing | none | no |
| Fixed Components | (box not read in strict mode) | Fixed | fuzzy | yes |
| Dynamic Content Area | (box not read in strict mode) | To Be Implemented | alias: Box holding the HTML display zone, the one part whose implementation the requirement leaves open. | yes |

Answer-set nodes not found (lenient): Launching Browser

## L2. Arrows between shared nodes (lenient)

* Found in both: Fixed -> Main Menu Bar; Fixed -> Navigational Toolbar; Fixed -> Text Field for URL Entry; To Be Implemented -> HTML Display Zone
* In the answer set only: Launching Browser -> Fixed; Launching Browser -> To Be Implemented
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Screen → Main Menu Bar | yes | none | no |
| 2 | Main Screen → Navigational Toolbar | yes | none | no |
| 3 | Main Screen → Text Field for URL Entry | yes | none | no |
| 4 | Main Screen → HTML Display Zone | yes | none | no |
| 5 | Main Screen → cluster_0 → [Main Screen Loaded] → cluster_1 | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Launching Browser -> Main Menu Bar | T1 | none |
| Launching Browser -> Navigational Toolbar | T1 | none |
| Launching Browser -> Text Field for URL Entry | T1 | none |
| Launching Browser -> HTML Display Zone | T1 | none |
| (compares two runs, cannot be a path) | T2 | none |

Test cases covered: none (0 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Screen → Main Menu Bar | yes | none | no |
| 2 | Main Screen → Navigational Toolbar | yes | none | no |
| 3 | Main Screen → Text Field for URL Entry | yes | none | no |
| 4 | Main Screen → HTML Display Zone | yes | none | no |
| 5 | Main Screen → cluster_0 → [Main Screen Loaded] → cluster_1 | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Launching Browser -> Main Menu Bar | T1 | none |
| Launching Browser -> Navigational Toolbar | T1 | none |
| Launching Browser -> Text Field for URL Entry | T1 | none |
| Launching Browser -> HTML Display Zone | T1 | none |
| (compares two runs, cannot be a path) | T2 | none |

Test cases covered: none (0 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: split | fanout | met: 'Main Screen' splits into ['HDZ', 'MMB', 'NT', 'TFUE'] | met: 'Main Screen' splits into ['FIX', 'TBI'] |
| S2: use of “HTML Display Zone” as the name of a node | uses_term | met: term used | met: term used |
| S3: compositions | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | met: box 'Fixed Components' holds ['MMB', 'NT', 'TFUE'] |
