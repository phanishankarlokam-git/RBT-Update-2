```dot
digraph B19_Reload {
  CurrentPageDisplayed [label="Current Page Displayed", shape=ellipse];
  HistoryEmpty [label="History Stacks Empty", shape=diamond];
  HistoryPopulated [label="History Stacks Populated", shape=diamond];
  ReloadPressed [label="Reload Pressed", shape=box];
  PageRedownloaded [label="Page Re-Downloaded From Same Location", shape=box];
  StacksUnchanged [label="Back and Forward Stacks Unchanged", shape=box];
  ReloadedPageDisplayed [label="Reloaded Page Displayed", shape=ellipse];

  CurrentPageDisplayed -> HistoryEmpty;
  CurrentPageDisplayed -> HistoryPopulated;
  HistoryEmpty -> ReloadPressed;
  HistoryPopulated -> ReloadPressed;
  ReloadPressed -> PageRedownloaded;
  PageRedownloaded -> StacksUnchanged;
  StacksUnchanged -> ReloadedPageDisplayed;
}
```

```text
1. Current Page Displayed → History Stacks Empty → Reload Pressed → Page Re-Downloaded From Same Location → Back and Forward Stacks Unchanged → Reloaded Page Displayed
2. Current Page Displayed → History Stacks Populated → Reload Pressed → Page Re-Downloaded From Same Location → Back and Forward Stacks Unchanged → Reloaded Page Displayed
```