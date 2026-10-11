# B12, pilot run3

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 0.0 | 0.0 | 0.0 | 0 of 11 answer-set nodes found; 6 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 10 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 0.0 | 0.0 | 0.0 | 0 of 4 routes walked; 0 of 4 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 0.0 | | | 0 of 4 |
| L1 nodes | lenient | 36.4 | 66.7 | 47.1 | 4 of 11 answer-set nodes found; 6 generated nodes |
| L2 arrows | lenient | 10.0 | 33.3 | 15.4 | 1 of 10 answer-set pairs found; 3 generated pairs |
| L3 tests | lenient | 50.0 | 25.0 | 33.3 | 2 of 4 routes walked; 1 of 4 paths needed; test cases covered 0/2 |
| L4 sparkles | lenient | 0.0 | | | 0 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main Window | nothing | Browser | alias: The browser's main window = the Browser start node. | yes |
| Dialog Displayed | nothing | Pop-up Window | alias: The dialog is the pop-up window. | yes |
| URL Entered | nothing | nothing | none | no |
| Address Field Updated | nothing | Text Field Content Copied to Address Field | alias: Address field updated with the text = Text Field Content Copied to Address Field. | yes |
| Download Attempted | nothing | Content Resource Downloaded to Browser | alias: Attempted download of the resource = Content Resource Downloaded to Browser. | yes |
| No Action Taken | nothing | nothing | none | no |

Answer-set nodes not found (lenient): Text Prompt, Text Field, “OK” Button, “Cancel” Button, Other(s), “OK” or “Cancel”?, Closing Pop-up Window

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window
* In the answer set only: “OK” or “Cancel”? -> Closing Pop-up Window; “OK” or “Cancel”? -> Content Resource Downloaded to Browser; “OK” or “Cancel”? -> Text Field Content Copied to Address Field; Pop-up Window -> “Cancel” Button; Pop-up Window -> “OK” or “Cancel”?; Pop-up Window -> “OK” Button; Pop-up Window -> Other(s); Pop-up Window -> Text Field; Pop-up Window -> Text Prompt
* In the generated graph only: Pop-up Window -> Text Field Content Copied to Address Field; Text Field Content Copied to Address Field -> Content Resource Downloaded to Browser

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Window → (File > Open selected) → Dialog Displayed → (OK pressed (empty field)) → Address Field Updated → (download attempted) → Download Attempted | yes | none | no |
| 2 | Main Window → (File > Open selected) → Dialog Displayed → (user enters URL) → URL Entered → (OK pressed) → Address Field Updated → (download attempted) → Download Attempted | yes | none | no |
| 3 | Main Window → (File > Open selected) → Dialog Displayed → (Cancel pressed (empty field)) → No Action Taken | yes | none | no |
| 4 | Main Window → (File > Open selected) → Dialog Displayed → (user enters URL) → URL Entered → (Cancel pressed) → No Action Taken | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (OK) -> Text Field Content Copied to Address Field | T1 | none |
| (OK) -> Content Resource Downloaded to Browser | T1 | none |
| (OK) -> Closing Pop-up Window | T1 | none |
| (Cancel) -> Closing Pop-up Window | T2 | none |

Test cases covered: none (0 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Window → (File > Open selected) → Dialog Displayed → (OK pressed (empty field)) → Address Field Updated → (download attempted) → Download Attempted | yes | (OK) -> Text Field Content Copied to Address Field; (OK) -> Content Resource Downloaded to Browser | yes |
| 2 | Main Window → (File > Open selected) → Dialog Displayed → (user enters URL) → URL Entered → (OK pressed) → Address Field Updated → (download attempted) → Download Attempted | yes | (OK) -> Text Field Content Copied to Address Field; (OK) -> Content Resource Downloaded to Browser | no |
| 3 | Main Window → (File > Open selected) → Dialog Displayed → (Cancel pressed (empty field)) → No Action Taken | yes | none | no |
| 4 | Main Window → (File > Open selected) → Dialog Displayed → (user enters URL) → URL Entered → (Cancel pressed) → No Action Taken | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (OK) -> Text Field Content Copied to Address Field | T1 | 1, 2 |
| (OK) -> Content Resource Downloaded to Browser | T1 | 1, 2 |
| (OK) -> Closing Pop-up Window | T1 | none |
| (Cancel) -> Closing Pop-up Window | T2 | none |

Test cases covered: none (0 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | not met: no node for other/optional items | not met: no node for other/optional items |
| S3: a single “Closing Pop-up Window” state that is shared between “OK” button press and “Cancel” button press | shared_target | not met: 0 nodes stand for CPW (need exactly one) | not met: 0 nodes stand for CPW (need exactly one) |
| S4: “AND” split after “OK” | fanout | not met: no split into the required nodes after 'OK' | not met: no split into the required nodes after 'OK' |
