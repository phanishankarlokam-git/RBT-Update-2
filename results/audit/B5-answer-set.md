# B5: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set nodes found; 5 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 4 of 4 answer-set pairs found; 4 generated pairs |
| L3 tests | strict | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 4 of 4 paths needed; test cases covered 2/2 |
| L4 sparkles | strict | 100.0 | | | 2 of 2 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set nodes found; 5 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 4 of 4 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 4 of 4 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 100.0 | | | 2 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| “File” Menu | “File” Menu | “File” Menu | exact | yes |
| Open | Open | Open | exact | yes |
| Close | Close | Close | exact | yes |
| Exit | Exit | Exit | exact | yes |
| Other(s) (e.g., Save) | Other(s) (e.g., Save) | Other(s) (e.g., Save) | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Open; “File” Menu -> Other(s) (e.g., Save)
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | “File” Menu → Open | yes | “File” Menu -> Open | yes |
| 2 | “File” Menu → Close | yes | “File” Menu -> Close | yes |
| 3 | “File” Menu → Exit | yes | “File” Menu -> Exit | yes |
| 4 | “File” Menu → Other(s) (e.g., Save) | yes | “File” Menu -> Other(s) (e.g., Save) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1 |
| “File” Menu -> Close | T1, T2 | 2 |
| “File” Menu -> Exit | T1, T2 | 3 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | 4 |

Test cases covered: T1, T2 (2 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | “File” Menu → Open | yes | “File” Menu -> Open | yes |
| 2 | “File” Menu → Close | yes | “File” Menu -> Close | yes |
| 3 | “File” Menu → Exit | yes | “File” Menu -> Exit | yes |
| 4 | “File” Menu → Other(s) (e.g., Save) | yes | “File” Menu -> Other(s) (e.g., Save) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1 |
| “File” Menu -> Close | T1, T2 | 2 |
| “File” Menu -> Exit | T1, T2 | 3 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | 4 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | met: composition from '“File” Menu' to ['CLOSE', 'EXIT', 'OPEN', 'OTH'] | met: composition from '“File” Menu' to ['CLOSE', 'EXIT', 'OPEN', 'OTH'] |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Other(s) (e.g., Save)' | met: optional items modelled as 'Other(s) (e.g., Save)' |
