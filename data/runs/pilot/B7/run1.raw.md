```dot
digraph B7_Toolbar {
  rankdir=TB;
  node [fontname="Helvetica", fontsize=10];

  start   [label="Start", shape=ellipse];
  pos     [label="Toolbar Positioned (Left, Under Menu Bar)", shape=box];
  back    [label="Back Button Present", shape=box];
  fwd     [label="Forward Button Present", shape=box];
  home    [label="Home Button Present", shape=box];
  reload  [label="Reload Button Present", shape=box];

  otherQ   [label="Other Buttons?", shape=diamond];
  otherYes [label="Other Buttons Present", shape=box];
  otherNo  [label="No Other Buttons", shape=box];

  backQ    [label="Back Icon Feasible?", shape=diamond];
  backIcon [label="Back Renders Icon", shape=box];
  backText [label="Back Renders Text", shape=box];

  fwdQ     [label="Forward Icon Feasible?", shape=diamond];
  fwdIcon  [label="Forward Renders Icon", shape=box];
  fwdText  [label="Forward Renders Text", shape=box];

  homeQ    [label="Home Icon Feasible?", shape=diamond];
  homeIcon [label="Home Renders Icon", shape=box];
  homeText [label="Home Renders Text", shape=box];

  reloadQ    [label="Reload Icon Feasible?", shape=diamond];
  reloadIcon [label="Reload Renders Icon", shape=box];
  reloadText [label="Reload Renders Text", shape=box];

  end [label="End", shape=ellipse];

  start -> pos;
  pos -> back;
  back -> fwd;
  fwd -> home;
  home -> reload;
  reload -> otherQ;

  otherQ -> otherYes [label="yes"];
  otherQ -> otherNo [label="no"];
  otherYes -> backQ;
  otherNo -> backQ;

  backQ -> backIcon [label="yes"];
  backQ -> backText [label="no"];
  backIcon -> fwdQ;
  backText -> fwdQ;

  fwdQ -> fwdIcon [label="yes"];
  fwdQ -> fwdText [label="no"];
  fwdIcon -> homeQ;
  fwdText -> homeQ;

  homeQ -> homeIcon [label="yes"];
  homeQ -> homeText [label="no"];
  homeIcon -> reloadQ;
  homeText -> reloadQ;

  reloadQ -> reloadIcon [label="yes"];
  reloadQ -> reloadText [label="no"];
  reloadIcon -> end;
  reloadText -> end;
}
```

```text
1. Start → Toolbar Positioned (Left, Under Menu Bar) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Other Buttons? → Other Buttons Present → Back Icon Feasible? → Back Renders Icon → Forward Icon Feasible? → Forward Renders Icon → Home Icon Feasible? → Home Renders Icon → Reload Icon Feasible? → Reload Renders Icon → End
2. Start → Toolbar Positioned (Left, Under Menu Bar) → Back Button Present → Forward Button Present → Home Button Present → Reload Button Present → Other Buttons? → No Other Buttons → Back Icon Feasible? → Back Renders Text → Forward Icon Feasible? → Forward Renders Text → Home Icon Feasible? → Home Renders Text → Reload Icon Feasible? → Reload Renders Text → End
```