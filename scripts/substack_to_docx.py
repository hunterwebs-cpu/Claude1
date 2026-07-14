#!/usr/bin/env python3
"""
substack_to_docx.py
Convert a Substack dispatch markdown file to a formatted .docx for the host publisher.
Produces a cover checklist (title, subtitle, tag, guest author instructions) followed
by the formatted article body, ready to paste into Substack's editor.

Usage:
    python3 scripts/substack_to_docx.py <input.md> [output.docx]
"""

import re
import sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def hex_rgb(h):
    h = h.lstrip('#')
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def parse_frontmatter(content):
    if not content.startswith('---'):
        return {}, content
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 5:]
    fm = {}
    for line in fm_text.strip().split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"')
    return fm, body


def add_hr(doc):
    """Thin grey horizontal rule."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '4')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'CCCCCC')
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p


def shade_paragraph(p, fill_hex):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex.lstrip('#'))
    pPr.append(shd)


def add_shaded_line(doc, text, bold=False, size=10,
                    text_hex='1a1a1a', fill_hex='EEF4FF',
                    space_before=1, space_after=1):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    shade_paragraph(p, fill_hex)
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = hex_rgb(text_hex)
    return p


def add_inline(paragraph, text, font_size=11):
    """
    Parse **bold**, *italic*, and plain text and add runs to paragraph.
    Handles mixed inline formatting including book titles in italic context.
    """
    tokens = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**'):
            run = paragraph.add_run(token[2:-2])
            run.bold = True
            run.italic = False
        elif token.startswith('*') and token.endswith('*'):
            run = paragraph.add_run(token[1:-1])
            run.bold = False
            run.italic = True
        else:
            run = paragraph.add_run(token)
            run.bold = False
            run.italic = False
        run.font.name = 'Calibri'
        run.font.size = Pt(font_size)


def build_clean_header(doc, fm):
    title = fm.get('title', '')
    subtitle = fm.get('subtitle', '')
    column = fm.get('column', '')

    if title:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(title)
        run.font.name = 'Calibri'
        run.font.size = Pt(22)
        run.font.bold = True

    if subtitle:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(subtitle)
        run.font.name = 'Calibri'
        run.font.size = Pt(13)
        run.font.italic = True
        run.font.color.rgb = hex_rgb('444444')

    if column:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run(column)
        run.font.name = 'Calibri'
        run.font.size = Pt(10)
        run.font.color.rgb = hex_rgb('888888')


def build_docx(md_path, output_path):
    content = Path(md_path).read_text()
    fm, body = parse_frontmatter(content)

    doc = Document()

    # Default Normal style
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(11)

    # Page margins
    for sec in doc.sections:
        sec.top_margin = Inches(1)
        sec.bottom_margin = Inches(1)
        sec.left_margin = Inches(1.25)
        sec.right_margin = Inches(1.25)

    build_clean_header(doc, fm)

    # Process line by line — each non-blank line is its own paragraph
    for line in body.split('\n'):
        stripped = line.strip()

        # Blank line — skip (paragraph spacing handles visual separation)
        if stripped == '':
            continue

        # H1 title
        if stripped.startswith('# '):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run(stripped[2:])
            run.font.name = 'Calibri'
            run.font.size = Pt(18)
            run.font.bold = True
            continue

        # Horizontal rule
        if stripped == '---':
            add_hr(doc)
            continue

        # WARNING block
        if stripped.startswith('WARNING:'):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run(stripped)
            run.font.name = 'Calibri'
            run.font.size = Pt(11)
            run.font.bold = True
            run.font.color.rgb = RGBColor(180, 0, 0)
            continue

        # Bold-only section heading: **text** (entire line)
        if re.match(r'^\*\*[^*]+\*\*$', stripped):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run(stripped[2:-2])
            run.font.name = 'Calibri'
            run.font.size = Pt(13)
            run.font.bold = True
            continue

        # Bullet list item
        if stripped.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.left_indent = Inches(0.25)
            add_inline(p, stripped[2:])
            continue

        # Regular paragraph (handles inline **bold** and *italic*)
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.space_before = Pt(0)
        add_inline(p, stripped)

    doc.save(str(output_path))
    print(f'Saved: {output_path}')


if __name__ == '__main__':
    md = sys.argv[1] if len(sys.argv) > 1 else 'content/substack/fort-dix-infrastructure-jackhammer.md'
    out = sys.argv[2] if len(sys.argv) > 2 else md.replace('.md', '.docx')
    build_docx(md, out)
