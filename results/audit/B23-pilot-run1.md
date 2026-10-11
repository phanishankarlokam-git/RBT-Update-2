# B23, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 44.4 | 44.4 | 44.4 | 4 of 9 answer-set nodes found; 9 generated nodes |
| L2 arrows | strict | 25.0 | 66.7 | 36.4 | 2 of 8 answer-set pairs found; 3 generated pairs |
| L3 tests | strict | 50.0 | 25.0 | 33.3 | 2 of 4 routes walked; 1 of 4 paths needed; test cases covered 1/3 |
| L4 sparkles | strict | 0.0 | | | 0 of 5 |
| L1 nodes | lenient | 55.6 | 55.6 | 55.6 | 5 of 9 answer-set nodes found; 9 generated nodes |
| L2 arrows | lenient | 25.0 | 40.0 | 30.8 | 2 of 8 answer-set pairs found; 5 generated pairs |
| L3 tests | lenient | 50.0 | 25.0 | 33.3 | 2 of 4 routes walked; 1 of 4 paths needed; test cases covered 1/3 |
| L4 sparkles | lenient | 0.0 | | | 0 of 5 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Anchor Rendered In Contrast | nothing | nothing | none | no |
| Anchor Clicked | nothing | nothing | none | no |
| Push Current Page To Back Stack | Pushing “current” Document into the “Back” Stack | Pushing “current” Document into the “Back” Stack | fuzzy | yes |
| Href Matches Forward Stack Top? | Anchor’s “href” = top of the “Forward” Stack? | Anchor’s “href” = top of the “Forward” Stack? | fuzzy | yes |
| Pop Forward Stack | “Forward” Stack Popped | “Forward” Stack Popped | exact | yes |
| Clear Forward Stack | “Forward” Stack Cleared | “Forward” Stack Cleared | exact | yes |
| Attempt Download | nothing | nothing | none | no |
| New Document Becomes Current | nothing | Document of the “Forward” Stack’s Top Displayed as “current” | alias: The downloaded document becomes current; on the 'match' branch this is the forward stack's top. | yes |
| Current Document Unchanged | nothing | nothing | none | no |

Answer-set nodes not found (lenient): Browser, Anchor content?, Content Click Disabled, Content Click Enabled

## L2. Arrows between shared nodes (lenient)

* Found in both: Anchor’s “href” = top of the “Forward” Stack? -> “Forward” Stack Cleared; Anchor’s “href” = top of the “Forward” Stack? -> “Forward” Stack Popped
* In the answer set only: Browser -> Anchor content?; Content Click Enabled -> Anchor’s “href” = top of the “Forward” Stack?; Content Click Enabled -> Pushing “current” Document into the “Back” Stack; Anchor content? -> Content Click Disabled; Anchor content? -> Content Click Enabled; Anchor’s “href” = top of the “Forward” Stack? -> Document of the “Forward” Stack’s Top Displayed as “current”
* In the generated graph only: “Forward” Stack Cleared -> Document of the “Forward” Stack’s Top Displayed as “current”; “Forward” Stack Popped -> Document of the “Forward” Stack’s Top Displayed as “current”; Pushing “current” Document into the “Back” Stack -> Anchor’s “href” = top of the “Forward” Stack?

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (Yes) → Pop Forward Stack → Attempt Download → (Success) → New Document Becomes Current → End | yes | Pushing “current” Document into the “Back” Stack | no |
| 2 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (Yes) → Pop Forward Stack → Attempt Download → (Failure) → Current Document Unchanged → End | yes | Pushing “current” Document into the “Back” Stack | no |
| 3 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (No) → Clear Forward Stack → Attempt Download → (Success) → New Document Becomes Current → End | yes | Pushing “current” Document into the “Back” Stack; “Forward” Stack Cleared | yes |
| 4 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (No) → Clear Forward Stack → Attempt Download → (Failure) → Current Document Unchanged → End | yes | Pushing “current” Document into the “Back” Stack; “Forward” Stack Cleared | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Content Click Disabled | T1 | none |
| Pushing “current” Document into the “Back” Stack | T2, T3 | 1, 2, 3, 4 |
| “Forward” Stack Cleared | T2 | 3, 4 |
| Document of the “Forward” Stack’s Top Displayed as “current” -> “Forward” Stack Popped | T3 | none |

Test cases covered: T2 (1 of 3).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (Yes) → Pop Forward Stack → Attempt Download → (Success) → New Document Becomes Current → End | yes | Pushing “current” Document into the “Back” Stack | no |
| 2 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (Yes) → Pop Forward Stack → Attempt Download → (Failure) → Current Document Unchanged → End | yes | Pushing “current” Document into the “Back” Stack | no |
| 3 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (No) → Clear Forward Stack → Attempt Download → (Success) → New Document Becomes Current → End | yes | Pushing “current” Document into the “Back” Stack; “Forward” Stack Cleared | yes |
| 4 | Anchor Rendered In Contrast → (click on anchor) → Anchor Clicked → Push Current Page To Back Stack → Href Matches Forward Stack Top? → (No) → Clear Forward Stack → Attempt Download → (Failure) → Current Document Unchanged → End | yes | Pushing “current” Document into the “Back” Stack; “Forward” Stack Cleared | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Content Click Disabled | T1 | none |
| Pushing “current” Document into the “Back” Stack | T2, T3 | 1, 2, 3, 4 |
| “Forward” Stack Cleared | T2 | 3, 4 |
| Document of the “Forward” Stack’s Top Displayed as “current” -> “Forward” Stack Popped | T3 | none |

Test cases covered: T2 (1 of 3).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: the “Anchor content?” conditional check | concepts | not met: missing: DEC1 | not met: missing: DEC1 |
| S2: explicitly modeling “Content Click Disabled” along the “no” branch | concepts | not met: missing: CCD | not met: missing: CCD |
| S3: the split after “click anchor element” that leads to one action and one conditional check | fanout | not met: no split into the required nodes | not met: no split into the required nodes |
| S4: the conditional check of “Anchor’s “href” = top of the “Forward” Stack?” is modeled after/inside a split | in_split | not met: DEC2 is not a branch of a split | not met: DEC2 is not a branch of a split |
| S5: one has to display the top first, and then pop the top | sequence | not met: no ordering between the two | not met: no ordering between the two |
