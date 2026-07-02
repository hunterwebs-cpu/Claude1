#!/usr/bin/env python3
"""
compile_volumes.py
Appendix volume compiler for In re S. Bradley Mell, No. 26-16834-EJO (Bankr. D.N.J.)
Hearing: July 16, 2026

Reads manifest.json, merges PDFs per volume with cover and separator pages,
auto-splits at MAX_VOLUME_BYTES, outputs to ./output/
"""

import json
import os
import re
import sys
import io
import textwrap
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
try:
    from pypdf import PdfWriter, PdfReader
except ImportError:
    print("ERROR: pypdf not installed. Run: pip install pypdf")
    sys.exit(1)

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
BASE_DIR = Path(__file__).parent
MANIFEST_PATH = BASE_DIR / "manifest.json"
DOWNLOADS_DIR = BASE_DIR / "downloads"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)
DOWNLOADS_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CASE_NAME = "In re S. Bradley Mell"
CASE_NO = "No. 26-16834-EJO (Bankr. D.N.J.)"
HEARING_DATE = "July 16, 2026"
OPPOSITION_LABEL = "Appendix to Opposition to Motion to Dismiss"

# Colors (dark navy for legal documents)
COLOR_NAVY = HexColor("#1B3A6B")
COLOR_GOLD = HexColor("#B8962E")
COLOR_LIGHT = HexColor("#F5F5F5")

# ---------------------------------------------------------------------------
# Pseudonymity rule
# The creditor's real name (Lilly, Cannon, or any combination) must NEVER
# appear in any cover page, separator page, or output file.
# Only the pseudonym "B.B." is permitted.
# ---------------------------------------------------------------------------
_BB_REAL_NAME_PATTERN = re.compile(r'\bLilly\b|\bCannon\b', re.IGNORECASE)


def sanitize_title(title: str) -> str:
    """Replace any real name for B.B. with the pseudonym 'B.B.'"""
    return _BB_REAL_NAME_PATTERN.sub("B.B.", title)

# ---------------------------------------------------------------------------
# PDF generation helpers
# ---------------------------------------------------------------------------

