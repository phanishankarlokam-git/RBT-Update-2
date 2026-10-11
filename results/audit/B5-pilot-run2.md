# B5, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 80.0 | 57.1 | 66.7 | 4 of 5 answer-set nodes found; 7 generated nodes |
| L2 arrows | strict | 75.0 | 60.0 | 66.7 | 3 of 4 answer-set pairs found; 5 generated pairs |
| L3 tests | strict | 75.0 | 75.0 | 75.0 | 3 of 4 routes walked; 3 of 4 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 50.0 | | | 1 of 2 |
| L1 nodes | lenient | 100.0 | 71.4 | 83.3 | 5 of 5 answer-set nodes found; 7 generated nodes |
| L2 arrows | lenient | 100.0 | 57.1 | 72.7 | 4 of 4 answer-set pairs found; 7 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 4 of 4 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| File Menu Closed | “File” Menu | “File” Menu | fuzzy | yes |
| File Menu Open | “File” Menu | “File” Menu | fuzzy | no, duplicate |
| "Open" Selected | Open | Open | fuzzy | yes |
| "Close" Selected | Close | Close | fuzzy | yes |
| "Exit" Selected | Exit | Exit | fuzzy | yes |
| Additional Option Selected (e.g. "Save") | nothing | Other(s) (e.g., Save) | alias: Additional option, e.g. Save = Other(s) (e.g., Save). | yes |
| Application Exited | Exit | Exit | fuzzy | no, duplicate |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Open; “File” Menu -> Other(s) (e.g., Save)
* In the answer set only: none
* In the generated graph only: Close -> “File” Menu; Open -> “File” Menu; Other(s) (e.g., Save) -> “File” Menu

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → File Menu Closed → (click "File") → File Menu Open → (select "Open") → "Open" Selected → (menu dismissed) → File Menu Closed | yes | “File” Menu -> Open | yes |
| 2 | Start → File Menu Closed → (click "File") → File Menu Open → (select "Close") → "Close" Selected → (menu dismissed) → File Menu Closed | yes | “File” Menu -> Close | yes |
| 3 | Start → File Menu Closed → (click "File") → File Menu Open → (select optional item, e.g. "Save") → Additional Option Selected (e.g. "Save") → (menu dismissed) → File Menu Closed | yes | none | no |
| 4 | Start → File Menu Closed → (click "File") → File Menu Open → (select "Exit") → "Exit" Selected → (application terminates) → Application Exited | yes | “File” Menu -> Exit | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1 |
| “File” Menu -> Close | T1, T2 | 2 |
| “File” Menu -> Exit | T1, T2 | 4 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | none |

Test cases covered: T1 (1 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → File Menu Closed → (click "File") → File Menu Open → (select "Open") → "Open" Selected → (menu dismissed) → File Menu Closed | yes | “File” Menu -> Open | yes |
| 2 | Start → File Menu Closed → (click "File") → File Menu Open → (select "Close") → "Close" Selected → (menu dismissed) → File Menu Closed | yes | “File” Menu -> Close | yes |
| 3 | Start → File Menu Closed → (click "File") → File Menu Open → (select optional item, e.g. "Save") → Additional Option Selected (e.g. "Save") → (menu dismissed) → File Menu Closed | yes | “File” Menu -> Other(s) (e.g., Save) | yes |
| 4 | Start → File Menu Closed → (click "File") → File Menu Open → (select "Exit") → "Exit" Selected → (application terminates) → Application Exited | yes | “File” Menu -> Exit | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1 |
| “File” Menu -> Close | T1, T2 | 2 |
| “File” Menu -> Exit | T1, T2 | 4 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | 3 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Additional Option Selected (e.g. "Save")' | met: optional items modelled as 'Additional Option Selected (e.g. "Save")' |
