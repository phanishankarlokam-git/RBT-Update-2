# B16: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set nodes found; 6 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | strict | 100.0 | 57.1 | 72.7 | 4 of 4 routes walked; 4 of 7 paths needed; test cases covered 3/3 |
| L4 sparkles | strict | 100.0 | | | 5 of 5 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set nodes found; 6 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | lenient | 100.0 | 57.1 | 72.7 | 4 of 4 routes walked; 4 of 7 paths needed; test cases covered 3/3 |
| L4 sparkles | lenient | 100.0 | | | 5 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Browser | Browser | exact | yes |
| Previous page exists? | Previous page exists? | Previous page exists? | exact | yes |
| “Back” Button Clickable | “Back” Button Clickable | “Back” Button Clickable | exact | yes |
| “Back” Button Disabled | “Back” Button Disabled | “Back” Button Disabled | exact | yes |
| Update History Stack | Update History Stack | Update History Stack | exact | yes |
| Current Page = Previous Page | Current Page = Previous Page | Current Page = Previous Page | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: “Back” Button Clickable -> Current Page = Previous Page; “Back” Button Clickable -> Update History Stack; Browser -> Previous page exists?; Previous page exists? -> “Back” Button Clickable; Previous page exists? -> “Back” Button Disabled
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Clickable → [click] → [bar] → Update History Stack | yes | none | no |
| 2 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Clickable → [click] → [bar] → Current Page = Previous Page | yes | none | no |
| 3 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Clickable → [click] → [bar] → [do nothing] → “Back” Button Clickable | yes | (no \| no previous page) -> (do nothing \| no action) | yes |
| 4 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Disabled | yes | “Back” Button Disabled | yes |
| 5 | Browser → [check] → Previous page exists? → [yes] → “Back” Button Clickable → [click] → [bar] → Update History Stack | yes | (yes \| previous page exists) -> Update History Stack | yes |
| 6 | Browser → [check] → Previous page exists? → [yes] → “Back” Button Clickable → [click] → [bar] → Current Page = Previous Page | yes | (yes \| previous page exists) -> Current Page = Previous Page | yes |
| 7 | Browser → [check] → Previous page exists? → [yes] → “Back” Button Clickable → [click] → [bar] → [do nothing] → “Back” Button Clickable | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | 4 |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 3 |
| (yes \| previous page exists) -> Update History Stack | T3 | 5 |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | 6 |

Test cases covered: T1, T2, T3 (3 of 3).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Clickable → [click] → [bar] → Update History Stack | yes | none | no |
| 2 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Clickable → [click] → [bar] → Current Page = Previous Page | yes | none | no |
| 3 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Clickable → [click] → [bar] → [do nothing] → “Back” Button Clickable | yes | (no \| no previous page) -> (do nothing \| no action) | yes |
| 4 | Browser → [check] → Previous page exists? → [no] → [bar] → “Back” Button Disabled | yes | “Back” Button Disabled | yes |
| 5 | Browser → [check] → Previous page exists? → [yes] → “Back” Button Clickable → [click] → [bar] → Update History Stack | yes | (yes \| previous page exists) -> Update History Stack | yes |
| 6 | Browser → [check] → Previous page exists? → [yes] → “Back” Button Clickable → [click] → [bar] → Current Page = Previous Page | yes | (yes \| previous page exists) -> Current Page = Previous Page | yes |
| 7 | Browser → [check] → Previous page exists? → [yes] → “Back” Button Clickable → [click] → [bar] → [do nothing] → “Back” Button Clickable | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| “Back” Button Disabled | T1 | 4 |
| (no \| no previous page) -> (do nothing \| no action) | T2 | 3 |
| (yes \| previous page exists) -> Update History Stack | T3 | 5 |
| (yes \| previous page exists) -> Current Page = Previous Page | T3 | 6 |

Test cases covered: T1, T2, T3 (3 of 3).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: having the conditional check BEFORE any potential “Back” button click | precedes | met: check comes first | met: check comes first |
| S2: a split of XOR (exclusive OR) after the “no” branch of the condition check | fanout | met: '[bar]' splits into ['BBC', 'BBD'] | met: '[bar]' splits into ['BBC', 'BBD'] |
| S3: a swimlane so that the “Back” button click can be minimally defined | manual | met: manual: Slide 13 has the dashed swimlane separating the 'no' side from the 'yes' side. | met: manual: Slide 13 has the dashed swimlane separating the 'no' side from the 'yes' side. |
| S4: a split of AND on the “yes” branch after the button click | fanout | met: '[bar]' splits into ['CPP', 'UHS'] | met: '[bar]' splits into ['CPP', 'UHS'] |
| S5: make sure that “Update History Stack” is explicitly modeled | concepts | met: all present | met: all present |
