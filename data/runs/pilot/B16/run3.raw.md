```dot
digraph BackButtonB16 {
    rankdir=LR;
    fontname="Helvetica";
    node [fontname="Helvetica", shape=box, style="rounded,filled", fillcolor="#eeeeee", color="#666666"];
    edge [fontname="Helvetica", fontsize=10, color="#444444"];

    Start [shape=circle, style=filled, fillcolor="#333333", fontcolor="white", width=0.7, fixedsize=true, label="Start"];
    NoPrev [label="No Previous Page"];
    HasPrev [label="Previous Page Exists"];
    Disabled [label="Back Button Disabled (Visible)", fillcolor="#ffe8a3"];
    NoAction [label="Back Click Yields No Action", fillcolor="#ffe8a3"];

    Start -> NoPrev [label="browser launch"];
    NoPrev -> HasPrev [label="navigate to new page"];
    HasPrev -> HasPrev [label="navigate to new page"];
    HasPrev -> HasPrev [label="click Back\n(previous page still remains)"];
    HasPrev -> NoPrev [label="click Back\n(stack becomes empty)"];
    NoPrev -> Disabled [label="Back shown disabled but visible"];
    NoPrev -> NoAction [label="click Back\n(button stays enabled)"];
    Disabled -> NoPrev [label="no state change"];
    NoAction -> NoPrev [label="no state change"];
}
```

```text
1. Start → No Previous Page → Previous Page Exists → Previous Page Exists → Previous Page Exists → No Previous Page → Back Button Disabled (Visible) → No Previous Page
2. Start → No Previous Page → Back Click Yields No Action → No Previous Page
```