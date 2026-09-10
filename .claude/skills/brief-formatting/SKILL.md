---
name: brief-formatting
description: Final-pass formatting for court filings (briefs, motions, certifications) after the substantive writing is done — builds a properly aligned caption, applies a clean Roman-numeral/letter/number heading scheme, converts to court-ready .docx and .pdf, and verifies the result by actually rendering and reading it before it goes anywhere near the client. Demonstrated on the Bernecky SORA filings (Monroe County Court). Use whenever a legal document's *content* is finished and it needs to look like a filed paper — not while the argument is still being drafted or revised.
---

# Brief Formatting — Final Pass

This is the **last step**, after a Writer/researcher has finished the substantive
argument. It does not touch legal content. Its job is: take a finished Markdown
draft and turn it into a properly captioned, properly numbered, properly spaced
`.docx` (and `.pdf`) that looks like something a court clerk would accept without
raising an eyebrow — and to actually *look at it* before calling it done.

Two real, client-visible failures happened building this skill. Both are called
out below at the exact step where they happened, because the fix is not
"be more careful" — it's a specific verification step that would have caught
each one immediately.

---

## 0. Before touching formatting: confirm the caption

**Caption format is not a matter of taste — it's jurisdiction- and
practice-specific, and getting it wrong is a real error, not a style choice.**
Before formatting anything:

- If the client has already built a caption by hand (common — captions are
  fiddly and clients often want to control this piece directly), **use their
  content verbatim.** Do not "correct" it back to a format you researched
  earlier unless the client asks. Your job is alignment and cleanup, not
  redesign. (This reversed a whole researched-and-applied caption format
  earlier in the Bernecky matter — the client's own hand-built version was
  the one that mattered.)
- If you're building a caption from scratch, verify the format against **real
  sample captions from filed papers or a practitioner guide** in that specific
  court and case type — never from general memory of "how captions look."
  A caption for a civil SORA proceeding, a criminal matter, and a bankruptcy
  filing are not interchangeable, and neither are captions across states.
- Confirm party names, case numbers, and the judge's full name against the
  matter's own record. A dropped surname or wrong index number is a
  substantive error wearing a formatting costume.

---

## 1. Heading numbering scheme

Default scheme, absent a court rule or client preference otherwise:

- **Top-level sections** (Preliminary Statement, Statement of Facts, Argument,
  Conclusion) — **Roman numerals**: `I.`, `II.`, `III.`, `IV.`
- **Subsections** under a top-level section — **letters**: `A.`, `B.`, `C.`...
  Reset the letter counter at the start of each new top-level section.
- **Sub-subsections** — **numbers**: `1.`, `2.`, `3.`...

**Do not invent a parallel numbering convention (e.g., "POINT I" / "POINT II")
unless the client specifically wants it.** It's tempting to treat argument
headings as special, but a second numbering system running alongside the
Roman/letter/number scheme is exactly what produces "orphaned" headings —
a heading with no number in a document where everything else is numbered.
If the client hasn't asked for `POINT` headings, argument section titles get
lettered like every other subsection, full stop.

**Never leave a heading unlabeled.** If something reads as a heading (bold,
its own line, structurally a new subsection) it needs a number at its own
level. An unlabeled heading directly under a numbered one reads as part of
the thing above it, not as its own section — this is what "orphaned heading"
means in practice, and it is a real comprehension problem for the reader,
not a cosmetic one.

A parenthetical statutory cross-reference directly under the title (e.g.
`(Pursuant to CPLR 2106)`) is a subtitle, not a heading — center it, italicize
it, and do not number it.

### Pitfall #3 (real, client-facing): a numbered heading needs a tab and a hanging indent, not just the right characters

Getting the label right ("I.", "A.", "1.") is not the same as getting the
heading *formatted* right. A real Word multilevel list — which is what it
looks like when someone builds headings by hand in Word — puts a **tab**
between the number and the heading text (not a space), and gives each level
a **hanging indent** that steps letters in from Roman numerals and numbers
in further still. Writing `"I. " + heading` as one plain text run gets the
character right and the formatting wrong: no tab, and every level sits flush
at the same margin instead of stepping in. This shipped on every one of a
matter's collateral filings before being caught — the fix (below) does not
require replicating Word's native numbered-list feature (`numPr`), which
needs a `numbering.xml` definition; a paragraph-level tab stop plus a
matching hanging indent produces an identical visual result and is far
simpler to generate from a script.

```js
// docx (npm): one heading paragraph, Roman-numeral level.
// `left` is where the heading text (and the tab stop) sits; `hanging` is
// how far left of that the number itself sits. Bump `left`/`hanging` up
// per level (e.g. left 1080 -> 1440 -> 2340 DXA) so each level steps in
// from the one above it -- match the exact values to the client's own
// document if one already exists (inspect its word/numbering.xml).
new Paragraph({
  tabStops: [{ type: TabStopType.LEFT, position: 1080 }],
  indent: { left: 1080, hanging: 720 },
  children: [
    new TextRun({ text: 'I.\t', bold: true }),   // literal tab char, not a space
    ...inlineRuns(headingText, { bold: true }),
  ],
});
```

A literal `\t` inside a `TextRun`'s `text` is a real fix here, not a hack —
`docx` (npm) serializes it to an actual `<w:tab/>` element, which Word and
LibreOffice both honor against the paragraph's `tabStops`. Verify by
rendering (per §5) and confirming the gap after the number is a tab jump to
a fixed column, not proportional word-spacing.

---

## 2. Spacing rules

- **Body paragraphs**: double-spaced (`line: 480` in docx twips), justified,
  0.5" first-line indent. This is the default NY court-rule spacing
  (22 NYCRR 202.5(a)) and a safe default elsewhere absent a specific rule.