def make_cover_page(volume_label: str, documents: list) -> bytes:
    """Generate a cover page PDF for a volume and return as bytes."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)
    w, h = letter

    # Background header bar
    c.setFillColor(COLOR_NAVY)
    c.rect(0, h - 2.2 * inch, w, 2.2 * inch, fill=True, stroke=False)

    # Case name (white, in header)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(w / 2, h - 0.75 * inch, CASE_NAME)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w / 2, h - 1.1 * inch, CASE_NO)
    c.setFont("Helvetica", 10)
    c.drawCentredString(w / 2, h - 1.4 * inch, f"Hearing: {HEARING_DATE}")
    c.drawCentredString(w / 2, h - 1.7 * inch, OPPOSITION_LABEL)

    # Gold rule
    c.setStrokeColor(COLOR_GOLD)
    c.setLineWidth(2)
    c.line(inch, h - 2.3 * inch, w - inch, h - 2.3 * inch)

    # Volume label
    c.setFillColor(COLOR_NAVY)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w / 2, h - 2.9 * inch, volume_label)

    # Document index table
    y = h - 3.4 * inch
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(COLOR_NAVY)
    c.drawString(inch, y, "Tab")
    c.drawString(1.6 * inch, y, "Document")
    c.drawString(w - 1.5 * inch, y, "Date")

    # Header underline
    y -= 0.05 * inch
    c.setStrokeColor(COLOR_NAVY)
    c.setLineWidth(0.5)
    c.line(inch, y, w - inch, y)
    y -= 0.2 * inch

    c.setFont("Helvetica", 8.5)
    c.setFillColor(black)

    for i, doc in enumerate(documents):
        if y < 0.8 * inch:
            c.showPage()
            y = h - inch
            c.setFont("Helvetica", 8.5)
            c.setFillColor(black)

        tab = doc.get("tab", "")
        title = doc.get("display_title", doc.get("local_filename", ""))
        date = doc.get("date", "")

        # Alternate row shading
        if i % 2 == 0:
            c.setFillColor(COLOR_LIGHT)
            c.rect(inch - 0.05 * inch, y - 0.05 * inch,
                   w - 2 * inch + 0.1 * inch, 0.22 * inch,
                   fill=True, stroke=False)
            c.setFillColor(black)

        c.drawString(inch, y, tab)

        max_title_width = int((w - 3.5 * inch) / (8.5 * 0.5))
        wrapped = textwrap.wrap(title, max_title_width) if len(title) > max_title_width else [title]
        c.drawString(1.6 * inch, y, wrapped[0])
        for extra in wrapped[1:]:
            y -= 0.15 * inch
            c.drawString(1.6 * inch, y, extra)

        c.drawString(w - 1.5 * inch, y, date)
        y -= 0.27 * inch

    # Footer
    c.setFillColor(grey)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(w / 2, 0.4 * inch,
                        f"CONFIDENTIAL volumes require protective order | Generated {datetime.now().strftime('%Y-%m-%d')}")

    c.save()
    buf.seek(0)
    return buf.read()


def make_separator_page(tab: str, title: str, confidential: bool = False) -> bytes:
    """Generate a tab separator page and return as bytes."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)
    w, h = letter

    # Side tab band
    c.setFillColor(COLOR_NAVY)
    c.rect(w - 1.2 * inch, 0, 1.2 * inch, h, fill=True, stroke=False)

    # Tab label rotated
    c.saveState()
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.translate(w - 0.6 * inch, h / 2)
    c.rotate(270)
    c.drawCentredString(0, 0, f"Tab {tab}")
    c.restoreState()

    # Center content
    c.setFillColor(COLOR_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString((w - 1.2 * inch) / 2, h / 2 + 0.5 * inch, f"Tab {tab}")

    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    wrapped = textwrap.wrap(title, 60)
    ypos = h / 2
    for line in wrapped:
        c.drawCentredString((w - 1.2 * inch) / 2, ypos, line)
        ypos -= 0.22 * inch

    if confidential:
        c.setFillColor(HexColor("#CC0000"))
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString((w - 1.2 * inch) / 2, h / 2 - 1.2 * inch,
                            "CONFIDENTIAL — DO NOT DISTRIBUTE WITHOUT PROTECTIVE ORDER")

    # Gold rule
    c.setStrokeColor(COLOR_GOLD)
    c.setLineWidth(1.5)
    y_rule = h / 2 + 0.8 * inch
    c.line(inch, y_rule, w - 1.5 * inch, y_rule)

    c.save()
    buf.seek(0)
    return buf.read()


# ---------------------------------------------------------------------------
# Volume compiler
# ---------------------------------------------------------------------------

def pdf_from_bytes(data: bytes) -> PdfReader:
    return PdfReader(io.BytesIO(data))


def compile_volume(vol_id: str, vol_label: str, documents: list,
                   max_bytes: int, warnings: list) -> list[tuple[str, int]]:
    """
    Compile one logical volume into one or more output files.
    Splits at max_bytes appending 'a', 'b', 'c'... suffixes when needed.

    Returns list of (output_filepath, page_count) tuples.
    """
    outputs = []

    # Collect valid docs (skip=False, confidential=False)
    valid_docs = [d for d in documents if not d.get("skip") and not d.get("confidential")]

    if not valid_docs:
        print(f"  [SKIP] Volume {vol_id} — no non-confidential, non-skipped documents")
        return outputs

    # Build list of (separator_bytes, pdf_path) for each doc
    parts = []  # list of (sep_bytes, pdf_bytes_or_None, doc)
    for doc in valid_docs:
        local_filename = doc["local_filename"]
        pdf_path = DOWNLOADS_DIR / local_filename
        safe_title = sanitize_title(doc.get("display_title", ""))
        sep = make_separator_page(doc.get("tab", "?"), safe_title, doc.get("confidential", False))

        if not pdf_path.exists():
            warnings.append(f"MISSING: {local_filename} (vol {vol_id}, tab {doc.get('tab')}) — file not found in downloads/")
            parts.append((sep, None, doc))
        else:
            try:
                pdf_bytes = pdf_path.read_bytes()
                parts.append((sep, pdf_bytes, doc))
            except Exception as e:
                warnings.append(f"ERROR reading {local_filename}: {e}")
                parts.append((sep, None, doc))

    # Now split into chunks under max_bytes
    # Strategy: accumulate docs into chunks, emit a new file when adding next doc would exceed limit
    suffix_idx = 0
    suffixes = [""] + list("abcdefghij")

    def get_suffix():
        return suffixes[suffix_idx] if suffix_idx < len(suffixes) else str(suffix_idx)

    chunk_docs = []
    chunk_parts = []
    chunk_size = 0

    def flush_chunk(chunk_docs_list, chunk_parts_list, suffix_str):
        """Write accumulated chunk to output file."""
        if not chunk_docs_list:
            return None, 0

        # Sanitize display titles for cover page (pseudonymity rule)
        sanitized_docs = [
            {**d, "display_title": sanitize_title(d.get("display_title", ""))}
            for d in chunk_docs_list
        ]
        cover = make_cover_page(vol_label, sanitized_docs)
        writer = PdfWriter()

        # Add cover
        for page in pdf_from_bytes(cover).pages:
            writer.add_page(page)

        # Add each doc with separator
        for sep_b, pdf_b, doc in chunk_parts_list:
            for page in pdf_from_bytes(sep_b).pages:
                writer.add_page(page)
            if pdf_b is not None:
                try:
                    reader = pdf_from_bytes(pdf_b)
                    for page in reader.pages:
                        writer.add_page(page)
                except Exception as e:
                    warnings.append(f"ERROR merging {doc['local_filename']}: {e}")

        safe_id = vol_id.replace("/", "_")
        fname = f"appendix_vol_{safe_id}{suffix_str}.pdf"
        out_path = OUTPUT_DIR / fname

        buf = io.BytesIO()
        writer.write(buf)
        buf.seek(0)
        out_bytes = buf.read()
        out_path.write_bytes(out_bytes)
        page_count = len(writer.pages)
        actual_size = len(out_bytes)
        print(f"    => {fname}  ({page_count} pages, {actual_size/1024/1024:.2f} MB)")
        return str(out_path), page_count

    for sep_b, pdf_b, doc in parts:
        doc_size = len(sep_b) + (len(pdf_b) if pdf_b else 0)

        # Check if adding this doc would exceed the limit (plus cover overhead ~50KB)
        cover_overhead = 51200
        if chunk_docs and (chunk_size + doc_size + cover_overhead) > max_bytes:
            # Flush current chunk
            suffix_str = get_suffix()
            out_path, pc = flush_chunk(chunk_docs, chunk_parts, suffix_str)
            if out_path:
                outputs.append((out_path, pc))
            suffix_idx += 1
            chunk_docs = []
            chunk_parts = []
            chunk_size = 0

        chunk_docs.append(doc)
        chunk_parts.append((sep_b, pdf_b, doc))
        chunk_size += doc_size

    # Flush remaining
    if chunk_docs:
        suffix_str = get_suffix()
        out_path, pc = flush_chunk(chunk_docs, chunk_parts, suffix_str)
        if out_path:
            outputs.append((out_path, pc))

    return outputs


def compile_confidential_volume(vol_id: str, vol_label: str, documents: list,
                                 max_bytes: int, warnings: list) -> list[tuple[str, int]]:
    """Compile confidential documents into a separate sealed volume."""
    outputs = []
    valid_docs = [d for d in documents if not d.get("skip") and d.get("confidential")]

    if not valid_docs:
        return outputs

    # Sanitize display titles (pseudonymity rule)
    sanitized_docs = [
        {**d, "display_title": sanitize_title(d.get("display_title", ""))}
        for d in valid_docs
    ]
    cover = make_cover_page(f"[SEALED] {vol_label}", sanitized_docs)
    writer = PdfWriter()

    for page in pdf_from_bytes(cover).pages:
        writer.add_page(page)

    for doc in valid_docs:
        safe_title = sanitize_title(doc.get("display_title", ""))
        sep = make_separator_page(doc.get("tab", "?"), safe_title, confidential=True)
        for page in pdf_from_bytes(sep).pages:
            writer.add_page(page)

        local_filename = doc["local_filename"]
        pdf_path = DOWNLOADS_DIR / local_filename
        if not pdf_path.exists():
            warnings.append(f"MISSING (confidential): {local_filename}")
        else:
            try:
                for page in PdfReader(str(pdf_path)).pages:
                    writer.add_page(page)
            except Exception as e:
                warnings.append(f"ERROR merging confidential {local_filename}: {e}")

    safe_id = vol_id.replace("/", "_")
    fname = f"appendix_vol_{safe_id}_SEALED.pdf"
    out_path = OUTPUT_DIR / fname

    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    out_bytes = buf.read()
    out_path.write_bytes(out_bytes)
    page_count = len(writer.pages)
    print(f"    => {fname}  ({page_count} pages, {len(out_bytes)/1024/1024:.2f} MB)  [SEALED]")
    outputs.append((str(out_path), page_count))
    return outputs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("APPENDIX VOLUME COMPILER")
    print(f"Case: {CASE_NAME}, {CASE_NO}")
    print(f"Hearing: {HEARING_DATE}")
    print("=" * 70)
    print()

    # Load manifest
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

    max_bytes = manifest.get("max_volume_bytes", 15099494)
    volumes = manifest.get("volumes", [])
    warnings = []
    summary_rows = []
    total_downloaded = 0

    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Downloads directory: {DOWNLOADS_DIR}")
    print(f"Max volume size: {max_bytes/1024/1024:.1f} MB")
    print(f"Volumes to compile: {len(volumes)}")
    print()

    for vol in volumes:
        vol_id = vol["id"]
        vol_label = vol["label"]
        documents = vol.get("documents", [])

        print(f"Processing Volume {vol_id}: {vol_label}")

        # Count available downloads
        for doc in documents:
            if doc.get("skip") or doc.get("confidential"):
                continue
            p = DOWNLOADS_DIR / doc["local_filename"]
            if p.exists():
                total_downloaded += 1

        # Compile main (non-confidential) content
        outputs = compile_volume(vol_id, vol_label, documents, max_bytes, warnings)
        for out_path, pc in outputs:
            fname = Path(out_path).name
            size_mb = Path(out_path).stat().st_size / 1024 / 1024
            doc_count = len([d for d in documents if not d.get("skip") and not d.get("confidential")])
            summary_rows.append({
                "volume": vol_id,
                "label": vol_label,
                "docs": doc_count,
                "pages": pc,
                "size_mb": size_mb,
                "filename": fname,
                "sealed": False
            })

        # Compile confidential content for this volume
        conf_outputs = compile_confidential_volume(vol_id, vol_label, documents, max_bytes, warnings)
        for out_path, pc in conf_outputs:
            fname = Path(out_path).name
            size_mb = Path(out_path).stat().st_size / 1024 / 1024
            doc_count = len([d for d in documents if not d.get("skip") and d.get("confidential")])
            summary_rows.append({
                "volume": vol_id,
                "label": f"[SEALED] {vol_label}",
                "docs": doc_count,
                "pages": pc,
                "size_mb": size_mb,
                "filename": fname,
                "sealed": True
            })

        print()

    # ---------------------------------------------------------------------------
    # Summary table
    # ---------------------------------------------------------------------------
    print()
    print("=" * 70)
    print("COMPILATION SUMMARY")
    print("=" * 70)
    print(f"{'Volume':<8} {'Docs':>4} {'Pages':>6} {'Size (MB)':>10}  {'Output File'}")
    print("-" * 70)
    for row in summary_rows:
        sealed_flag = " [SEALED]" if row["sealed"] else ""
        print(f"{row['volume']:<8} {row['docs']:>4} {row['pages']:>6} {row['size_mb']:>9.2f}  {row['filename']}{sealed_flag}")

    total_outputs = len(summary_rows)
    total_pages = sum(r["pages"] for r in summary_rows)
    total_size_mb = sum(r["size_mb"] for r in summary_rows)
    print("-" * 70)
    print(f"{'TOTAL':<8} {sum(r['docs'] for r in summary_rows):>4} {total_pages:>6} {total_size_mb:>9.2f}  ({total_outputs} output files)")
    print()

    # ---------------------------------------------------------------------------
    # Warnings
    # ---------------------------------------------------------------------------
    if warnings:
        print("=" * 70)
        print(f"WARNINGS ({len(warnings)})")
        print("=" * 70)
        for w in warnings:
            print(f"  ! {w}")
        print()

    # ---------------------------------------------------------------------------
    # Oversized file notice
    # ---------------------------------------------------------------------------
    oversized = manifest.get("oversized_files", [])
    if oversized:
        print("=" * 70)
        print("OVERSIZED FILES (excluded from volumes — deliver separately):")
        print("=" * 70)
        for f in oversized:
            mb = f.get("size_bytes", 0) / 1024 / 1024
            print(f"  {f['local_filename']} ({mb:.1f} MB) — {f['reason']}")
        print()

    print(f"Files available in downloads/: {total_downloaded}")
    print("Done. Output files are in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
