```dot
digraph B5_FileMenu {
    rankdir=LR;
    node [shape=box, fontname="Helvetica"];

    Start [shape=ellipse, label="Start"];
    MenuClosed [shape=box, label="File Menu Closed"];
    MenuOpen [shape=diamond, label="File Menu Open"];
    OpenSelected [shape=box, label="\"Open\" Selected"];
    CloseSelected [shape=box, label="\"Close\" Selected"];
    ExitSelected [shape=box, label="\"Exit\" Selected"];
    OtherSelected [shape=box, label="Additional Option Selected (e.g. \"Save\")"];
    AppExited [shape=ellipse, label="Application Exited"];

    Start -> MenuClosed;
    MenuClosed -> MenuOpen [label="click \"File\""];
    MenuOpen -> OpenSelected [label="select \"Open\""];
    MenuOpen -> CloseSelected [label="select \"Close\""];
    MenuOpen -> ExitSelected [label="select \"Exit\""];
    MenuOpen -> OtherSelected [label="select optional item, e.g. \"Save\""];
    OpenSelected -> MenuClosed [label="menu dismissed"];
    CloseSelected -> MenuClosed [label="menu dismissed"];
    OtherSelected -> MenuClosed [label="menu dismissed"];
    ExitSelected -> AppExited [label="application terminates"];
}
```

```text
1. Start → File Menu Closed → File Menu Open → "Open" Selected → File Menu Closed
2. Start → File Menu Closed → File Menu Open → "Close" Selected → File Menu Closed
3. Start → File Menu Closed → File Menu Open → Additional Option Selected (e.g. "Save") → File Menu Closed
4. Start → File Menu Closed → File Menu Open → "Exit" Selected → Application Exited
```