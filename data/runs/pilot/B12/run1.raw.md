```dot
digraph B12_FileOpen {
  rankdir=TB;
  node [shape=box, style=rounded, fontname="Helvetica"];

  n1 [label="Main Browser Window", shape=oval];
  n2 [label="Select File > Open"];
  n3 [label="Open Dialog Displayed"];
  n4 [label="Enter URL in Text Field"];
  n5 [label="Click OK"];
  n6 [label="Click Cancel"];
  n7 [label="Dialog Closes; Contents Remembered and Copied to Address Field"];
  n8 [label="Browser Attempts Download", shape=oval, peripheries=2];
  n9 [label="Dialog Closes; No Further Action Taken", shape=oval, peripheries=2];

  n1 -> n2;
  n2 -> n3;
  n3 -> n4;
  n4 -> n5;
  n4 -> n6;
  n5 -> n7;
  n7 -> n8;
  n6 -> n9;
}
```

```text
1. Main Browser Window → Select File > Open → Open Dialog Displayed → Enter URL in Text Field → Click OK → Dialog Closes; Contents Remembered and Copied to Address Field → Browser Attempts Download
2. Main Browser Window → Select File > Open → Open Dialog Displayed → Enter URL in Text Field → Click Cancel → Dialog Closes; No Further Action Taken
```