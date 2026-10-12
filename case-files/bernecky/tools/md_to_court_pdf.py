#!/usr/bin/env python3
"""
Convert a SORA filing Markdown file into a properly formatted PDF for
Monroe County Court, per 22 NYCRR Part 202 (Uniform Civil Rules for the
Supreme Court and the County Court):
  - 1-inch margins on all sides (22 NYCRR 202.5(a))
  - Double-spaced body text, except quotations, block quotes, headings, and
    name/address lines (22 NYCRR 202.5(a); headings/titles are conventionally
    single-spaced even though the rule's double-spacing requirement runs to
    body text)
  - Consecutive page numbering
Font: Times-Roman family (12pt body), the de facto standard for NY court
filings and a safe default absent a court-specific typeface rule.

Caption format: adversarial "PEOPLE OF THE STATE OF NEW YORK -against-
[Name], Respondent." caption with Index No./NYSID No. fields, matching the
sample captions in the New York State Defenders Association's "A Defense
Attorney's Guide to SORA Modification Proceedings."
"""
import re
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib import colors

PAGE_W, PAGE_H = letter
MARGIN = 1 * inch
USABLE_W = PAGE_W - 2 * MARGIN

ROMAN_NUMERALS = [
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
]


def int_to_roman(n):
    result = []
    for value, symbol in ROMAN_NUMERALS:
        while n >= value:
            result.append(symbol)
            n -= value
    return ''.join(result)


# ---------- styles ----------

def build_styles():
    styles = {}
    styles['caption_court'] = ParagraphStyle(
        'caption_court', fontName='Times-Roman', fontSize=12, leading=14,
        alignment=TA_CENTER, spaceAfter=0,
    )
    styles['caption_body'] = ParagraphStyle(
        'caption_body', fontName='Times-Roman', fontSize=12, leading=14,
        alignment=TA_LEFT, spaceAfter=0,
    )
    styles['caption_indent'] = ParagraphStyle(
        'caption_indent', fontName='Times-Roman', fontSize=12, leading=14,
        alignment=TA_LEFT, spaceAfter=0, leftIndent=0.45 * inch,
    )
    styles['caption_party'] = ParagraphStyle(
        'caption_party', fontName='Times-Bold', fontSize=12, leading=14,
        alignment=TA_LEFT, spaceAfter=0,
    )
    # Single-spaced per client instruction: headings, subheadings, and
    # titles are never double-spaced, even though body text is.
    styles['doc_title'] = ParagraphStyle(
        'doc_title', fontName='Times-Bold', fontSize=13, leading=16,
        alignment=TA_CENTER, spaceBefore=18, spaceAfter=4,
    )
    styles['subtitle'] = ParagraphStyle(
        'subtitle', fontName='Times-Italic', fontSize=11, leading=13,
        alignment=TA_CENTER, spaceBefore=0, spaceAfter=14,
    )
    styles['h1'] = ParagraphStyle(
        'h1', fontName='Times-Bold', fontSize=12, leading=14,
        alignment=TA_CENTER, spaceBefore=18, spaceAfter=6,
    )
    styles['h2'] = ParagraphStyle(
        'h2', fontName='Times-Bold', fontSize=12, leading=14,
        alignment=TA_LEFT, spaceBefore=16, spaceAfter=8,
    )
    styles['h3'] = ParagraphStyle(
        'h3', fontName='Times-BoldItalic', fontSize=12, leading=14,
        alignment=TA_LEFT, spaceBefore=10, spaceAfter=6,
    )
    styles['body'] = ParagraphStyle(
        'body', fontName='Times-Roman', fontSize=12, leading=24,
        alignment=TA_JUSTIFY, spaceAfter=0, firstLineIndent=0.5 * inch,
    )
    styles['numbered'] = ParagraphStyle(
        'numbered', fontName='Times-Roman', fontSize=12, leading=24,
        alignment=TA_JUSTIFY, spaceAfter=6, leftIndent=0,
    )
    # Block quotes: single-spaced, indented both sides, per client
    # instruction ("same with block quotes"). No content currently uses
    # this, but it is built correctly in advance.
    styles['blockquote'] = ParagraphStyle(
        'blockquote', fontName='Times-Roman', fontSize=12, leading=14,
        alignment=TA_JUSTIFY, leftIndent=0.5 * inch, rightIndent=0.5 * inch,
        spaceBefore=8, spaceAfter=8,
    )
    styles['sig_line'] = ParagraphStyle(
        'sig_line', fontName='Times-Roman', fontSize=12, leading=14,
        alignment=TA_LEFT, spaceAfter=0,
    )
    styles['footnote'] = ParagraphStyle(
        'footnote', fontName='Times-Roman', fontSize=10, leading=13,
        alignment=TA_JUSTIFY, spaceAfter=0,
    )
    styles['notes_head'] = ParagraphStyle(
        'notes_head', fontName='Times-Bold', fontSize=11, leading=14,
        alignment=TA_CENTER, spaceBefore=18, spaceAfter=8,
    )
    return styles


