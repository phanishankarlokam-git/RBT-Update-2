# B20: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 7 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 8 of 8 answer-set pairs found; 8 generated pairs |
| L3 tests | strict | 100.0 | 100.0 | 100.0 | 10 of 10 routes walked; 8 of 8 paths needed; test cases covered 6/6 |
| L4 sparkles | strict | 100.0 | | | 5 of 5 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 7 of 7 answer-set nodes found; 7 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 8 of 8 answer-set pairs found; 8 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 10 of 10 routes walked; 8 of 8 paths needed; test cases covered 6/6 |
| L4 sparkles | lenient | 100.0 | | | 5 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Browser | Browser | exact | yes |
| To-be-opened resource is a valid URL? | To-be-opened resource is a valid URL? | To-be-opened resource is a valid URL? | exact | yes |
| Document of the URL Downloaded and Displayed as “current” | Document of the URL Downloaded and Displayed as “current” | Document of the URL Downloaded and Displayed as “current” | exact | yes |
| Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | exact | yes |
| Displaying No “current” Document | Displaying No “current” Document | Displaying No “current” Document | exact | yes |
| Showing an Error Message in the HTML Display Zone | Showing an Error Message in the HTML Display Zone | Showing an Error Message in the HTML Display Zone | exact | yes |
| Displaying the Last “current” Document | Displaying the Last “current” Document | Displaying the Last “current” Document | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> To-be-opened resource is a valid URL?; To-be-opened resource is a valid URL? -> Document of the URL Downloaded and Displayed as “current”; To-be-opened resource is a valid URL? -> Displaying No “current” Document; To-be-opened resource is a valid URL? -> Pushing “current” Document into the “Back” Stack; To-be-opened resource is a valid URL? -> Showing an Error Message in the HTML Display Zone; Displaying No “current” Document -> Displaying the Last “current” Document; Pushing “current” Document into the “Back” Stack -> Displaying the Last “current” Document; Showing an Error Message in the HTML Display Zone -> Displaying the Last “current” Document
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [yes] → Document of the URL Downloaded and Displayed as “current” | yes | (enter address field) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 2 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [no] → [bar] → Pushing “current” Document into the “Back” Stack → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (enter address field) -> Pushing “current” Document into the “Back” Stack; (enter address field) -> Displaying the Last “current” Document | yes |
| 3 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [no] → [bar] → Displaying No “current” Document → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (enter address field) -> Displaying No “current” Document; (enter address field) -> Displaying the Last “current” Document | yes |
| 4 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [no] → [bar] → Showing an Error Message in the HTML Display Zone → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (enter address field) -> Showing an Error Message in the HTML Display Zone; (enter address field) -> Displaying the Last “current” Document | yes |
| 5 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [yes] → Document of the URL Downloaded and Displayed as “current” | yes | (click File Open) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 6 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [no] → [bar] → Pushing “current” Document into the “Back” Stack → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (click File Open) -> Pushing “current” Document into the “Back” Stack; (click File Open) -> Displaying the Last “current” Document | yes |
| 7 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [no] → [bar] → Displaying No “current” Document → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (click File Open) -> Displaying No “current” Document; (click File Open) -> Displaying the Last “current” Document | yes |
| 8 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [no] → [bar] → Showing an Error Message in the HTML Display Zone → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (click File Open) -> Showing an Error Message in the HTML Display Zone; (click File Open) -> Displaying the Last “current” Document | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (enter address field) -> Document of the URL Downloaded and Displayed as “current” | T1a | 1 |
| (enter address field) -> Pushing “current” Document into the “Back” Stack | T2a | 2 |
| (enter address field) -> Displaying No “current” Document | T2a | 3 |
| (enter address field) -> Showing an Error Message in the HTML Display Zone | T2a | 4 |
| (enter address field) -> Displaying the Last “current” Document | T3a | 2, 3, 4 |
| (click File Open) -> Document of the URL Downloaded and Displayed as “current” | T1b | 5 |
| (click File Open) -> Pushing “current” Document into the “Back” Stack | T2b | 6 |
| (click File Open) -> Displaying No “current” Document | T2b | 7 |
| (click File Open) -> Showing an Error Message in the HTML Display Zone | T2b | 8 |
| (click File Open) -> Displaying the Last “current” Document | T3b | 6, 7, 8 |

