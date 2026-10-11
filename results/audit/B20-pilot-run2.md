# B20, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 57.1 | 36.4 | 44.4 | 4 of 7 answer-set nodes found; 11 generated nodes |
| L2 arrows | strict | 12.5 | 33.3 | 18.2 | 1 of 8 answer-set pairs found; 3 generated pairs |
| L3 tests | strict | 80.0 | 50.0 | 61.5 | 8 of 10 routes walked; 2 of 4 paths needed; test cases covered 4/6 |
| L4 sparkles | strict | 0.0 | | | 0 of 5 |
| L1 nodes | lenient | 85.7 | 54.5 | 66.7 | 6 of 7 answer-set nodes found; 11 generated nodes |
| L2 arrows | lenient | 37.5 | 60.0 | 46.2 | 3 of 8 answer-set pairs found; 5 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 10 of 10 routes walked; 4 of 4 paths needed; test cases covered 6/6 |
| L4 sparkles | lenient | 20.0 | | | 1 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Enter Key Pressed in Address Field | nothing | nothing | none | no |
| File > Open Selected | nothing | nothing | none | no |
| Retrieve and Analyze Text | nothing | nothing | none | no |
| Correct URL? | nothing | To-be-opened resource is a valid URL? | alias: The URL validity check. | yes |
| Download Document | nothing | Document of the URL Downloaded and Displayed as “current” | alias: Downloading the document of a correct URL (it then becomes current). | yes |
| Push Current Document to Back Stack | Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | exact | yes |
| No Current Document | Displaying No “current” Document | Displaying No “current” Document | fuzzy | yes |
| Display Error Message | Showing an Error Message in the HTML Display Zone | Showing an Error Message in the HTML Display Zone | fuzzy | yes |
| Back Button Pressed | nothing | nothing | none | no |
| Restore Last Page as Current | nothing | Displaying the Last “current” Document | alias: As above. | yes |
| Document Is Current | Displaying the Last “current” Document | nothing | alias: Shared end state of BOTH the download branch and the Back branch; the step before it says which one. The automatic rule matched it to the Back outcome only. | no |

Answer-set nodes not found (lenient): Browser

## L2. Arrows between shared nodes (lenient)

* Found in both: To-be-opened resource is a valid URL? -> Document of the URL Downloaded and Displayed as “current”; To-be-opened resource is a valid URL? -> Pushing “current” Document into the “Back” Stack; Showing an Error Message in the HTML Display Zone -> Displaying the Last “current” Document
* In the answer set only: Browser -> To-be-opened resource is a valid URL?; To-be-opened resource is a valid URL? -> Displaying No “current” Document; To-be-opened resource is a valid URL? -> Showing an Error Message in the HTML Display Zone; Displaying No “current” Document -> Displaying the Last “current” Document; Pushing “current” Document into the “Back” Stack -> Displaying the Last “current” Document
* In the generated graph only: Displaying No “current” Document -> Showing an Error Message in the HTML Display Zone; Pushing “current” Document into the “Back” Stack -> Displaying No “current” Document

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Enter Key Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → (Yes) → Download Document → Document Is Current | yes | (enter address field) -> Displaying the Last “current” Document | no |
| 2 | Start → Enter Key Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → (No) → Push Current Document to Back Stack → No Current Document → Display Error Message → Back Button Pressed → Restore Last Page as Current → Document Is Current | yes | (enter address field) -> Pushing “current” Document into the “Back” Stack; (enter address field) -> Displaying No “current” Document; (enter address field) -> Showing an Error Message in the HTML Display Zone; (enter address field) -> Displaying the Last “current” Document | yes |
| 3 | Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → (Yes) → Download Document → Document Is Current | yes | (click File Open) -> Displaying the Last “current” Document | no |
| 4 | Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → (No) → Push Current Document to Back Stack → No Current Document → Display Error Message → Back Button Pressed → Restore Last Page as Current → Document Is Current | yes | (click File Open) -> Pushing “current” Document into the “Back” Stack; (click File Open) -> Displaying No “current” Document; (click File Open) -> Showing an Error Message in the HTML Display Zone; (click File Open) -> Displaying the Last “current” Document | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (enter address field) -> Document of the URL Downloaded and Displayed as “current” | T1a | none |
| (enter address field) -> Pushing “current” Document into the “Back” Stack | T2a | 2 |
| (enter address field) -> Displaying No “current” Document | T2a | 2 |
| (enter address field) -> Showing an Error Message in the HTML Display Zone | T2a | 2 |
| (enter address field) -> Displaying the Last “current” Document | T3a | 1, 2 |
| (click File Open) -> Document of the URL Downloaded and Displayed as “current” | T1b | none |
| (click File Open) -> Pushing “current” Document into the “Back” Stack | T2b | 4 |
| (click File Open) -> Displaying No “current” Document | T2b | 4 |
| (click File Open) -> Showing an Error Message in the HTML Display Zone | T2b | 4 |
| (click File Open) -> Displaying the Last “current” Document | T3b | 3, 4 |