# ---------- inline markdown -> reportlab markup ----------

def inline_md(text):
    # Convert literal "&nbsp;" markup (used in source markdown for manual
    # indentation, e.g. in the signature block) to real non-breaking spaces
    # *before* escaping ampersands, or it would render as literal "&nbsp;"
    # text instead of whitespace.
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # bold+italic ***x***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # bold **x**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # italic *x*
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
    # footnote reference [^1]
    text = re.sub(r'\[\^(\d+)\]', r'<super rise="4" size="8">\1</super>', text)
    return text


def strip_md_line(line):
    return inline_md(line.strip())


# ---------- caption parsing ----------

def parse_caption(caption_lines):
    """Split the raw caption block into: court header lines, the ordered
    party-block lines (People / -against- / Name / Respondent.), the Index
    No. and NYSID No. values, and the Hearing Date / Before lines."""
    court_lines = []
    party_lines = []
    idx_no = ''
    nysid_no = ''
    hearing_lines = []
    for cl in caption_lines:
        s = cl.strip()
        if s == '' or set(s) <= {'-'}:
            continue
        if s.startswith('Hearing Date') or s.startswith('Before:'):
            hearing_lines.append(s)
        elif s.startswith('Index No.'):
            idx_no = s
        elif s.startswith('NYSID No.'):
            nysid_no = s
        elif s == 'STATE OF NEW YORK' or s.startswith('COUNTY COURT'):
            court_lines.append(s)
        else:
            party_lines.append(s)
    return court_lines, party_lines, idx_no, nysid_no, hearing_lines


def build_caption_flow(caption_lines, styles):
    court_lines, party_lines, idx_no, nysid_no, hearing_lines = parse_caption(caption_lines)
    flow = []

    for cl in court_lines:
        flow.append(Paragraph(strip_md_line(cl), styles['caption_court']))

    flow.append(Spacer(1, 8))
    flow.append(HRFlowable(width='100%', thickness=0.75, color=colors.black))
    flow.append(Spacer(1, 8))

    if len(party_lines) == 4:
        # Expected order: "People of the State of New York,", "-against-",
        # "**Name,**" (bold), "Respondent." / "Respondent[^n]."
        plaintiff, against, party_name, designation = party_lines
        rows = [
            [Paragraph(strip_md_line(plaintiff), styles['caption_body']),
             Paragraph('', styles['caption_body'])],
            [Paragraph(strip_md_line(against), styles['caption_indent']),
             Paragraph(strip_md_line(idx_no), styles['caption_body'])],
            [Paragraph(strip_md_line(party_name), styles['caption_party']),
             Paragraph('', styles['caption_body'])],
            [Paragraph(strip_md_line(designation), styles['caption_indent']),
             Paragraph(strip_md_line(nysid_no), styles['caption_body'])],
        ]
        tbl = Table(rows, colWidths=[USABLE_W * 0.62, USABLE_W * 0.38])
        tbl.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        flow.append(tbl)
    else:
        # Fallback: render whatever we parsed, plain, one line at a time,
        # plus the Index/NYSID lines if present.
        for pl in party_lines:
            style = styles['caption_party'] if pl.startswith('**') else styles['caption_body']
            flow.append(Paragraph(strip_md_line(pl), style))
        if idx_no:
            flow.append(Paragraph(strip_md_line(idx_no), styles['caption_body']))
        if nysid_no:
            flow.append(Paragraph(strip_md_line(nysid_no), styles['caption_body']))

    flow.append(Spacer(1, 8))
    flow.append(HRFlowable(width='100%', thickness=0.75, color=colors.black))
    flow.append(Spacer(1, 8))

    for hl in hearing_lines:
        flow.append(Paragraph(strip_md_line(hl), styles['caption_body']))

    return flow


