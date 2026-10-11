```dot
digraph FileOpenDialog {
    rankdir=TB;
    node [shape=box, style=rounded, fontname="Helvetica"];

    Main        [label="Main Window", shape=ellipse];
    Dialog      [label="Dialog Displayed"];
    URLEntered  [label="URL Entered"];
    AddrUpdated [label="Address Field Updated"];
    Download    [label="Download Attempted", shape=ellipse];
    NoAction    [label="No Action Taken", shape=ellipse];

    Main        -> Dialog      [label="File > Open selected"];
    Dialog      -> URLEntered  [label="user enters URL"];
    Dialog      -> AddrUpdated [label="OK pressed (empty field)"];
    URLEntered  -> AddrUpdated [label="OK pressed"];
    Dialog      -> NoAction    [label="Cancel pressed (empty field)"];
    URLEntered  -> NoAction    [label="Cancel pressed"];
    AddrUpdated -> Download    [label="download attempted"];
}
```

```text
1. Main Window → Dialog Displayed → Address Field Updated → Download Attempted
2. Main Window → Dialog Displayed → URL Entered → Address Field Updated → Download Attempted
3. Main Window → Dialog Displayed → No Action Taken
4. Main Window → Dialog Displayed → URL Entered → No Action Taken
```