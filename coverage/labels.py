"""
STEP 3 of the procedure: deciding whether two labels mean the same thing.

The rule, in plain words
------------------------
1. Clean both labels: lower-case, drop quotes and punctuation, split into words,
   drop filler words ("the", "of", "to", ...), and cut simple English endings
   (-ing, -ed, -s, a final -e) so that "Launching" and "launch" become the same word.
2. Compare the two word sets with the Jaccard score:

        score = (words both labels share) / (all different words in the two labels)

3. The labels match when the score is 0.5 or more, OR when every word of the
   answer-set label appears in the generated label ("Open" inside 'Verify "Open" Present'),
   EXCEPT when
     - one label is negated and the other is not ("No Current Page" vs "Current Page"), or
     - the labels differ by a known pair of opposites ("Enabled" vs "Disabled").
4. A generated label is read as the answer-set label it matches best (highest score among
   the labels it matches). If two answer-set labels tie for best, we say "no match" rather
   than guess.

Everything here is deterministic: the same two labels always give the same answer.
"""
import re
import unicodedata

THRESHOLD = 0.5

# Filler words carry no meaning for matching. "user" is included because generated
# labels often name the actor ("user enters URL") while the answer set never does.
STOPWORDS = {
    "a", "an", "the", "of", "for", "to", "in", "into", "on", "at", "by", "with", "from",
    "and", "or", "is", "are", "be", "been", "being", "as", "it", "its", "this", "that",
    "these", "those", "all", "any", "some", "e", "g", "eg", "etc", "re", "if", "then",
    "than", "will", "shall", "can", "may", "must", "also", "s", "via", "do", "does",
    "user", "he", "she", "his", "her", "their",
}

# Words that turn a label into its negative. Stored in their cleaned (stemmed) form.
NEGATIONS = {"no", "not", "non", "none", "never", "without", "noth", "noop"}

# Pairs of opposite words (raw form; they are stemmed below). If one label has the first
# word and the other label has the second word, the two labels are never matched.
_OPPOSITE_WORDS = [
    ("enabled", "disabled"), ("clickable", "disabled"), ("active", "inactive"),
    ("valid", "invalid"), ("correct", "incorrect"), ("success", "failure"),
    ("successful", "failed"), ("succeed", "fail"), ("show", "hide"), ("shown", "hidden"),
    ("open", "close"), ("push", "pop"), ("clear", "pop"), ("back", "forward"),
    ("empty", "populated"), ("empty", "nonempty"), ("match", "mismatch"),
    ("add", "remove"), ("first", "last"), ("yes", "no"),
]

# Two-word spellings that mean one word ("pop up" = "popup").
_COMPOUNDS = {("pop", "up"): "popup", ("tool", "bar"): "toolbar", ("drop", "down"): "dropdown",
              ("pull", "down"): "pulldown", ("web", "page"): "webpage", ("no", "op"): "noop"}


def stem(word):
    """Cut common English endings so that different forms of one word look the same.

    launching/launched/launch -> launch, closing/closed/close -> clos,
    popped/pop -> pop, copied/copy -> copy, components -> component.
    """
    w = word
    if len(w) <= 3:
        return w
    if w.endswith("ational"):
        w = w[:-7] + "ation"
    elif w.endswith("ies") and len(w) > 4:
        w = w[:-3] + "y"
    elif w.endswith("sses"):
        w = w[:-2]
    elif w.endswith("ing") and len(w) > 5:
        w = w[:-3]
    elif w.endswith("ed") and len(w) > 4:
        w = w[:-2]
        if w.endswith("i"):
            w = w[:-1] + "y"
    elif w.endswith("es") and len(w) > 4 and (w[-3] in "sxz" or w[-4:-2] in ("ch", "sh")):
        w = w[:-2]
    elif w.endswith("s") and not w.endswith(("ss", "us", "is")) and len(w) > 3:
        w = w[:-1]
    if len(w) > 3 and w[-1] == w[-2] and w[-1] not in "lsz" and w[-1] not in "aeiou":
        w = w[:-1]
    if len(w) > 4 and w.endswith("e"):
        w = w[:-1]
    return w


