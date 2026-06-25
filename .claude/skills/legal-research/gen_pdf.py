#!/usr/bin/env python3
"""
gen_pdf.py — Legal Memo PDF Generator
Part of .claude/skills/legal-research

Usage:
    python3 gen_pdf.py <input.md> [output.pdf]

Reads a FINAL-MEMO.md produced by the legal-research skill workflow,
extracts citations for a Table of Authorities, pre-processes the
markdown, and produces a professional PDF via pandoc + pdflatex.

Output defaults to <input>.pdf in the same directory.
"""

import re
import sys
import subprocess
import tempfile
import os
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import date

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SKILL_DIR = Path(__file__).parent
TEMPLATE = SKILL_DIR / "templates" / "legal-memo.tex"


# ---------------------------------------------------------------------------
# Citation extraction
# ---------------------------------------------------------------------------

def extract_cases(text: str) -> list[str]:
    """Extract case citations. Returns deduplicated sorted list."""
    raw = set()

    # Pattern 1: "In re Name, Vol Rep Page (Court Year)"
    for m in re.finditer(
        r'In re [A-Z][A-Za-z\s\.\-\']+(?:LLC|LP|Inc\.|Corp\.|Co\.)?'
        r',\s*\d+[^,\n\[\]]{3,50}\(\s*[^)]*\d{4}\)',
        text
    ):
        raw.add(m.group().strip())

    # Pattern 2: "Name v. Name, Vol Rep Page (Court Year)"
    for m in re.finditer(
        r'[A-Z][A-Za-z\s\.\-\']+\bv\.\s+[A-Z][A-Za-z\s\.\-\']+(?:,\s*\d+[^,\n\[\]]{3,50}\(\s*[^)]*\d{4}\))',
        text
    ):
        raw.add(m.group().strip())

    # Clean up: remove trailing punctuation, footnote markers, VERIFY tags
    cleaned = set()
    for cite in raw:
        cite = re.sub(r'\s*\[(?:VERIFY|BINDING|PERSUASIVE)[^\]]*\]', '', cite)
        cite = re.sub(r'[\s\.\,;:]+$', '', cite)
        cite = cite.strip()
        if len(cite) > 15:
            cleaned.add(cite)

    return sorted(cleaned, key=lambda x: re.sub(r'^In re ', '', x).lstrip())


def extract_statutes(text: str) -> list[str]:
    """Extract statute citations. Returns deduplicated sorted list."""
    raw = set()

    patterns = [
        r'\d+ U\.S\.C\. §+\s*[\d\w\(\)\-]+(?:\([^\)]{1,30}\))?',
        r'N\.J\.S\.A\. [\dA-Z:a-z\-]+',
        r'N\.J\.S\.A\. \d+[A-Za-z]?:\d+[A-Za-z]?-\d+',
    ]

    for pat in patterns:
        for m in re.finditer(pat, text):
            cite = m.group().strip()
            cite = re.sub(r'[\s\.\,;:]+$', '', cite)
            raw.add(cite)

    return sorted(raw)


def extract_rules(text: str) -> list[str]:
    """Extract procedural rules. Returns deduplicated sorted list."""
    raw = set()

    patterns = [
        r'Fed\. R\. Bankr\. P\. \d+(?:\(\w\)(?:\(\d+\))?)?',
        r'Fed\. R\. (?:Civ\.|Evid\.) P\. \d+(?:\(\w\))?',
        r'N\.J\. (?:Ct\. R\.|R\.) \d+:\d+[-\d]*(?:\([a-z]\)(?:\(\d+\))?)?',
        r'N\.J\. RPC \d+\.\d+(?:\([a-z]\))?',
        r'Bankr\. R\. \d+',
    ]

    for pat in patterns:
        for m in re.finditer(pat, text):
            cite = m.group().strip()
            cite = re.sub(r'[\s\.\,;:]+$', '', cite)
            raw.add(cite)

    return sorted(raw)


# ---------------------------------------------------------------------------
# TOA LaTeX builder
# ---------------------------------------------------------------------------

def escape_latex(s: str) -> str:
    """Escape special LaTeX characters in a string."""
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    for old, new in replacements:
        s = s.replace(old, new)
    return s


