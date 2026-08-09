"""Parse Appendix A (Statutory Index) of the USSC Guidelines Manual (Nov 1, 2024)
into structured JSON.

Reads the per-page text dump produced by tools/_dump_text.py.
Appendix A occupies PDF pages 573-597 (1-based); 573 carries the title and
introduction as well as the first index entries.

Every field is transcribed from the PDF. Nothing is inferred. Blocks that do not
match the expected shape are emitted to the `unparsed` list rather than guessed at.

Usage: python3 tools/parse_appendix_a.py <pagedump_dir> <out.json>
"""
import sys, os, json, re

FIRST_PAGE, LAST_PAGE = 573, 597
EDITION = "November 1, 2024"

# "2 U.S.C. § 192", "49 U.S.C. App. § 1687(g)", "26 U.S.C. § 7201"
STATUTE_RE = re.compile(r"^(?P<title>\d+)\s+U\.S\.C\.\s+(?P<app>App\.\s+)?§+\s*(?P<rest>.*)$")
# A guideline token: 2D1.1, 2B1.1, 3C1.1 ... optionally with a trailing letter
GUIDELINE_RE = re.compile(r"(2[A-Z]\d+\.\d+)")
GUIDELINE_SEARCH_RE = re.compile(r"\b2[A-Z]\d+\.\d+\b")
# Running-header / footer noise to strip from each page
NOISE_RE = re.compile(
    r"^(APPENDIX A|INDEX|INTRODUCTION|STATUTORY INDEX|Statute\s+Guideline.*|"
    r"\d+\s*║\s*Guidelines Manual.*|Guidelines Manual.*║\s*\d+)\s*$"
)


def page_blocks(text):
    """Split one page of the index into blank-line-delimited blocks."""
    lines = []
    for raw in text.split("\n"):
        line = raw.rstrip()
        if NOISE_RE.match(line.strip()):
            continue
        lines.append(line)
    blocks, cur = [], []
    for line in lines:
        if not line.strip():
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    return blocks


def split_top_level(blob):
    """Split a guideline column on commas that are not inside parentheses."""
    parts, depth, cur = [], 0, ""
    for ch in blob:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


def parse_guideline_column(blob):
    """Turn the printed guideline column into structured references.

    The column is a comma-separated list. Each item is a guideline section that
    may carry a verbatim parenthetical qualifier, e.g.
        "2A1.5, 2C1.1 (if conspiracy to defraud ...), 2K2.1 (if ...)"
    A parenthetical may itself name a *different* guideline that applies only in
    the stated circumstance, e.g.
        "2K2.4 (2K1.4 for offenses committed prior to November 18, 1988)"
    In that case the leading section is the primary reference and the one inside
    the parenthetical is recorded as an alternate, never as a co-equal peer.
    """
    refs, leftover = [], []
    for item in split_top_level(blob):
        m = GUIDELINE_RE.match(item)
        if not m:
            # A continuation fragment with no leading section (rare); attach it
            # to the previous reference verbatim rather than dropping it.
            if refs:
                refs[-1]["condition"] = (
                    (refs[-1].get("condition") or "") + " " + item).strip()
            else:
                leftover.append(item)
            continue
        ref = {"guideline": m.group(1)}
        tail = item[m.end():].strip()
        if tail:
            cond = tail.strip()
            if cond.startswith("(") and cond.endswith(")"):
                cond = cond[1:-1].strip()
            inner = GUIDELINE_RE.match(cond)
            if inner:
                ref["alternate_guideline"] = inner.group(1)
                ref["alternate_condition"] = cond[inner.end():].strip()
            else:
                ref["condition"] = cond
        refs.append(ref)
    return refs, leftover