# ---------- main conversion ----------

def convert(md_path, pdf_path, doc_title_override=None):
    with open(md_path, encoding='utf-8') as f:
        raw = f.read()

    lines = raw.split('\n')
    styles = build_styles()
    story = []

    footnotes = {}  # num -> text
    i = 0
    n = len(lines)

    # --- Parse caption block (first lines up to the first '# ' title) ---
    caption_lines = []
    while i < n and not lines[i].startswith('# '):
        caption_lines.append(lines[i])
        i += 1

    story.extend(build_caption_flow(caption_lines, styles))
    story.append(Spacer(1, 14))

    # --- Parse the rest ---
    para_buf = []
    quote_buf = []
    top_level_counter = 0

    def flush_para(style_key='body'):
        if para_buf:
            text = ' '.join(p.strip() for p in para_buf if p.strip())
            if text:
                story.append(Paragraph(inline_md(text), styles[style_key]))
                story.append(Spacer(1, 6))
            para_buf.clear()

    def flush_quote():
        if quote_buf:
            text = ' '.join(p.strip() for p in quote_buf if p.strip())
            if text:
                story.append(Paragraph(inline_md(text), styles['blockquote']))
            quote_buf.clear()

    in_notes = False

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Block quote: consecutive "> " lines
        if stripped.startswith('>'):
            flush_para()
            quote_buf.append(stripped.lstrip('>').strip())
            i += 1
            continue
        elif quote_buf:
            flush_quote()

        # Horizontal rule
        if set(stripped) <= {'-'} and len(stripped) >= 3:
            flush_para()
            i += 1
            continue

        # Blank line -> paragraph break
        if stripped == '':
            flush_para('numbered' if in_notes else 'body')
            i += 1
            continue

        # Footnote definition: [^1]: text
        m = re.match(r'^\[\^(\d+)\]:\s*(.*)$', stripped)
        if m:
            flush_para()
            footnotes[m.group(1)] = m.group(2)
            i += 1
            continue

        # Headings
        if stripped.startswith('#### '):
            flush_para()
            story.append(Paragraph(inline_md(stripped[5:].strip()), styles['h3']))
            i += 1
            continue
        if stripped.startswith('### '):
            flush_para()
            story.append(Paragraph(inline_md(stripped[4:].strip()), styles['h3']))
            i += 1
            continue
        if stripped.startswith('## '):
            flush_para()
            heading_text = stripped[3:].strip()
            if heading_text.upper() == 'NOTES':
                in_notes = True
                story.append(Spacer(1, 4))
                story.append(HRFlowable(width='100%', thickness=0.5, color=colors.black))
                story.append(Paragraph('NOTES', styles['notes_head']))
                i += 1
                continue
            # A parenthetical statutory subtitle directly under the title
            # (e.g. "(Pursuant to CPLR 2106)") is not a numbered section.
            if heading_text.startswith('(') and heading_text.endswith(')'):
                story.append(Paragraph(inline_md(heading_text), styles['subtitle']))
                i += 1
                continue
            top_level_counter += 1
            numeral = int_to_roman(top_level_counter)
            story.append(Paragraph(f"{numeral}. {inline_md(heading_text)}", styles['h2']))
            i += 1
            continue
        if stripped.startswith('# '):
            flush_para()
            title_text = doc_title_override or stripped[2:].strip()
            story.append(Paragraph(inline_md(title_text), styles['doc_title']))
            # Clear visual separation between the title and the first
            # heading beneath it, so the first section is never mistaken
            # for a continuation of the title.
            story.append(HRFlowable(width='40%', thickness=0.5, color=colors.black, hAlign='CENTER'))
            story.append(Spacer(1, 10))
            i += 1
            continue

        # Signature block detection: a line of underscores followed by name/
        # title/address lines, rendered single-spaced.
        if set(stripped) <= {'_'} and len(stripped) >= 10:
            flush_para()
            story.append(Spacer(1, 24))
            story.append(Paragraph(stripped, styles['sig_line']))
            i += 1
            # consume following short signature lines (name, title, address)
            while i < n and lines[i].strip() != '' and not lines[i].strip().startswith('#'):
                sig_stripped = lines[i].strip()
                if set(sig_stripped) <= {'-'}:
                    break
                story.append(Paragraph(inline_md(sig_stripped), styles['sig_line']))
                i += 1
            continue

        # "Dated:" line and "Respectfully submitted," -- single spaced-ish,
        # keep as their own short paragraphs
        if stripped.startswith('Dated:') or stripped == 'Respectfully submitted,':
            flush_para()
            story.append(Spacer(1, 12))
            story.append(Paragraph(inline_md(stripped), styles['sig_line']))
            i += 1
            # A venue line (e.g. "&nbsp;&nbsp;...Rochester, New York") often
            # follows "Dated:" directly -- keep it as part of the same
            # single-spaced signature block rather than letting it fall
            # through into a justified, indented body paragraph.
            if stripped.startswith('Dated:') and i < n and lines[i].strip().startswith('&nbsp;'):
                story.append(Paragraph(inline_md(lines[i].strip()), styles['sig_line']))
                i += 1
            continue

        # NOTES section numbered footnote text lines: "[1] text"
        if in_notes:
            fm = re.match(r'^\[(\d+)\]\s*(.*)$', stripped)
            if fm:
                flush_para('numbered')
                story.append(Paragraph(f"<b>[{fm.group(1)}]</b> {inline_md(fm.group(2))}", styles['footnote']))
                story.append(Spacer(1, 6))
                i += 1
                continue

        # Otherwise: accumulate into paragraph buffer
        para_buf.append(line)
        i += 1

    flush_quote()
    flush_para('numbered' if in_notes else 'body')

    # If the document defined footnotes ([^1]: ...) but never rendered them
    # via an explicit "## NOTES" heading, append a NOTES section now so no
    # footnote text is silently dropped.
    if footnotes and not in_notes:
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width='100%', thickness=0.5, color=colors.black))
        story.append(Paragraph('NOTES', styles['notes_head']))
        for num in sorted(footnotes.keys(), key=lambda x: int(x)):
            story.append(Paragraph(f"<b>[{num}]</b> {inline_md(footnotes[num])}", styles['footnote']))
            story.append(Spacer(1, 6))

    # ---- Page numbering ----
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 10)
        canvas.drawCentredString(PAGE_W / 2.0, 0.5 * inch, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(
        pdf_path, pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title=doc_title_override or 'SORA Filing',
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return len(footnotes)


if __name__ == '__main__':
    md_path, pdf_path = sys.argv[1], sys.argv[2]
    title_override = sys.argv[3] if len(sys.argv) > 3 else None
    convert(md_path, pdf_path, title_override)
    print(f"Wrote {pdf_path}")