- **Headings, subheadings, and the title**: single-spaced (`line: 240`),
  never double — a double-spaced heading looks like a formatting bug, not
  emphasis.
- **Block quotes**: single-spaced, indented both sides, same rule as
  headings — quoted material is conventionally exempt from double-spacing
  even where the underlying rule requires it for body text.
- **The signature block, "Dated:" line, and any address/venue lines**:
  single-spaced, left-aligned, never justified or indented like body text.

---

## 3. Building the caption as a table, not with spaces

If the caption needs two columns (party info on the left, index number/hearing
date/title on the right — a very common NY practice pattern), **build it as a
real borderless table**, not with typed space characters. Space-padding in a
proportional font produces inconsistent column starts the moment any line's
text length differs even slightly — it will look "close enough" until you
measure it, and a client who built one by hand will notice immediately
("my tabs weren't working").

```js
// See scripts/md_to_filing_docx.js for the full working implementation.
// Core technique: a docx.js Table with BorderStyle.NONE on every side,
// fixed column widths (DXA) summing to the usable page width, and
// tcMar/leftIndent on individual cells for any intentional indentation
// (e.g., "-against-" or "Respondent." indented under the party name) --
// never simulate indentation with literal spaces inside a cell.
```

### Pitfall #1 (real, client-facing): don't stack a border under a line that's already a line

If a horizontal rule in the caption is rendered as literal text
(`-----------------------------------------------------X`), **do not also
put a paragraph border on that paragraph, or on the paragraph before it.**
Word/LibreOffice renders the border as an actual solid horizontal rule *in
addition to* the dashes — the result is two visually stacked lines where the
client expects one. This happened on every generated filing in one pass of
this matter and drew an all-caps, multiply-profane correction. The fix is
categorical, not case-by-case: **a caption rule is either a literal dashed
text line, or a real paragraph border — never both, anywhere in the same
document.** Grep the generated XML for `<w:pBdr>` before considering a
caption done, and account for every single match.

### Pitfall #2 (real, client-facing): title auto-wrap needs a conservative width

When a document title is split across lines to fit a table cell, don't trust
a character-count estimate above ~28 characters for bold 12pt Times New Roman
in a ~3.25" column — bold text and wide letters (M, W) blow through a naive
estimate and the renderer re-wraps the line a second time, stranding one or
two words on their own line with a visible gap above them. Wrap
conservatively (`wrapTitle(text, 28)` in the reference script), and — this is
the actual fix, not the character count — **render the result and read it**
before it ships. A number that "should" fit is not a substitute for looking.

---

## 4. Converting to .docx and .pdf

Prefer **one source of truth**: build the `.docx` (via `docx` (npm) for a
from-scratch document, or direct `word/document.xml` XML edits per the `docx`
skill when merging into a document the client hand-edited), then get the PDF
by converting *that* file — don't maintain a parallel PDF-generation pipeline
(e.g., a separate reportlab script) that can drift out of sync with the docx.

```bash
soffice --headless --convert-to pdf the-file.docx --outdir .
```

If `soffice`/LibreOffice Writer or `pdftoppm`/poppler-utils aren't installed,
`apt-get install -y libreoffice-writer poppler-utils` — both are needed for
this workflow (Writer specifically, not just `libreoffice-core`) and are
usually installable even in otherwise network-restricted environments.
`apt-get update` first if a package 404s on the first try.

---

## 5. Verification — do all of these, every time, before sending anything

1. **OOXML schema validation**:
   `python3 <docx-skill>/scripts/office/validate.py the-file.docx` — catches
   malformed XML (e.g., element ordering inside `pPr`/`tblPr`, which follows
   a strict CT_PPrBase/CT_TblPrBase sequence — `pBdr` before `spacing`,
   `tblLayout` before `tblCellMar`, etc.).
2. **Word-count integrity check**: tokenize both the source Markdown (past
   any caption you're replacing) and the extracted docx text
   (`pandoc -t plain`), compare counts. Ratio should land close to 1.00 —
   materially over-1 means you injected text you didn't mean to keep in the
   comparison (e.g., new caption content); materially under-1 means you
   dropped something. Either way, explain the gap before moving on.
3. **Actually render it and look.** `soffice --headless --convert-to pdf`,
   then `pdftoppm -jpeg -r 130` the first page *and* the last page *and* any
   page with a structurally different layout (a lettered ARGUMENT section, a
   NOTES/footnote block). Read the images. Both real bugs in this skill's
   history (the double border-lines, the orphaned title wrap) were things a
   validator and a word-count check both passed cleanly — they are only
   visible on an actual rendered page.
4. **Grep every filing for stale cross-references** whenever a heading label
   or numbering scheme changes. A memo that used to say "Point II.A" and now
   says "B.1" needs every *other* document in the matter that cites
   "Point II.A" updated too — including internal self-references within the
   same document. `grep -rn "Point I\b\|Point II\b"` (or whatever the old
   label was) across every filing before considering the pass complete.

---

## 6. Reference implementation

`scripts/md_to_filing_docx.js` — a working, tested Node.js/`docx` converter
implementing everything above: table-based caption with a configurable
title/case-info block, Roman/letter/number heading numbering with automatic
counters and real tab-stop/hanging-indent formatting per level (`HEADING_LEVELS`),
single-spaced headings and double-spaced justified indented body
text, footnote collection into a trailing NOTES section, and page numbering.
Run directly (`node md_to_filing_docx.js config.json`) or import
`{ convert, buildCaption, wrapTitle }` to reuse pieces in a client-specific
script. Treat it as a starting point, not a black box — the caption content
in `buildCaption()` is written for one client's confirmed format and needs
its party-info/case-info text adapted per matter.
