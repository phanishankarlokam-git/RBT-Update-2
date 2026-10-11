```dot
digraph RequirementB20 {
    rankdir=TB;
    node [fontname="Helvetica"];

    start      [label="Start", shape=ellipse];
    enter_key  [label="Enter Pressed in Address Field", shape=box];
    file_open  [label="File -> Open Selected", shape=box];
    retrieve   [label="Retrieve and Analyze Text", shape=box];
    decision   [label="Text Forms Correct URL?", shape=diamond];
    download   [label="Download Document", shape=box];
    current    [label="Document Becomes Current", shape=ellipse];
    push_back  [label="Push Current Document to Back Stack", shape=box];
    no_current [label="No Current Document", shape=box];
    error_msg  [label="Display Error Message in HTML Display Zone", shape=box];
    back_btn   [label="Back Button Pressed", shape=box];
    restore    [label="Restore Last Current Page", shape=box];

    start -> enter_key;
    start -> file_open;
    enter_key -> retrieve;
    file_open -> retrieve;
    retrieve -> decision;
    decision -> download   [label="Correct"];
    decision -> push_back  [label="Not Correct"];
    download -> current;
    push_back -> no_current;
    no_current -> error_msg;
    error_msg -> back_btn;
    back_btn -> restore;
    restore -> current;
}
```

```text
1. Start → Enter Pressed in Address Field → Retrieve and Analyze Text → Text Forms Correct URL? → Download Document → Document Becomes Current
2. Start → Enter Pressed in Address Field → Retrieve and Analyze Text → Text Forms Correct URL? → Push Current Document to Back Stack → No Current Document → Display Error Message in HTML Display Zone → Back Button Pressed → Restore Last Current Page → Document Becomes Current
3. Start → File -> Open Selected → Retrieve and Analyze Text → Text Forms Correct URL? → Download Document → Document Becomes Current
4. Start → File -> Open Selected → Retrieve and Analyze Text → Text Forms Correct URL? → Push Current Document to Back Stack → No Current Document → Display Error Message in HTML Display Zone → Back Button Pressed → Restore Last Current Page → Document Becomes Current
```