OPPOSITES = [(stem(a), stem(b)) for a, b in _OPPOSITE_WORDS]


def clean_text(label):
    """Lower-case, remove quotes, arrows and punctuation. Returns a plain string."""
    s = unicodedata.normalize("NFKC", str(label or "")).lower()
    s = s.replace("\\n", " ").replace("\n", " ")
    s = re.sub(r"[“”‘’\"'`]", "", s)      # quotes
    s = s.replace("(s)", "s")                                    # Other(s) -> others
    s = re.sub(r"<-+|-+>|→|←|=>", " ", s)               # arrows
    s = re.sub(r"[^a-z0-9]+", " ", s)                            # everything else
    return s.strip()


def words(label):
    """The set of cleaned words of a label (this is what gets compared)."""
    raw = clean_text(label).split()
    merged, i = [], 0
    while i < len(raw):
        if i + 1 < len(raw) and (raw[i], raw[i + 1]) in _COMPOUNDS:
            merged.append(_COMPOUNDS[(raw[i], raw[i + 1])])
            i += 2
        else:
            merged.append(raw[i])
            i += 1
    return frozenset(stem(w) for w in merged if w not in STOPWORDS)


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def is_negated(ws):
    return bool(ws & NEGATIONS)


def blocked(wa, wb):
    """True when the two word sets must never match (negation or opposites)."""
    if is_negated(wa) != is_negated(wb):
        return True
    for x, y in OPPOSITES:
        if (x in wa and y not in wa and y in wb and x not in wb) or \
           (y in wa and x not in wa and x in wb and y not in wb):
            return True
    return False


def similarity(label_a, label_b):
    """Jaccard score of two labels, or 0.0 when a guard blocks the pair."""
    wa, wb = words(label_a), words(label_b)
    if blocked(wa, wb):
        return 0.0
    return jaccard(wa, wb)


def contains_all(label_small, label_big):
    """True when every cleaned word of label_small also appears in label_big (and no guard blocks)."""
    ws, wb = words(label_small), words(label_big)
    if not ws:
        return False
    if is_negated(ws) != is_negated(wb) and not (ws <= NEGATIONS):
        return False
    return ws <= wb


def is_exact(label_a, label_b):
    """Same word set after cleaning (score 1.0)."""
    wa, wb = words(label_a), words(label_b)
    return bool(wa) and wa == wb


def match(ref_label, gen_label, threshold=THRESHOLD):
    """(does it match?, score). Score is the Jaccard score; containment of all the
    answer-set words also counts as a match."""
    wa, wb = words(ref_label), words(gen_label)
    if not wa or not wb or blocked(wa, wb):
        return False, 0.0
    j = jaccard(wa, wb)
    return (j >= threshold or wa <= wb), j


def best_match(label, candidates, threshold=THRESHOLD):
    """Find the candidate label that `label` matches best.

    candidates: dict id -> label text (the answer-set side).
    Returns (id or None, score, note). note is 'exact', 'fuzzy', 'contains', 'tie' or 'none'.
    """
    scored = []
    for cid, text in candidates.items():
        ok, sc = match(text, label, threshold)
        if ok:
            scored.append((sc, cid))
    if not scored:
        best = max((similarity(label, t) for t in candidates.values()), default=0.0)
        return None, best, "none"
    scored.sort(key=lambda t: (-t[0], t[1]))
    top = scored[0][0]
    tied = [cid for sc, cid in scored if abs(sc - top) < 1e-9]
    if len(tied) > 1:
        return None, top, "tie"
    if top >= 1.0 - 1e-9:
        how = "exact"
    elif top >= threshold:
        how = "fuzzy"
    else:
        how = "contains"
    return tied[0], top, how
