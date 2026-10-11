# B16, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 33.3 | 50.0 | 40.0 | 2 of 6 answer-set nodes found; 4 generated nodes |
| L2 arrows | strict | 20.0 | 50.0 | 28.6 | 1 of 5 answer-set pairs found; 2 generated pairs |
| L3 tests | strict | 50.0 | 100.0 | 66.7 | 2 of 4 routes walked; 2 of 2 paths needed; test cases covered 2/3 |
| L4 sparkles | strict | 0.0 | | | 0 of 5 |
| L1 nodes | lenient | 33.3 | 50.0 | 40.0 | 2 of 6 answer-set nodes found; 4 generated nodes |
| L2 arrows | lenient | 20.0 | 50.0 | 28.6 | 1 of 5 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 75.0 | 100.0 | 85.7 | 3 of 4 routes walked; 2 of 2 paths needed; test cases covered 2/3 |
| L4 sparkles | lenient | 0.0 | | | 0 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| No Previous Page | nothing | nothing | none | no |
| Previous Page Exists | Previous page exists? | Previous page exists? | exact | yes |
| Back Button Disabled (Visible) | “Back” Button Disabled | “Back” Button Disabled | fuzzy | yes |
| Back Click Yields No Action | nothing | nothing | alias: A Back click that does nothing. | no |

Answer-set nodes not found (lenient): Browser, “Back” Button Clickable, Update History Stack, Current Page = Previous Page

## L2. Arrows between shared nodes (lenient)

* Found in both: Previous page exists? -> “Back” Button Disabled
* In the answer set only: “Back” Button Clickable -> Current Page = Previous Page; “Back” Button Clickable -> Update History Stack; Browser -> Previous page exists?; Previous page exists? -> “Back” Button Clickable
* In the generated graph only: “Back” Button Disabled -> Previous page exists?

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (browser launch) → No Previous Page → (navigate to new page) → Previous Page Exists → (navigate to new page / click Back (previous page still remains)) → Previous Page Exists → (navigate to new page / click Back (previous page still remains)) → Previous Page Exists → (click Back (stack becomes empty)) → No Previous Page → (Back shown disabled but visible) → Back Button Disabled (Visible) → (no state change) → No Previous Page | yes | “Back” Button Disabled | yes |
| 2 | Start → (browser launch) → No Previous Page → (click Back (button stays enabled)) → Back Click Yields No Action → (no state change) → No Previous Page | yes | (no \| no previous page) -> (do nothing \| no action) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | 1 |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 2 |
| (yes \| previous page exists) -> Update History Stack | T3 | none |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | none |

Test cases covered: T1, T2 (2 of 3).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (browser launch) → No Previous Page → (navigate to new page) → Previous Page Exists → (navigate to new page / click Back (previous page still remains)) → Previous Page Exists → (navigate to new page / click Back (previous page still remains)) → Previous Page Exists → (click Back (stack becomes empty)) → No Previous Page → (Back shown disabled but visible) → Back Button Disabled (Visible) → (no state change) → No Previous Page | yes | “Back” Button Disabled; (yes \| previous page exists) -> Current Page = Previous Page | yes |
| 2 | Start → (browser launch) → No Previous Page → (click Back (button stays enabled)) → Back Click Yields No Action → (no state change) → No Previous Page | yes | (no \| no previous page) -> (do nothing \| no action) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | 1 |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 2 |
| (yes \| previous page exists) -> Update History Stack | T3 | none |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | 1 |

Test cases covered: T1, T2 (2 of 3).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: having the conditional check BEFORE any potential “Back” button click | precedes | not met: order not as required | not met: order not as required |
| S2: a split of XOR (exclusive OR) after the “no” branch of the condition check | fanout | not met: no split into the required nodes after 'no' | not met: no split into the required nodes after 'no' |
| S3: a swimlane so that the “Back” button click can be minimally defined | manual | not met: manual: No lanes or boxes separating the two sides of the Back click. | not met: manual: No lanes or boxes separating the two sides of the Back click. |
| S4: a split of AND on the “yes” branch after the button click | fanout | not met: no split into the required nodes after 'click back' | not met: no split into the required nodes after 'click back' |
| S5: make sure that “Update History Stack” is explicitly modeled | concepts | not met: missing: UHS | not met: missing: UHS |
