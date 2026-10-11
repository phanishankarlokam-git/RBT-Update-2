# B7, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 66.7 | 36.4 | 47.1 | 4 of 6 answer-set nodes found; 11 generated nodes |
| L2 arrows | strict | 20.0 | 20.0 | 20.0 | 1 of 5 answer-set pairs found; 5 generated pairs |
| L3 tests | strict | 60.0 | 50.0 | 54.5 | 3 of 5 routes walked; 2 of 4 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 50.0 | | | 2 of 4 |
| L1 nodes | lenient | 100.0 | 27.3 | 42.9 | 6 of 6 answer-set nodes found; 11 generated nodes |
| L2 arrows | lenient | 80.0 | 33.3 | 47.1 | 4 of 5 answer-set pairs found; 12 generated pairs |
| L3 tests | lenient | 100.0 | 25.0 | 40.0 | 5 of 5 routes walked; 1 of 4 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 50.0 | | | 2 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser Displays Toolbar | Toolbar | Toolbar | contains | yes |
| Toolbar on Left Side Under Menu Bar? | Toolbar | Toolbar | contains | no, duplicate |
| Position Defect (Fail) | nothing | nothing | none | no |
| Back, Forward, Home, Reload Present? | nothing | Back or <--, Forward or -->, Home, Reload | alias: One check node that names all four mandatory buttons. | yes |
| Required Button Missing (Fail) | nothing | nothing | none | no |
| Other Action Buttons Present? | Other(s) | Other(s) | contains | no, duplicate |
| Render Other Buttons | Other(s) | Other(s) | contains | yes |
| Icon Rendering Possible? | nothing | nothing | none | no |
| Render Arrow/Home Icons | Home | Home | contains | no, duplicate |
| Render Text Labels (e.g. "Back", "<--") | Back or <-- | Back or <-- | contains | no, duplicate |
| Toolbar Complete (Pass) | Toolbar | Toolbar | contains | no, duplicate |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload
* In the answer set only: Toolbar -> Other(s)
* In the generated graph only: Back or <-- -> Other(s); Back or <-- -> Toolbar; Forward or --> -> Other(s); Home -> Other(s); Home -> Toolbar; Other(s) -> Back or <--; Other(s) -> Home; Reload -> Other(s)

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (No) → Position Defect (Fail) | yes | none | no |
| 2 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (Yes) → Back, Forward, Home, Reload Present? → (No) → Required Button Missing (Fail) | yes | none | no |
| 3 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (Yes) → Back, Forward, Home, Reload Present? → (Yes) → Other Action Buttons Present? → (No) → Icon Rendering Possible? → (Yes) → Render Arrow/Home Icons → Toolbar Complete (Pass) | yes | Toolbar -> Home; Toolbar -> Other(s) | yes |
| 4 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (Yes) → Back, Forward, Home, Reload Present? → (Yes) → Other Action Buttons Present? → (Yes) → Render Other Buttons → Icon Rendering Possible? → (No) → Render Text Labels (e.g. "Back", "<--") → Toolbar Complete (Pass) | yes | Toolbar -> Back or <--; Toolbar -> Other(s) | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 4 |
| Toolbar -> Forward or --> | T1, T2 | none |
| Toolbar -> Home | T1, T2 | 3 |
| Toolbar -> Reload | T1, T2 | none |
| Toolbar -> Other(s) | T2 | 3, 4 |

Test cases covered: none (0 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (No) → Position Defect (Fail) | yes | none | no |
| 2 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (Yes) → Back, Forward, Home, Reload Present? → (No) → Required Button Missing (Fail) | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload | no |
| 3 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (Yes) → Back, Forward, Home, Reload Present? → (Yes) → Other Action Buttons Present? → (No) → Icon Rendering Possible? → (Yes) → Render Arrow/Home Icons → Toolbar Complete (Pass) | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | yes |
| 4 | Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → (Yes) → Back, Forward, Home, Reload Present? → (Yes) → Other Action Buttons Present? → (Yes) → Render Other Buttons → Icon Rendering Possible? → (No) → Render Text Labels (e.g. "Back", "<--") → Toolbar Complete (Pass) | yes | Toolbar -> Back or <--; Toolbar -> Forward or -->; Toolbar -> Home; Toolbar -> Reload; Toolbar -> Other(s) | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| Toolbar -> Back or <-- | T1, T2 | 2, 3, 4 |
| Toolbar -> Forward or --> | T1, T2 | 2, 3, 4 |
| Toolbar -> Home | T1, T2 | 2, 3, 4 |
| Toolbar -> Reload | T1, T2 | 2, 3, 4 |
| Toolbar -> Other(s) | T2 | 3, 4 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: modeling OPTIONALS as a child node | optional_child | met: optional items modelled as 'Other Action Buttons Present?' | met: optional items modelled as 'Other Action Buttons Present?' |
| S3: modeling “<--” and “-->” as part of the “Back” and “Forward” respectively | label_has | not met: missing for: FWD | not met: missing for: FWD |
| S4: an annotation note about the LOCATION of the “Toolbar” (i.e., to the LEFT and DIRECTL UNDER) | text_has | met: found in: 'toolbar on left side under menu bar?' | met: found in: 'toolbar on left side under menu bar?' |
