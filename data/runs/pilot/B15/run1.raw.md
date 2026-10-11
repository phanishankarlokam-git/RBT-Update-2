```dot
digraph HelpAbout_B15 {
    rankdir=TB;
    node [fontname="Helvetica", fontsize=10];

    Start [shape=ellipse];
    HelpMenuOpened [shape=box, label="Help Menu Opened"];
    AboutSelected [shape=box, label="About Selected"];
    AboutPopupDisplayed [shape=box, label="About Pop-up Window Displayed"];
    ProgrammerNameShown [shape=box, label="Programmer Name Shown"];
    CS585HomeworkMentionShown [shape=box, label="CS 585 Homework Mention Shown"];
    ReleaseDateShown [shape=box, label="Release Date Shown"];
    VersionNumberShown [shape=diamond, label="Version Number Shown"];
    AdditionalInfoShown [shape=box, label="Additional Info Shown"];
    PopupClosed [shape=box, label="About Pop-up Window Closed"];
    End [shape=ellipse];

    Start -> HelpMenuOpened [label="select Help menu"];
    HelpMenuOpened -> AboutSelected [label="select About"];
    AboutSelected -> AboutPopupDisplayed [label="pop-up opens"];
    AboutPopupDisplayed -> ProgrammerNameShown;
    ProgrammerNameShown -> CS585HomeworkMentionShown;
    CS585HomeworkMentionShown -> ReleaseDateShown;
    ReleaseDateShown -> VersionNumberShown;
    VersionNumberShown -> AdditionalInfoShown [label="other info included"];
    VersionNumberShown -> PopupClosed [label="no other info"];
    AdditionalInfoShown -> PopupClosed [label="close pop-up"];
    PopupClosed -> End [label="return to browser"];
}
```

```text
1. Start → Help Menu Opened → About Selected → About Pop-up Window Displayed → Programmer Name Shown → CS 585 Homework Mention Shown → Release Date Shown → Version Number Shown → Additional Info Shown → About Pop-up Window Closed → End
2. Start → Help Menu Opened → About Selected → About Pop-up Window Displayed → Programmer Name Shown → CS 585 Homework Mention Shown → Release Date Shown → Version Number Shown → About Pop-up Window Closed → End
```