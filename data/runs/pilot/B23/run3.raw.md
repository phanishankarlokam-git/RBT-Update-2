```dot
digraph B23_AnchorNavigation {
    rankdir=TB;

    AnchorsContrast [label="Anchors Rendered in Contrast", shape=ellipse];
    AnchorClicked [label="Anchor Clicked", shape=box];
    PushBack [label="Push Back Stack", shape=box];
    CheckMatch [label="Href Matches Forward Stack Top?", shape=diamond];
    PopForward [label="Pop Forward Stack", shape=box];
    ClearForward [label="Clear Forward Stack", shape=box];
    AttemptDownload [label="Attempt Download", shape=box];
    DownloadSuccessful [label="Download Successful?", shape=diamond];
    DocUpdated [label="Current Document Updated", shape=box];
    DocUnchanged [label="Current Document Unchanged", shape=box];
    End [label="End", shape=ellipse];

    AnchorsContrast -> AnchorClicked;
    AnchorClicked -> PushBack;
    PushBack -> CheckMatch;
    CheckMatch -> PopForward [label="Match"];
    CheckMatch -> ClearForward [label="No Match"];
    PopForward -> AttemptDownload;
    ClearForward -> AttemptDownload;
    AttemptDownload -> DownloadSuccessful;
    DownloadSuccessful -> DocUpdated [label="Success"];
    DownloadSuccessful -> DocUnchanged [label="Failure"];
    DocUpdated -> End;
    DocUnchanged -> End;
}
```

```text
1. Anchors Rendered in Contrast → Anchor Clicked → Push Back Stack → Href Matches Forward Stack Top? → Pop Forward Stack → Attempt Download → Download Successful? → Current Document Updated → End
2. Anchors Rendered in Contrast → Anchor Clicked → Push Back Stack → Href Matches Forward Stack Top? → Pop Forward Stack → Attempt Download → Download Successful? → Current Document Unchanged → End
3. Anchors Rendered in Contrast → Anchor Clicked → Push Back Stack → Href Matches Forward Stack Top? → Clear Forward Stack → Attempt Download → Download Successful? → Current Document Updated → End
4. Anchors Rendered in Contrast → Anchor Clicked → Push Back Stack → Href Matches Forward Stack Top? → Clear Forward Stack → Attempt Download → Download Successful? → Current Document Unchanged → End
```