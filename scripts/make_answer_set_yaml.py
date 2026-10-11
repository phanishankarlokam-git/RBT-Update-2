"""
One-off helper used to create data/answer_set/B*.yaml.

The requirement text and every quoted note are copied verbatim from Browser.pptx
(the script asserts that each quote really is a substring of the slide notes),
so the only hand-made parts are the node ids in the routes and the sparkle checks.
"""
import json, sys, textwrap
import yaml
from pptx import Presentation

PPTX = sys.argv[1] if len(sys.argv) > 1 else 'Browser.pptx'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'data/answer_set'

prs = Presentation(PPTX)
req_text, notes_text, diagram_slide, notes_slides = {}, {}, {}, {}
for i, s in enumerate(prs.slides, 1):
    if s.has_notes_slide:
        t = s.notes_slide.notes_text_frame.text.strip()
        if t[:1] == 'B' and ':' in t:
            rid, body = t.split(':', 1)
            body = body.strip()
            if body.startswith('“') and body.endswith('”'):
                body = body[1:-1]
            req_text[rid] = body
            diagram_slide[rid] = i
    title, body = None, None
    for sh in s.shapes:
        if sh.is_placeholder and sh.has_text_frame:
            if title is None:
                title = sh.text_frame.text
            else:
                body = sh.text_frame.text
    if title and 'Notes' in title:
        rid = title.split()[0]
        notes_text[rid] = (notes_text.get(rid, '') + '\n' + (body or '')).strip()
        notes_slides.setdefault(rid, []).append(i)

