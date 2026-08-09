"""Parse Chapter Two (Offense Conduct) of the USSC Guidelines Manual
(November 1, 2024) into structured JSON.

Reads the per-page text dump produced by tools/_dump_text.py. Chapter Two
occupies PDF pages 61-360 (1-based).

Design rules, in order of importance:

1.  Verbatim text is the source of truth. Every base offense level alternative
    and every specific offense characteristic carries the exact printed text.
2.  Structured values (a level number, an "+2") are a convenience layer on top
    of the verbatim text. When the printed text does not yield a value that can
    be read off directly, the structured field is null and the record is
    flagged -- it is never guessed.
3.  Anything that does not fit the expected shape is emitted to `unparsed`.

Usage: python3 tools/_parse_chapter2.py <pagedump_dir> <out.json> [appendix_a.json]
"""
import sys, os, json, re, collections

FIRST_PAGE, LAST_PAGE = 61, 360
EDITION = "November 1, 2024"

BULLET = "⚫"

# Filled by load_lines(). Used to repair the stray spaces the PDF's text layer
# drops inside words ("weapo n", "o ffense"). Never used to change a number.
SOLID_WORDS = collections.Counter()

SECTION_DEF_RE = re.compile(r"^§(2[A-Z]\d+\.\d+)\.\s+(?P<title>\S.*)$")
PART_RE = re.compile(r"^PART ([A-Z])\s*[―—-]\s*(?P<title>.*)$")
SUBPART_RE = re.compile(r"^(\d+)\.\s+([A-Z][A-Z ,'\-/&\(\)\.]{4,})$")
RUNNING_HEAD_RE = re.compile(
    r"^(§\d[A-Z]?\d*\.?\d*\s*|APPENDIX .*|CHAPTER .*)$")
FOOTER_RE = re.compile(r"Guidelines Manual\s*\(November 1, 20\s*24\)")

SUBSECTION_RE = re.compile(r"^\((?P<letter>[a-z])\)\s+(?P<rest>.*)$")
ITEM_RE = re.compile(r"^\((?P<num>\d{1,2})\)\s+(?P<rest>.*)$")


# --------------------------------------------------------------------------
# Text normalisation
# --------------------------------------------------------------------------

def build_vocabulary(pagedir, total_pages=620):
    """Count how every word is spelled when it is NOT broken across a line.

    Two counters are built from the whole manual, not just Chapter Two, because
    more evidence makes the call safer:

      joined  -- "dissemination", spelled solid somewhere on a line
      hyphen  -- "mass-marketing", spelled with a hyphen somewhere on a line

    Tokens sitting at the end of a line and ending in "-" are excluded, since
    those are exactly the ambiguous ones being decided.
    """
    joined, hyphened = collections.Counter(), collections.Counter()
    for pno in range(1, total_pages + 1):
        path = os.path.join(pagedir, f"p{pno:04d}.txt")
        if not os.path.exists(path):
            continue
        with open(path) as fh:
            text = fh.read()
        for line in text.split("\n"):
            line = line.rstrip()
            words = re.findall(r"[A-Za-z][A-Za-z\-]*[A-Za-z]", line)
            if not words:
                continue
            if line.endswith("-"):
                words = words[:-1]  # the broken tail is not evidence
            for w in words:
                (hyphened if "-" in w else joined)[w.lower()] += 1
    return joined, hyphened


def dehyphenate(lines, vocab, stats):
    """Rejoin words that the manual's justified setting broke across a line.

    A line-final "-" is either a soft hyphen inserted by the typesetter or part
    of a real compound. The manual gives no marker distinguishing them, so the
    decision is made on evidence from the rest of the document:

      * the solid spelling is attested more often  -> join
      * the hyphenated spelling is attested        -> keep the hyphen
      * neither is attested anywhere               -> join, and record it

    The third case is a default, not a finding. Every word decided that way is
    listed in the output so it can be reviewed; there are few of them and they
    are overwhelmingly ordinary words the manual happens to use once.
    """
    joined_vocab, hyphened_vocab = vocab
    out = []
    i = 0
    while i < len(lines):
        text, page = lines[i]
        m = re.search(r"([A-Za-z]{2,})-$", text.rstrip())
        if m and i + 1 < len(lines):
            nxt = lines[i + 1][0].lstrip()
            nm = re.match(r"([A-Za-z]+)", nxt)
            if nm:
                head, tail = m.group(1), nm.group(1)
                solid = (head + tail).lower()
                hyph = (head + "-" + tail).lower()
                n_solid, n_hyph = joined_vocab[solid], hyphened_vocab[hyph]
                if n_solid == 0 and n_hyph == 0:
                    decision = "join"
                    stats["joined_by_default"] += 1
                    stats.setdefault("joined_by_default_words", []).append(
                        head + "-" + tail)
                elif n_solid >= n_hyph:
                    decision = "join"
                    stats["joined_on_evidence"] += 1
                else:
                    decision = "keep"
                    stats["hyphen_kept_on_evidence"] += 1
                    stats.setdefault("hyphen_kept_words", []).append(hyph)
                if decision == "join":
                    lines[i + 1] = (text.rstrip()[:-1] + nxt, page)
                    i += 1
                    continue
        out.append((text, page))
        i += 1
    return out


