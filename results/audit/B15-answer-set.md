# B15: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set nodes found; 6 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | strict | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 4 of 4 paths needed; test cases covered 2/2 |
| L4 sparkles | strict | 100.0 | | | 2 of 2 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set nodes found; 6 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 4 of 4 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 100.0 | | | 2 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Browser | Browser | exact | yes |
| Pop-up Window | Pop-up Window | Pop-up Window | exact | yes |
| Name of Programmer | Name of Programmer | Name of Programmer | exact | yes |
| Mention of Homework Assignment for CS 585 | Mention of Homework Assignment for CS 585 | Mention of Homework Assignment for CS 585 | exact | yes |
| Release Date and Version Number | Release Date and Version Number | Release Date and Version Number | exact | yes |
| Other(s) | Other(s) | Other(s) | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window; Pop-up Window -> Mention of Homework Assignment for CS 585; Pop-up Window -> Name of Programmer; Pop-up Window -> Other(s); Pop-up Window -> Release Date and Version Number
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [click “Help - -> About”] → Pop-up Window → Name of Programmer | yes | Name of Programmer | yes |
| 2 | Browser → [click “Help - -> About”] → Pop-up Window → Mention of Homework Assignment for CS 585 | yes | Mention of Homework Assignment for CS 585 | yes |
| 3 | Browser → [click “Help - -> About”] → Pop-up Window → Release Date and Version Number | yes | Release Date and Version Number | yes |
| 4 | Browser → [click “Help - -> About”] → Pop-up Window → Other(s) | yes | Other(s) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Name of Programmer | T1, T2 | 1 |
| Mention of Homework Assignment for CS 585 | T1, T2 | 2 |
| Release Date and Version Number | T1, T2 | 3 |
| Other(s) | T2 | 4 |

Test cases covered: T1, T2 (2 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [click “Help - -> About”] → Pop-up Window → Name of Programmer | yes | Name of Programmer | yes |
| 2 | Browser → [click “Help - -> About”] → Pop-up Window → Mention of Homework Assignment for CS 585 | yes | Mention of Homework Assignment for CS 585 | yes |
| 3 | Browser → [click “Help - -> About”] → Pop-up Window → Release Date and Version Number | yes | Release Date and Version Number | yes |
| 4 | Browser → [click “Help - -> About”] → Pop-up Window → Other(s) | yes | Other(s) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Name of Programmer | T1, T2 | 1 |
| Mention of Homework Assignment for CS 585 | T1, T2 | 2 |
| Release Date and Version Number | T1, T2 | 3 |
| Other(s) | T2 | 4 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | met: composition from 'Pop-up Window' to ['MH', 'NP', 'OTH', 'RDV'] | met: composition from 'Pop-up Window' to ['MH', 'NP', 'OTH', 'RDV'] |
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | met: optional items modelled as 'Other(s)' | met: optional items modelled as 'Other(s)' |
