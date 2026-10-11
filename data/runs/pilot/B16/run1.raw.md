```dot
digraph B16_Back_Button {
    rankdir=LR;
    node [shape=box, style=rounded, fontname="Helvetica"];
    edge [fontname="Helvetica"];

    start [shape=point, width=0.15, label=""];
    S0 [label="Page1 Current (No Previous Page)"];
    S1 [label="Page2 Current (1 Previous Page)"];
    S2 [label="Page3 Current (2 Previous Pages)"];

    start -> S0;
    S0 -> S1 [label="Open Page2"];
    S1 -> S2 [label="Open Page3"];
    S1 -> S0 [label="Click Back"];
    S2 -> S1 [label="Click Back"];
    S0 -> S0 [label="Click Back (no previous page: disabled or no-op)"];
}
```

```text
1. Page1 Current (No Previous Page) → Page1 Current (No Previous Page)
2. Page1 Current (No Previous Page) → Page2 Current (1 Previous Page) → Page1 Current (No Previous Page)
3. Page1 Current (No Previous Page) → Page2 Current (1 Previous Page) → Page3 Current (2 Previous Pages) → Page2 Current (1 Previous Page) → Page1 Current (No Previous Page)
```