def load_lines(pagedir, first, last):
    """Return [(line_text, pdf_page)] with running heads and footers removed."""
    raw_pages = []
    for pno in range(first, last + 1):
        with open(os.path.join(pagedir, f"p{pno:04d}.txt")) as fh:
            raw_pages.append((pno, fh.read()))
    vocab = build_vocabulary(pagedir)
    SOLID_WORDS.clear()
    SOLID_WORDS.update(vocab[0])

    lines = []
    for pno, text in raw_pages:
        page_lines = text.split("\n")
        # The running head / folio block sits in the first few lines of a page.
        start = 0
        for idx, ln in enumerate(page_lines[:7]):
            s = ln.strip()
            if not s:
                continue
            if FOOTER_RE.search(s) or RUNNING_HEAD_RE.match(s):
                start = idx + 1
        for ln in page_lines[start:]:
            if FOOTER_RE.search(ln):
                continue
            lines.append((ln.rstrip(), pno))
    stats = {"joined_on_evidence": 0, "joined_by_default": 0,
             "hyphen_kept_on_evidence": 0}
    lines = dehyphenate(lines, vocab, stats)
    return lines, stats


# Three separate passes, not one alternation: a single regex with both shapes
# lets the "word + lone letter" branch consume "resulting o" before the
# "lone letter + word" branch can see "o ffense".
LETTER_THEN_WORD_RE = re.compile(r"\b([b-hj-z]) ([a-z]{2,})\b")
WORD_THEN_LETTER_RE = re.compile(r"\b([a-z]{2,}) ([b-hj-z])\b")
LETTER_THEN_LETTER_RE = re.compile(r"\b([b-hj-z]) ([b-hj-z])\b")


def repair_spaced_letters(txt):
    """Rejoin a single letter that the PDF's text layer split off from its word.

    The extractor occasionally emits "dangerous weapo n", "resulting o ffense"
    or "invasion o f". Only a lone letter is moved, and only when the rejoined
    spelling is well attested elsewhere in the manual. A single letter is never
    an English word apart from "a" and "I", both of which are excluded, so the
    join cannot merge two real words. Digits are never touched, so no offense
    level, quantity or dollar figure can be altered by this step.
    """
    def repair(pattern, threshold):
        def sub(m):
            merged = m.group(1) + m.group(2)
            if SOLID_WORDS[merged.lower()] >= threshold:
                return merged
            return m.group(0)
        return sub

    txt = LETTER_THEN_WORD_RE.sub(repair(LETTER_THEN_WORD_RE, 3), txt)
    txt = WORD_THEN_LETTER_RE.sub(repair(WORD_THEN_LETTER_RE, 3), txt)
    # Two lone letters ("o f") only merge for very common short words.
    txt = LETTER_THEN_LETTER_RE.sub(repair(LETTER_THEN_LETTER_RE, 50), txt)
    return txt


def flatten(chunk):
    """Join a run of lines into one verbatim paragraph, normalising only the
    whitespace that the PDF's justification introduced."""
    txt = " ".join(l.strip() for l in chunk if l.strip())
    txt = txt.replace(" ", " ").replace(" ", " ")
    # The extractor emits stray double spaces inside citations ("21  U.S.C.").
    txt = re.sub(r"\s{2,}", " ", txt)
    # " § 841" style spacing is preserved; only collapse space before punctuation
    txt = re.sub(r"\s+([,;:.\)])", r"\1", txt)
    txt = re.sub(r"\(\s+", "(", txt)
    return repair_spaced_letters(txt).strip()


