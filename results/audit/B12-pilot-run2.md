# B12, pilot run2

Every number in the summary for this run comes from the tables below.

## Scores

| Level | Mode | Recall | Precision | F1 | Counted |
|---|---|---|---|---|---|
| L1 nodes | strict | 9.1 | 12.5 | 10.5 | 1 of 11 answer-set nodes found; 8 generated nodes |
| L2 arrows | strict | 0.0 | 0.0 | 0.0 | 0 of 10 answer-set pairs found; 0 generated pairs |
| L3 tests | strict | 25.0 | 50.0 | 33.3 | 1 of 4 routes walked; 1 of 2 paths needed; test cases covered 0/2 |
| L4 sparkles | strict | 0.0 | | | 0 of 4 |
| L1 nodes | lenient | 45.5 | 62.5 | 52.6 | 5 of 11 answer-set nodes found; 8 generated nodes |
| L2 arrows | lenient | 10.0 | 16.7 | 12.5 | 1 of 10 answer-set pairs found; 6 generated pairs |
| L3 tests | lenient | 100.0 | 100.0 | 100.0 | 4 of 4 routes walked; 2 of 2 paths needed; test cases covered 2/2 |
| L4 sparkles | lenient | 0.0 | | | 0 of 4 |

## Step 3. What each generated node stands for

| Generated node or box | Strict | Lenient | How (lenient) | Credited at L1 (lenient) |
|---|---|---|---|---|
| Main Browser Window | Browser | Browser | contains | yes |
| Open Dialog Displayed | nothing | Pop-up Window | alias: The Open dialog is the pop-up window. | yes |
| Dialog Closed (OK) | nothing | Closing Pop-up Window | alias: Dialog closed = Closing Pop-up Window. | yes |
| Text Field Contents Remembered | nothing | Text Field Content Copied to Address Field | alias: Remembering the text and copying it to the address field are one node in the answer set. | yes |
| Address Field Updated | nothing | Text Field Content Copied to Address Field | alias: Address field updated with the text = Text Field Content Copied to Address Field. | no, duplicate |
| Download Attempted | nothing | Content Resource Downloaded to Browser | alias: Attempted download of the resource = Content Resource Downloaded to Browser. | yes |
| Dialog Closed (Cancel) | nothing | Closing Pop-up Window | alias: Dialog closed = Closing Pop-up Window. | no, duplicate |
| No Further Action Taken | nothing | nothing | none | no |

Answer-set nodes not found (lenient): Text Prompt, Text Field, “OK” Button, “Cancel” Button, Other(s), “OK” or “Cancel”?

## L2. Arrows between shared nodes (lenient)

* Found in both: Browser -> Pop-up Window
* In the answer set only: “OK” or “Cancel”? -> Closing Pop-up Window; “OK” or “Cancel”? -> Content Resource Downloaded to Browser; “OK” or “Cancel”? -> Text Field Content Copied to Address Field; Pop-up Window -> “Cancel” Button; Pop-up Window -> “OK” or “Cancel”?; Pop-up Window -> “OK” Button; Pop-up Window -> Other(s); Pop-up Window -> Text Field; Pop-up Window -> Text Prompt
* In the generated graph only: Closing Pop-up Window -> Browser; Closing Pop-up Window -> Text Field Content Copied to Address Field; Content Resource Downloaded to Browser -> Browser; Pop-up Window -> Closing Pop-up Window; Text Field Content Copied to Address Field -> Content Resource Downloaded to Browser

## L3. Test paths

How each path was read (arrow labels taken from the graph are in round brackets, arrow labels written in the path in square brackets, unknown steps between question marks):

### strict

| # | Path as read | Valid in its own graph | Routes it walks | Needed |
|---|---|---|---|---|
| 1 | Main Browser Window → (select File -> Open) → Open Dialog Displayed → (press OK) → Dialog Closed (OK) → (remember text field contents) → Text Field Contents Remembered → (copy contents to address field) → Address Field Updated → (attempt to download resource) → Download Attempted → (ready for next command) → Main Browser Window | yes | (OK) -> Text Field Content Copied to Address Field | yes |
| 2 | Main Browser Window → (select File -> Open) → Open Dialog Displayed → (press Cancel) → Dialog Closed (Cancel) → (no action re: Open command) → No Further Action Taken → (ready for next command) → Main Browser Window | yes | none | no |

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
| 1 | Main Browser Window → (select File -> Open) → Open Dialog Displayed → (press OK) → Dialog Closed (OK) → (remember text field contents) → Text Field Contents Remembered → (copy contents to address field) → Address Field Updated → (attempt to download resource) → Download Attempted → (ready for next command) → Main Browser Window | yes | (OK) -> Text Field Content Copied to Address Field; (OK) -> Content Resource Downloaded to Browser; (OK) -> Closing Pop-up Window | yes |
| 2 | Main Browser Window → (select File -> Open) → Open Dialog Displayed → (press Cancel) → Dialog Closed (Cancel) → (no action re: Open command) → No Further Action Taken → (ready for next command) → Main Browser Window | yes | (Cancel) -> Closing Pop-up Window | yes |

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
