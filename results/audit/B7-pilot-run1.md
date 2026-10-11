# B7, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 30.0 | 46.2 | 6 of 6 answer-set nodes found; 20 generated nodes |
| L2 arrows | strict | 20.0 | 16.7 | 18.2 | 1 of 5 answer-set pairs found; 6 generated pairs |
| L3 tests | strict | 100.0 | 50.0 | 66.7 | 5 of 5 routes walked; 1 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | strict | 50.0 | | | 2 of 4 |
| L1 nodes | lenient | 100.0 | 30.0 | 46.2 | 6 of 6 answer-set nodes found; 20 generated nodes |
| L2 arrows | lenient | 20.0 | 16.7 | 18.2 | 1 of 5 answer-set pairs found; 6 generated pairs |
| L3 tests | lenient | 100.0 | 50.0 | 66.7 | 5 of 5 routes walked; 1 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 2 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Toolbar Positioned (Left, Under Menu Bar) | Toolbar | Toolbar | contains | yes |
| Back Button Present | Back or <-- | Back or <-- | contains | yes |
| Forward Button Present | Forward or --> | Forward or --> | contains | yes |
| Home Button Present | Home | Home | contains | yes |
| Reload Button Present | Reload | Reload | contains | yes |
| Other Buttons? | Other(s) | Other(s) | fuzzy | yes |
| Other Buttons Present | Other(s) | Other(s) | contains | no, duplicate |
| No Other Buttons | nothing | nothing | none | no |
| Back Icon Feasible? | Back or <-- | Back or <-- | contains | no, duplicate |
| Back Renders Icon | Back or <-- | Back or <-- | contains | no, duplicate |
| Back Renders Text | Back or <-- | Back or <-- | contains | no, duplicate |
| Forward Icon Feasible? | Forward or --> | Forward or --> | contains | no, duplicate |
| Forward Renders Icon | Forward or --> | Forward or --> | contains | no, duplicate |
| Forward Renders Text | Forward or --> | Forward or --> | contains | no, duplicate |
| Home Icon Feasible? | Home | Home | contains | no, duplicate |
| Home Renders Icon | Home | Home | contains | no, duplicate |
| Home Renders Text | Home | Home | contains | no, duplicate |
| Reload Icon Feasible? | Reload | Reload | contains | no, duplicate |
| Reload Renders Icon | Reload | Reload | contains | no, duplicate |
| Reload Renders Text | Reload | Reload | contains | no, duplicate |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Toolbar -> Back or <--
* In the answer set only: Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Other(s); Toolbar -> Reload
* In the generated graph only: Back or <-- -> Forward or -->; Forward or --> -> Home; Home -> Reload; Other(s) -> Back or <--; Reload -> Other(s)

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Toolbar Positioned (Left, Under Menu Bar) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Other Buttons? → (yes) → Other Buttons Present → Back Icon Feasible? → (yes) → Back Renders Icon → Forward Icon Feasible? → (yes) → Forward Renders Icon → Home Icon Feasible? → (yes) → Home Renders Icon → Reload Icon Feasible? → (yes) → Reload Renders Icon → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | yes |
| 2 | Start → Toolbar Positioned (Left, Under Menu Bar) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Other Buttons? → (no) → No Other Buttons → Back Icon Feasible? → (no) → Back Renders Text → Forward Icon Feasible? → (no) → Forward Renders Text → Home Icon Feasible? → (no) → Home Renders Text → Reload Icon Feasible? → (no) → Reload Renders Text → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 1, 2 |
| Toolbar -> Forward or --> | T1, T2 | 1, 2 |
| Toolbar -> Home | T1, T2 | 1, 2 |
| Toolbar -> Reload | T1, T2 | 1, 2 |
| Toolbar -> Other(s) | T2 | 1, 2 |

Test cases covered: T1, T2 (2 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Toolbar Positioned (Left, Under Menu Bar) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Other Buttons? → (yes) → Other Buttons Present → Back Icon Feasible? → (yes) → Back Renders Icon → Forward Icon Feasible? → (yes) → Forward Renders Icon → Home Icon Feasible? → (yes) → Home Renders Icon → Reload Icon Feasible? → (yes) → Reload Renders Icon → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | yes |
| 2 | Start → Toolbar Positioned (Left, Under Menu Bar) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Other Buttons? → (no) → No Other Buttons → Back Icon Feasible? → (no) → Back Renders Text → Forward Icon Feasible? → (no) → Forward Renders Text → Home Icon Feasible? → (no) → Home Renders Text → Reload Icon Feasible? → (no) → Reload Renders Text → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 1, 2 |
| Toolbar -> Forward or --> | T1, T2 | 1, 2 |
| Toolbar -> Home | T1, T2 | 1, 2 |
| Toolbar -> Reload | T1, T2 | 1, 2 |
| Toolbar -> Other(s) | T2 | 1, 2 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Other Buttons Present' | met: optional items modelled as 'Other Buttons Present' |
| S3: modeling “<--” and “-->” as part of the “Back” and “Forward” respectively | label_has | not met: missing for: BACK, FWD | not met: missing for: BACK, FWD |
| S4: an annotation note about the LOCATION of the “Toolbar” (i.e., to the LEFT and DIRECTL UNDER) | text_has | met: found in: 'toolbar positioned (left, under menu bar)' | met: found in: 'toolbar positioned (left, under menu bar)' |