# --------------------------------------------------------------------------
# Structure extraction
# --------------------------------------------------------------------------

def wrapped_heading(lines, idx, first):
    """Part and subpart headings are set in caps and wrap onto the next line.

    Continue the heading while the following line is still all upper case and
    is not itself a new heading or a section definition.
    """
    pieces = [first.strip()]
    j = idx + 1
    while j < len(lines):
        nxt = lines[j][0].strip()
        if not nxt:
            break
        if (PART_RE.match(nxt) or SUBPART_RE.match(nxt)
                or SECTION_DEF_RE.match(nxt)):
            break
        letters = [c for c in nxt if c.isalpha()]
        if not letters or not all(c.isupper() for c in letters):
            break
        pieces.append(nxt)
        j += 1
    return re.sub(r"\s{2,}", " ", " ".join(pieces)).strip()


def find_structure(lines):
    """Locate PART / subpart headers and guideline section definitions."""
    parts, sections = [], []
    for idx, (text, page) in enumerate(lines):
        s = text.strip()
        pm = PART_RE.match(s)
        if pm:
            parts.append({"idx": idx, "part": pm.group(1),
                          "title": wrapped_heading(lines, idx, pm.group("title")),
                          "page": page})
            continue
        sm = SUBPART_RE.match(s)
        if sm and parts:
            parts[-1].setdefault("subparts", []).append(
                {"idx": idx, "number": int(sm.group(1)),
                 "title": wrapped_heading(lines, idx, sm.group(2)), "page": page})
            continue
        dm = SECTION_DEF_RE.match(s)
        if dm:
            # A bare "§2B1.5." at the start of a line is a cross-reference stub
            # inside commentary, not a section definition; it has no title text.
            sections.append({"idx": idx, "section": dm.group(1),
                             "title_head": dm.group("title").strip(),
                             "page": page})
    return parts, sections


def collect_title(lines, start_idx):
    """A guideline title may wrap onto following lines until a blank line."""
    m = SECTION_DEF_RE.match(lines[start_idx][0].strip())
    pieces = [m.group("title").strip()]
    i = start_idx + 1
    while i < len(lines):
        s = lines[i][0].strip()
        if not s:
            break
        if SUBSECTION_RE.match(s) or s == "Commentary":
            break
        pieces.append(s)
        i += 1
    return flatten(pieces), i


def split_subsections(body):
    """Split a guideline body into lettered subsections, in printed order.

    A "(x)" line opens a subsection when either
      * the letter continues the expected a, b, c ... sequence, or
      * the text after it is one of Chapter Two's subsection headings.

    The second rule matters because the manual does not always print the
    subsections in alphabetical order: §2D1.1 prints (d) Cross Reference and
    (e) Special Instruction *before* (c) DRUG QUANTITY TABLE, because the table
    is set as a full-page block. Requiring strict alphabetical order silently
    folded (d) and (e) into the tail of the last specific offense characteristic.

    The heading test also keeps a roman-numeral sub-item such as
    "(i) level 32, decrease by 2 levels" from being read as subsection (i).
    """
    subs, cur = [], None
    used = set()
    expected = "a"
    for text, page in body:
        s = text.strip()
        m = SUBSECTION_RE.match(s)
        opens = False
        if m and m.group("letter") not in used:
            letter, rest = m.group("letter"), m.group("rest")
            if letter == expected or HEADING_RE.match(rest.strip()):
                opens = True
        if opens:
            if cur:
                subs.append(cur)
            letter = m.group("letter")
            used.add(letter)
            cur = {"letter": letter, "lines": [(m.group("rest"), page)],
                   "page": page}
            nxt = chr(ord(letter) + 1)
            while nxt in used:
                nxt = chr(ord(nxt) + 1)
            expected = nxt
        elif cur is not None:
            cur["lines"].append((text, page))
    if cur:
        subs.append(cur)
    return subs


def split_items(lines):
    """Split a subsection into numbered items, in printed order."""
    items, cur, preamble = [], None, []
    expected = 1
    for text, page in lines:
        s = text.strip()
        m = ITEM_RE.match(s)
        if m and int(m.group("num")) == expected:
            if cur:
                items.append(cur)
            cur = {"number": expected, "lines": [(m.group("rest"), page)],
                   "page": page}
            expected += 1
        elif cur is not None:
            cur["lines"].append((text, page))
        else:
            preamble.append(text)
    if cur:
        items.append(cur)
    return preamble, items


