# B20, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 57.1 | 36.4 | 44.4 | 4 of 7 answer-set nodes found; 11 generated nodes |
| L2 arrows | strict | 12.5 | 25.0 | 16.7 | 1 of 8 answer-set pairs found; 4 generated pairs |
| L3 tests | strict | 40.0 | 50.0 | 44.4 | 4 of 10 routes walked; 1 of 2 paths needed; test cases covered 2/6 |
| L4 sparkles | strict | 0.0 | | | 0 of 5 |
| L1 nodes | lenient | 85.7 | 54.5 | 66.7 | 6 of 7 answer-set nodes found; 11 generated nodes |
| L2 arrows | lenient | 37.5 | 42.9 | 40.0 | 3 of 8 answer-set pairs found; 7 generated pairs |
| L3 tests | lenient | 50.0 | 100.0 | 66.7 | 5 of 10 routes walked; 2 of 2 paths needed; test cases covered 3/6 |
| L4 sparkles | lenient | 20.0 | | | 1 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Enter Pressed in Address Field | nothing | nothing | none | no |
| File > Open Selected | nothing | nothing | none | no |
| Retrieve and Analyze Text | nothing | nothing | none | no |
| Correct URL? | nothing | To-be-opened resource is a valid URL? | alias: The URL validity check. | yes |
| Download Document | nothing | Document of the URL Downloaded and Displayed as “current” | alias: Downloading the document of a correct URL (it then becomes current). | yes |
| Document Becomes Current | nothing | nothing | none | no |
| Push Current Document to Back Stack | Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | exact | yes |
| No Current Document | Displaying No “current” Document | Displaying No “current” Document | fuzzy | yes |
| Display Error Message in HTML Display Zone | Showing an Error Message in the HTML Display Zone | Showing an Error Message in the HTML Display Zone | fuzzy | yes |
| Back Button Pressed | nothing | nothing | none | no |
| Restore Last Document as Current | Displaying the Last “current” Document | Displaying the Last “current” Document | fuzzy | yes |

Answer-set nodes not found (lenient): Browser

## L2. Arrows between shared nodes (lenient)

* Found in both: To-be-opened resource is a valid URL? -> Document of the URL Downloaded and Displayed as “current”; To-be-opened resource is a valid URL? -> Pushing “current” Document into the “Back” Stack; Showing an Error Message in the HTML Display Zone -> Displaying the Last “current” Document
* In the answer set only: Browser -> To-be-opened resource is a valid URL?; To-be-opened resource is a valid URL? -> Displaying No “current” Document; To-be-opened resource is a valid URL? -> Showing an Error Message in the HTML Display Zone; Displaying No “current” Document -> Displaying the Last “current” Document; Pushing “current” Document into the “Back” Stack -> Displaying the Last “current” Document
* In the generated graph only: Document of the URL Downloaded and Displayed as “current” -> To-be-opened resource is a valid URL?; Displaying the Last “current” Document -> To-be-opened resource is a valid URL?; Displaying No “current” Document -> Showing an Error Message in the HTML Display Zone; Pushing “current” Document into the “Back” Stack -> Displaying No “current” Document

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Enter Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → (Yes) → Download Document → Document Becomes Current → Start | yes | none | no |
| 2 | Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → (No) → Push Current Document to Back Stack → No Current Document → Display Error Message in HTML Display Zone → Back Button Pressed → Restore Last Document as Current → Start | yes | (click File Open) -> Pushing “current” Document into the “Back” Stack; (click File Open) -> Displaying No “current” Document; (click File Open) -> Showing an Error Message in the HTML Display Zone; (click File Open) -> Displaying the Last “current” Document | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (enter address field) -> Document of the URL Downloaded and Displayed as “current” | T1a | none |
| (enter address field) -> Pushing “current” Document into the “Back” Stack | T2a | none |
| (enter address field) -> Displaying No “current” Document | T2a | none |
| (enter address field) -> Showing an Error Message in the HTML Display Zone | T2a | none |
| (enter address field) -> Displaying the Last “current” Document | T3a | none |
| (click File Open) -> Document of the URL Downloaded and Displayed as “current” | T1b | none |
| (click File Open) -> Pushing “current” Document into the “Back” Stack | T2b | 2 |
| (click File Open) -> Displaying No “current” Document | T2b | 2 |
| (click File Open) -> Showing an Error Message in the HTML Display Zone | T2b | 2 |
| (click File Open) -> Displaying the Last “current” Document | T3b | 2 |

Test cases covered: T2b, T3b (2 of 6).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Enter Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → (Yes) → Download Document → Document Becomes Current → Start | yes | (enter address field) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 2 | Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → (No) → Push Current Document to Back Stack → No Current Document → Display Error Message in HTML Display Zone → Back Button Pressed → Restore Last Document as Current → Start | yes | (click File Open) -> Pushing “current” Document into the “Back” Stack; (click File Open) -> Displaying No “current” Document; (click File Open) -> Showing an Error Message in the HTML Display Zone; (click File Open) -> Displaying the Last “current” Document | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (enter address field) -> Document of the URL Downloaded and Displayed as “current” | T1a | 1 |
| (enter address field) -> Pushing “current” Document into the “Back” Stack | T2a | none |
| (enter address field) -> Displaying No “current” Document | T2a | none |
| (enter address field) -> Showing an Error Message in the HTML Display Zone | T2a | none |
| (enter address field) -> Displaying the Last “current” Document | T3a | none |
| (click File Open) -> Document of the URL Downloaded and Displayed as “current” | T1b | none |
| (click File Open) -> Pushing “current” Document into the “Back” Stack | T2b | 2 |
| (click File Open) -> Displaying No “current” Document | T2b | 2 |
| (click File Open) -> Showing an Error Message in the HTML Display Zone | T2b | 2 |
| (click File Open) -> Displaying the Last “current” Document | T3b | 2 |

Test cases covered: T1a, T2b, T3b (3 of 6).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: the TWO transitions coming out of “Browser” | converge | not met: 0 nodes stand for DEC (need exactly one) | met: one shared node reached from all branches |
| S2: use of “To-be-opened resource” to ABSTRACT both “address field” entering and “File - -> Open” clicking | label_has | not met: missing for: DEC | not met: missing for: DEC |
| S3: the split to organize the three “AND” actions | fanout | not met: no split into the required nodes | not met: no split into the required nodes |
| S4: the merge to synchronize (bring back) the completion of the three actions | fanin | not met: no join of the required nodes | not met: no join of the required nodes |
| S5: make sure that the click “Back” button is on the “no” branch and is coming out of the merge | fanin | not met: no join of the required nodes leading to DLC | not met: no join of the required nodes leading to DLC |
