#!/usr/bin/env python3
"""
gen_master_toc.py
Master Table of Contents generator for appendix volumes.
In re S. Bradley Mell, No. 26-16834-EJO (Bankr. D.N.J.)
Hearing: July 16, 2026

Reads ../manifest.json and generates MASTER_TOC.pdf in this directory.
"""

import json
import io
import re
import sys
from pathlib import Path

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, black, white, grey
except ImportError:
    print("ERROR: reportlab not installed. Run: pip install reportlab")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
MANIFEST_PATH = SCRIPT_DIR.parent / "manifest.json"
OUTPUT_PATH = SCRIPT_DIR / "MASTER_TOC.pdf"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CASE_NAME = "In re S. Bradley Mell"
CASE_NO = "No. 26-16834-EJO (Bankr. D.N.J.)"
HEARING_DATE = "July 16, 2026"
TITLE_LINE1 = "APPENDIX TO OPPOSITION TO MOTION TO DISMISS"
TITLE_LINE2 = f"{CASE_NAME}, {CASE_NO}  |  {HEARING_DATE}"

COLOR_NAVY = HexColor("#1B3A6B")
COLOR_GOLD = HexColor("#B8962E")
COLOR_LIGHT = HexColor("#F5F5F5")

# ---------------------------------------------------------------------------
# Pseudonymity substitution
# Real names for B.B. are Lilly, Cannon (or combinations thereof).
# Any display_title containing these names must use "B.B." instead.
# ---------------------------------------------------------------------------
_BB_PATTERN = re.compile(r'\bLilly\b|\bCannon\b', re.IGNORECASE)


