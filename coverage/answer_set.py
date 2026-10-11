"""
STEP 1 of the procedure: the answer set in machine-readable form.

For each requirement there are two files in data/answer_set/:
  B2.dot   the answer-set diagram, node by node and arrow by arrow
  B2.yaml  the notes: requirement text, logical test cases broken into routes, sparkles

check_against_pptx() compares these files with Browser.pptx automatically:
  - every labelled shape on the diagram slide must appear as a node label in the DOT file
    (and the other way round), and every arrow-label text box must appear as an arrow label;
  - the requirement text in the YAML must equal the slide's speaker notes.
This catches typing mistakes in the hand-made encoding.
"""
import os

import yaml

from .graph import load_dot
from .labels import clean_text


def load(answer_dir, rid):
    tg = load_dot(os.path.join(answer_dir, f"{rid}.dot"), name=rid)
    spec = yaml.safe_load(open(os.path.join(answer_dir, f"{rid}.yaml"), encoding="utf-8"))
    # sanity: every node id used in routes / checks exists in the DOT file
    ids = set(tg.nodes)
    for tc in spec["test_cases"]:
        for rt in tc.get("routes", []):
            for cp in rt:
                if not cp.startswith("(") and cp not in ids:
                    raise ValueError(f"{rid} {tc['id']}: unknown node id {cp}")
    return tg, spec


def check_against_pptx(pptx_path, answer_dir, rids):
    """Returns a list of text lines describing any difference found (empty list = all good)."""
    from pptx import Presentation
    from pptx.util import Emu  # noqa: F401  (imported to fail early if python-pptx is missing)

    prs = Presentation(pptx_path)
    report = []
    slide_of = {}
    for i, s in enumerate(prs.slides, 1):
        if s.has_notes_slide:
            t = s.notes_slide.notes_text_frame.text.strip()
            if t[:1] == "B" and ":" in t:
                slide_of[t.split(":", 1)[0]] = (i, s, t.split(":", 1)[1].strip())
    for rid in rids:
        if rid not in slide_of:
            report.append(f"{rid}: no diagram slide found")
            continue
        i, slide, req = slide_of[rid]
        tg, spec = load(answer_dir, rid)
        shapes, boxes = set(), set()
        for sh in slide.shapes:
            if not sh.has_text_frame:
                continue
            txt = " ".join(p.text for p in sh.text_frame.paragraphs).strip()
            if not txt or clean_text(txt) == clean_text(rid):
                continue
            geom = sh.auto_shape_type if sh.shape_type == 1 else None
            if sh.shape_type == 17:            # text box = arrow label on these slides
                boxes.add(clean_text(txt))
            else:
                shapes.add(clean_text(txt))
        node_labels = {clean_text(n.label) for n in tg.nodes.values() if n.label.strip()}
        edge_labels = {clean_text(e.label) for e in tg.edges if e.label}
        for s in sorted(shapes - node_labels):
            report.append(f"{rid} (slide {i}): shape text '{s}' is not a node label in {rid}.dot")
        for s in sorted(node_labels - shapes):
            report.append(f"{rid} (slide {i}): node label '{s}' in {rid}.dot has no shape on the slide")
        for s in sorted(boxes - edge_labels):
            report.append(f"{rid} (slide {i}): text box '{s}' is not an arrow label in {rid}.dot")
        for s in sorted(edge_labels - boxes):
            report.append(f"{rid} (slide {i}): arrow label '{s}' in {rid}.dot has no text box on the slide")
        want = req
        if want.startswith("“") and want.endswith("”"):
            want = want[1:-1]
        if " ".join(spec["requirement"].split()) != " ".join(want.split()):
            report.append(f"{rid}: requirement text in {rid}.yaml differs from the slide notes")
    return report
