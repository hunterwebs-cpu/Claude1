#!/usr/bin/env python3
"""Convert a Surviving the Feds dispatch (markdown) into a Word document for Doug.

The output has two parts:

  1. A shaded cover block -- the PUBLISHER CHECKLIST. This is not the article.
     It carries the title, subtitle, column tag, and the guest-author note so
     Doug has everything he needs without reading the whole piece first.

  2. The article body below a separator, formatted so that pasting it straight
     into Substack's editor preserves bold, italic, horizontal rules, and the
     WARNING callout.

Usage:
    python3 scripts/substack_to_docx.py content/substack/<slug>.md
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

COVER_SHADE = "DCE6F1"      # pale blue
RULE_SHADE = "000000"
WARNING_RED = RGBColor(0xB0, 0x00, 0x00)

INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


def shade(paragraph, hex_fill):
    """Apply a solid background fill to a paragraph."""
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    paragraph._p.get_or_add_pPr().append(shd)


def horizontal_rule(doc):
    """Insert a thin horizontal rule as a bottom border on an empty paragraph."""
    p = doc.add_paragraph()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), RULE_SHADE)
    pbdr.append(bottom)
    p._p.get_or_add_pPr().append(pbdr)


def add_rich_text(paragraph, text):
    """Render **bold** and *italic* markdown spans as real Word runs."""
    for chunk in INLINE.split(text):
        if not chunk:
            continue
        if chunk.startswith("**") and chunk.endswith("**"):
            paragraph.add_run(chunk[2:-2]).bold = True
        elif chunk.startswith("*") and chunk.endswith("*"):
            paragraph.add_run(chunk[1:-1]).italic = True
        else:
            paragraph.add_run(chunk)


def parse(md_path):
    """Split the source file into its title, subtitle, and body lines."""
    lines = Path(md_path).read_text().splitlines()
    title = subtitle = None
    body_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if title is None and stripped.startswith("# "):
            title = stripped[2:].strip()
            continue
        if title and subtitle is None and stripped.startswith("*") and stripped.endswith("*"):
            subtitle = stripped.strip("*").strip()
            continue
        if stripped == "---":
            body_start = i + 1
            break

    if not title:
        sys.exit(f"error: no '# Title' heading found in {md_path}")

    return title, subtitle or "", lines[body_start:]


def build_cover(doc, title, subtitle):
    header = doc.add_paragraph()
    shade(header, COVER_SHADE)
    run = header.add_run("PUBLISHER CHECKLIST")
    run.bold = True
    run.font.size = Pt(13)

    fields = [
        ("Title", title),
        ("Subtitle (email preview text)", subtitle),
        ("Column", "Surviving the Feds: Dispatches from the Inside"),
        ("Author", "Bilal Khan (guest author — set byline to guest, not Doug)"),
        ("Paste target", "Substack editor. Formatting below is paste-ready."),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        shade(p, COVER_SHADE)
        p.add_run(f"{label}: ").bold = True
        p.add_run(value)

    spacer = doc.add_paragraph()
    shade(spacer, COVER_SHADE)

    horizontal_rule(doc)
    doc.add_paragraph()


def build_body(doc, body_lines):
    for raw in body_lines:
        line = raw.strip()

        if not line:
            continue

        if line == "---":
            horizontal_rule(doc)
            continue

        if line.startswith("WARNING:"):
            p = doc.add_paragraph()
            run = p.add_run(line)
            run.bold = True
            run.font.color.rgb = WARNING_RED
            continue

        # A lone bolded line is a section label, not prose.
        if line.startswith("**") and line.endswith("**") and line.count("**") == 2:
            p = doc.add_paragraph()
            p.add_run(line[2:-2]).bold = True
            continue

        if line.startswith("~"):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_rich_text(p, line)
            continue

        add_rich_text(doc.add_paragraph(), line)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: substack_to_docx.py <path-to-dispatch.md>")

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        sys.exit(f"error: {md_path} not found")

    title, subtitle, body_lines = parse(md_path)

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    build_cover(doc, title, subtitle)
    build_body(doc, body_lines)

    out_path = md_path.with_suffix(".docx")
    doc.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
