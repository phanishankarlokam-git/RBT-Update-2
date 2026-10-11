# B2, official run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 71.4 | 55.6 | 62.5 | 5 of 7 answer-set nodes found; 9 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 4 generated pairs |
| L3 tests | strict | 80.0 | 40.0 | 53.3 | 4 of 5 routes walked; 4 of 10 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 66.7 | | | 2 of 3 |
| L1 nodes | lenient | 100.0 | 63.6 | 77.8 | 7 of 7 answer-set nodes found; 11 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set pairs found; 6 generated pairs |
| L3 tests | lenient | 80.0 | 40.0 | 53.3 | 4 of 5 routes walked; 4 of 10 paths needed; test cases covered 1/2 |
| L4 sparkles | lenient | 100.0 | | | 3 of 3 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Launching Browser | Launching Browser | fuzzy | yes |
| Main Screen | nothing | nothing | none | no |
| Main menu bar | Main Menu Bar | Main Menu Bar | exact | yes |
| Navigational toolbar | Navigational Toolbar | Navigational Toolbar | exact | yes |
| Text field for URL entry | Text Field for URL Entry | Text Field for URL Entry | exact | yes |
| HTML Display Zone | HTML Display Zone | HTML Display Zone | exact | yes |
| cluster_0 (Graphviz leftover) | nothing | nothing | none | no |
| cluster_1 (Graphviz leftover) | nothing | nothing | none | no |
| Content displayed here | nothing | nothing | none | no |
| Fixed Browser Components | (box not read in strict mode) | Fixed | contains | yes |
| Dynamic Content Area | (box not read in strict mode) | To Be Implemented | alias: Box holding the HTML display zone, the one part whose implementation the requirement leaves open. | yes |

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
| 1 | Browser → (launch browser) → Main Screen → Main menu bar → cluster_0 → (Main screen loaded) → cluster_1 | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Browser → (launch browser) → Main Screen → Navigational toolbar → cluster_0 → (Main screen loaded) → cluster_1 | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Browser → (launch browser) → Main Screen → Text field for URL entry → cluster_0 → (Main screen loaded) → cluster_1 | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Browser → (launch browser) → Main Screen → HTML Display Zone → cluster_0 → Content displayed here | no: no arrow from 'HTML Display Zone' to 'cluster_0' in this graph; no arrow from 'cluster_0' to 'Content displayed here' in this graph | Launching Browser -> HTML Display Zone | yes |
| 5 | Browser → (launch browser) → Main Screen → Fixed Browser Components → cluster_0 → (Main screen loaded) → cluster_1 | yes | none | no |
| 6 | Browser → (launch browser) → Main Screen → HTML Display Zone → cluster_0 → Content displayed here | no: no arrow from 'HTML Display Zone' to 'cluster_0' in this graph; no arrow from 'cluster_0' to 'Content displayed here' in this graph | Launching Browser -> HTML Display Zone | no |
| 7 | Browser → (launch browser) → Main Screen → Main menu bar → cluster_0 → (Main screen loaded) → cluster_1 → ?loop back? | no: step 'loop back' is not a node or arrow of this graph | Launching Browser -> Main Menu Bar | no |
| 8 | Browser → (launch browser) → Main Screen → Navigational toolbar → cluster_0 → (Main screen loaded) → cluster_1 → ?loop back? | no: step 'loop back' is not a node or arrow of this graph | Launching Browser -> Navigational Toolbar | no |
| 9 | Browser → (launch browser) → Main Screen → Text field for URL entry → cluster_0 → (Main screen loaded) → cluster_1 → ?loop back? | no: step 'loop back' is not a node or arrow of this graph | Launching Browser -> Text Field for URL Entry | no |
| 10 | Browser → (launch browser) → Main Screen → HTML Display Zone → cluster_0 → Content displayed here → ?loop back? | no: step 'loop back' is not a node or arrow of this graph; no arrow from 'HTML Display Zone' to 'cluster_0' in this graph; no arrow from 'cluster_0' to 'Content displayed here' in this graph | Launching Browser -> HTML Display Zone | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Launching Browser -> Main Menu Bar | T1 | 1, 7 |
| Launching Browser -> Navigational Toolbar | T1 | 2, 8 |
| Launching Browser -> Text Field for URL Entry | T1 | 3, 9 |
| Launching Browser -> HTML Display Zone | T1 | 4, 6, 10 |
| (compares two runs, cannot be a path) | T2 | none |

Test cases covered: T1 (1 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → (launch browser) → Main Screen → Main menu bar → cluster_0 → (Main screen loaded) → cluster_1 | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Browser → (launch browser) → Main Screen → Navigational toolbar → cluster_0 → (Main screen loaded) → cluster_1 | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Browser → (launch browser) → Main Screen → Text field for URL entry → cluster_0 → (Main screen loaded) → cluster_1 | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Browser → (launch browser) → Main Screen → HTML Display Zone → cluster_0 → Content displayed here | no: no arrow from 'HTML Display Zone' to 'cluster_0' in this graph; no arrow from 'cluster_0' to 'Content displayed here' in this graph | Launching Browser -> HTML Display Zone | yes |
| 5 | Browser → (launch browser) → Main Screen → Fixed Browser Components → cluster_0 → (Main screen loaded) → cluster_1 | yes | none | no |
| 6 | Browser → (launch browser) → Main Screen → HTML Display Zone → cluster_0 → Content displayed here | no: no arrow from 'HTML Display Zone' to 'cluster_0' in this graph; no arrow from 'cluster_0' to 'Content displayed here' in this graph | Launching Browser -> HTML Display Zone | no |
| 7 | Browser → (launch browser) → Main Screen → Main menu bar → cluster_0 → (Main screen loaded) → cluster_1 → ?loop back? | no: step 'loop back' is not a node or arrow of this graph | Launching Browser -> Main Menu Bar | no |
| 8 | Browser → (launch browser) → Main Screen → Navigational toolbar → cluster_0 → (Main screen loaded) → cluster_1 → ?loop back? | no: step 'loop back' is not a node or arrow of this graph | Launching Browser -> Navigational Toolbar | no |
| 9 | Browser → (launch browser) → Main Screen → Text field for URL entry → cluster_0 → (Main screen loaded) → cluster_1 → ?loop back? | no: step 'loop back' is not a node or arrow of this graph | Launching Browser -> Text Field for URL Entry | no |
| 10 | Browser → (launch browser) → Main Screen → HTML Display Zone → cluster_0 → Content displayed here → ?loop back? | no: step 'loop back' is not a node or arrow of this graph; no arrow from 'HTML Display Zone' to 'cluster_0' in this graph; no arrow from 'cluster_0' to 'Content displayed here' in this graph | Launching Browser -> HTML Display Zone | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Launching Browser -> Main Menu Bar | T1 | 1, 7 |
| Launching Browser -> Navigational Toolbar | T1 | 2, 8 |
| Launching Browser -> Text Field for URL Entry | T1 | 3, 9 |
| Launching Browser -> HTML Display Zone | T1 | 4, 6, 10 |
| (compares two runs, cannot be a path) | T2 | none |

Test cases covered: T1 (1 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: split | fanout | met: 'Main Screen' splits into ['HDZ', 'MMB', 'NT', 'TFUE'] | met: 'Main Screen' splits into ['FIX', 'TBI'] |
| S2: use of “HTML Display Zone” as the name of a node | uses_term | met: term used | met: term used |
| S3: compositions | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | met: box 'Fixed Browser Components' holds ['MMB', 'NT', 'TFUE'] |
