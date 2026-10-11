# B23: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 9 of 9 answer-set nodes found; 9 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 8 of 8 answer-set pairs found; 8 generated pairs |
| L3 tests | strict | 75.0 | 60.0 | 66.7 | 3 of 4 routes walked; 3 of 5 paths needed; test cases covered 2/3 |
| L4 sparkles | strict | 100.0 | | | 5 of 5 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 9 of 9 answer-set nodes found; 9 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 8 of 8 answer-set pairs found; 8 generated pairs |
| L3 tests | lenient | 75.0 | 60.0 | 66.7 | 3 of 4 routes walked; 3 of 5 paths needed; test cases covered 2/3 |
| L4 sparkles | lenient | 100.0 | | | 5 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Browser | Browser | exact | yes |
| Anchor content? | Anchor content? | Anchor content? | exact | yes |
| Content Click Disabled | Content Click Disabled | Content Click Disabled | exact | yes |
| Content Click Enabled | Content Click Enabled | Content Click Enabled | exact | yes |
| Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | exact | yes |
| Anchor’s “href” = top of the “Forward” Stack? | Anchor’s “href” = top of the “Forward” Stack? | Anchor’s “href” = top of the “Forward” Stack? | exact | yes |
| “Forward” Stack Cleared | “Forward” Stack Cleared | “Forward” Stack Cleared | exact | yes |
| Document of the “Forward” Stack’s Top Displayed as “current” | Document of the “Forward” Stack’s Top Displayed as “current” | Document of the “Forward” Stack’s Top Displayed as “current” | exact | yes |
| “Forward” Stack Popped | “Forward” Stack Popped | “Forward” Stack Popped | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Anchor content?; Content Click Enabled -> Anchor’s “href” = top of the “Forward” Stack?; Content Click Enabled -> Pushing “current” Document into the “Back” Stack; Anchor content? -> Content Click Disabled; Anchor content? -> Content Click Enabled; Anchor’s “href” = top of the “Forward” Stack? -> Document of the “Forward” Stack’s Top Displayed as “current”; Anchor’s “href” = top of the “Forward” Stack? -> “Forward” Stack Cleared; Anchor’s “href” = top of the “Forward” Stack? -> “Forward” Stack Popped
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [render a simple HTML document] → Anchor content? → [no] → Content Click Disabled | yes | Content Click Disabled | yes |
| 2 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Pushing “current” Document into the “Back” Stack | yes | Pushing “current” Document into the “Back” Stack | yes |
| 3 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Anchor’s “href” = top of the “Forward” Stack? → [no] → “Forward” Stack Cleared | yes | “Forward” Stack Cleared | yes |
| 4 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Anchor’s “href” = top of the “Forward” Stack? → [yes] → [bar] → Document of the “Forward” Stack’s Top Displayed as “current” | yes | none | no |
| 5 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Anchor’s “href” = top of the “Forward” Stack? → [yes] → [bar] → “Forward” Stack Popped | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Content Click Disabled | T1 | 1 |
| Pushing “current” Document into the “Back” Stack | T2, T3 | 2 |
| “Forward” Stack Cleared | T2 | 3 |
| Document of the “Forward” Stack’s Top Displayed as “current” -> “Forward” Stack Popped | T3 | none |

Test cases covered: T1, T2 (2 of 3).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [render a simple HTML document] → Anchor content? → [no] → Content Click Disabled | yes | Content Click Disabled | yes |
| 2 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Pushing “current” Document into the “Back” Stack | yes | Pushing “current” Document into the “Back” Stack | yes |
| 3 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Anchor’s “href” = top of the “Forward” Stack? → [no] → “Forward” Stack Cleared | yes | “Forward” Stack Cleared | yes |
| 4 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Anchor’s “href” = top of the “Forward” Stack? → [yes] → [bar] → Document of the “Forward” Stack’s Top Displayed as “current” | yes | none | no |
| 5 | Browser → [render a simple HTML document] → Anchor content? → [yes] → Content Click Enabled → [click anchor element] → [bar] → Anchor’s “href” = top of the “Forward” Stack? → [yes] → [bar] → “Forward” Stack Popped | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Content Click Disabled | T1 | 1 |
| Pushing “current” Document into the “Back” Stack | T2, T3 | 2 |
| “Forward” Stack Cleared | T2 | 3 |
| Document of the “Forward” Stack’s Top Displayed as “current” -> “Forward” Stack Popped | T3 | none |

Test cases covered: T1, T2 (2 of 3).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: the “Anchor content?” conditional check | concepts | met: all present | met: all present |
| S2: explicitly modeling “Content Click Disabled” along the “no” branch | concepts | met: all present | met: all present |
| S3: the split after “click anchor element” that leads to one action and one conditional check | fanout | met: 'Content Click Enabled' splits into ['DEC2', 'PCB'] | met: 'Content Click Enabled' splits into ['DEC2', 'PCB'] |
| S4: the conditional check of “Anchor’s “href” = top of the “Forward” Stack?” is modeled after/inside a split | in_split | met: 'Content Click Enabled' splits and one branch is DEC2 | met: 'Content Click Enabled' splits and one branch is DEC2 |
| S5: one has to display the top first, and then pop the top | sequence | met: bar marked sequential, in the right order | met: bar marked sequential, in the right order |