def split_citation_and_guidelines(block_text):
    """Given the flattened text of an entry, return (citation, guideline_blob).

    The citation runs from the start up to the first guideline token; everything
    from that token onward is the guideline column. Parenthetical qualifiers that
    precede the first guideline token (e.g. "(felony provisions only)") belong to
    the statute side, exactly as printed.
    """
    m = GUIDELINE_SEARCH_RE.search(block_text)
    if not m:
        return block_text.strip(), ""
    return block_text[: m.start()].strip(), block_text[m.start():].strip()


def normalize(citation):
    """Derive title / section / subsection from the printed citation.

    Returns None for any part that cannot be read off the text directly.
    """
    m = STATUTE_RE.match(citation)
    if not m:
        return None
    rest = m.group("rest").strip()
    # Strip a trailing parenthetical qualifier before reading the section number
    qualifier = None
    qm = re.search(r"\((?:felony|misdemeanor|not|other|only|for)\b[^)]*\)\s*$", rest, re.I)
    if qm:
        qualifier = qm.group(0).strip()
        rest = rest[: qm.start()].strip()
    # section = leading numeric/alphanumeric run; subsection = the (a)(1) tail
    sm = re.match(r"^([0-9]+[A-Za-z\-]*(?:[0-9]+[A-Za-z\-]*)*)(.*)$", rest)
    if not sm:
        return None
    section = sm.group(1)
    subsection = sm.group(2).strip() or None
    return {
        "title": int(m.group("title")),
        "code": "U.S.C. App." if m.group("app") else "U.S.C.",
        "section": section,
        "subsection": subsection,
        "qualifier": qualifier,
    }


def parse(pagedir):
    entries, unparsed = [], []
    for pno in range(FIRST_PAGE, LAST_PAGE + 1):
        with open(os.path.join(pagedir, f"p{pno:04d}.txt")) as fh:
            text = fh.read()
        # Page 573 also holds the introduction; index entries begin at the first
        # line that looks like a statute citation.
        for block in page_blocks(text):
            flat = " ".join(x.strip() for x in block).strip()
            flat = re.sub(r"\s{2,}", " ", flat)
            if not STATUTE_RE.match(flat):
                continue  # introduction / historical-note prose
            citation, gblob = split_citation_and_guidelines(flat)
            refs, leftover = parse_guideline_column(gblob)
            guidelines = [r["guideline"] for r in refs]
            norm = normalize(citation)
            rec = {
                "citation": citation,
                "guidelines": guidelines,
                "guideline_refs": refs,
                "pdf_page": pno,
            }
            if leftover:
                unparsed.append({"pdf_page": pno, "text": flat,
                                 "reason": "guideline column fragment: "
                                           + " | ".join(leftover)})
            if norm:
                rec.update({
                    "title": norm["title"],
                    "code": norm["code"],
                    "section": norm["section"],
                    "subsection": norm["subsection"],
                })
                if norm["qualifier"]:
                    rec["statute_qualifier"] = norm["qualifier"]
            if not guidelines or not norm:
                unparsed.append({"pdf_page": pno, "text": flat,
                                 "reason": "no guideline token" if not guidelines
                                           else "citation did not normalize"})
                continue
            entries.append(rec)
    return entries, unparsed


def main():
    pagedir, outpath = sys.argv[1], sys.argv[2]
    entries, unparsed = parse(pagedir)
    payload = {
        "source": "USSC Guidelines Manual, Appendix A (Statutory Index)",
        "manual_edition": EDITION,
        "pdf_pages": [FIRST_PAGE, LAST_PAGE],
        "entry_count": len(entries),
        "unparsed": unparsed,
        "entries": entries,
    }
    with open(outpath, "w") as fh:
        json.dump(payload, fh, indent=1)
    multi = sum(1 for e in entries if len(e["guidelines"]) > 1)
    print(f"entries={len(entries)} multi_guideline={multi} unparsed={len(unparsed)}")
    for u in unparsed[:20]:
        print("  UNPARSED", u["pdf_page"], u["text"][:100])


if __name__ == "__main__":
    main()
