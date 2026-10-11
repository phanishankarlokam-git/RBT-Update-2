```dot
digraph B19_Reload {
    rankdir=TB;
    node [shape=box, fontname="Helvetica"];
    "Start" [shape=ellipse];
    "End" [shape=ellipse];

    "Start" -> "Current Page Displayed";
    "Current Page Displayed" -> "History Stacks Empty" [label="back/forward stacks empty"];
    "Current Page Displayed" -> "History Stacks Non-Empty" [label="back/forward stacks non-empty"];
    "History Stacks Empty" -> "Press Reload";
    "History Stacks Non-Empty" -> "Press Reload";
    "Press Reload" -> "Request Current Location";
    "Request Current Location" -> "Page Downloaded";
    "Page Downloaded" -> "Back Stack Unchanged";
    "Back Stack Unchanged" -> "Forward Stack Unchanged";
    "Forward Stack Unchanged" -> "End";
}
```

```text
1. Start → Current Page Displayed → History Stacks Empty → Press Reload → Request Current Location → Page Downloaded → Back Stack Unchanged → Forward Stack Unchanged → End
2. Start → Current Page Displayed → History Stacks Non-Empty → Press Reload → Request Current Location → Page Downloaded → Back Stack Unchanged → Forward Stack Unchanged → End
```