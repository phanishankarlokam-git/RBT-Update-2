# B15, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 16.7 | 25.0 | 20.0 | 1 of 6 answer-set nodes found; 4 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 5 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 0.0 | 0.0 | 0.0 | 0 of 4 routes walked; 0 of 2 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 0.0 | | | 0 of 2 |
| L1 nodes | lenient | 33.3 | 50.0 | 40.0 | 2 of 6 answer-set nodes found; 4 generated nodes |
| L2 arrows | lenient | 20.0 | 50.0 | 28.6 | 1 of 5 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 0.0 | 0.0 | 0.0 | 0 of 4 routes walked; 0 of 2 paths needed; test cases covered 0/2 |
| L4 sparkles | lenient | 0.0 | | | 0 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser Main Window | Browser | Browser | contains | yes |
| Help Menu Open | nothing | nothing | none | no |
| About Pop-up Displayed | nothing | Pop-up Window | alias: The About pop-up = Pop-up Window. | yes |
| About Content Verified | nothing | nothing | none | no |

Answer-set nodes not found (lenient): Name of Programmer, Mention of Homework Assignment for CS 585, Release Date and Version Number, Other(s)

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window
* In the answer set only: Pop-up Window -> Mention of Homework Assignment for CS 585; Pop-up Window -> Name of Programmer; Pop-up Window -> Other(s); Pop-up Window -> Release Date and Version Number
* In the generated graph only: Pop-up Window -> Browser

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser Main Window → (select Help) → Help Menu Open → (select About) → About Pop-up Displayed → (read pop-up text) → About Content Verified → (close pop-up) → Browser Main Window | yes | none | no |
| 2 | Browser Main Window → (select Help) → Help Menu Open → (dismiss menu (no selection)) → Browser Main Window | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Name of Programmer | T1, T2 | none |
| Mention of Homework Assignment for CS 585 | T1, T2 | none |
| Release Date and Version Number | T1, T2 | none |
| Other(s) | T2 | none |

Test cases covered: none (0 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser Main Window → (select Help) → Help Menu Open → (select About) → About Pop-up Displayed → (read pop-up text) → About Content Verified → (close pop-up) → Browser Main Window | yes | none | no |
| 2 | Browser Main Window → (select Help) → Help Menu Open → (dismiss menu (no selection)) → Browser Main Window | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Name of Programmer | T1, T2 | none |
| Mention of Homework Assignment for CS 585 | T1, T2 | none |
| Release Date and Version Number | T1, T2 | none |
| Other(s) | T2 | none |

Test cases covered: none (0 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | not met: no node for other/optional items | not met: no node for other/optional items |
