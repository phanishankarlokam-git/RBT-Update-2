# B12, pilot run1

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 27.3 | 33.3 | 30.0 | 3 of 11 answer-set nodes found; 9 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 10 answer-set pairs found; 3 generated pairs |
| L3 tests | strict | 25.0 | 50.0 | 33.3 | 1 of 4 routes walked; 1 of 2 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 0.0 | | | 0 of 4 |
| L1 nodes | lenient | 54.5 | 55.6 | 55.0 | 6 of 11 answer-set nodes found; 9 generated nodes |
| L2 arrows | lenient | 20.0 | 33.3 | 25.0 | 2 of 10 answer-set pairs found; 6 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 2 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 0.0 | | | 0 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main Browser Window | Browser | Browser | contains | yes |
| Select File > Open | nothing | nothing | none | no |
| Open Dialog Displayed | nothing | Pop-up Window | alias: The Open dialog is the pop-up window. | yes |
| Enter URL in Text Field | Text Field | Text Field | fuzzy | yes |
| Click OK | nothing | nothing | none | no |
| Click Cancel | nothing | nothing | none | no |
| Dialog Closes; Contents Remembered and Copied to Address Field | Text Field Content Copied to Address Field | Closing Pop-up Window, Text Field Content Copied to Address Field | alias: One node that says both things: the pop-up closes, and the text is copied to the address field. | yes |
| Browser Attempts Download | Browser | Content Resource Downloaded to Browser | alias: Download of the resource; the automatic rule wrongly read it as the Browser start node. | yes |
| Dialog Closes; No Further Action Taken | nothing | Closing Pop-up Window | alias: The pop-up closes (Cancel branch). The word 'No' refers to further action, not to the closing. | no, duplicate |

Answer-set nodes not found (lenient): Text Prompt, “OK” Button, “Cancel” Button, Other(s), “OK” or “Cancel”?

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window; Pop-up Window -> Text Field
* In the answer set only: “OK” or “Cancel”? -> Closing Pop-up Window; “OK” or “Cancel”? -> Content Resource Downloaded to Browser; “OK” or “Cancel”? -> Text Field Content Copied to Address Field; Pop-up Window -> “Cancel” Button; Pop-up Window -> “OK” or “Cancel”?; Pop-up Window -> “OK” Button; Pop-up Window -> Other(s); Pop-up Window -> Text Prompt
* In the generated graph only: Closing Pop-up Window -> Content Resource Downloaded to Browser; Text Field -> Closing Pop-up Window; Text Field -> Text Field Content Copied to Address Field; Text Field Content Copied to Address Field -> Content Resource Downloaded to Browser

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Browser Window → Select File > Open → Open Dialog Displayed → Enter URL in Text Field → Click OK → Dialog Closes; Contents Remembered and Copied to Address Field → Browser Attempts Download | yes | (OK) -> Text Field Content Copied to Address Field | yes |
| 2 | Main Browser Window → Select File > Open → Open Dialog Displayed → Enter URL in Text Field → Click Cancel → Dialog Closes; No Further Action Taken | yes | none | no |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (OK) -> Text Field Content Copied to Address Field | T1 | 1 |
| (OK) -> Content Resource Downloaded to Browser | T1 | none |
| (OK) -> Closing Pop-up Window | T1 | none |
| (Cancel) -> Closing Pop-up Window | T2 | none |

Test cases covered: none (0 of 2).

### lenient

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Browser Window → Select File > Open → Open Dialog Displayed → Enter URL in Text Field → Click OK → Dialog Closes; Contents Remembered and Copied to Address Field → Browser Attempts Download | yes | (OK) -> Text Field Content Copied to Address Field; (OK) -> Content Resource Downloaded to Browser; (OK) -> Closing Pop-up Window | yes |
| 2 | Main Browser Window → Select File > Open → Open Dialog Displayed → Enter URL in Text Field → Click Cancel → Dialog Closes; No Further Action Taken | yes | (Cancel) -> Closing Pop-up Window | yes |

| Route (answer set) | Test case(s) | Walked by path(s) |
|---|---|---|
| (OK) -> Text Field Content Copied to Address Field | T1 | 1 |
| (OK) -> Content Resource Downloaded to Browser | T1 | 1 |
| (OK) -> Closing Pop-up Window | T1 | 1 |
| (Cancel) -> Closing Pop-up Window | T2 | 2 |

Test cases covered: T1, T2 (2 of 2).

## L4. Sparkles

| Sparkle (from the notes) | Check | Strict | Lenient |
|---|---|---|---|
| S1: composition | composition | not met: no composition notation around the parts (boxes not counted in strict mode) | not met: no composition notation around the parts |
| S2: making sure that “Other(s)” is a part of “Pop-up Window | optional_child | not met: no node for other/optional items | not met: no node for other/optional items |
| S3: a single “Closing Pop-up Window” state that is shared between “OK” button press and “Cancel” button press | shared_target | not met: 0 nodes stand for CPW (need exactly one) | not met: 2 nodes stand for CPW (need exactly one) |
| S4: “AND” split after “OK” | fanout | not met: no split into the required nodes after 'OK' | not met: no split into the required nodes after 'OK' |
