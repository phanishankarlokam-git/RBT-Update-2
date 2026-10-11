# B16, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set nodes found; 4 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 5 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 25.0 | 20.0 | 22.2 | 1 of 4 routes walked; 1 of 5 paths needed; test cases covered 1/3 |
| L4 sparkles | strict | 0.0 | | | 0 of 5 |
| L1 nodes | lenient | 33.3 | 50.0 | 40.0 | 2 of 6 answer-set nodes found; 4 generated nodes |
| L2 arrows | lenient | 0.0 | 0.0 | 0.0 | 0 of 5 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 75.0 | 40.0 | 52.2 | 3 of 4 routes walked; 2 of 5 paths needed; test cases covered 2/3 |
| L4 sparkles | lenient | 0.0 | | | 0 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| No Previous Page (Back Disabled but Visible) | nothing | “Back” Button Disabled | alias: Back disabled but visible = Back Button Disabled. | yes |
| No Previous Page (Back Enabled, No Action) | nothing | “Back” Button Clickable | alias: Back is clickable but a click does nothing = Back Button Clickable + do nothing. | yes |
| One Previous Page (Back Enabled) | nothing | “Back” Button Clickable | alias: A previous page exists and Back is clickable. | no, duplicate |
| Two or More Previous Pages (Back Enabled) | nothing | “Back” Button Clickable | alias: A previous page exists and Back is clickable. | no, duplicate |

Answer-set nodes not found (lenient): Browser, Previous page exists?, Update History Stack, Current Page = Previous Page

## L2. Arrows between shared nodes (lenient)

* Found in both: none
* In the answer set only: “Back” Button Clickable -> Current Page = Previous Page; “Back” Button Clickable -> Update History Stack; Browser -> Previous page exists?; Previous page exists? -> “Back” Button Clickable; Previous page exists? -> “Back” Button Disabled
* In the generated graph only: “Back” Button Clickable -> “Back” Button Disabled; “Back” Button Disabled -> “Back” Button Clickable

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (launch, variant: disable when empty) → No Previous Page (Back Disabled but Visible) → (Back activation attempted, disabled: no navigation) → No Previous Page (Back Disabled but Visible) | yes | none | no |
| 2 | Start → (launch, variant: no action when empty) → No Previous Page (Back Enabled, No Action) → (click Back, no previous page: no action) → No Previous Page (Back Enabled, No Action) | yes | (no \| no previous page) -> (do nothing \| no action) | yes |
| 3 | Start → (launch, variant: disable when empty) → No Previous Page (Back Disabled but Visible) → (navigate to new page, push current page onto stack) → One Previous Page (Back Enabled) → (click Back, returns to first page) → No Previous Page (Back Disabled but Visible) | yes | none | no |
| 4 | Start → (launch, variant: no action when empty) → No Previous Page (Back Enabled, No Action) → (navigate to new page, push current page onto stack) → One Previous Page (Back Enabled) → (click Back, returns to first page) → No Previous Page (Back Enabled, No Action) | yes | (no \| no previous page) -> (do nothing \| no action) | no |
| 5 | Start → (launch, variant: disable when empty) → No Previous Page (Back Disabled but Visible) → (navigate to new page, push current page onto stack) → One Previous Page (Back Enabled) → (navigate to new page, push current page onto stack) → Two or More Previous Pages (Back Enabled) → (navigate to new page, push current page onto stack / click Back, two or more pages still remain) → Two or More Previous Pages (Back Enabled) → (navigate to new page, push current page onto stack / click Back, two or more pages still remain) → Two or More Previous Pages (Back Enabled) → (click Back, exactly one page remains) → One Previous Page (Back Enabled) → (click Back, returns to first page) → No Previous Page (Back Disabled but Visible) | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | none |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 2, 4 |
| (yes \| previous page exists) -> Update History Stack | T3 | none |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | none |

Test cases covered: T2 (1 of 3).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → (launch, variant: disable when empty) → No Previous Page (Back Disabled but Visible) → (Back activation attempted, disabled: no navigation) → No Previous Page (Back Disabled but Visible) | yes | “Back” Button Disabled | yes |
| 2 | Start → (launch, variant: no action when empty) → No Previous Page (Back Enabled, No Action) → (click Back, no previous page: no action) → No Previous Page (Back Enabled, No Action) | yes | (no \| no previous page) -> (do nothing \| no action) | no |
| 3 | Start → (launch, variant: disable when empty) → No Previous Page (Back Disabled but Visible) → (navigate to new page, push current page onto stack) → One Previous Page (Back Enabled) → (click Back, returns to first page) → No Previous Page (Back Disabled but Visible) | yes | “Back” Button Disabled; (yes \| previous page exists) -> Current Page = Previous Page | no |
| 4 | Start → (launch, variant: no action when empty) → No Previous Page (Back Enabled, No Action) → (navigate to new page, push current page onto stack) → One Previous Page (Back Enabled) → (click Back, returns to first page) → No Previous Page (Back Enabled, No Action) | yes | (no \| no previous page) -> (do nothing \| no action); (yes \| previous page exists) -> Current Page = Previous Page | yes |
| 5 | Start → (launch, variant: disable when empty) → No Previous Page (Back Disabled but Visible) → (navigate to new page, push current page onto stack) → One Previous Page (Back Enabled) → (navigate to new page, push current page onto stack) → Two or More Previous Pages (Back Enabled) → (navigate to new page, push current page onto stack / click Back, two or more pages still remain) → Two or More Previous Pages (Back Enabled) → (navigate to new page, push current page onto stack / click Back, two or more pages still remain) → Two or More Previous Pages (Back Enabled) → (click Back, exactly one page remains) → One Previous Page (Back Enabled) → (click Back, returns to first page) → No Previous Page (Back Disabled but Visible) | yes | “Back” Button Disabled; (yes \| previous page exists) -> Current Page = Previous Page | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | 1, 3, 5 |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 2, 4 |
| (yes \| previous page exists) -> Update History Stack | T3 | none |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | 3, 4, 5 |

Test cases covered: T1, T2 (2 of 3).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: having the conditional check BEFORE any potential “Back” button click | precedes | not met: one of the two steps is missing | not met: one of the two steps is missing |
| S2: a split of XOR (exclusive OR) after the “no” branch of the condition check | fanout | not met: no split into the required nodes after 'no' | not met: no split into the required nodes after 'no' |
| S3: a swimlane so that the “Back” button click can be minimally defined | manual | not met: manual: No lanes or boxes; the Back click is drawn once per state (repeated, not defined once). | not met: manual: No lanes or boxes; the Back click is drawn once per state (repeated, not defined once). |
| S4: a split of AND on the “yes” branch after the button click | fanout | not met: no split into the required nodes after 'click back' | not met: no split into the required nodes after 'click back' |
| S5: make sure that “Update History Stack” is explicitly modeled | concepts | not met: missing: UHS | not met: missing: UHS |
