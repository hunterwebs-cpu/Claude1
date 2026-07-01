#!/usr/bin/env python3
"""
generate-briefing-pdf.py  —  Internal Legal Briefing PDF Generator

Usage:
  python generate-briefing-pdf.py --md MARKDOWN_FILE --out OUTPUT.pdf [--config CONFIG.json]

Config JSON fields (all optional except case_name / case_number):
  {
    "case_name":    "S. Bradley Mell",          # italic on cover
    "case_number":  "26-16834-EJO",
    "court":        "United States Bankruptcy Court\nDistrict of New Jersey",
    "hearing_date": "July 16, 2026",
    "judge":        "Hon. Eamonn J. O'Hagan, U.S.B.J.",
    "subject":      "Opposition to Motion to Dismiss (Doc. 8)",
    "date":         "June 28, 2026",
    "distribution": "Legal Team — INTERNAL USE ONLY",
    "title":        "INTERNAL LEGAL RESEARCH MEMORANDUM"
  }

Requires:
  pip install playwright
  apt install pandoc
  Chromium at /opt/pw-browsers/chromium-*/chrome-linux/chrome (pre-installed in Claude Code cloud)
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile


# ---------------------------------------------------------------------------
# Chromium discovery
# ---------------------------------------------------------------------------

def _find_chromium():
    candidates = [
        "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
        "/opt/pw-browsers/chromium-1179/chrome-linux/chrome",
    ]
    # Try any versioned path
    candidates += glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None


# ---------------------------------------------------------------------------
# CSS + templates
# ---------------------------------------------------------------------------

CSS = """
<style>
@page { size: letter; }

*, *::before, *::after { box-sizing: border-box; }

body {
  font-family: "Times New Roman", Times, serif;
  font-size: 12pt;
  line-height: 1.45;
  color: #000;
  margin: 0;
  padding: 0;
}

/* -- COVER PAGE -- */
.cover-page {
  page-break-after: always;
  text-align: center;
  padding-top: 1.1in;
}
.wp-block { margin-bottom: 0.35in; }
.wp-line1 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14.5pt;
  font-weight: bold;
  color: #A50000;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.wp-line2 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13pt;
  font-weight: bold;
  color: #A50000;
  letter-spacing: 0.04em;
  margin-top: 4pt;
}
.wp-line3 {
  font-family: "Times New Roman", Times, serif;
  font-size: 10pt;
  color: #A50000;
  letter-spacing: 0.02em;
  margin-top: 4pt;
}
.cover-bar {
  background: #828282;
  height: 6pt;
  margin: 0.3in auto 0.35in;
  width: 5in;
}
.cover-title {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 22pt;
  font-weight: bold;
  color: #000;
  line-height: 1.25;
  margin-bottom: 0.3in;
}
.cover-rule-thin {
  border: none;
  border-top: 0.5pt solid #828282;
  margin: 0 auto 0.35in;
  width: 5in;
}
.cover-info {
  display: inline-table;
  text-align: left;
  border-collapse: collapse;
  font-size: 10.5pt;
  line-height: 1.7;
}
.ci-label {
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  padding-right: 1.2em;
  vertical-align: top;
  white-space: nowrap;
  color: #000;
}
.ci-val {
  font-family: "Times New Roman", Times, serif;
  vertical-align: top;
  color: #000;
}

/* -- HEADINGS -- */
h1 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14pt;
  font-weight: bold;
  text-align: center;
  margin: 1.4em 0 0.5em;
  page-break-after: avoid;
}
h2 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 12pt;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  margin: 1.3em 0 0.15em;
  border-bottom: 0.8pt solid #555;
  padding-bottom: 2pt;
  page-break-after: avoid;
}
h3 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11.5pt;
  font-weight: bold;
  margin: 1.1em 0 0.2em;
  page-break-after: avoid;
}
h4, h5, h6 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 11pt;
  font-weight: bold;
  margin: 0.9em 0 0.15em;
  page-break-after: avoid;
}

/* -- BODY -- */
p { margin: 0 0 0.65em 0; text-align: justify; }
em { font-style: italic; }
strong { font-weight: bold; }

blockquote {
  margin: 0.7em 0 0.7em 2em;
  padding-left: 0.8em;
  border-left: 2pt solid #bbb;
  font-style: italic;
}

hr {
  border: none;
  border-top: 0.5pt solid #aaa;
  margin: 1.2em 0;
}

/* -- TABLES -- */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.8em 0;
  font-size: 10.5pt;
}
th {
  background: #e8e8e8;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  border: 0.75pt solid #999;
  padding: 4pt 6pt;
  text-align: left;
}
td {
  border: 0.75pt solid #ccc;
  padding: 3pt 6pt;
  vertical-align: top;
}

/* -- LISTS -- */
ul, ol { margin: 0.3em 0 0.65em 0; padding-left: 1.6em; }
li { margin-bottom: 0.25em; text-align: justify; }

/* -- CODE -- */
code { font-family: "Courier New", Courier, monospace; font-size: 9.5pt; }

/* -- PAGE BREAKS -- */
h1, h2, h3, h4 { page-break-after: avoid; }
tr { page-break-inside: avoid; }
</style>
"""

HEADER_TEMPLATE = """
<div style="font-family:Arial,Helvetica,sans-serif;font-size:8pt;font-weight:bold;
  color:#A50000;letter-spacing:0.05em;width:100%;padding:0 0.5in 3px;
  border-bottom:0.5pt solid #999;display:flex;justify-content:space-between;
  align-items:baseline;">
  <span>ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL</span>
  <span style="color:#505050;font-weight:normal;font-size:8pt;letter-spacing:0;">{case_number}</span>
