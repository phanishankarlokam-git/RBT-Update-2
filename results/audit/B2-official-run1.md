# B2, official run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 71.4 | 50.0 | 58.8 | 5 of 7 answer-set nodes found; 10 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 4 generated pairs |
| L3 tests | strict | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 66.7 | | | 2 of 3 |
| L1 nodes | lenient | 71.4 | 50.0 | 58.8 | 5 of 7 answer-set nodes found; 10 generated nodes |
| L2 arrows | lenient | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | lenient | 100.0 | | | 3 of 3 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main screen components appear | nothing | nothing | none | no |
| launch browser | Launching Browser | Launching Browser | exact | yes |
| Browser | Launching Browser | Launching Browser | fuzzy | no, duplicate |
| Main menu bar | Main Menu Bar | Main Menu Bar | exact | yes |
| Navigational toolbar | Navigational Toolbar | Navigational Toolbar | exact | yes |
| Text field for URL entry | Text Field for URL Entry | Text Field for URL Entry | exact | yes |
| HTML Display Zone | HTML Display Zone | HTML Display Zone | exact | yes |
| cluster_0 (Graphviz leftover) | nothing | nothing | none | no |
| cluster_1 (Graphviz leftover) | nothing | nothing | none | no |
| HTML content displayed here | nothing | nothing | none | no |

Answer-set nodes not found (lenient): Fixed, To Be Implemented

## L2. Arrows between shared nodes (lenient)

* Found in both: none
* In the answer set only: Fixed -> Main Menu Bar; Fixed -> Navigational Toolbar; Fixed -> Text Field for URL Entry; Launching Browser -> Fixed; Launching Browser -> To Be Implemented; To Be Implemented -> HTML Display Zone
* In the generated graph only: Launching Browser -> HTML Display Zone; Launching Browser -> Main Menu Bar; Launching Browser -> Navigational Toolbar; Launching Browser -> Text Field for URL Entry

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | launch browser → Browser → Main screen components appear → [Menu bar] → Main menu bar → cluster_0 → [Main screen loaded] → cluster_1 | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | launch browser → Browser → Main screen components appear → [Toolbar] → Navigational toolbar → cluster_0 → [Main screen loaded] → cluster_1 | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | launch browser → Browser → Main screen components appear → [URL entry] → Text field for URL entry → cluster_0 → [Main screen loaded] → cluster_1 | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | launch browser → Browser → Main screen components appear → [HTML Display] → HTML Display Zone → [Content Displayed] → HTML content displayed here | yes | Launching Browser -> HTML Display Zone | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Launching Browser -> Main Menu Bar | T1 | 1 |
| Launching Browser -> Navigational Toolbar | T1 | 2 |
| Launching Browser -> Text Field for URL Entry | T1 | 3 |
| Launching Browser -> HTML Display Zone | T1 | 4 |
| (compares two runs, cannot be a path) | T2 | none |

Test cases covered: T1 (1 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | launch browser → Browser → Main screen components appear → [Menu bar] → Main menu bar → cluster_0 → [Main screen loaded] → cluster_1 | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | launch browser → Browser → Main screen components appear → [Toolbar] → Navigational toolbar → cluster_0 → [Main screen loaded] → cluster_1 | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | launch browser → Browser → Main screen components appear → [URL entry] → Text field for URL entry → cluster_0 → [Main screen loaded] → cluster_1 | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | launch browser → Browser → Main screen components appear → [HTML Display] → HTML Display Zone → [Content Displayed] → HTML content displayed here | yes | Launching Browser -> HTML Display Zone | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Launching Browser -> Main Menu Bar | T1 | 1 |
| Launching Browser -> Navigational Toolbar | T1 | 2 |
| Launching Browser -> Text Field for URL Entry | T1 | 3 |
| Launching Browser -> HTML Display Zone | T1 | 4 |
| (compares two runs, cannot be a path) | T2 | none |

Test cases covered: T1 (1 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: split | fanout | met: 'Main screen components appear' splits into ['HDZ', 'MMB', 'NT', 'TFUE'] | met: 'Main screen components appear' splits into ['HDZ', 'MMB', 'NT', 'TFUE'] |
| S2: use of “HTML Display Zone” as the name of a node | uses_term | met: term used | met: term used |
| S3: compositions | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | met: box 'cluster_0' holds ['MMB', 'NT', 'TFUE'] |
