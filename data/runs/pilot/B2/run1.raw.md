```dot
digraph B2 {
    rankdir=LR;
    node [shape=box, style=rounded, fontname="Helvetica"];
    edge [fontname="Helvetica", fontsize=10];

    Start [shape=oval, label="Start"];
    MainScreen [label="Main Screen Displayed"];
    MenuBar [label="Main Menu Bar Present"];
    Toolbar [label="Navigational Toolbar Present"];
    URLField [label="URL Entry Field Present"];
    HTMLZone [label="HTML Display Zone Present"];
    End [shape=oval, label="End"];

    Start -> MainScreen [label="launch browser"];
    MainScreen -> MenuBar [label="verify menu bar"];
    MainScreen -> Toolbar [label="verify toolbar"];
    MainScreen -> URLField [label="verify URL field"];
    MainScreen -> HTMLZone [label="verify HTML display zone"];
    MenuBar -> End;
    Toolbar -> End;
    URLField -> End;
    HTMLZone -> End;
}
```

```text
1. Start → Main Screen Displayed → Main Menu Bar Present → End
2. Start → Main Screen Displayed → Navigational Toolbar Present → End
3. Start → Main Screen Displayed → URL Entry Field Present → End
4. Start → Main Screen Displayed → HTML Display Zone Present → End
```