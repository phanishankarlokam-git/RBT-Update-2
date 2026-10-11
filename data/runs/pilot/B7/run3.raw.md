```dot
digraph B7_Toolbar {
    rankdir=TB;
    node [fontname="Helvetica", fontsize=11];
    edge [fontname="Helvetica", fontsize=10];

    start       [label="Start", shape=ellipse];
    displayed   [label="Browser Displays Toolbar", shape=box];
    pos_check   [label="Toolbar on Left Side Under Menu Bar?", shape=diamond];
    pos_fail    [label="Position Defect (Fail)", shape=box, style=filled, fillcolor=lightpink];
    req_check   [label="Back, Forward, Home, Reload Present?", shape=diamond];
    req_fail    [label="Required Button Missing (Fail)", shape=box, style=filled, fillcolor=lightpink];
    opt_check   [label="Other Action Buttons Present?", shape=diamond];
    opt_render  [label="Render Other Buttons", shape=box];
    icon_check  [label="Icon Rendering Possible?", shape=diamond];
    icon_render [label="Render Arrow/Home Icons", shape=box];
    text_render [label="Render Text Labels (e.g. \"Back\", \"<--\")", shape=box];
    complete    [label="Toolbar Complete (Pass)", shape=ellipse, style=filled, fillcolor=lightgreen];

    start       -> displayed;
    displayed   -> pos_check;
    pos_check   -> req_check   [label="Yes"];
    pos_check   -> pos_fail    [label="No"];
    req_check   -> opt_check   [label="Yes"];
    req_check   -> req_fail    [label="No"];
    opt_check   -> opt_render  [label="Yes"];
    opt_check   -> icon_check  [label="No"];
    opt_render  -> icon_check;
    icon_check  -> icon_render [label="Yes"];
    icon_check  -> text_render [label="No"];
    icon_render -> complete;
    text_render -> complete;
}
```

```text
1. Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → Position Defect (Fail)
2. Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → Back, Forward, Home, Reload Present? → Required Button Missing (Fail)
3. Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → Back, Forward, Home, Reload Present? → Other Action Buttons Present? → Icon Rendering Possible? → Render Arrow/Home Icons → Toolbar Complete (Pass)
4. Start → Browser Displays Toolbar → Toolbar on Left Side Under Menu Bar? → Back, Forward, Home, Reload Present? → Other Action Buttons Present? → Render Other Buttons → Icon Rendering Possible? → Render Text Labels (e.g. "Back", "<--") → Toolbar Complete (Pass)
```