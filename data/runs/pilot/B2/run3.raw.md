```dot
digraph B2_BrowserLaunch {
    rankdir=TB;
    node [fontname="Helvetica", fontsize=10];

    Start [shape=ellipse, label="Start"];
    MainScreen [shape=box, label="Main Screen Displayed"];
    MenuBar [shape=diamond, label="Main Menu Bar Present?"];
    NavToolbar [shape=diamond, label="Navigational Toolbar Present?"];
    URLField [shape=diamond, label="URL Entry Text Field Present?"];
    HTMLZone [shape=diamond, label="HTML Display Zone Present?"];
    Complete [shape=ellipse, label="Main Screen Complete"];
    Incomplete [shape=ellipse, label="Main Screen Incomplete"];

    Start -> MainScreen [label="Launch Browser"];
    MainScreen -> MenuBar;
    MenuBar -> NavToolbar [label="Yes"];
    MenuBar -> Incomplete [label="No"];
    NavToolbar -> URLField [label="Yes"];
    NavToolbar -> Incomplete [label="No"];
    URLField -> HTMLZone [label="Yes"];
    URLField -> Incomplete [label="No"];
    HTMLZone -> Complete [label="Yes"];
    HTMLZone -> Incomplete [label="No"];
}
```

```text
1. Start → Main Screen Displayed → Main Menu Bar Present? → Navigational Toolbar Present? → URL Entry Text Field Present? → HTML Display Zone Present? → Main Screen Complete
2. Start → Main Screen Displayed → Main Menu Bar Present? → Main Screen Incomplete
3. Start → Main Screen Displayed → Main Menu Bar Present? → Navigational Toolbar Present? → Main Screen Incomplete
4. Start → Main Screen Displayed → Main Menu Bar Present? → Navigational Toolbar Present? → URL Entry Text Field Present? → Main Screen Incomplete
5. Start → Main Screen Displayed → Main Menu Bar Present? → Navigational Toolbar Present? → URL Entry Text Field Present? → HTML Display Zone Present? → Main Screen Incomplete
```