SPEC = {
 'B2': dict(
   test_cases=[
     dict(id='T1', type='fork',
          notes='Launching Browser → (display) → [showing all FOUR] components',
          routes=[['LB','MMB'], ['LB','NT'], ['LB','TFUE'], ['LB','HDZ']]),
     dict(id='T2', type='relational',
          notes='Launching Browser → (display) → [showing all FOUR] components AND making sure that the first three are “fixed”',
          routes=[],
          why_not_a_path='It compares two separate launches: the first three components must be the SAME in both. '
                         'One path, or a list of separate paths, cannot express that comparison.'),
   ],
   sparkles=[
     dict(id='S1', notes='split', check=dict(type='fanout', targets=['FIX','TBI','MMB','NT','TFUE','HDZ'], min=2)),
     dict(id='S2', notes='use of “HTML Display Zone” as the name of a node', check=dict(type='uses_term', node='HDZ')),
     dict(id='S3', notes='compositions', check=dict(type='composition', parts=['MMB','NT','TFUE','HDZ'], min=2)),
   ]),
 'B5': dict(
   test_cases=[
     dict(id='T1', type='fork', notes='“File” → (all THREE mandatory children)',
          routes=[['FM','OPEN'], ['FM','CLOSE'], ['FM','EXIT']]),
     dict(id='T2', type='fork', notes='“File” → (all THREE mandatory children + an optional, Save, child)',
          routes=[['FM','OPEN'], ['FM','CLOSE'], ['FM','EXIT'], ['FM','OTH']]),
   ],
   sparkles=[
     dict(id='S1', notes='composition', check=dict(type='composition', parts=['OPEN','CLOSE','EXIT','OTH'], min=2)),
     dict(id='S2', notes='modeling OPTIONALS as a child node', check=dict(type='optional_child', whole='FM')),
   ]),
 'B7': dict(
   test_cases=[
     dict(id='T1', type='fork', notes='“Toolbar” → (all FOUR mandatory children)',
          routes=[['TB','BACK'], ['TB','FWD'], ['TB','HOME'], ['TB','RELOAD']]),
     dict(id='T2', type='fork', notes='“Toolbar” → (all FOUR mandatory children + an optional, [e.g., Extensions], child)',
          routes=[['TB','BACK'], ['TB','FWD'], ['TB','HOME'], ['TB','RELOAD'], ['TB','OTH']]),
   ],
   sparkles=[
     dict(id='S1', notes='composition', check=dict(type='composition', parts=['BACK','FWD','HOME','RELOAD','OTH'], min=2)),
     dict(id='S2', notes='modeling OPTIONALS as a child node', check=dict(type='optional_child', whole='TB')),
     dict(id='S3', notes='modeling “<--” and “-->” as part of the “Back” and “Forward” respectively',
          check=dict(type='label_has', nodes={'BACK': ['<--', '<-', '←', 'arrow'], 'FWD': ['-->', '->', '→', 'arrow']})),
     dict(id='S4', notes='an annotation note about the LOCATION of the “Toolbar” (i.e., to the LEFT and DIRECTL UNDER)',
          check=dict(type='text_has', all_of=[['left'], ['under', 'below', 'beneath']])),
   ]),
 'B11': dict(
   test_cases=[
     dict(id='T1', type='path', notes='“No Current Page” → (display one simple HTML page) → “Current Page”', routes=[['NCP','CP']]),
     dict(id='T2', type='path', notes='“Current Page” → (display no simple HTML page) → “No Current Page”', routes=[['CP','NCP']]),
   ],
   sparkles=[
     dict(id='S1', notes='do NOT model “Browser” at all', check=dict(type='no_word', word='browser')),
     dict(id='S2', notes='designate “No Current Page” and “Current Page” as the two, parallel initial/starting states',
          check=dict(type='entry_states', nodes=['NCP','CP'])),
     dict(id='S3', notes='use of “No Current Page” and “Current Page” as the labels of the states',
          check=dict(type='uses_term', node=['NCP','CP'])),
     dict(id='S4', notes='the XOR status is modeled as two separate states',
          check=dict(type='concepts', nodes=['NCP','CP'])),
   ]),
 'B12': dict(
   test_cases=[
     dict(id='T1', type='fork', notes='“Browser” → … → (“OK”) → do THREE things',
          routes=[['(OK)','TFC'], ['(OK)','CRD'], ['(OK)','CPW']]),
     dict(id='T2', type='path', notes='“Browser” → …. → (“Cancel”) → do ONE thing',
          routes=[['(Cancel)','CPW']]),
   ],
   sparkles=[
     dict(id='S1', notes='composition', check=dict(type='composition', parts=['TP','TF','OKB','CB','OTH'], min=2)),
     dict(id='S2', notes='making sure that “Other(s)” is a part of “Pop-up Window', check=dict(type='optional_child', whole='PW')),
     dict(id='S3', notes='a single “Closing Pop-up Window” state that is shared between “OK” button press and “Cancel” button press',
          check=dict(type='shared_target', node='CPW', after=['OK', 'Cancel'])),
     dict(id='S4', notes='“AND” split after “OK”', check=dict(type='fanout', targets=['TFC','CRD','CPW'], min=2, after='OK')),
   ]),
 'B15': dict(
   test_cases=[
     dict(id='T1', type='fork', notes='“Browser” → …  → show the THREE mandatory items',
          routes=[['NP'], ['MH'], ['RDV']]),
     dict(id='T2', type='fork', notes='“Browser” → …. → show the THREE mandatory items AND one optional item (e.g., Programming Language = C)',
          routes=[['NP'], ['MH'], ['RDV'], ['OTH']]),
   ],
   sparkles=[
     dict(id='S1', notes='composition', check=dict(type='composition', parts=['NP','MH','RDV','OTH'], min=2)),
     dict(id='S2', notes='making sure that “Other(s)” is a part of “Pop-up Window', check=dict(type='optional_child', whole='PW')),
   ]),
 'B16': dict(
   test_cases=[
     dict(id='T1', type='path', notes='“Browser” → (check) … → (no) → “Back” Button Disabled', routes=[['BBD']]),
     dict(id='T2', type='loop', notes='“Browser” → (check) … → (no) → “Back” Button Clickable → (click) → (do nothing) → “Back” Button Clickable',
          routes=[['(no | no previous page)','(do nothing | no action)']]),
     dict(id='T3', type='fork', notes='“Browser” → (check) … → (yes) → “Back” Button Clickable → (click) … → Do TWO things',
          routes=[['(yes | previous page exists)','UHS'], ['(yes | previous page exists)','CPP']]),
   ],
   sparkles=[
     dict(id='S1', notes='having the conditional check BEFORE any potential “Back” button click', check=dict(type='precedes', first='DEC', then='(click back)')),
     dict(id='S2', notes='a split of XOR (exclusive OR) after the “no” branch of the condition check', check=dict(type='fanout', targets=['BBC','BBD'], min=2, after='no')),
     dict(id='S3', notes='a swimlane so that the “Back” button click can be minimally defined', check=dict(type='manual')),
     dict(id='S4', notes='a split of AND on the “yes” branch after the button click', check=dict(type='fanout', targets=['UHS','CPP'], min=2, after='click back')),
     dict(id='S5', notes='make sure that “Update History Stack” is explicitly modeled', check=dict(type='concepts', nodes=['UHS'])),
   ]),
 'B19': dict(
   test_cases=[
     dict(id='T1', type='fork', notes='“Browser” → (click …) → do the TWO things', routes=[['KHSU'], ['DCPA']]),
   ],
   sparkles=[
     dict(id='S1', notes='split', check=dict(type='fanout', targets=['KHSU','DCPA'], min=2)),
     dict(id='S2', notes='make sure that “Keeping History Stack Unchanged” is explicitly modeled', check=dict(type='concepts', nodes=['KHSU'])),
   ]),
 'B20': dict(
   test_cases=[
     dict(id='T1a', type='path', notes='“Browser” → (enter “address field”) → CONDITION → (yes) → “Document … downloaded and displayed …”',
          routes=[['(enter address field)','DDC']]),
     dict(id='T2a', type='fork', notes='“Browser” → (enter “address field”) → CONDITION → (no) → do the THREE things and END here',
          routes=[['(enter address field)','PCB'], ['(enter address field)','DNC'], ['(enter address field)','SEM']]),
     dict(id='T3a', type='path', notes='“Browser” → (enter “address field”) → CONDITION → (no) → do the THREE things → (merge) → click “Back” button → “Displaying the Last …”',
          routes=[['(enter address field)','DLC']]),
     dict(id='T1b', type='path', notes='3 additional logical test cases that begin with “Browser” → (click “File - -> Open”) → …',
          routes=[['(click File Open)','DDC']]),
     dict(id='T2b', type='fork', notes='3 additional logical test cases that begin with “Browser” → (click “File - -> Open”) → …',
          routes=[['(click File Open)','PCB'], ['(click File Open)','DNC'], ['(click File Open)','SEM']]),
     dict(id='T3b', type='path', notes='3 additional logical test cases that begin with “Browser” → (click “File - -> Open”) → …',
          routes=[['(click File Open)','DLC']]),
   ],
   sparkles=[
     dict(id='S1', notes='the TWO transitions coming out of “Browser”', check=dict(type='converge', node='DEC', after=['enter address field', 'click File Open'])),
     dict(id='S2', notes='use of “To-be-opened resource” to ABSTRACT both “address field” entering and “File - -> Open” clicking',
          check=dict(type='label_has', nodes={'DEC': ['resource', 'to-be-opened', 'to be opened']})),
     dict(id='S3', notes='the split to organize the three “AND” actions', check=dict(type='fanout', targets=['PCB','DNC','SEM'], min=3)),
     dict(id='S4', notes='the merge to synchronize (bring back) the completion of the three actions', check=dict(type='fanin', sources=['PCB','DNC','SEM'], min=2)),
     dict(id='S5', notes='make sure that the click “Back” button is on the “no” branch and is coming out of the merge',
          check=dict(type='fanin', sources=['PCB','DNC','SEM'], min=2, then='DLC')),
   ]),
 'B23': dict(
   test_cases=[
     dict(id='T1', type='path', notes='“Browser” → (render …) → Anchor context? → (no) → “Content Click Disabled”', routes=[['CCD']]),
     dict(id='T2', type='fork', notes='“Browser” → (render …) → Anchor context? → (yes) → “Content Click Enabled” → do “Pushing … “Back” Stack” and the second conditional check → (no) → “ “Forward” Stack Cleared”',
          routes=[['PCB'], ['FSC']]),
     dict(id='T3', type='ordered', notes='“Browser” → (render …) → Anchor context? → (yes) → “Content Click Enabled” → do “Pushing … “Back” Stack” and the second conditional check → (yes) → sequentially, do two things/actions, “Displaying top …” first, and then “Pop top …”',
          routes=[['PCB'], ['DFT','FSP']]),
   ],
   sparkles=[
     dict(id='S1', notes='the “Anchor content?” conditional check', check=dict(type='concepts', nodes=['DEC1'])),
     dict(id='S2', notes='explicitly modeling “Content Click Disabled” along the “no” branch', check=dict(type='concepts', nodes=['CCD'])),
     dict(id='S3', notes='the split after “click anchor element” that leads to one action and one conditional check', check=dict(type='fanout', targets=['PCB','DEC2'], min=2)),
     dict(id='S4', notes='the conditional check of “Anchor’s “href” = top of the “Forward” Stack?” is modeled after/inside a split', check=dict(type='in_split', node='DEC2')),
     dict(id='S5', notes='one has to display the top first, and then pop the top', check=dict(type='sequence', first='DFT', then='FSP')),
   ]),
}
DATA_NOTES = {
 'B2':  ['The composition diamond and the fork bar are drawn as notation. The bar is kept as an unlabelled node; composition lines are edges with kind=composition.'],
 'B11': ['The slide spells "HMTL" in both transition labels; kept as on the slide. The notes spell it "HTML".'],
 'B19': ['The notes say a second test case (page no longer exists) is missing from the requirement; only ONE test case is defined, as instructed.'],
 'B20': ['The notes list the three "enter address field" test cases and say the same three exist for "click File --> Open"; T1b-T3b are those three.'],
 'B23': ['Slide 21 also holds an unconnected "Downloading Current Page Again" ellipse and an unconnected "click “Toolbar - -> Reload”" label. '
         'They are not linked to anything and look left over from B19, so they are not encoded. Please confirm.',
         'The notes write "Anchor context?"; the diagram says "Anchor content?". The diagram wording is used.'],
}

