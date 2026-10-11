```dot
digraph FileMenuTestGraph {
    node [shape=box, style=rounded];

    Start [shape=ellipse, label="Start"];
    ClickFile [label="Click \"File\""];
    MenuDisplayed [label="File Menu Displayed"];
    CheckOpen [label="Verify \"Open\" Present"];
    CheckClose [label="Verify \"Close\" Present"];
    CheckExit [label="Verify \"Exit\" Present"];
    OtherDecision [shape=diamond, label="Other Options Present?"];
    ExtraPresent [label="Additional Options (e.g. \"Save\") Shown"];
    NoExtra [label="No Additional Options Shown"];
    DismissMenu [label="Dismiss Menu"];
    End [shape=doublecircle, label="End"];

    Start -> ClickFile;
    ClickFile -> MenuDisplayed;
    MenuDisplayed -> CheckOpen;
    CheckOpen -> CheckClose;
    CheckClose -> CheckExit;
    CheckExit -> OtherDecision;
    OtherDecision -> ExtraPresent [label="Yes"];
    OtherDecision -> NoExtra [label="No"];
    ExtraPresent -> DismissMenu;
    NoExtra -> DismissMenu;
    DismissMenu -> End;
}
```

```text
1. Start → Click "File" → File Menu Displayed → Verify "Open" Present → Verify "Close" Present → Verify "Exit" Present → Other Options Present? → Additional Options (e.g. "Save") Shown → Dismiss Menu → End
2. Start → Click "File" → File Menu Displayed → Verify "Open" Present → Verify "Close" Present → Verify "Exit" Present → Other Options Present? → No Additional Options Shown → Dismiss Menu → End
```