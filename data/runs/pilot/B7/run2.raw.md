```dot
digraph B7_Toolbar {
    rankdir=TB;
    node [shape=box, style=rounded, fontname="Helvetica"];
    edge [fontname="Helvetica"];

    Start [shape=ellipse, label="Start"];
    ToolbarPosition [label="Toolbar Below Menu Bar (Left)"];
    BackBtn [label="Back Button Present"];
    ForwardBtn [label="Forward Button Present"];
    HomeBtn [label="Home Button Present"];
    ReloadBtn [label="Reload Button Present"];
    AdditionalDecision [shape=diamond, label="Additional Buttons Present?"];
    AdditionalRendered [label="Additional Buttons Rendered"];
    IconDecision [shape=diamond, label="Icon Rendering Possible?"];
    RenderIcons [label="Render Arrow and Home Icons"];
    RenderText [label="Render Button Text"];
    End [shape=ellipse, label="End"];

    Start -> ToolbarPosition;
    ToolbarPosition -> BackBtn;
    BackBtn -> ForwardBtn;
    ForwardBtn -> HomeBtn;
    HomeBtn -> ReloadBtn;
    ReloadBtn -> AdditionalDecision;
    AdditionalDecision -> AdditionalRendered [label="Yes"];
    AdditionalDecision -> IconDecision [label="No"];
    AdditionalRendered -> IconDecision;
    IconDecision -> RenderIcons [label="Yes"];
    IconDecision -> RenderText [label="No"];
    RenderIcons -> End;
    RenderText -> End;
}
```

```text
1. Start → Toolbar Below Menu Bar (Left) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Additional Buttons Present? → Additional Buttons Rendered → Icon Rendering Possible? → Render Arrow and Home Icons → End
2. Start → Toolbar Below Menu Bar (Left) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Additional Buttons Present? → Icon Rendering Possible? → Render Button Text → End
```