# --------------------------------------------------------------------------
# Value readers -- these only ever read what is printed
# --------------------------------------------------------------------------

LEVEL_LEAD_RE = re.compile(r"^(\d{1,2})\s*(?=,|;|\.|$)")
APPLY_RE = re.compile(r"\(Apply the (Greatest|Least|greatest|least)\)")


def read_base_level_item(text):
    """Read one base-offense-level alternative.

    Returns (level_or_None, condition_text, note). A level is returned only when
    the item literally begins with a number that stands alone before its
    condition. Everything else keeps level=None and the full verbatim text, so
    the wizard cannot print a number the manual did not print.
    """
    m = LEVEL_LEAD_RE.match(text)
    if not m:
        return None, text, "level is derived from other text, not a fixed number"
    level = int(m.group(1))
    cond = text[m.end():].lstrip(" ,;")
    if cond.lower().startswith("if "):
        cond = cond[3:].strip()
    return level, cond.strip(), None


ADJ_PATTERNS = [
    (re.compile(r"increase by (\d{1,2}) levels?", re.I), "increase"),
    (re.compile(r"decrease by (\d{1,2}) levels?", re.I), "decrease"),
    (re.compile(r"increase to level (\d{1,2})", re.I), "increase_to"),
    (re.compile(r"decrease to level (\d{1,2})", re.I), "decrease_to"),
    (re.compile(r"add (\d{1,2}) levels?", re.I), "increase"),
    (re.compile(r"subtract (\d{1,2}) levels?", re.I), "decrease"),
]
FLOOR_RE = re.compile(
    r"[Ii]f the resulting offense level is less than level (\d{1,2}),\s*"
    r"increase to level (\d{1,2})")
CEILING_RE = re.compile(
    r"[Ii]f the resulting offense level is greater than level (\d{1,2}),\s*"
    r"decrease to level (\d{1,2})")
TABLE_RE = re.compile(r"increase (?:the offense level )?(?:by the number of levels|"
                      r"according to the (?:special )?table)", re.I)


def read_adjustments(text):
    """Read every level adjustment printed in an SOC, in printed order.

    A floor ("if the resulting offense level is less than level 26, increase to
    level 26") is recorded as a floor, not as an increase, because the two
    behave differently in a calculation.
    """
    found = []
    consumed = []
    for m in FLOOR_RE.finditer(text):
        found.append({"pos": m.start(), "type": "floor",
                      "level": int(m.group(2)), "text": m.group(0)})
        consumed.append((m.start(), m.end()))
    for m in CEILING_RE.finditer(text):
        found.append({"pos": m.start(), "type": "ceiling",
                      "level": int(m.group(2)), "text": m.group(0)})
        consumed.append((m.start(), m.end()))

    def inside(pos):
        return any(a <= pos < b for a, b in consumed)

    for pat, kind in ADJ_PATTERNS:
        for m in pat.finditer(text):
            if inside(m.start()):
                continue
            entry = {"pos": m.start(), "type": kind, "text": m.group(0)}
            if kind in ("increase", "decrease"):
                entry["levels"] = int(m.group(1))
            else:
                entry["level"] = int(m.group(1))
            found.append(entry)
    found.sort(key=lambda e: e["pos"])
    for e in found:
        e.pop("pos")
    return found



# --------------------------------------------------------------------------
# Inline tables
#
# Several guidelines set a lookup table inside the operative text rather than
# stating a single adjustment: the loss table in §2B1.1(b)(1), the number-of-
# firearms table in §2K2.1(b)(1), the tax table that is the whole of §2T4.1.
# These rows are regular enough to read directly, and the verbatim text is kept
# either way, so nothing depends on the structured form being present.
# --------------------------------------------------------------------------

TABLE_CUT_RE = re.compile(r"\*\s*Notes to Table", re.I)
TABLE_ROW_RE = re.compile(
    r"^(?P<label>.*?)\s+(?:add\s+(?P<add>\d{1,2})"
    r"|(?P<noinc>no increase)"
    r"|(?P<lvl>\d{1,2}))\.?$", re.I)
TABLE_HINT_RE = re.compile(
    r"(INCREASE IN LEVEL|OFFENSE LEVEL|APPLY THE GREATEST)", re.I)