def build_toa_latex(cases: list[str], statutes: list[str], rules: list[str]) -> str:
    """Build the Table of Authorities as a LaTeX string for the $toa$ variable."""
    lines = []
    lines.append(r'\thispagestyle{frontmatter}')
    lines.append(r'\section*{TABLE OF AUTHORITIES}')
    lines.append(
        r'\textit{Binding Third Circuit and Supreme Court authorities are '
        r'marked \textbf{(BINDING)}. All other federal circuit authority '
        r'is marked \textbf{(PERSUASIVE)}. Citations marked '
        r'\textcolor{verifyAmber}{\textbf{[VERIFY]}} require Westlaw or '
        r'PACER confirmation before filing.}'
    )
    lines.append(r'\vspace{0.5em}')

    def authority_table(items: list[str], label: str) -> list[str]:
        out = []
        out.append(r'\subsection*{' + label + r'}')
        out.append(r'\begin{longtable}{@{}p{\textwidth-0.1in}@{}}')
        out.append(r'\toprule')
        for item in items:
            out.append(escape_latex(item) + r' \\')
        out.append(r'\bottomrule')
        out.append(r'\end{longtable}')
        return out

    if cases:
        lines.extend(authority_table(cases, 'CASES'))
    if statutes:
        lines.extend(authority_table(statutes, 'STATUTES'))
    if rules:
        lines.extend(authority_table(rules, 'RULES AND REGULATIONS'))

    lines.append(r'\newpage')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Markdown pre-processing
# ---------------------------------------------------------------------------

UNICODE_SUBSTITUTIONS = [
    # Math symbols — use pandoc math delimiters $...$ (NOT raw LaTeX \(...\))
    # Pandoc converts $...$ to proper inline math in LaTeX output.
    ('≠', r'$\neq$'),
    ('≤', r'$\leq$'),
    ('≥', r'$\geq$'),
    ('→', r'$\rightarrow$'),
    ('←', r'$\leftarrow$'),
    ('↔', r'$\leftrightarrow$'),
    ('×', r'$\times$'),
    ('÷', r'$\div$'),
    ('±', r'$\pm$'),
    ('°', r'$^{\circ}$'),
    # Typography — safe plain-text forms
    ('—', '---'),    # em dash
    ('–', '--'),     # en dash
    ('‘', "`"),      # left single quote
    ('’', "'"),      # right single quote
    ('“', "``"),     # left double quote
    ('”', "''"),     # right double quote
    ('…', '...'),    # ellipsis
    # Legal symbols handled via LaTeX commands
    ('§', r'\S{}'),         # section sign
    ('¶', r'\P{}'),         # pilcrow
    ('©', r'\textcopyright{}'),
    ('®', r'\textregistered{}'),
    ('™', r'\texttrademark{}'),
    # Misc
    (' ', ' '),       # non-breaking space
    ('•', r'\textbullet{}'),  # bullet
]


def normalize_unicode(text: str) -> str:
    """Replace Unicode characters that pdflatex cannot handle natively."""
    for char, replacement in UNICODE_SUBSTITUTIONS:
        text = text.replace(char, replacement)
    return text

