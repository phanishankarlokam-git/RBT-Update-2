# B19: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 3 of 3 answer-set nodes found; 3 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 2 of 2 answer-set pairs found; 2 generated pairs |
| L3 tests | strict | 100.0 | 100.0 | 100.0 | 2 of 2 routes walked; 2 of 2 paths needed; test cases covered 1/1 |
| L4 sparkles | strict | 100.0 | | | 2 of 2 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 3 of 3 answer-set nodes found; 3 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 2 of 2 answer-set pairs found; 2 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 2 of 2 routes walked; 2 of 2 paths needed; test cases covered 1/1 |
| L4 sparkles | lenient | 100.0 | | | 2 of 2 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Browser | Browser | exact | yes |
| Keeping History Stack Unchanged | Keeping History Stack Unchanged | Keeping History Stack Unchanged | exact | yes |
| Downloading Current Page Again | Downloading Current Page Again | Downloading Current Page Again | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Downloading Current Page Again; Browser -> Keeping History Stack Unchanged
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [click “Toolbar - -> Reload”] → [bar] → Keeping History Stack Unchanged | yes | Keeping History Stack Unchanged | yes |
| 2 | Browser → [click “Toolbar - -> Reload”] → [bar] → Downloading Current Page Again | yes | Downloading Current Page Again | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Keeping History Stack Unchanged | T1 | 1 |
| Downloading Current Page Again | T1 | 2 |

Test cases covered: T1 (1 of 1).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [click “Toolbar - -> Reload”] → [bar] → Keeping History Stack Unchanged | yes | Keeping History Stack Unchanged | yes |
| 2 | Browser → [click “Toolbar - -> Reload”] → [bar] → Downloading Current Page Again | yes | Downloading Current Page Again | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Keeping History Stack Unchanged | T1 | 1 |
| Downloading Current Page Again | T1 | 2 |

Test cases covered: T1 (1 of 1).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: split | fanout | met: 'Browser' splits into ['DCPA', 'KHSU'] | met: 'Browser' splits into ['DCPA', 'KHSU'] |
| S2: make sure that “Keeping History Stack Unchanged” is explicitly modeled | concepts | met: all present | met: all present |
