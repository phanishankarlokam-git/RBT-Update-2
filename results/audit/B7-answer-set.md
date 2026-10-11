# B7: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set nodes found; 6 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | strict | 100.0 | 100.0 | 100.0 | 5 of 5 routes walked; 5 of 5 paths needed; test cases covered 2/2 |
| L4 sparkles | strict | 100.0 | | | 4 of 4 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 6 of 6 answer-set nodes found; 6 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 5 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 5 of 5 routes walked; 5 of 5 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 100.0 | | | 4 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Toolbar | Toolbar | Toolbar | exact | yes |
| Back or <-- | Back or <-- | Back or <-- | exact | yes |
| Forward or --> | Forward or --> | Forward or --> | exact | yes |
| Home | Home | Home | exact | yes |
| Reload | Reload | Reload | exact | yes |
| Other(s) | Other(s) | Other(s) | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Other(s); Toolbar -> Reload
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Toolbar → Back or <-- | yes | Toolbar -> Back or <-- | yes |
| 2 | Toolbar → Forward or --> | yes | Toolbar -> Forward or --> | yes |
| 3 | Toolbar → Home | yes | Toolbar -> Home | yes |
| 4 | Toolbar → Reload | yes | Toolbar -> Reload | yes |
| 5 | Toolbar → Other(s) | yes | Toolbar -> Other(s) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 1 |
| Toolbar -> Forward or --> | T1, T2 | 2 |
| Toolbar -> Home | T1, T2 | 3 |
| Toolbar -> Reload | T1, T2 | 4 |
| Toolbar -> Other(s) | T2 | 5 |

Test cases covered: T1, T2 (2 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Toolbar → Back or <-- | yes | Toolbar -> Back or <-- | yes |
| 2 | Toolbar → Forward or --> | yes | Toolbar -> Forward or --> | yes |
| 3 | Toolbar → Home | yes | Toolbar -> Home | yes |
| 4 | Toolbar → Reload | yes | Toolbar -> Reload | yes |
| 5 | Toolbar → Other(s) | yes | Toolbar -> Other(s) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 1 |
| Toolbar -> Forward or --> | T1, T2 | 2 |
| Toolbar -> Home | T1, T2 | 3 |
| Toolbar -> Reload | T1, T2 | 4 |
| Toolbar -> Other(s) | T2 | 5 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | met: composition from 'Toolbar' to ['BACK', 'FWD', 'HOME', 'OTH', 'RELOAD'] | met: composition from 'Toolbar' to ['BACK', 'FWD', 'HOME', 'OTH', 'RELOAD'] |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Other(s)' | met: optional items modelled as 'Other(s)' |
| S3: modeling “<--” and “-->” as part of the “Back” and “Forward” respectively | label_has | met: marks present | met: marks present |
| S4: an annotation note about the LOCATION of the “Toolbar” (i.e., to the LEFT and DIRECTL UNDER) | text_has | met: found in: 'toolbar shall be located on the left side of the browser screen direct' | met: found in: 'toolbar shall be located on the left side of the browser screen direct' |
