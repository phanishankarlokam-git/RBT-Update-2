# B5, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 80.0 | 40.0 | 53.3 | 4 of 5 answer-set nodes found; 10 generated nodes |
| L2 arrows | strict | 25.0 | 33.3 | 28.6 | 1 of 4 answer-set pairs found; 3 generated pairs |
| L3 tests | strict | 75.0 | 20.0 | 31.6 | 3 of 4 routes walked; 1 of 5 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 50.0 | | | 1 of 2 |
| L1 nodes | lenient | 100.0 | 50.0 | 66.7 | 5 of 5 answer-set nodes found; 10 generated nodes |
| L2 arrows | lenient | 25.0 | 25.0 | 25.0 | 1 of 4 answer-set pairs found; 4 generated pairs |
| L3 tests | lenient | 100.0 | 20.0 | 33.3 | 4 of 4 routes walked; 1 of 5 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Click File Menu | “File” Menu | “File” Menu | fuzzy | yes |
| File Menu Displayed | “File” Menu | “File” Menu | fuzzy | no, duplicate |
| Open Present? | Open | Open | fuzzy | yes |
| Close Present? | Close | Close | fuzzy | yes |
| Exit Present? | Exit | Exit | fuzzy | yes |
| Extra Options Present? | nothing | Other(s) (e.g., Save) | alias: Check for extra options = Other(s). | yes |
| Extra Option Found | nothing | Other(s) (e.g., Save) | alias: An extra option on the menu = the answer set's Other(s) (e.g., Save). | no, duplicate |
| No Extra Options | nothing | nothing | none | no |
| Pass | nothing | nothing | none | no |
| Fail | nothing | nothing | none | no |

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
| 1 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (Yes) → Exit Present? → (Yes) → Extra Options Present? → (Yes) → Extra Option Found → Pass | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit | yes |
| 2 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (Yes) → Exit Present? → (Yes) → Extra Options Present? → (No) → No Extra Options → Pass | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit | no |
| 3 | Start → Click File Menu → File Menu Displayed → Open Present? → (No) → Fail | yes | “File” Menu -> Open | no |
| 4 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (No) → Fail | yes | “File” Menu -> Open; “File” Menu -> Close | no |
| 5 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (Yes) → Exit Present? → (No) → Fail | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1, 2, 3, 4, 5 |
| “File” Menu -> Close | T1, T2 | 1, 2, 4, 5 |
| “File” Menu -> Exit | T1, T2 | 1, 2, 5 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | none |

Test cases covered: T1 (1 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (Yes) → Exit Present? → (Yes) → Extra Options Present? → (Yes) → Extra Option Found → Pass | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Other(s) (e.g., Save) | yes |
| 2 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (Yes) → Exit Present? → (Yes) → Extra Options Present? → (No) → No Extra Options → Pass | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit; “File” Menu -> Other(s) (e.g., Save) | no |
| 3 | Start → Click File Menu → File Menu Displayed → Open Present? → (No) → Fail | yes | “File” Menu -> Open | no |
| 4 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (No) → Fail | yes | “File” Menu -> Open; “File” Menu -> Close | no |
| 5 | Start → Click File Menu → File Menu Displayed → Open Present? → (Yes) → Close Present? → (Yes) → Exit Present? → (No) → Fail | yes | “File” Menu -> Open; “File” Menu -> Close; “File” Menu -> Exit | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “File” Menu -> Open | T1, T2 | 1, 2, 3, 4, 5 |
| “File” Menu -> Close | T1, T2 | 1, 2, 4, 5 |
| “File” Menu -> Exit | T1, T2 | 1, 2, 5 |
| “File” Menu -> Other(s) (e.g., Save) | T2 | 1, 2 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Extra Option Found' | met: optional items modelled as 'Extra Option Found' |
