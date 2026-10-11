# B2, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 71.4 | 71.4 | 71.4 | 5 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 4 generated pairs |
| L3 tests | strict | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 66.7 | | | 2 of 3 |
| L1 nodes | lenient | 71.4 | 71.4 | 71.4 | 5 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | lenient | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | lenient | 66.7 | | | 2 of 3 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser Launched | Launching Browser | Launching Browser | exact | yes |
| Main Screen Displayed | nothing | nothing | none | no |
| Main Menu Bar Displayed | Main Menu Bar | Main Menu Bar | fuzzy | yes |
| Navigational Toolbar Displayed | Navigational Toolbar | Navigational Toolbar | fuzzy | yes |
| URL Text Field Displayed | Text Field for URL Entry | Text Field for URL Entry | fuzzy | yes |
| HTML Display Zone Displayed | HTML Display Zone | HTML Display Zone | exact | yes |
| Main Screen Complete | nothing | nothing | none | no |

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
| 1 | Browser Launched → Main Screen Displayed → Main Menu Bar Displayed → Main Screen Complete | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Browser Launched → Main Screen Displayed → Navigational Toolbar Displayed → Main Screen Complete | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Browser Launched → Main Screen Displayed → URL Text Field Displayed → Main Screen Complete | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Browser Launched → Main Screen Displayed → HTML Display Zone Displayed → Main Screen Complete | yes | Launching Browser -> HTML Display Zone | yes |

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
| 1 | Browser Launched → Main Screen Displayed → Main Menu Bar Displayed → Main Screen Complete | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Browser Launched → Main Screen Displayed → Navigational Toolbar Displayed → Main Screen Complete | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Browser Launched → Main Screen Displayed → URL Text Field Displayed → Main Screen Complete | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Browser Launched → Main Screen Displayed → HTML Display Zone Displayed → Main Screen Complete | yes | Launching Browser -> HTML Display Zone | yes |

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
| S1: split | fanout | met: 'Main Screen Displayed' splits into ['HDZ', 'MMB', 'NT', 'TFUE'] | met: 'Main Screen Displayed' splits into ['HDZ', 'MMB', 'NT', 'TFUE'] |
| S2: use of “HTML Display Zone” as the name of a node | uses_term | met: term used | met: term used |
| S3: compositions | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