def parse_inline_table(text):
    """Read a lettered lookup table out of a run of guideline text.

    Returns None when the text does not hold one, so a guideline that merely
    mentions a table is never given invented rows.
    """
    if not TABLE_HINT_RE.search(text):
        return None
    cut = TABLE_CUT_RE.search(text)
    region = text[: cut.start()] if cut else text
    first = re.search(r"\(A\)\s", region)
    if not first:
        return None
    header = region[: first.start()].strip()
    parts = re.split(r"\(([A-Z])\)\s*", region[first.start():])
    rows, expected = [], "A"
    for i in range(1, len(parts) - 1, 2):
        letter, chunk = parts[i], parts[i + 1].strip()
        if letter != expected:
            break
        m = TABLE_ROW_RE.match(chunk)
        if not m:
            return None  # an unreadable row invalidates the whole table
        row = {"key": letter, "label": m.group("label").strip(), "printed": chunk}
        if m.group("add") is not None:
            row["increase_levels"] = int(m.group("add"))
        elif m.group("noinc"):
            row["increase_levels"] = 0
        else:
            row["offense_level"] = int(m.group("lvl"))
        rows.append(row)
        expected = chr(ord(expected) + 1)
    if len(rows) < 3:
        return None
    kind = ("offense_level" if "offense_level" in rows[0] else "increase")
    apply_rule = "greatest" if re.search(r"APPLY THE GREATEST", header, re.I) else None
    return {"header": header, "kind": kind, "apply_rule": apply_rule, "rows": rows}


HEADING_RE = re.compile(
    r"^(Base Offense Level|Specific Offense Characteristic(?:s)?|"
    r"Cross Reference(?:s)?|Special Instruction(?:s)?|Adjustment(?:s)?|"
    r"Departure Provision(?:s)?|Alternative Base Offense Level(?:s)?|"
    r"DRUG QUANTITY TABLE|CHEMICAL QUANTITY TABLE|LIST I CHEMICALS|"
    r"Offense Level|Special Cross Reference(?:s)?)\b", re.I)


def classify(heading):
    h = heading.lower()
    if h.startswith("base offense level"):
        return "base_offense_level"
    if h.startswith("alternative base offense level"):
        return "alternative_base_offense_level"
    if h.startswith("specific offense characteristic"):
        return "specific_offense_characteristics"
    if h.startswith("cross reference"):
        return "cross_references"
    if h.startswith("special instruction"):
        return "special_instructions"
    if h.startswith("adjustment"):
        return "adjustments"
    if h.startswith("departure"):
        return "departure_provisions"
    return "other"


# --------------------------------------------------------------------------