</div>"""

FOOTER_TEMPLATE = """
<div style="font-family:'Times New Roman',Times,serif;font-size:8pt;color:#505050;
  width:100%;padding:3px 0.5in 0;border-top:0.5pt solid #bbb;
  display:flex;justify-content:space-between;align-items:baseline;">
  <span><em>{case_short}</em></span>
  <span class="pageNumber"></span>
</div>"""


# ---------------------------------------------------------------------------
# Cover page builder
# ---------------------------------------------------------------------------

def _esc(s):
    """Minimal HTML escaping."""
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _row(label, value_html):
    return f'<tr><td class="ci-label">{_esc(label)}</td><td class="ci-val">{value_html}</td></tr>\n'


def build_cover(meta):
    title = meta.get("title", "INTERNAL LEGAL RESEARCH MEMORANDUM")
    title_html = "<br>".join(title.split("\n"))

    rows = []
    case_name = meta.get("case_name", "")
    if case_name:
        rows.append(_row("IN RE:", f"<em>{_esc(case_name)}</em>"))
    if meta.get("case_number"):
        rows.append(_row("Case No.:", _esc(meta["case_number"])))
    if meta.get("court"):
        court_html = "<br>".join(_esc(l) for l in meta["court"].split("\n"))
        rows.append(_row("Court:", court_html))
    if meta.get("hearing_date"):
        rows.append(_row("Hearing:", _esc(meta["hearing_date"])))
    if meta.get("judge"):
        rows.append(_row("Before:", _esc(meta["judge"])))
    if meta.get("subject"):
        subject_html = "<br>".join(_esc(l) for l in meta["subject"].split("\n"))
        rows.append(_row("Subject:", subject_html))
    if meta.get("date"):
        rows.append(_row("Date:", _esc(meta["date"])))
    dist = meta.get("distribution", "Legal Team — INTERNAL USE ONLY")
    rows.append(_row("Distribution:", _esc(dist)))

    return f"""
<div class="cover-page">
  <div class="wp-block">
    <div class="wp-line1">ATTORNEY WORK PRODUCT</div>
    <div class="wp-line2">PRIVILEGED AND CONFIDENTIAL</div>
    <div class="wp-line3">DO NOT DISTRIBUTE WITHOUT COUNSEL AUTHORIZATION</div>
  </div>
  <div class="cover-bar"></div>
  <div class="cover-title">{title_html}</div>
  <div class="cover-rule-thin"></div>
  <table class="cover-info">
    {"    ".join(rows)}
  </table>
</div>
"""


# ---------------------------------------------------------------------------
# Markdown -> HTML body
# ---------------------------------------------------------------------------

def md_to_body(md_text):
    """Run pandoc on the markdown and return the body HTML after the first <hr />."""
    # Strip any GitHub MCP metadata prefix
    md_text = re.sub(r'^\[Resource from github[^\]]*\]\s*', '', md_text)

    result = subprocess.run(
        ['pandoc', '-f', 'markdown', '-t', 'html'],
        input=md_text, capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"pandoc error: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    html = result.stdout
    # The first <hr /> separates cover metadata from body content
    hr_pos = html.find('<hr />')
    if hr_pos == -1:
        return html  # no separator found, use full output
    return html[hr_pos + len('<hr />'):]


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def generate_pdf(html_path, out_path, meta):
    from playwright.sync_api import sync_playwright

    chromium = _find_chromium()
    if not chromium:
        print("Chromium not found. Install playwright browsers.", file=sys.stderr)
        sys.exit(1)

    case_number = meta.get("case_number", "")
    # Short name for footer: "In re [case_name]" or just the case name
    case_name = meta.get("case_name", "")
    case_short = f"In re {case_name}" if case_name else case_number

    header_html = HEADER_TEMPLATE.format(case_number=_esc(case_number))
    footer_html = FOOTER_TEMPLATE.format(case_short=_esc(case_short))

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium)
        page = browser.new_page()
        page.goto(f'file://{os.path.abspath(html_path)}', wait_until='networkidle')
        page.pdf(
            path=out_path,
            format='Letter',
            margin={'top': '0.85in', 'bottom': '0.75in', 'left': '1in', 'right': '1in'},
            display_header_footer=True,
            header_template=header_html,
            footer_template=footer_html,
            print_background=True,
        )
        browser.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate an internal legal briefing PDF.")
    parser.add_argument('--md', required=True, help='Path to the source markdown file')
    parser.add_argument('--out', required=True, help='Output PDF path')
    parser.add_argument('--config', help='JSON file with case metadata')
    args = parser.parse_args()

    # Load case metadata
    meta = {}
    if args.config:
        with open(args.config) as f:
            meta = json.load(f)

    # Load markdown
    with open(args.md) as f:
        md_text = f.read()

    # Build HTML
    cover = build_cover(meta)
    body = md_to_body(md_text)

    full_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8">{CSS}</head>
<body>
{cover}
{body}
</body>
</html>"""

    # Write intermediate HTML to a temp file
    tmp_html = args.out.replace('.pdf', '.html')
    with open(tmp_html, 'w') as f:
        f.write(full_html)
    print(f"HTML written: {tmp_html}")

    # Render PDF
    generate_pdf(tmp_html, args.out, meta)
    size = os.path.getsize(args.out)
    print(f"PDF generated: {args.out} ({size // 1024} KB)")


if __name__ == '__main__':
    main()
