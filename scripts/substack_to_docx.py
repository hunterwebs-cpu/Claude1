#!/usr/bin/env python3
"""Convert a Substack dispatch markdown source into a delivery .docx.

Usage: python3 scripts/substack_to_docx.py content/substack/[slug].md

Produces content/substack/[slug].docx containing:
  1. A shaded blue "PUBLISHER CHECKLIST" cover block (title, subtitle,
     column, author, paste instructions) — not part of the article.
  2. The article body below a separator, with bold/italic/dividers/
     WARNING text rendered so it can be pasted straight into Substack.
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

COLUMN_TAG = "Surviving the Feds: Dispatches from the Inside"
DIVIDER_RE = re.compile(r"^\s*-{3,}\s*$")


def shade_paragraph(paragraph, hex_color):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    paragraph._p.get_or_add_pPr().append(shd)


def add_runs(paragraph, text):
    """Parse **bold** and *italic* markdown spans into docx runs."""
    pos = 0
    pattern = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")
    for m in pattern.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        token = m.group(0)
        if token.startswith("**"):
            paragraph.add_run(token[2:-2]).bold = True
        else:
            paragraph.add_run(token[1:-1]).italic = True
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


def parse_source(path: Path):
    raw = path.read_text().strip("\n")
    lines = [l for l in raw.split("\n")]

    # Title / subtitle are the first two non-empty lines.
    idx = 0
    non_empty = [(i, l) for i, l in enumerate(lines) if l.strip()]
    title = non_empty[0][1].strip()
    subtitle = non_empty[1][1].strip()

    # Body starts at the first divider line; everything before it
    # (byline, column tag) is discarded — it's regenerated in the header.
    body_start = None
    for i, l in enumerate(lines):
        if DIVIDER_RE.match(l):
            body_start = i + 1
            break
    if body_start is None:
        body_start = non_empty[1][0] + 1

    body_lines = lines[body_start:]
    body_text = "\n".join(body_lines).strip("\n")

    # Split into blocks on divider lines; each block splits into
    # paragraphs on blank lines.
    blocks, current = [], []
    for l in body_text.split("\n"):
        if DIVIDER_RE.match(l):
            if current:
                blocks.append("\n".join(current))
                current = []
            blocks.append("---")
        else:
            current.append(l)
    if current:
        blocks.append("\n".join(current))

    paragraphs = []
    for block in blocks:
        if block == "---":
            paragraphs.append("---")
            continue
        for para in re.split(r"\n\s*\n", block.strip("\n")):
            para = para.strip()
            if para:
                paragraphs.append(para)

    return title, subtitle, paragraphs


def build_docx(title, subtitle, paragraphs, out_path: Path):
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Georgia"
    style.font.size = Pt(11)

    # --- Cover block: publisher checklist ---
    header = doc.add_paragraph()
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = header.add_run("PUBLISHER CHECKLIST")
    run.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    shade_paragraph(header, "2E5A8C")

    def cover_line(label, value):
        p = doc.add_paragraph()
        shade_paragraph(p, "DCE8F5")
        r1 = p.add_run(f"{label}: ")
        r1.bold = True
        p.add_run(value)

    cover_line("Title", title)
    cover_line("Subtitle", subtitle)
    cover_line("Column", COLUMN_TAG)
    cover_line("Author", "Bilal Khan (guest column)")
    instr = doc.add_paragraph()
    shade_paragraph(instr, "DCE8F5")
    instr_run = instr.add_run(
        "Guest column for Doug Passon's Substack. Paste everything below "
        "the separator into the Substack editor as-is; do not include this "
        "checklist block."
    )
    instr_run.italic = True

    sep = doc.add_paragraph()
    sep_run = sep.add_run("— — — — — — — — — — — — — — — — — — — —")
    sep_run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
    sep.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # --- Article body ---
    t = doc.add_heading(level=1)
    t.add_run(title)

    sub = doc.add_paragraph()
    sub_run = sub.add_run(subtitle)
    sub_run.italic = True
    sub_run.font.size = Pt(13)

    byline = doc.add_paragraph()
    byline.add_run("By Bilal Khan").bold = True
    tag = doc.add_paragraph()
    tag.add_run(COLUMN_TAG).italic = True

    for para in paragraphs:
        if para == "---":
            hr = doc.add_paragraph()
            hr.alignment = WD_ALIGN_PARAGRAPH.CENTER
            hr.add_run("* * *")
            continue

        p = doc.add_paragraph()
        if para.startswith("WARNING:"):
            run = p.add_run(para)
            run.bold = True
        else:
            add_runs(p, para)

    doc.save(out_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/substack_to_docx.py content/substack/[slug].md")
        sys.exit(1)

    src = Path(sys.argv[1])
    title, subtitle, paragraphs = parse_source(src)
    out_path = src.with_suffix(".docx")
    build_docx(title, subtitle, paragraphs, out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
