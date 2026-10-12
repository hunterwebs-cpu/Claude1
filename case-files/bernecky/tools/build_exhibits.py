#!/usr/bin/env python3
"""Build the combined Exhibits A-E package: a cover/index page, then a
divider page before each exhibit, then the exhibit's own pages, all merged
into a single PDF."""
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from pypdf import PdfReader, PdfWriter

PAGE_W, PAGE_H = letter
MARGIN = 1 * inch
FONT = 'Times-Roman'

styles = {
    'caption_court': ParagraphStyle('cc', fontName='Times-Roman', fontSize=12, leading=14, alignment=TA_CENTER),
    'caption_body': ParagraphStyle('cb', fontName='Times-Roman', fontSize=12, leading=14, alignment=TA_LEFT),
    'caption_party': ParagraphStyle('cp', fontName='Times-Bold', fontSize=12, leading=14, alignment=TA_LEFT),
    'title': ParagraphStyle('title', fontName='Times-Bold', fontSize=14, leading=17, alignment=TA_CENTER, spaceBefore=30, spaceAfter=24),
    'index_item': ParagraphStyle('idx', fontName='Times-Roman', fontSize=12, leading=20, alignment=TA_LEFT, leftIndent=20, spaceAfter=6),
    'divider_label': ParagraphStyle('dl', fontName='Times-Bold', fontSize=28, leading=32, alignment=TA_CENTER, spaceBefore=200, spaceAfter=20),
    'divider_desc': ParagraphStyle('dd', fontName='Times-Roman', fontSize=12, leading=16, alignment=TA_CENTER, spaceAfter=6, leftIndent=60, rightIndent=60),
}

EXHIBITS = [
    ('A', "Government's Supplemental Sentencing Statement, filed January 13, 2012, "
          "in Docket No. 6:11-CR-06045, Doc. 24 (W.D.N.Y.)."),
    ('B', "Amended Sentencing Statement, filed May 29, 2018, in Docket No. "
          "6:18-CR-06018, Doc. 24 (W.D.N.Y.)."),
    ('C', "Government's Statement with Respect to Sentencing Factors, filed "
          "April 24, 2018, in Docket No. 6:18-CR-06018, Doc. 18 (W.D.N.Y.)."),
    ('D', "Bureau of Prisons Program Statement 1351.05, Release of Information "
          "(as amended)."),
    ('E', "Defendant's Sentencing Memorandum, filed January 6, 2012, in Docket "
          "No. 6:11-CR-06045, Doc. 23 (W.D.N.Y.), submitted by then-counsel "
          "Adrian J. Burke, Esq."),
]

SOURCE_FILES = {
    'A': 'exhibit_A.pdf',
    'B': 'exhibit_B.pdf',
    'C': 'exhibit_C.pdf',
    'D': 'bop_1351_05.pdf',
    'E': 'exhibit_E.pdf',
}


def build_cover_pdf():
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                             topMargin=MARGIN, bottomMargin=MARGIN)
    story = []
    story.append(Paragraph('State of New York', styles['caption_court']))
    story.append(Paragraph('Monroe County Supreme &amp; County Courts', styles['caption_court']))
    story.append(Spacer(1, 8))
    story.append(Paragraph('-----------------------------------------------------X', styles['caption_body']))
    story.append(Spacer(1, 4))

    left_col = [
        ['In re: Matter of the Application for a.', 'Index No: None Provided by Clerk'],
        ['Risk Level Determination Pursuant to.', 'Hearing Date: September 11, 2026'],
        ['Article 6-C of the Correction Law.', 'Before: Hon. Karen Bailey Turner, J.C.C.'],
        ['(Sex Offender Registration Act) as to:', ''],
        ['', ''],
    ]
    rows = [[Paragraph(l, styles['caption_body']), Paragraph(r, styles['caption_body'])] for l, r in left_col]
    rows.append([Paragraph('<b>JEFFREY BERNECKY,</b>', styles['caption_body']),
                 Paragraph('<b>EXHIBITS TO CERTIFICATION</b>', styles['caption_body'])])
    rows.append([Paragraph('NYSID No. OS6430', styles['caption_body']),
                 Paragraph('<b>OF JEFFREY BERNECKY</b>', styles['caption_body'])])
    rows.append([Paragraph('&nbsp;&nbsp;&nbsp;<i>Respondent, Pro Se.</i>', styles['caption_body']), ''])
    tbl = Table(rows, colWidths=[3.35 * inch, 3.15 * inch])
    tbl.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 4))
    story.append(Paragraph('-----------------------------------------------------X', styles['caption_body']))

    story.append(Paragraph('EXHIBITS A THROUGH E', styles['title']))
    story.append(Paragraph(
        'Annexed to and authenticated by the Certification of Jeffrey Bernecky, submitted '
        'pursuant to CPLR 2106 in connection with the risk-level classification hearing '
        'scheduled for September 11, 2026.',
        ParagraphStyle('sub', fontName='Times-Roman', fontSize=11, leading=15, alignment=TA_CENTER,
                        spaceAfter=28, leftIndent=40, rightIndent=40)))

    story.append(Paragraph('INDEX OF EXHIBITS', ParagraphStyle('idxhead', fontName='Times-Bold', fontSize=12,
                                                                 leading=16, alignment=TA_CENTER, spaceAfter=16)))
    for letter_, desc in EXHIBITS:
        story.append(Paragraph(f'<b>Exhibit {letter_}.</b> {desc}', styles['index_item']))

    doc.build(story)
    buf.seek(0)
    return buf


def build_divider_pdf(letter_, desc):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                             topMargin=MARGIN, bottomMargin=MARGIN)
    story = [
        Paragraph(f'EXHIBIT {letter_}', styles['divider_label']),
        HRFlowable(width='30%', thickness=1, color=colors.black, hAlign='CENTER'),
        Spacer(1, 16),
        Paragraph(desc, styles['divider_desc']),
    ]
    doc.build(story)
    buf.seek(0)
    return buf


def main():
    writer = PdfWriter()

    cover = PdfReader(build_cover_pdf())
    for p in cover.pages:
        writer.add_page(p)

    for letter_, desc in EXHIBITS:
        divider = PdfReader(build_divider_pdf(letter_, desc))
        for p in divider.pages:
            writer.add_page(p)
        exhibit = PdfReader(SOURCE_FILES[letter_])
        for p in exhibit.pages:
            writer.add_page(p)

    out_path = 'Exhibits-A-through-E.pdf'
    with open(out_path, 'wb') as f:
        writer.write(f)
    print('Wrote', out_path, 'with', len(writer.pages), 'total pages')


if __name__ == '__main__':
    main()