Test cases covered: T1a, T2a, T3a, T1b, T2b, T3b (6 of 6).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [yes] → Document of the URL Downloaded and Displayed as “current” | yes | (enter address field) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 2 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [no] → [bar] → Pushing “current” Document into the “Back” Stack → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (enter address field) -> Pushing “current” Document into the “Back” Stack; (enter address field) -> Displaying the Last “current” Document | yes |
| 3 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [no] → [bar] → Displaying No “current” Document → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (enter address field) -> Displaying No “current” Document; (enter address field) -> Displaying the Last “current” Document | yes |
| 4 | Browser → [enter “address field”] → To-be-opened resource is a valid URL? → [no] → [bar] → Showing an Error Message in the HTML Display Zone → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (enter address field) -> Showing an Error Message in the HTML Display Zone; (enter address field) -> Displaying the Last “current” Document | yes |
| 5 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [yes] → Document of the URL Downloaded and Displayed as “current” | yes | (click File Open) -> Document of the URL Downloaded and Displayed as “current” | yes |
| 6 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [no] → [bar] → Pushing “current” Document into the “Back” Stack → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (click File Open) -> Pushing “current” Document into the “Back” Stack; (click File Open) -> Displaying the Last “current” Document | yes |
| 7 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [no] → [bar] → Displaying No “current” Document → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (click File Open) -> Displaying No “current” Document; (click File Open) -> Displaying the Last “current” Document | yes |
| 8 | Browser → [click “File - -> Open”] → To-be-opened resource is a valid URL? → [no] → [bar] → Showing an Error Message in the HTML Display Zone → [bar] → [click “Back” button] → Displaying the Last “current” Document | yes | (click File Open) -> Showing an Error Message in the HTML Display Zone; (click File Open) -> Displaying the Last “current” Document | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (enter address field) -> Document of the URL Downloaded and Displayed as “current” | T1a | 1 |
| (enter address field) -> Pushing “current” Document into the “Back” Stack | T2a | 2 |
| (enter address field) -> Displaying No “current” Document | T2a | 3 |
| (enter address field) -> Showing an Error Message in the HTML Display Zone | T2a | 4 |
| (enter address field) -> Displaying the Last “current” Document | T3a | 2, 3, 4 |
| (click File Open) -> Document of the URL Downloaded and Displayed as “current” | T1b | 5 |
| (click File Open) -> Pushing “current” Document into the “Back” Stack | T2b | 6 |
| (click File Open) -> Displaying No “current” Document | T2b | 7 |
| (click File Open) -> Showing an Error Message in the HTML Display Zone | T2b | 8 |
| (click File Open) -> Displaying the Last “current” Document | T3b | 6, 7, 8 |

Test cases covered: T1a, T2a, T3a, T1b, T2b, T3b (6 of 6).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: the TWO transitions coming out of “Browser” | converge | met: one shared node reached from all branches | met: one shared node reached from all branches |
| S2: use of “To-be-opened resource” to ABSTRACT both “address field” entering and “File - -> Open” clicking | label_has | met: marks present | met: marks present |
| S3: the split to organize the three “AND” actions | fanout | met: 'To-be-opened resource is a valid URL?' splits into ['DNC', 'PCB', 'SEM'] | met: 'To-be-opened resource is a valid URL?' splits into ['DNC', 'PCB', 'SEM'] |
| S4: the merge to synchronize (bring back) the completion of the three actions | fanin | met: '[bar]' joins ['DNC', 'PCB', 'SEM'] | met: '[bar]' joins ['DNC', 'PCB', 'SEM'] |
| S5: make sure that the click “Back” button is on the “no” branch and is coming out of the merge | fanin | met: '[bar]' joins ['DNC', 'PCB', 'SEM'] | met: '[bar]' joins ['DNC', 'PCB', 'SEM'] |
