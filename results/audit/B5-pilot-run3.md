# B5, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 80.0 | 44.4 | 57.1 | 4 of 5 answer-set nodes found; 9 generated nodes |
| L2 arrows | strict | 25.0 | 33.3 | 28.6 | 1 of 4 answer-set pairs found; 3 generated pairs |
| L3 tests | strict | 75.0 | 50.0 | 60.0 | 3 of 4 routes walked; 1 of 2 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 50.0 | | | 1 of 2 |
| L1 nodes | lenient | 100.0 | 55.6 | 71.4 | 5 of 5 answer-set nodes found; 9 generated nodes |
| L2 arrows | lenient | 25.0 | 25.0 | 25.0 | 1 of 4 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 100.0 | 50.0 | 66.7 | 4 of 4 routes walked; 1 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Click "File" | nothing | nothing | none | no |
| File Menu Displayed | “File” Menu | “File” Menu | fuzzy | yes |
| Verify "Open" Present | Open | Open | contains | yes |
| Verify "Close" Present | Close | Close | contains | yes |
| Verify "Exit" Present | Exit | Exit | contains | yes |
| Other Options Present? | nothing | Other(s) (e.g., Save) | alias: Check for other options = Other(s). | yes |
| Additional Options (e.g. "Save") Shown | nothing | Other(s) (e.g., Save) | alias: Additional options, e.g. Save = Other(s) (e.g., Save). | no, duplicate |
| No Additional Options Shown | nothing | nothing | none | no |
| Dismiss Menu | nothing | nothing | none | no |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: “File” Menu -> Open
* In the answer set only: “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Other(s) (e.g., Save)
* In the generated graph only: Close -> Exit; Exit -> Other(s) (e.g., Save); Open -> Close

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Click "File" → File Menu Displayed → Verify "Open" Present → Verify "Close" Present → Verify "Exit" Present → Other Options Present? → (Yes) → Additional Options (e.g. "Save") Shown → Dismiss Menu → End | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit | yes |
| 2 | Start → Click "File" → File Menu Displayed → Verify "Open" Present → Verify "Close" Present → Verify "Exit" Present → Other Options Present? → (No) → No Additional Options Shown → Dismiss Menu → End | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1, 2 |
| “File” Menu -> Close | T1, T2 | 1, 2 |
| “File” Menu -> Exit | T1, T2 | 1, 2 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | none |

Test cases covered: T1 (1 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Click "File" → File Menu Displayed → Verify "Open" Present → Verify "Close" Present → Verify "Exit" Present → Other Options Present? → (Yes) → Additional Options (e.g. "Save") Shown → Dismiss Menu → End | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Other(s) (e.g., Save) | yes |
| 2 | Start → Click "File" → File Menu Displayed → Verify "Open" Present → Verify "Close" Present → Verify "Exit" Present → Other Options Present? → (No) → No Additional Options Shown → Dismiss Menu → End | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Other(s) (e.g., Save) | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1, 2 |
| “File” Menu -> Close | T1, T2 | 1, 2 |
| “File” Menu -> Exit | T1, T2 | 1, 2 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | 1, 2 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Additional Options (e.g. "Save") Shown' | met: optional items modelled as 'Additional Options (e.g. "Save") Shown' |