def preprocess_markdown(text: str) -> str:
    """
    Pre-process the markdown for pandoc → LaTeX conversion.

    - Strip the existing H1 title (pandoc uses YAML title for the cover page)
    - Strip the initial ## classification block (goes on cover page already)
    - Promote H4 (####) to H3 (###) so it renders as subsubsection not paragraph
    - Annotate [VERIFY BEFORE FILING] with a styled marker
    """
    lines = text.split('\n')
    out = []
    skip_header_block = True
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip the initial H1 and classification lines (already on cover page)
        if skip_header_block:
            if line.startswith('# ') or line.startswith('**Classification:**') or \
               line.startswith('**Compiled:**') or line.startswith('**24-Hour'):
                i += 1
                continue
            elif line.strip() == '---' and i < 15:
                i += 1
                continue
            elif line.startswith('## EXECUTIVE SUMMARY'):
                skip_header_block = False

        # Demote #### to ### (paragraph -> subsubsection looks better)
        if line.startswith('#### '):
            line = '### ' + line[5:]

        # Style [VERIFY BEFORE FILING] and [VERIFY PINPOINT] flags
        line = re.sub(
            r'\[VERIFY(?:[^\]]*)\]',
            r'\\textbf{\\textcolor{verifyAmber}{[VERIFY BEFORE FILING]}}',
            line
        )

        out.append(line)
        i += 1

    return '\n'.join(out)


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def generate_pdf(
    input_md: Path,
    output_pdf: Path,
    case_number: str = "26-16834-EJO",
    case_name_short: str = "In re Mell",
    memo_date: str = None,
) -> None:
    """
    Full pipeline: extract citations → build TOA → pre-process markdown → pandoc → PDF.
    """
    if memo_date is None:
        memo_date = date.today().strftime("%B %d, %Y")

    print(f"[gen_pdf] Reading: {input_md}")
    raw_text = input_md.read_text(encoding='utf-8')

    # Extract citations from ORIGINAL text (before Unicode normalization replaces § etc.)
    print("[gen_pdf] Extracting citations...")
    cases = extract_cases(raw_text)
    statutes = extract_statutes(raw_text)
    rules = extract_rules(raw_text)
    print(f"          Cases: {len(cases)}  |  Statutes: {len(statutes)}  |  Rules: {len(rules)}")

    # Build TOA LaTeX (uses raw citation strings; escape_latex handles special chars)
    toa_latex = build_toa_latex(cases, statutes, rules)

    # Normalize Unicode for pandoc/pdflatex compatibility
    text = normalize_unicode(raw_text)

    # Pre-process markdown layout
    processed_md = preprocess_markdown(text)

    # Write to temp directory so pandoc can find assets
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # Write pre-processed markdown
        md_tmp = tmp / "input.md"
        md_tmp.write_text(processed_md, encoding='utf-8')

        # Copy template to tmp dir (pandoc needs local path)
        tpl_tmp = tmp / "legal-memo.tex"
        shutil.copy(TEMPLATE, tpl_tmp)

        # Write TOA to a file that pandoc includes via variable
        toa_tmp = tmp / "toa.tex"
        toa_tmp.write_text(toa_latex, encoding='utf-8')

        # Build pandoc command
        cmd = [
            "pandoc",
            str(md_tmp),
            "--pdf-engine=pdflatex",
            "--template", str(tpl_tmp),
            "--standalone",
            "--toc",
            "--toc-depth=2",
            "--from", "markdown+pipe_tables+task_lists+fenced_code_blocks+raw_tex",
            "--variable", f"date={memo_date}",
            "--variable", f"case-number={case_number}",
            "--variable", f"case-name-short={case_name_short}",
            "--variable", f"toa=\\input{{{toa_tmp}}}",
            "--pdf-engine-opt", "-interaction=nonstopmode",
            "--pdf-engine-opt", f"-output-directory={tmpdir}",
            "--output", str(tmp / "output.pdf"),
        ]

        print("[gen_pdf] Running pandoc...")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=tmpdir,
        )

        if result.returncode != 0:
            print("[gen_pdf] ERROR — pandoc/pdflatex stderr:")
            # Print last 80 lines of stderr (pdflatex is verbose)
            stderr_lines = result.stderr.strip().split('\n')
            for line in stderr_lines[-80:]:
                print("  ", line)
            # Try to find and show the log file
            log_files = list(tmp.glob("*.log"))
            if log_files:
                log_text = log_files[0].read_text(errors='replace')
                # Show only error lines
                error_lines = [l for l in log_text.split('\n') if l.startswith('!') or 'Error' in l]
                if error_lines:
                    print("[gen_pdf] LaTeX errors:")
                    for l in error_lines[:20]:
                        print("  ", l)
            sys.exit(1)

        # Copy output PDF
        out_tmp = tmp / "output.pdf"
        if not out_tmp.exists():
            print("[gen_pdf] ERROR — PDF not produced. Check LaTeX log above.")
            sys.exit(1)

        shutil.copy(out_tmp, output_pdf)
        size_kb = output_pdf.stat().st_size // 1024
        print(f"[gen_pdf] SUCCESS → {output_pdf}  ({size_kb} KB)")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_md = Path(sys.argv[1]).resolve()
    if not input_md.exists():
        print(f"[gen_pdf] ERROR: Input file not found: {input_md}")
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_pdf = Path(sys.argv[2]).resolve()
    else:
        output_pdf = input_md.with_suffix('.pdf')

    generate_pdf(input_md, output_pdf)


if __name__ == "__main__":
    main()
