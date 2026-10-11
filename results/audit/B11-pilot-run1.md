# B11, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 2 of 2 answer-set nodes found; 2 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 2 of 2 answer-set pairs found; 2 generated pairs |
| L3 tests | strict | 100.0 | 100.0 | 100.0 | 2 of 2 routes walked; 1 of 1 paths needed; test cases covered 2/2 |
| L4 sparkles | strict | 75.0 | | | 3 of 4 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 2 of 2 answer-set nodes found; 2 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 2 of 2 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 2 of 2 routes walked; 1 of 1 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 75.0 | | | 3 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| No Current Page | No Current Page | No Current Page | exact | yes |
| Current Page | Current Page | Current Page | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Current Page -> No Current Page; No Current Page -> Current Page
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → No Current Page → (display a page) → Current Page → (display no page) → No Current Page | yes | No Current Page -> Current Page; Current Page -> No Current Page | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| No Current Page -> Current Page | T1 | 1 |
| Current Page -> No Current Page | T2 | 1 |

Test cases covered: T1, T2 (2 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → No Current Page → (display a page) → Current Page → (display no page) → No Current Page | yes | No Current Page -> Current Page; Current Page -> No Current Page | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| No Current Page -> Current Page | T1 | 1 |
| Current Page -> No Current Page | T2 | 1 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: do NOT model “Browser” at all | no_word | met: not used | met: not used |
| S2: designate “No Current Page” and “Current Page” as the two, parallel initial/starting states | entry_states | not met: not a start state: CP | not met: not a start state: CP |
| S3: use of “No Current Page” and “Current Page” as the labels of the states | uses_term | met: term used | met: term used |
| S4: the XOR status is modeled as two separate states | concepts | met: all present | met: all present |
