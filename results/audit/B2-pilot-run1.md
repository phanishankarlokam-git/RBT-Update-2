# B2, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 57.1 | 80.0 | 66.7 | 4 of 7 answer-set nodes found; 5 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 66.7 | | | 2 of 3 |
| L1 nodes | lenient | 57.1 | 80.0 | 66.7 | 4 of 7 answer-set nodes found; 5 generated nodes |
| L2 arrows | lenient | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set pairs found; 0 generated pairs |
| L3 tests | lenient | 80.0 | 100.0 | 88.9 | 4 of 5 routes walked; 4 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | lenient | 66.7 | | | 2 of 3 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main Screen Displayed | nothing | nothing | none | no |
| Main Menu Bar Present | Main Menu Bar | Main Menu Bar | fuzzy | yes |
| Navigational Toolbar Present | Navigational Toolbar | Navigational Toolbar | fuzzy | yes |
| URL Entry Field Present | Text Field for URL Entry | Text Field for URL Entry | fuzzy | yes |
| HTML Display Zone Present | HTML Display Zone | HTML Display Zone | fuzzy | yes |

Answer-set nodes not found (lenient): Launching Browser, Fixed, To Be Implemented

## L2. Arrows between shared nodes (lenient)

* Found in both: none
* In the answer set only: Fixed -> Main Menu Bar; Fixed -> Navigational Toolbar; Fixed -> Text Field for URL Entry; Launching Browser -> Fixed; Launching Browser -> To Be Implemented; To Be Implemented -> HTML Display Zone
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (launch browser) → Main Screen Displayed → (verify menu bar) → Main Menu Bar Present → End | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Start → (launch browser) → Main Screen Displayed → (verify toolbar) → Navigational Toolbar Present → End | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Start → (launch browser) → Main Screen Displayed → (verify URL field) → URL Entry Field Present → End | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Start → (launch browser) → Main Screen Displayed → (verify HTML display zone) → HTML Display Zone Present → End | yes | Launching Browser -> HTML Display Zone | yes |

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
| 1 | Start → (launch browser) → Main Screen Displayed → (verify menu bar) → Main Menu Bar Present → End | yes | Launching Browser -> Main Menu Bar | yes |
| 2 | Start → (launch browser) → Main Screen Displayed → (verify toolbar) → Navigational Toolbar Present → End | yes | Launching Browser -> Navigational Toolbar | yes |
| 3 | Start → (launch browser) → Main Screen Displayed → (verify URL field) → URL Entry Field Present → End | yes | Launching Browser -> Text Field for URL Entry | yes |
| 4 | Start → (launch browser) → Main Screen Displayed → (verify HTML display zone) → HTML Display Zone Present → End | yes | Launching Browser -> HTML Display Zone | yes |

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