Test cases covered: T2a, T3a, T2b, T3b (4 of 6).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Enter Key Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → (Yes) → Download Document → Document Is Current | yes | (enter address field) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 2 | Start → Enter Key Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → (No) → Push Current Document to Back Stack → No Current Document → Display Error Message → Back Button Pressed → Restore Last Page as Current → Document Is Current | yes | (enter address field) -> Pushing “current” Document into the “Back” Stack; (enter address field) -> Displaying No “current” Document; (enter address field) -> Showing an Error Message in the HTML Display Zone; (enter address field) -> Displaying the Last “current” Document | yes |
| 3 | Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → (Yes) → Download Document → Document Is Current | yes | (click File Open) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 4 | Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → (No) → Push Current Document to Back Stack → No Current Document → Display Error Message → Back Button Pressed → Restore Last Page as Current → Document Is Current | yes | (click File Open) -> Pushing “current” Document into the “Back” Stack; (click File Open) -> Displaying No “current” Document; (click File Open) -> Showing an Error Message in the HTML Display Zone; (click File Open) -> Displaying the Last “current” Document | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (enter address field) -> Document of the URL Downloaded and Displayed as “current” | T1a | 1 |
| (enter address field) -> Pushing “current” Document into the “Back” Stack | T2a | 2 |
| (enter address field) -> Displaying No “current” Document | T2a | 2 |
| (enter address field) -> Showing an Error Message in the HTML Display Zone | T2a | 2 |
| (enter address field) -> Displaying the Last “current” Document | T3a | 2 |
| (click File Open) -> Document of the URL Downloaded and Displayed as “current” | T1b | 3 |
| (click File Open) -> Pushing “current” Document into the “Back” Stack | T2b | 4 |
| (click File Open) -> Displaying No “current” Document | T2b | 4 |
| (click File Open) -> Showing an Error Message in the HTML Display Zone | T2b | 4 |
| (click File Open) -> Displaying the Last “current” Document | T3b | 4 |

Test cases covered: T1a, T2a, T3a, T1b, T2b, T3b (6 of 6).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: the TWO transitions coming out of “Browser” | converge | not met: 0 nodes stand for DEC (need exactly one) | met: one shared node reached from all branches |
| S2: use of “To-be-opened resource” to ABSTRACT both “address field” entering and “File - -> Open” clicking | label_has | not met: missing for: DEC | not met: missing for: DEC |
| S3: the split to organize the three “AND” actions | fanout | not met: no split into the required nodes | not met: no split into the required nodes |
| S4: the merge to synchronize (bring back) the completion of the three actions | fanin | not met: no join of the required nodes | not met: no join of the required nodes |
| S5: make sure that the click “Back” button is on the “no” branch and is coming out of the merge | fanin | not met: no join of the required nodes leading to DLC | not met: no join of the required nodes leading to DLC |
