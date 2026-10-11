```dot
digraph RequirementB2 {
    rankdir=LR;
    label="Requirement B2 — Browser Main Screen on Launch";
    labelloc=t;
    fontsize=14;
    node [shape=box, style="rounded,filled", fillcolor="#f0f0f0", fontname="Helvetica"];

    "Browser Launched" [shape=ellipse, fillcolor="#d9d9d9"];
    "Main Screen Displayed";
    "Main Menu Bar Displayed" [fillcolor="#e6e6e6"];
    "Navigational Toolbar Displayed" [fillcolor="#e6e6e6"];
    "URL Text Field Displayed" [fillcolor="#e6e6e6"];
    "HTML Display Zone Displayed" [style="rounded,filled,dashed", fillcolor="#fff2cc"];
    "Main Screen Complete" [shape=ellipse, fillcolor="#d9d9d9"];

    "Browser Launched" -> "Main Screen Displayed";
    "Main Screen Displayed" -> "Main Menu Bar Displayed";
    "Main Screen Displayed" -> "Navigational Toolbar Displayed";
    "Main Screen Displayed" -> "URL Text Field Displayed";
    "Main Screen Displayed" -> "HTML Display Zone Displayed";
    "Main Menu Bar Displayed" -> "Main Screen Complete";
    "Navigational Toolbar Displayed" -> "Main Screen Complete";
    "URL Text Field Displayed" -> "Main Screen Complete";
    "HTML Display Zone Displayed" -> "Main Screen Complete";
}
```

```text
1. Browser Launched → Main Screen Displayed → Main Menu Bar Displayed → Main Screen Complete
2. Browser Launched → Main Screen Displayed → Navigational Toolbar Displayed → Main Screen Complete
3. Browser Launched → Main Screen Displayed → URL Text Field Displayed → Main Screen Complete
4. Browser Launched → Main Screen Displayed → HTML Display Zone Displayed → Main Screen Complete
```