def parse_guideline(section, title, body, unparsed):
    rec = {
        "section": section,
        "title": title,
        "pdf_page": body[0][1] if body else None,
        "base_offense_level": None,
        "specific_offense_characteristics": [],
        "cross_references": [],
        "special_instructions": [],
        "other_subsections": [],
    }
    if re.match(r"^\[(Deleted|Not Used)\]", title, re.I):
        rec["status"] = "deleted"
        return rec
    rec["status"] = "active"

    subsections = split_subsections(body)
    if not subsections and body:
        body_text = flatten([l for l, _ in body])
        if body_text:
            rec["body_text"] = body_text
            tbl = parse_inline_table(body_text)
            if tbl:
                rec["table"] = tbl
            else:
                # The whole guideline is a prose instruction -- "Apply §2X5.1",
                # "the same level as that for the underlying offense". The text
                # is captured in full; there is simply no number to compute, so
                # the wizard must hand off rather than print one.
                rec["body_is_prose_instruction"] = True
                rec["requires_attorney_review"] = True
    for sub in subsections:
        head_text = flatten([l for l, _ in sub["lines"][:3]])
        hm = HEADING_RE.match(head_text)
        kind = classify(hm.group(1)) if hm else "other"
        preamble, items = split_items(sub["lines"])
        pre_text = flatten(preamble)

        if kind == "base_offense_level" or kind == "alternative_base_offense_level":
            apply_rule = "single"
            am = APPLY_RE.search(pre_text)
            if am:
                apply_rule = am.group(1).lower()
            alts = []
            if not items:
                # "(a) Base Offense Level: 43"
                m = re.search(r"Base Offense Level:\s*(\d{1,2})\s*$", pre_text)
                if m:
                    alts.append({"level": int(m.group(1)), "condition": None,
                                 "text": pre_text})
                else:
                    # e.g. "Base Offense Level: The offense level applicable to
                    # the underlying offense". There is no printed number; the
                    # level is derived from another guideline or table.
                    body_text = re.sub(r"^Base Offense Level:\s*", "", pre_text)
                    alts.append({
                        "level": None,
                        "condition": None,
                        "text": pre_text,
                        "level_note": body_text,
                        "derived_from_other_text": True,
                        "requires_attorney_review": True,
                    })
            for it in items:
                text = flatten([l for l, _ in it["lines"]])
                level, cond, note = read_base_level_item(text)
                alt = {"number": it["number"], "level": level,
                       "condition": cond or None, "text": text}
                if note:
                    alt["level_note"] = note
                    alt["requires_attorney_review"] = True
                alts.append(alt)
            if len(alts) <= 1:
                apply_rule = "single"
            elif not am:
                # Several alternatives but the manual prints no "apply the
                # greatest/least" instruction: the alternatives are mutually
                # exclusive conditions, not a maximum. Do not invent a rule.
                apply_rule = "conditional"
            payload = {"subsection": f"({sub['letter']})",
                       "apply_rule": apply_rule,
                       "heading": pre_text, "alternatives": alts}
            if kind == "base_offense_level" and rec["base_offense_level"] is None:
                rec["base_offense_level"] = payload
            else:
                rec["other_subsections"].append({"kind": kind, **payload})

        elif kind == "specific_offense_characteristics":
            for it in items:
                text = flatten([l for l, _ in it["lines"]])
                # The manual sets a bracketed editorial note about where a large
                # table is printed (§2D1.1). It is a layout note about the
                # guideline, not part of the characteristic it happens to follow.
                lm = re.search(r"\s*(\[Subsection [^\]]*\])\s*$", text)
                if lm:
                    rec.setdefault("layout_notes", []).append(lm.group(1))
                    text = text[: lm.start()].strip()
                soc = {
                    "subsection": f"({sub['letter']})({it['number']})",
                    "text": text,
                    "adjustments": read_adjustments(text),
                    "page": it["page"],
                }
                tbl = parse_inline_table(text)
                if tbl:
                    soc["table"] = tbl
                if not soc["adjustments"] and not tbl:
                    # The manual states no readable adjustment here -- typically
                    # the level comes from another guideline. Say so rather than
                    # letting the wizard assume there is none.
                    soc["adjustment_not_reducible"] = True
                rec["specific_offense_characteristics"].append(soc)
        elif kind in ("cross_references", "special_instructions"):
            key = kind
            for it in items:
                text = flatten([l for l, _ in it["lines"]])
                rec[key].append({
                    "subsection": f"({sub['letter']})({it['number']})",
                    "text": text, "page": it["page"]})
            if not items and pre_text:
                rec[key].append({"subsection": f"({sub['letter']})",
                                 "text": pre_text, "page": sub["page"]})
        else:
            entry = {"kind": kind, "subsection": f"({sub['letter']})",
                     "heading": pre_text,
                     "items": [{"subsection": f"({sub['letter']})({it['number']})",
                                "text": flatten([l for l, _ in it["lines"]])}
                               for it in items]}
            rec["other_subsections"].append(entry)
    return rec


def parse(pagedir):
    lines, stats = load_lines(pagedir, FIRST_PAGE, LAST_PAGE)
    parts, sections = find_structure(lines)
    unparsed = []

    # Attach each section to the PART / subpart it falls under.
    def context_for(idx):
        cur_part, cur_sub = None, None
        for p in parts:
            if p["idx"] <= idx:
                cur_part = p
            else:
                break
        if cur_part:
            for sp in cur_part.get("subparts", []):
                if sp["idx"] <= idx:
                    cur_sub = sp
        return cur_part, cur_sub

    guidelines, seen = [], {}
    for n, sec in enumerate(sections):
        title, after_title = collect_title(lines, sec["idx"])
        end = sections[n + 1]["idx"] if n + 1 < len(sections) else len(lines)
        # The operative text ends where the Commentary begins. Not every
        # guideline has one -- §2T4.1 (Tax Table) runs straight into its
        # Historical Note -- so the note, the star separator and the next Part
        # heading all close the body as well.
        body = []
        for i in range(after_title, end):
            s = lines[i][0].strip()
            if s in ("Commentary", "Historical", "Historical Note"):
                break
            if re.match(r"^\*(\s+\*)+\s*$", s):
                break
            if PART_RE.match(s) or SUBPART_RE.match(s):
                break
            body.append(lines[i])
        rec = parse_guideline(sec["section"], title, body, unparsed)
        part, sub = context_for(sec["idx"])
        if part:
            rec["chapter2_part"] = part["part"]
            rec["chapter2_part_title"] = part["title"]
        if sub:
            rec["chapter2_subpart"] = sub["title"]
        rec["pdf_page"] = sec["page"]
        if sec["section"] in seen:
            unparsed.append({"section": sec["section"], "where": "definition",
                             "text": title,
                             "reason": "duplicate section definition; kept the "
                                       "first occurrence"})
            continue
        seen[sec["section"]] = True
        guidelines.append(rec)
    return guidelines, parts, unparsed, stats


