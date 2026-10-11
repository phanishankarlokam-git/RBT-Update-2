```dot
digraph B20_URL_Entry {
    rankdir=TB;
    node [fontname="Helvetica", shape=box];

    start       [label="Start", shape=ellipse];
    enter       [label="Enter Key Pressed in Address Field"];
    fileopen    [label="File > Open Selected"];
    retrieve    [label="Retrieve and Analyze Text"];
    decision    [label="Correct URL?", shape=diamond];
    download    [label="Download Document"];
    pushback    [label="Push Current Document to Back Stack"];
    nocurrent   [label="No Current Document"];
    error       [label="Display Error Message"];
    backpressed [label="Back Button Pressed"];
    restore     [label="Restore Last Page as Current"];
    doccurrent  [label="Document Is Current", shape=ellipse];

    start -> enter;
    start -> fileopen;
    enter -> retrieve;
    fileopen -> retrieve;
    retrieve -> decision;
    decision -> download    [label="Yes"];
    decision -> pushback    [label="No"];
    download -> doccurrent;
    pushback -> nocurrent;
    nocurrent -> error;
    error -> backpressed;
    backpressed -> restore;
    restore -> doccurrent;
}
```

```text
1. Start → Enter Key Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → Download Document → Document Is Current
2. Start → Enter Key Pressed in Address Field → Retrieve and Analyze Text → Correct URL? → Push Current Document to Back Stack → No Current Document → Display Error Message → Back Button Pressed → Restore Last Page as Current → Document Is Current
3. Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → Download Document → Document Is Current
4. Start → File > Open Selected → Retrieve and Analyze Text → Correct URL? → Push Current Document to Back Stack → No Current Document → Display Error Message → Back Button Pressed → Restore Last Page as Current → Document Is Current
```