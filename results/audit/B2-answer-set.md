# B2: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 7 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set pairs found; 6 generated pairs |
| L3 tests | strict | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 100.0 | | | 3 of 3 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 7 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set pairs found; 6 generated pairs |
| L3 tests | lenient | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | lenient | 100.0 | | | 3 of 3 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Launching Browser | Launching Browser | Launching Browser | exact | yes |
| Fixed | Fixed | Fixed | exact | yes |
| To Be Implemented | To Be Implemented | To Be Implemented | exact | yes |
| Main Menu Bar | Main Menu Bar | Main Menu Bar | exact | yes |
| Navigational Toolbar | Navigational Toolbar | Navigational Toolbar | exact | yes |
| Text Field for URL Entry | Text Field for URL Entry | Text Field for URL Entry | exact | yes |
| HTML Display Zone | HTML Display Zone | HTML Display Zone | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Fixed -> Main Menu Bar; Fixed -> Navigational Toolbar; Fixed -> Text Field for URL Entry; Launching Browser -> Fixed; Launching Browser -> To Be Implemented; To Be Implemented -> HTML Display Zone
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Launching Browser → [display] → [bar] → Fixed → Main Menu Bar | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Launching Browser → [display] → [bar] → Fixed → Navigational Toolbar | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Launching Browser → [display] → [bar] → Fixed → Text Field for URL Entry | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Launching Browser → [display] → [bar] → To Be Implemented → HTML Display Zone | yes | Launching Browser -> HTML Display Zone | yes |

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
| 1 | Launching Browser → [display] → [bar] → Fixed → Main Menu Bar | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Launching Browser → [display] → [bar] → Fixed → Navigational Toolbar | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Launching Browser → [display] → [bar] → Fixed → Text Field for URL Entry | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Launching Browser → [display] → [bar] → To Be Implemented → HTML Display Zone | yes | Launching Browser -> HTML Display Zone | yes |

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
| S1: split | fanout | met: 'Launching Browser' splits into ['FIX', 'TBI'] | met: 'Launching Browser' splits into ['FIX', 'TBI'] |
| S2: use of “HTML Display Zone” as the name of a node | uses_term | met: term used | met: term used |
| S3: compositions | composition | met: composition from 'Fixed' to ['MMB', 'NT', 'TFUE'] | met: composition from 'Fixed' to ['MMB', 'NT', 'TFUE'] |
