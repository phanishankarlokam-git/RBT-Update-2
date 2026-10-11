# B7, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 83.3 | 50.0 | 62.5 | 5 of 6 answer-set nodes found; 10 generated nodes |
| L2 arrows | strict | 20.0 | 20.0 | 20.0 | 1 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | strict | 80.0 | 50.0 | 61.5 | 4 of 5 routes walked; 1 of 2 paths needed; test cases covered 1/2 |
| L4 sparkles | strict | 50.0 | | | 2 of 4 |
| L1 nodes | lenient | 100.0 | 60.0 | 75.0 | 6 of 6 answer-set nodes found; 10 generated nodes |
| L2 arrows | lenient | 20.0 | 16.7 | 18.2 | 1 of 5 answer-set pairs found; 6 generated pairs |
| L3 tests | lenient | 100.0 | 50.0 | 66.7 | 5 of 5 routes walked; 1 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 2 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Toolbar Below Menu Bar (Left) | Toolbar | Toolbar | contains | yes |
| Back Button Present | Back or <-- | Back or <-- | contains | yes |
| Forward Button Present | Forward or --> | Forward or --> | contains | yes |
| Home Button Present | Home | Home | contains | yes |
| Reload Button Present | Reload | Reload | contains | yes |
| Additional Buttons Present? | nothing | Other(s) | alias: Additional buttons = Other(s). | yes |
| Additional Buttons Rendered | nothing | Other(s) | alias: Additional buttons = Other(s). | no, duplicate |
| Icon Rendering Possible? | nothing | nothing | none | no |
| Render Arrow and Home Icons | Home | Home | contains | no, duplicate |
| Render Button Text | nothing | nothing | none | no |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Toolbar -> Back or <--
* In the answer set only: Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Other(s); Toolbar -> Reload
* In the generated graph only: Back or <-- -> Forward or -->; Forward or --> -> Home; Home -> Reload; Other(s) -> Home; Reload -> Other(s)

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Toolbar Below Menu Bar (Left) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Additional Buttons Present? → (Yes) → Additional Buttons Rendered → Icon Rendering Possible? → (Yes) → Render Arrow and Home Icons → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload | yes |
| 2 | Start → Toolbar Below Menu Bar (Left) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Additional Buttons Present? → (No) → Icon Rendering Possible? → (No) → Render Button Text → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 1, 2 |
| Toolbar -> Forward or --> | T1, T2 | 1, 2 |
| Toolbar -> Home | T1, T2 | 1, 2 |
| Toolbar -> Reload | T1, T2 | 1, 2 |
| Toolbar -> Other(s) | T2 | none |

Test cases covered: T1 (1 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Toolbar Below Menu Bar (Left) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Additional Buttons Present? → (Yes) → Additional Buttons Rendered → Icon Rendering Possible? → (Yes) → Render Arrow and Home Icons → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | yes |
| 2 | Start → Toolbar Below Menu Bar (Left) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Additional Buttons Present? → (No) → Icon Rendering Possible? → (No) → Render Button Text → End | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | no |

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
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Additional Buttons Present?' | met: optional items modelled as 'Additional Buttons Present?' |
| S3: modeling “<--” and “-->” as part of the “Back” and “Forward” respectively | label_has | not met: missing for: BACK, FWD | not met: missing for: BACK, FWD |
| S4: an annotation note about the LOCATION of the “Toolbar” (i.e., to the LEFT and DIRECTL UNDER) | text_has | met: found in: 'toolbar below menu bar (left)' | met: found in: 'toolbar below menu bar (left)' |
