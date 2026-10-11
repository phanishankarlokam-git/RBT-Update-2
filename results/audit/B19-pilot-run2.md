# B19, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 66.7 | 25.0 | 36.4 | 2 of 3 answer-set nodes found; 8 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 2 answer-set pairs found; 1 generated pairs |
| L3 tests | strict | 100.0 | 50.0 | 66.7 | 2 of 2 routes walked; 1 of 2 paths needed; test cases covered 1/1 |
| L4 sparkles | strict | 50.0 | | | 1 of 2 |
| L1 nodes | lenient | 100.0 | 37.5 | 54.5 | 3 of 3 answer-set nodes found; 8 generated nodes |
| L2 arrows | lenient | 50.0 | 50.0 | 50.0 | 1 of 2 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 100.0 | 50.0 | 66.7 | 2 of 2 routes walked; 1 of 2 paths needed; test cases covered 1/1 |
| L4 sparkles | lenient | 50.0 | | | 1 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Page Displayed | nothing | Browser | alias: The browser showing a page = the Browser start node. | yes |
| Stacks State? | nothing | nothing | none | no |
| Back/Forward Empty | nothing | nothing | none | no |
| Back/Forward Non-Empty | nothing | nothing | none | no |
| Press Reload | nothing | nothing | none | no |
| Page Re-downloaded | Downloading Current Page Again | Downloading Current Page Again | fuzzy | yes |
| Page Redisplayed | nothing | nothing | none | no |
| Stacks Unchanged | Keeping History Stack Unchanged | Keeping History Stack Unchanged | fuzzy | yes |

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
| 1 | Page Displayed → Stacks State? → (empty) → Back/Forward Empty → Press Reload → Page Re-downloaded → Page Redisplayed → Stacks Unchanged | yes | Keeping History Stack Unchanged; Downloading Current Page Again | yes |
| 2 | Page Displayed → Stacks State? → (non-empty) → Back/Forward Non-Empty → Press Reload → Page Re-downloaded → Page Redisplayed → Stacks Unchanged | yes | Keeping History Stack Unchanged; Downloading Current Page Again | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Keeping History Stack Unchanged | T1 | 1, 2 |
| Downloading Current Page Again | T1 | 1, 2 |

Test cases covered: T1 (1 of 1).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Page Displayed → Stacks State? → (empty) → Back/Forward Empty → Press Reload → Page Re-downloaded → Page Redisplayed → Stacks Unchanged | yes | Keeping History Stack Unchanged; Downloading Current Page Again | yes |
| 2 | Page Displayed → Stacks State? → (non-empty) → Back/Forward Non-Empty → Press Reload → Page Re-downloaded → Page Redisplayed → Stacks Unchanged | yes | Keeping History Stack Unchanged; Downloading Current Page Again | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Keeping History Stack Unchanged | T1 | 1, 2 |
| Downloading Current Page Again | T1 | 1, 2 |

Test cases covered: T1 (1 of 1).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: split | fanout | not met: no split into the required nodes | not met: no split into the required nodes |
| S2: make sure that “Keeping History Stack Unchanged” is explicitly modeled | concepts | met: all present | met: all present |
