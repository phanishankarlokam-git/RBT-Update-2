# B15, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 50.0 | 33.3 | 40.0 | 3 of 6 answer-set nodes found; 9 generated nodes |
| L2 arrows | strict | 20.0 | 33.3 | 25.0 | 1 of 5 answer-set pairs found; 3 generated pairs |
| L3 tests | strict | 75.0 | 50.0 | 60.0 | 3 of 4 routes walked; 1 of 2 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 50.0 | | | 1 of 2 |
| L1 nodes | lenient | 83.3 | 55.6 | 66.7 | 5 of 6 answer-set nodes found; 9 generated nodes |
| L2 arrows | lenient | 20.0 | 25.0 | 22.2 | 1 of 5 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 100.0 | 50.0 | 66.7 | 4 of 4 routes walked; 1 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Help Menu Opened | nothing | nothing | none | no |
| About Selected | nothing | nothing | none | no |
| About Pop-up Window Displayed | Pop-up Window | Pop-up Window | fuzzy | yes |
| Programmer Name Shown | Name of Programmer | Name of Programmer | fuzzy | yes |
| CS 585 Homework Mention Shown | Mention of Homework Assignment for CS 585 | Mention of Homework Assignment for CS 585 | fuzzy | yes |
| Release Date Shown | nothing | Release Date and Version Number | alias: The answer set keeps release date and version number in one node. | yes |
| Version Number Shown | nothing | Release Date and Version Number | alias: The answer set keeps release date and version number in one node. | no, duplicate |
| Additional Info Shown | nothing | Other(s) | alias: Additional information = Other(s). | yes |
| About Pop-up Window Closed | Pop-up Window | nothing | alias: Closing the pop-up is not the pop-up window itself (the automatic rule matched it on shared words). | no |

Answer-set nodes not found (lenient): Browser

## L2. Arrows between shared nodes (lenient)

* Found in both: Pop-up Window -> Name of Programmer
* In the answer set only: Browser -> Pop-up Window; Pop-up Window -> Mention of Homework Assignment for CS 585; Pop-up Window -> Other(s); Pop-up Window -> Release Date and Version Number
* In the generated graph only: Mention of Homework Assignment for CS 585 -> Release Date and Version Number; Name of Programmer -> Mention of Homework Assignment for CS 585; Release Date and Version Number -> Other(s)

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (select Help menu) → Help Menu Opened → (select About) → About Selected → (pop-up opens) → About Pop-up Window Displayed → Programmer Name Shown → CS 585 Homework Mention Shown → Release Date Shown → Version Number Shown → (other info included) → Additional Info Shown → (close pop-up) → About Pop-up Window Closed → (return to browser) → End | yes | Name of Programmer; Mention of Homework Assignment for CS 585; Other(s) | yes |
| 2 | Start → (select Help menu) → Help Menu Opened → (select About) → About Selected → (pop-up opens) → About Pop-up Window Displayed → Programmer Name Shown → CS 585 Homework Mention Shown → Release Date Shown → Version Number Shown → (no other info) → About Pop-up Window Closed → (return to browser) → End | yes | Name of Programmer; Mention of Homework Assignment for CS 585 | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Name of Programmer | T1, T2 | 1, 2 |
| Mention of Homework Assignment for CS 585 | T1, T2 | 1, 2 |
| Release Date and Version Number | T1, T2 | none |
| Other(s) | T2 | 1 |

Test cases covered: none (0 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (select Help menu) → Help Menu Opened → (select About) → About Selected → (pop-up opens) → About Pop-up Window Displayed → Programmer Name Shown → CS 585 Homework Mention Shown → Release Date Shown → Version Number Shown → (other info included) → Additional Info Shown → (close pop-up) → About Pop-up Window Closed → (return to browser) → End | yes | Name of Programmer; Mention of Homework Assignment for CS 585; Release Date and Version Number; Other(s) | yes |
| 2 | Start → (select Help menu) → Help Menu Opened → (select About) → About Selected → (pop-up opens) → About Pop-up Window Displayed → Programmer Name Shown → CS 585 Homework Mention Shown → Release Date Shown → Version Number Shown → (no other info) → About Pop-up Window Closed → (return to browser) → End | yes | Name of Programmer; Mention of Homework Assignment for CS 585; Release Date and Version Number | no |

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
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | met: optional items modelled as 'Additional Info Shown' | met: optional items modelled as 'Additional Info Shown' |