def sanitize_title(title: str) -> str:
    """Replace any real name for B.B. with the pseudonym 'B.B.'"""
    return _BB_PATTERN.sub("B.B.", title)


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def generate_master_toc(manifest: dict, output_path: Path):
    buf = io.BytesIO()
    c = canvas.Canvas(str(output_path), pagesize=letter)
    w, h = letter

    def draw_header(page_num: int):
        """Draw header bar on current page."""
        # Navy header bar
        c.setFillColor(COLOR_NAVY)
        c.rect(0, h - 2.0 * inch, w, 2.0 * inch, fill=True, stroke=False)

        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(w / 2, h - 0.65 * inch, TITLE_LINE1)
        c.setFont("Helvetica", 10)
        c.drawCentredString(w / 2, h - 1.05 * inch, TITLE_LINE2)

        # Gold rule
        c.setStrokeColor(COLOR_GOLD)
        c.setLineWidth(2)
        c.line(inch, h - 2.1 * inch, w - inch, h - 2.1 * inch)

        # "MASTER TABLE OF CONTENTS" title
        c.setFillColor(COLOR_NAVY)
        c.setFont("Helvetica-Bold", 13)
        c.drawCentredString(w / 2, h - 2.5 * inch, "MASTER TABLE OF CONTENTS")

        # Column headers
        y_header = h - 2.9 * inch
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(COLOR_NAVY)
        c.drawString(inch, y_header, "Tab")
        c.drawString(1.75 * inch, y_header, "Document")

        # Dot leaders start after title, end before "Tab" reference
        c.drawRightString(w - inch, y_header, "Ref.")

        y_header -= 0.05 * inch
        c.setStrokeColor(COLOR_NAVY)
        c.setLineWidth(0.5)
        c.line(inch, y_header, w - inch, y_header)

        return h - 3.2 * inch  # starting y for content

    def draw_footer(page_num: int):
        c.setFillColor(grey)
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(w / 2, 0.4 * inch,
                            f"Appendix — Master TOC  |  {CASE_NAME}  |  Page {page_num}")

    def dot_leaders(c_obj, x_start: float, x_end: float, y: float, font_size: float = 8.5):
        """Draw dot leaders between two x positions."""
        c_obj.setFont("Helvetica", font_size)
        c_obj.setFillColor(grey)
        dot_w = c_obj.stringWidth(".", "Helvetica", font_size)
        gap = dot_w + 0.8
        x = x_start
        while x + dot_w < x_end - 2:
            c_obj.drawString(x, y, ".")
            x += gap

    volumes = manifest.get("volumes", [])

    page_num = 1
    y = draw_header(page_num)
    row_idx = 0

    for vol in volumes:
        vol_label = vol.get("label", "")
        documents = vol.get("documents", [])

        # Skip volumes with no renderable documents
        renderable = [d for d in documents if not d.get("skip")]
        if not renderable:
            continue

        # Check if we need a new page for the volume header
        if y < 1.8 * inch:
            draw_footer(page_num)
            c.showPage()
            page_num += 1
            y = draw_header(page_num)
            row_idx = 0

        # Volume header row
        y -= 0.05 * inch
        c.setFillColor(COLOR_NAVY)
        c.rect(inch - 0.05 * inch, y - 0.07 * inch,
               w - 2 * inch + 0.1 * inch, 0.25 * inch,
               fill=True, stroke=False)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(inch + 0.05 * inch, y + 0.02 * inch, vol_label)
        y -= 0.30 * inch

        for doc in renderable:
            if y < 1.2 * inch:
                draw_footer(page_num)
                c.showPage()
                page_num += 1
                y = draw_header(page_num)
                row_idx = 0

            tab = doc.get("tab", "")
            title = sanitize_title(doc.get("display_title", doc.get("local_filename", "")))
            ref = f"  {tab}"  # The "page" reference is the tab designation

            # Determine if confidential
            conf = doc.get("confidential", False)

            # Alternate shading
            if row_idx % 2 == 0:
                c.setFillColor(COLOR_LIGHT)
                c.rect(inch - 0.05 * inch, y - 0.07 * inch,
                       w - 2 * inch + 0.1 * inch, 0.22 * inch,
                       fill=True, stroke=False)

            # Tab cell
            c.setFillColor(COLOR_NAVY)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(inch, y, tab)

            # Confidential flag
            if conf:
                c.setFillColor(HexColor("#CC0000"))
                c.setFont("Helvetica-Bold", 7)
                c.drawString(inch, y - 0.12 * inch, "[SEALED]")

            # Title (may need truncation for single-line layout)
            c.setFillColor(black)
            c.setFont("Helvetica", 8.5)
            max_title_chars = 75
            if len(title) > max_title_chars:
                title_display = title[:max_title_chars - 3] + "..."
            else:
                title_display = title

            title_x = 1.75 * inch
            title_end_x = w - 1.6 * inch

            c.drawString(title_x, y, title_display)

            # Dot leaders
            title_width = c.stringWidth(title_display, "Helvetica", 8.5)
            dot_start = title_x + title_width + 0.1 * inch
            dot_end = w - 1.55 * inch

            if dot_start < dot_end:
                dot_leaders(c, dot_start, dot_end, y, 8.5)

            # Tab reference (right-aligned)
            c.setFillColor(COLOR_NAVY)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawRightString(w - inch, y, tab)

            y -= 0.27 * inch
            row_idx += 1

        y -= 0.05 * inch  # space between volumes

    draw_footer(page_num)
    c.save()


def main():
    print(f"Reading manifest from: {MANIFEST_PATH}")
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

    print(f"Writing master TOC to: {OUTPUT_PATH}")
    generate_master_toc(manifest, OUTPUT_PATH)

    size_kb = OUTPUT_PATH.stat().st_size / 1024
    print(f"Generated: MASTER_TOC.pdf ({size_kb:.1f} KB)")

    # Count entries
    total_docs = sum(
        len([d for d in vol.get("documents", []) if not d.get("skip")])
        for vol in manifest.get("volumes", [])
    )
    print(f"TOC covers {len(manifest.get('volumes', []))} volumes, {total_docs} documents")
    print("Done.")


if __name__ == "__main__":
    main()
