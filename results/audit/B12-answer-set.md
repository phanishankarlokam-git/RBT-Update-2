# B12: the answer set scored against itself

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 100.0 | 100.0 | 100.0 | 11 of 11 answer-set nodes found; 11 generated nodes |
| L2 arrows | strict | 100.0 | 100.0 | 100.0 | 10 of 10 answer-set pairs found; 10 generated pairs |
| L3 tests | strict | 100.0 | 44.4 | 61.5 | 4 of 4 routes walked; 4 of 9 paths needed; test cases covered 2/2 |
| L4 sparkles | strict | 100.0 | | | 4 of 4 |
| L1 nodes | lenient | 100.0 | 100.0 | 100.0 | 11 of 11 answer-set nodes found; 11 generated nodes |
| L2 arrows | lenient | 100.0 | 100.0 | 100.0 | 10 of 10 answer-set pairs found; 10 generated pairs |
| L3 tests | lenient | 100.0 | 44.4 | 61.5 | 4 of 4 routes walked; 4 of 9 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 100.0 | | | 4 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Browser | Browser | Browser | exact | yes |
| Pop-up Window | Pop-up Window | Pop-up Window | exact | yes |
| Text Prompt | Text Prompt | Text Prompt | exact | yes |
| Text Field | Text Field | Text Field | exact | yes |
| “OK” Button | “OK” Button | “OK” Button | exact | yes |
| “Cancel” Button | “Cancel” Button | “Cancel” Button | exact | yes |
| Other(s) | Other(s) | Other(s) | exact | yes |
| “OK” or “Cancel”? | “OK” or “Cancel”? | “OK” or “Cancel”? | exact | yes |
| Text Field Content Copied to Address Field | Text Field Content Copied to Address Field | Text Field Content Copied to Address Field | exact | yes |
| Content Resource Downloaded to Browser | Content Resource Downloaded to Browser | Content Resource Downloaded to Browser | exact | yes |
| Closing Pop-up Window | Closing Pop-up Window | Closing Pop-up Window | exact | yes |

Answer-set nodes not found (lenient): none

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window; “OK” or “Cancel”? -> Closing Pop-up Window; “OK” or “Cancel”? -> Content Resource Downloaded to Browser; “OK” or “Cancel”? -> Text Field Content Copied to Address Field; Pop-up Window -> “Cancel” Button; Pop-up Window -> “OK” or “Cancel”?; Pop-up Window -> “OK” Button; Pop-up Window -> Other(s); Pop-up Window -> Text Field; Pop-up Window -> Text Prompt
* In the answer set only: none
* In the generated graph only: none

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [click “File - -> Open”] → Pop-up Window → Text Prompt | yes | none | no |
| 2 | Browser → [click “File - -> Open”] → Pop-up Window → Text Field | yes | none | no |
| 3 | Browser → [click “File - -> Open”] → Pop-up Window → “OK” Button | yes | none | no |
| 4 | Browser → [click “File - -> Open”] → Pop-up Window → “Cancel” Button | yes | none | no |
| 5 | Browser → [click “File - -> Open”] → Pop-up Window → Other(s) | yes | none | no |
| 6 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“OK”] → [bar] → Text Field Content Copied to Address Field | yes | (OK) -> Text Field Content Copied to Address Field | yes |
| 7 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“OK”] → [bar] → Content Resource Downloaded to Browser | yes | (OK) -> Content Resource Downloaded to Browser | yes |
| 8 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“OK”] → [bar] → Closing Pop-up Window | yes | (OK) -> Closing Pop-up Window | yes |
| 9 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“Cancel”] → Closing Pop-up Window | yes | (Cancel) -> Closing Pop-up Window | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (OK) -> Text Field Content Copied to Address Field | T1 | 6 |
| (OK) -> Content Resource Downloaded to Browser | T1 | 7 |
| (OK) -> Closing Pop-up Window | T1 | 8 |
| (Cancel) -> Closing Pop-up Window | T2 | 9 |

Test cases covered: T1, T2 (2 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Browser → [click “File - -> Open”] → Pop-up Window → Text Prompt | yes | none | no |
| 2 | Browser → [click “File - -> Open”] → Pop-up Window → Text Field | yes | none | no |
| 3 | Browser → [click “File - -> Open”] → Pop-up Window → “OK” Button | yes | none | no |
| 4 | Browser → [click “File - -> Open”] → Pop-up Window → “Cancel” Button | yes | none | no |
| 5 | Browser → [click “File - -> Open”] → Pop-up Window → Other(s) | yes | none | no |
| 6 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“OK”] → [bar] → Text Field Content Copied to Address Field | yes | (OK) -> Text Field Content Copied to Address Field | yes |
| 7 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“OK”] → [bar] → Content Resource Downloaded to Browser | yes | (OK) -> Content Resource Downloaded to Browser | yes |
| 8 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“OK”] → [bar] → Closing Pop-up Window | yes | (OK) -> Closing Pop-up Window | yes |
| 9 | Browser → [click “File - -> Open”] → Pop-up Window → [press] → “OK” or “Cancel”? → [“Cancel”] → Closing Pop-up Window | yes | (Cancel) -> Closing Pop-up Window | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (OK) -> Text Field Content Copied to Address Field | T1 | 6 |
| (OK) -> Content Resource Downloaded to Browser | T1 | 7 |
| (OK) -> Closing Pop-up Window | T1 | 8 |
| (Cancel) -> Closing Pop-up Window | T2 | 9 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | met: composition from 'Pop-up Window' to ['CB', 'OKB', 'OTH', 'TF', 'TP'] | met: composition from 'Pop-up Window' to ['CB', 'OKB', 'OTH', 'TF', 'TP'] |
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | met: optional items modelled as 'Other(s)' | met: optional items modelled as 'Other(s)' |
| S3: a single “Closing Pop-up Window” state that is shared between “OK” button press and “Cancel” button press | shared_target | met: one shared node reached from all branches | met: one shared node reached from all branches |
| S4: “AND” split after “OK” | fanout | met: '[bar]' splits into ['CPW', 'CRD', 'TFC'] | met: '[bar]' splits into ['CPW', 'CRD', 'TFC'] |
