# B15, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set nodes found; 8 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 5 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 0.0 | 0.0 | 0.0 | 0 of 4 routes walked; 0 of 3 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 50.0 | | | 1 of 2 |
| L1 nodes | lenient | 50.0 | 37.5 | 42.9 | 3 of 6 answer-set nodes found; 8 generated nodes |
| L2 arrows | lenient | 40.0 | 50.0 | 44.4 | 2 of 5 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 100.0 | 33.3 | 50.0 | 4 of 4 routes walked; 1 of 3 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main Window | nothing | Browser | alias: The browser's main window = the Browser start node. | yes |
| Help Menu Open | nothing | nothing | none | no |
| About Selected? | nothing | nothing | none | no |
| About Dialog Displayed | nothing | Pop-up Window | alias: The About dialog = Pop-up Window. | yes |
| Required Content Verified | nothing | nothing | none | no |
| Optional Info Included? | nothing | nothing | none | no |
| Optional Info Displayed | nothing | Other(s) | alias: Optional information = Other(s). | yes |
| Dialog Closed | nothing | nothing | none | no |

Answer-set nodes not found (lenient): Name of Programmer, Mention of Homework Assignment for CS 585, Release Date and Version Number

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window; Pop-up Window -> Other(s)
* In the answer set only: Pop-up Window -> Mention of Homework Assignment for CS 585; Pop-up Window -> Name of Programmer; Pop-up Window -> Release Date and Version Number
* In the generated graph only: Other(s) -> Browser; Pop-up Window -> Browser

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Window → (click Help) → Help Menu Open → (menu shown) → About Selected? → (Yes) → About Dialog Displayed → (popup opens) → Required Content Verified → (name, CS 585 mention, release date, version # shown) → Optional Info Included? → (Yes) → Optional Info Displayed → (close popup) → Dialog Closed → (return) → Main Window | yes | none | no |
| 2 | Main Window → (click Help) → Help Menu Open → (menu shown) → About Selected? → (Yes) → About Dialog Displayed → (popup opens) → Required Content Verified → (name, CS 585 mention, release date, version # shown) → Optional Info Included? → (No) → Dialog Closed → (return) → Main Window | yes | none | no |
| 3 | Main Window → (click Help) → Help Menu Open → (menu shown) → About Selected? → (No) → Main Window | yes | none | no |

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
| 1 | Main Window → (click Help) → Help Menu Open → (menu shown) → About Selected? → (Yes) → About Dialog Displayed → (popup opens) → Required Content Verified → (name, CS 585 mention, release date, version # shown) → Optional Info Included? → (Yes) → Optional Info Displayed → (close popup) → Dialog Closed → (return) → Main Window | yes | Name of Programmer; Mention of Homework Assignment for CS 585; Release Date and Version Number; Other(s) | yes |
| 2 | Main Window → (click Help) → Help Menu Open → (menu shown) → About Selected? → (Yes) → About Dialog Displayed → (popup opens) → Required Content Verified → (name, CS 585 mention, release date, version # shown) → Optional Info Included? → (No) → Dialog Closed → (return) → Main Window | yes | Name of Programmer; Mention of Homework Assignment for CS 585; Release Date and Version Number | no |
| 3 | Main Window → (click Help) → Help Menu Open → (menu shown) → About Selected? → (No) → Main Window | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Name of Programmer | T1, T2 | 1, 2 |
| Mention of Homework Assignment for CS 585 | T1, T2 | 1, 2 |
| Release Date and Version Number | T1, T2 | 1, 2 |
| Other(s) | T2 | 1 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | met: optional items modelled as 'Optional Info Displayed' | met: optional items modelled as 'Optional Info Displayed' |
