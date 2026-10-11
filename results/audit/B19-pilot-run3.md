# B19, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 0.0 | 0.0 | 0.0 | 0 of 3 answer-set nodes found; 7 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 2 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 0.0 | 0.0 | 0.0 | 0 of 2 routes walked; 0 of 2 paths needed; test cases covered 0/1 |
| L4 sparkles | strict | 0.0 | | | 0 of 2 |
| L1 nodes | lenient | 100.0 | 42.9 | 60.0 | 3 of 3 answer-set nodes found; 7 generated nodes |
| L2 arrows | lenient | 50.0 | 50.0 | 50.0 | 1 of 2 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 100.0 | 50.0 | 66.7 | 2 of 2 routes walked; 1 of 2 paths needed; test cases covered 1/1 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Current Page Displayed | nothing | Browser | alias: The browser showing its current page = the Browser start node. | yes |
| History Stacks Empty | nothing | nothing | none | no |
| History Stacks Populated | nothing | nothing | none | no |
| Reload Pressed | nothing | nothing | none | no |
| Page Re-Downloaded From Same Location | nothing | Downloading Current Page Again | alias: Downloading the current page again from its location. | yes |
| Back and Forward Stacks Unchanged | nothing | Keeping History Stack Unchanged | alias: Back and forward stacks unchanged = history stack unchanged. | yes |
| Reloaded Page Displayed | nothing | nothing | none | no |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Downloading Current Page Again
* In the answer set only: Browser -> Keeping History Stack Unchanged
* In the generated graph only: Downloading Current Page Again -> Keeping History Stack Unchanged

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Current Page Displayed → History Stacks Empty → Reload Pressed → Page Re-Downloaded From Same Location → Back and Forward Stacks Unchanged → Reloaded Page Displayed | yes | none | no |
| 2 | Current Page Displayed → History Stacks Populated → Reload Pressed → Page Re-Downloaded From Same Location → Back and Forward Stacks Unchanged → Reloaded Page Displayed | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Keeping History Stack Unchanged | T1 | none |
| Downloading Current Page Again | T1 | none |

Test cases covered: none (0 of 1).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Current Page Displayed → History Stacks Empty → Reload Pressed → Page Re-Downloaded From Same Location → Back and Forward Stacks Unchanged → Reloaded Page Displayed | yes | Keeping History Stack Unchanged; Downloading Current Page Again | yes |
| 2 | Current Page Displayed → History Stacks Populated → Reload Pressed → Page Re-Downloaded From Same Location → Back and Forward Stacks Unchanged → Reloaded Page Displayed | yes | Keeping History Stack Unchanged; Downloading Current Page Again | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Keeping History Stack Unchanged | T1 | 1, 2 |
| Downloading Current Page Again | T1 | 1, 2 |

Test cases covered: T1 (1 of 1).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: split | fanout | not met: no split into the required nodes | not met: no split into the required nodes |
| S2: make sure that “Keeping History Stack Unchanged” is explicitly modeled | concepts | not met: missing: KHSU | met: all present |
