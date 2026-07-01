# Internal Legal Briefing — PDF Generation Skill

When the user asks for an "Internal Briefing" or "Internal Legal Research Memorandum" PDF for any legal matter, follow this exact workflow to produce a PDF that matches the established format.

## Format standards (non-negotiable)

Every internal briefing PDF must have:

- **Cover page** (full first page, no header/footer):
  - Dark red (#A50000) block: "ATTORNEY WORK PRODUCT" (14.5pt Arial bold) / "PRIVILEGED AND CONFIDENTIAL" (13pt Arial bold) / "DO NOT DISTRIBUTE WITHOUT COUNSEL AUTHORIZATION" (10pt Times New Roman)
  - Grey separator bar (6pt tall, #828282, 5in wide)
  - Large bold title: "INTERNAL LEGAL RESEARCH MEMORANDUM" (22pt Arial, centered, 2 lines)
  - Thin grey rule (0.5pt, #828282)
  - Case info table with bold Arial labels and Times New Roman values — rows: IN RE (italic case name), Case No., Court, Hearing (if applicable), Before (judge), Subject, Date, Distribution

- **Running header** (every body page): Dark red (#A50000) Arial bold 8pt — "ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL" left, grey case number right, hairline rule below

- **Running footer** (every body page): Times New Roman 8pt #505050 — italic "In re [Name]" left, page number right, hairline rule above

- **Body typography**: Times New Roman 12pt justified, 1.45 line-height
  - H2: Arial bold uppercase with bottom border rule — used for major section headings
  - H3: Arial bold — used for subsections
  - `*italic*` in markdown → italic in PDF (use for all case citations, e.g., *In re Tamecki*, 229 F.3d 205)
  - Blockquotes: indented, italic, left border bar
  - Tables: Arial bold headers, light grey background

## Workflow

### Step 1 — Produce the markdown

Write the full briefing in markdown. Structure:

```
# [TITLE — usually omit, it goes on cover]

Case info lines (these are consumed by the cover builder — put them here as a reference block, then a `---` separator)

---

## EXECUTIVE SUMMARY

[body...]

## I. FACTUAL BACKGROUND
...
```

The `---` horizontal rule after any opening metadata separates cover content (discarded) from body content (rendered). The cover is built programmatically from the `--config` JSON, not from the markdown text itself.

For **citations**: always wrap in `*asterisks*` in markdown so they render italic in the PDF. Use full citation format:
- Case: *In re Tamecki*, 229 F.3d 205, 207 (3d Cir. 2000)
- Statute: 11 U.S.C. § 707(a)
- Document: Doc. 8 (filed June 23, 2026)

### Step 2 — Build the case config JSON

Create a config file with case metadata:

```json
{
  "case_name": "[debtor/party name — rendered italic on cover]",
  "case_number": "[docket number]",
  "court": "[full court name — use \\n for line breaks]",
  "hearing_date": "[date of upcoming hearing, if any]",
  "judge": "[Hon. First Last, Title]",
  "subject": "[brief description of what this memo covers]",
  "date": "[today's date]",
  "distribution": "Legal Team — INTERNAL USE ONLY",
  "title": "INTERNAL LEGAL\nRESEARCH MEMORANDUM"
}
```

### Step 3 — Run the generator

The generator script is at `case-files/scripts/generate-briefing-pdf.py` in this repository.

```bash
python3 case-files/scripts/generate-briefing-pdf.py \
  --md path/to/BRIEFING.md \
  --config path/to/config.json \
  --out path/to/OUTPUT.pdf
```

Requires:
- `pandoc` (install: `apt-get install -y pandoc`)
- `playwright` Python package (install: `pip install playwright`)
- Chromium at `/opt/pw-browsers/chromium-*/chrome-linux/chrome` (pre-installed in Claude Code cloud)

### Step 4 — Deliver

Send the PDF to the user via `SendUserFile` so it appears as a download button in the conversation.

## Accuracy standards for legal content

- **Never characterize advocacy as established fact.** If an attorney made a statement at a hearing, frame it as their position: "Counsel argued that..." not "...was established that..."
- **Cite the actual record.** Every factual claim must be traceable to a docket entry, transcript, exhibit, or filed document. Use parenthetical citations: *(Doc. 8, p. 3)*.
- **Court holdings are not advocacy.** If a court ruled on something, state what it held — even if unfavorable to the client. Accuracy in an internal briefing protects counsel from relying on incorrect summaries.
- **Verify statute numbers.** Before citing any code section, confirm the section exists and says what you say it says.

## Saving to the repository

After generating the PDF:
1. Commit the markdown source to the relevant case folder (e.g., `case-files/in-re-mell/research-output/`)
2. Commit the PDF alongside it
3. Do **not** commit the intermediate `.html` file — it is a build artifact