class Dumper(yaml.SafeDumper):
    pass
def str_rep(d, s):
    if '\n' in s or len(s) > 100:
        return d.represent_scalar('tag:yaml.org,2002:str', s, style='|' if '\n' in s else '>')
    return d.represent_scalar('tag:yaml.org,2002:str', s)
Dumper.add_representer(str, str_rep)
def list_rep(d, l):
    flow = all(isinstance(x, str) and len(x) <= 30 for x in l) and len(l) <= 8
    return d.represent_sequence('tag:yaml.org,2002:seq', l, flow_style=flow)
Dumper.add_representer(list, list_rep)

HEADER = """# Answer set {rid}, encoded from Browser.pptx (diagram slide {ds}, notes slide(s) {ns}).
# The graph itself is in {rid}.dot. This file holds what the notes say.
#
# routes: each logical test case is broken into routes. A route is a list of
#   checkpoints that one generated test path must pass through, in this order.
#     NODE    a node id from {rid}.dot (the path must visit a node that means the same thing)
#     (text)  an event or guard word from the notes, e.g. (OK); some step of the path must carry it.
#             "(a | b)" means either wording is accepted.
#   A route keeps: the start node (unless it is the neutral "Browser" every test starts from),
#   the event/guard words that tell this test case apart from the others, and the outcome
#   nodes the test checks. In-between nodes are left out, because a generated path can reach
#   the same outcome without drawing them.
#   A test case with several routes (type: fork) is covered only when every route is covered.
#   type: relational means the test case compares two runs and has no route at all.
# sparkles: the expert modelling decisions listed in the notes, each with the
#   mechanical check the tool runs (see coverage/checks.py). type: manual = judged by hand.
"""

for rid, spec in SPEC.items():
    nt = notes_text[rid]
    for tc in spec['test_cases']:
        assert tc['notes'] in nt, (rid, tc['id'], tc['notes'])
    for sp in spec['sparkles']:
        assert sp['notes'] in nt, (rid, sp['id'], sp['notes'])
    doc = {
        'id': rid,
        'diagram_slide': diagram_slide[rid],
        'notes_slides': notes_slides[rid],
        'requirement': req_text[rid],
        'test_cases': spec['test_cases'],
        'sparkles': spec['sparkles'],
        'data_notes': DATA_NOTES.get(rid, []),
        'notes_verbatim': nt,
    }
    txt = yaml.dump(doc, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=110)
    hdr = HEADER.format(rid=rid, ds=diagram_slide[rid], ns=', '.join(map(str, notes_slides[rid])))
    open(f'{OUT}/{rid}.yaml', 'w').write(hdr + txt)
    print('wrote', rid, len(spec['test_cases']), 'test cases,', len(spec['sparkles']), 'sparkles')