def main():
    pagedir, outpath = sys.argv[1], sys.argv[2]
    appa = sys.argv[3] if len(sys.argv) > 3 else None
    guidelines, parts, unparsed, stats = parse(pagedir)

    referenced = set()
    if appa:
        with open(appa) as fh:
            for e in json.load(fh)["entries"]:
                referenced.update(e["guidelines"])
                for r in e.get("guideline_refs", []):
                    if r.get("alternate_guideline"):
                        referenced.add(r["alternate_guideline"])
    for g in guidelines:
        g["referenced_by_statutory_index"] = g["section"] in referenced

    missing = sorted(referenced - {g["section"] for g in guidelines})
    for m in missing:
        unparsed.append({"section": m, "where": "chapter 2",
                         "reason": "referenced by Appendix A but no section "
                                   "definition found in Chapter Two"})

    soc_count = sum(len(g["specific_offense_characteristics"]) for g in guidelines)
    payload = {
        "source": "USSC Guidelines Manual, Chapter Two (Offense Conduct)",
        "manual_edition": EDITION,
        "pdf_pages": [FIRST_PAGE, LAST_PAGE],
        "counts": {
            "guidelines": len(guidelines),
            "active": sum(1 for g in guidelines if g["status"] == "active"),
            "deleted": sum(1 for g in guidelines if g["status"] == "deleted"),
            "referenced_by_statutory_index":
                sum(1 for g in guidelines if g["referenced_by_statutory_index"]),
            "specific_offense_characteristics": soc_count,
            "cross_references": sum(len(g["cross_references"]) for g in guidelines),
            "inline_tables": sum(
                (1 if g.get("table") else 0)
                + sum(1 for s in g["specific_offense_characteristics"] if s.get("table"))
                for g in guidelines),
            "socs_not_reducible_to_an_adjustment": sum(
                1 for g in guidelines for s in g["specific_offense_characteristics"]
                if s.get("adjustment_not_reducible")),
        },
        "extraction_notes": {
            "line_break_hyphens": {
                "explanation":
                    "The manual is justified text, so a hyphen at the end of a "
                    "line may be a typesetting artefact or part of a real "
                    "compound. Each one was decided using how the rest of the "
                    "620-page manual spells that word.",
                "rejoined_on_evidence": stats["joined_on_evidence"],
                "hyphen_kept_on_evidence": stats["hyphen_kept_on_evidence"],
                "rejoined_by_default_no_evidence_either_way":
                    stats["joined_by_default"],
                "hyphen_kept_words": sorted(set(stats.get("hyphen_kept_words", []))),
                "rejoined_by_default_words":
                    sorted(set(stats.get("joined_by_default_words", []))),
            },
        },
        "chapter2_parts": [
            {"part": p["part"], "title": p["title"], "pdf_page": p["page"],
             "subparts": [{"number": s["number"], "title": s["title"],
                           "pdf_page": s["page"]}
                          for s in p.get("subparts", [])]}
            for p in parts],
        "unparsed": unparsed,
        "guidelines": guidelines,
    }
    with open(outpath, "w") as fh:
        json.dump(payload, fh, indent=1)
    print(json.dumps(payload["counts"], indent=1))
    print("unparsed:", len(unparsed))
    for u in unparsed[:25]:
        print("  ", u.get("section"), "|", u.get("reason"), "|",
              str(u.get("text"))[:70])


if __name__ == "__main__":
    main()
