# B16, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 16.7 | 33.3 | 22.2 | 1 of 6 answer-set nodes found; 3 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 5 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 0.0 | 0.0 | 0.0 | 0 of 4 routes walked; 0 of 3 paths needed; test cases covered 0/3 |
| L4 sparkles | strict | 0.0 | | | 0 of 5 |
| L1 nodes | lenient | 0.0 | 0.0 | 0.0 | 0 of 6 answer-set nodes found; 3 generated nodes |
| L2 arrows | lenient | 0.0 | 0.0 | 0.0 | 0 of 5 answer-set pairs found; 0 generated pairs |
| L3 tests | lenient | 75.0 | 66.7 | 70.6 | 3 of 4 routes walked; 2 of 3 paths needed; test cases covered 2/3 |
| L4 sparkles | lenient | 0.0 | | | 0 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Page1 Current (No Previous Page) | nothing | nothing | none | no |
| Page2 Current (1 Previous Page) | Current Page = Previous Page | nothing | alias: A state in which a previous page exists (the 'yes' side). Not 'Current Page = Previous Page', which the automatic rule matched on shared words. | no |
| Page3 Current (2 Previous Pages) | Current Page = Previous Page | nothing | alias: As above. | no |

Answer-set nodes not found (lenient): Browser, Previous page exists?, “Back” Button Clickable, “Back” Button Disabled, Update History Stack, Current Page = Previous Page

## L2. Arrows between shared nodes (lenient)

* Found in both: none
* In the answer set only: “Back” Button Clickable -> Current Page = Previous Page; “Back” Button Clickable -> Update History Stack; Browser -> Previous page exists?; Previous page exists? -> “Back” Button Clickable; Previous page exists? -> “Back” Button Disabled
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Page1 Current (No Previous Page) → (Click Back (no previous page: disabled or no-op)) → Page1 Current (No Previous Page) | yes | none | no |
| 2 | Page1 Current (No Previous Page) → (Open Page2) → Page2 Current (1 Previous Page) → (Click Back) → Page1 Current (No Previous Page) | yes | none | no |
| 3 | Page1 Current (No Previous Page) → (Open Page2) → Page2 Current (1 Previous Page) → (Open Page3) → Page3 Current (2 Previous Pages) → (Click Back) → Page2 Current (1 Previous Page) → (Click Back) → Page1 Current (No Previous Page) | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | none |
| (no \| no previous page) -> (do nothing \| no action) | T2 | none |
| (yes \| previous page exists) -> Update History Stack | T3 | none |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | none |

Test cases covered: none (0 of 3).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Page1 Current (No Previous Page) → (Click Back (no previous page: disabled or no-op)) → Page1 Current (No Previous Page) | yes | “Back” Button Disabled; (no \| no previous page) -> (do nothing \| no action) | yes |
| 2 | Page1 Current (No Previous Page) → (Open Page2) → Page2 Current (1 Previous Page) → (Click Back) → Page1 Current (No Previous Page) | yes | (yes \| previous page exists) -> Current Page = Previous Page | yes |
| 3 | Page1 Current (No Previous Page) → (Open Page2) → Page2 Current (1 Previous Page) → (Open Page3) → Page3 Current (2 Previous Pages) → (Click Back) → Page2 Current (1 Previous Page) → (Click Back) → Page1 Current (No Previous Page) | yes | (yes \| previous page exists) -> Current Page = Previous Page | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | 1 |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 1 |
| (yes \| previous page exists) -> Update History Stack | T3 | none |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | 2, 3 |

Test cases covered: T1, T2 (2 of 3).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: having the conditional check BEFORE any potential “Back” button click | precedes | not met: one of the two steps is missing | not met: one of the two steps is missing |
| S2: a split of XOR (exclusive OR) after the “no” branch of the condition check | fanout | not met: no split into the required nodes after 'no' | not met: no split into the required nodes after 'no' |
| S3: a swimlane so that the “Back” button click can be minimally defined | manual | not met: manual: No lanes or boxes; the Back click is drawn separately in each page state. | not met: manual: No lanes or boxes; the Back click is drawn separately in each page state. |
| S4: a split of AND on the “yes” branch after the button click | fanout | not met: no split into the required nodes after 'click back' | not met: no split into the required nodes after 'click back' |
| S5: make sure that “Update History Stack” is explicitly modeled | concepts | not met: missing: UHS | not met: missing: UHS |
