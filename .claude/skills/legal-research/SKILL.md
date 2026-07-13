---
name: legal-research
description: Full-stack legal research workflow across practice areas — bankruptcy, criminal defense, civil rights (§1983/Bivens/prison litigation), FOIA/public records, and family law. Covers parallel subagent research architecture, source prioritization, a flexible final-memo structure, citation verification protocol, pre-filing quality checks, and automatic PDF generation (cover page + TOC + Table of Authorities + formatted body via pandoc/pdflatex) with a fully data-driven cover page for any matter type. Practice-area deep references live in references/*.md and are loaded on demand.
---

# Legal Research Skill

Use this skill whenever tasked with producing comprehensive legal research and a court-
or agency-ready work product: an opposition brief, a FOIA request and appeal, a suppression
motion, a civil rights complaint or opposition, a custody/support motion, or similar. The
workflow runs several independent research tracks in parallel through subagents,
synthesizes them into a structured memorandum, and (optionally) renders a professional PDF.

This file is the **generic orchestration layer** — source prioritization, research
architecture, citation protocols, writing craft, quality checklists, and the PDF pipeline.
It applies regardless of practice area. Practice-area-specific legal standards, checklists,
and worked citations live in `references/*.md` and should be loaded only for the practice
area(s) actually in play, to keep this file lean.

## Practice Areas Covered

| Practice area | Reference file | What's inside |
|---|---|---|
| Bankruptcy | `references/bankruptcy.md` | § 707(a) dismissal, § 523(a)(6) nondischargeability, mandatory abstention, automatic stay/§ 362(k), Third Circuit quick-reference table |
| Criminal defense | `references/criminal.md` | 4th/5th/6th Amendment suppression standards, discovery (Brady/Giglio/Jencks), sentencing (§ 3553(a), Booker) |
| Civil rights | `references/civil-rights.md` | § 1983 elements, Bivens viability post-Egbert, qualified immunity, Monell, Eighth Amendment conditions of confinement, PLRA exhaustion |
| FOIA / public records | `references/foia.md` | Fee categories, fee waiver & expedited-processing standards, exemptions (b)(1)–(b)(9), administrative appeal, litigation |
| Family law | `references/family-law.md` | UCCJEA/UIFSA jurisdiction, custody best-interests factors, support, property division — heavily state-dependent |

**Adding a new practice area**: create `references/<area>.md` following the same shape as
the existing files (statutory/case framework → checklists/templates → burden allocation →
key cases marked [VERIFY BEFORE FILING] → a suggested track breakdown table at the bottom),
then add a row to the table above. Don't inline practice-specific standards into this file.

---

## Step 0: Identify the Matter Type and the Deliverable

Before launching research, pin down what's actually being produced — the six-part
architecture below adapts to it:

| Matter type | Typical external deliverable | Typical internal work product |
|---|---|---|
| Motion opposition (bankruptcy, criminal, civil) | Opposition brief filed with the court | Research memo → brief |
| FOIA request | Request letter (and later, an administrative appeal) | Strategy memo with fee/expedite showing |
| Civil rights suit | Complaint, or opposition to a dispositive motion | Element-by-element research memo |
| Custody/support | Motion, certification, or proposed order | Factual + standard-of-law memo |

If unclear, ask the user what the deliverable is before architecting the research tracks —
a FOIA request letter and a six-track bankruptcy-style memo are very different amounts of
work, and over-building wastes the user's time.

---

## The Master Architecture: N-Track Parallel Research

The core insight: a single motion, request, or filing rarely turns on one issue. Break
research into **independent tracks** and run them simultaneously through subagents. Each
subagent has a focused scope, writes its own output file, and does not depend on the others.

**Track count scales to matter complexity** — not a fixed six. A FOIA request letter might
need only two or three tracks (background/scoping, drafting, later the appeal). A
multi-issue bankruptcy opposition or civil rights suit might need five or six. Each
practice-area reference file ends with a "Suggested Track Breakdown" table as a starting
point — adjust it to the actual matter.

Plus, as needed: one document-analysis subagent per major opposing/source document, and one
synthesis pass (run in the main context, not a subagent) that reads all track outputs and
produces the final memorandum.

### When to Add More Subagents

Spawn an additional subagent whenever:
- A source document exceeds ~50K characters (a brief, an appellate opinion, a large
  production)
- A source requires authentication that would conflict with another subagent's session
- A new bombshell finding (e.g., an undisclosed settlement, a contradicted timeline)
  warrants isolated deep-dive analysis

---

## Research Source Priority Stack

Run sources in this order; stop at the first reliable result per proposition.

### Tier 1 — Authoritative Free Sources
1. **CourtListener** (`courtlistener.com/opinion/`) — full text, citation counts, subsequent
   history
2. **Google Scholar** (`scholar.google.com/scholar_case?q=...`) — fast federal circuit search
3. **Justia US Law** (`law.justia.com/cases/federal/`) — reliable for SCOTUS and circuits

### Tier 2 — Official Sources (Slower, More Reliable)
4. **GovInfo.gov** — regulations, statutory text, Federal Register
5. **Congress.gov** — statute text and amendments
6. **eCFR.gov** — current Code of Federal Regulations text (agency regs — essential for FOIA
   and any administrative-law-adjacent matter)
7. **State legislature/statute portals** — for family law and any state-law claim; every
   state's official code site is the only citable source for its current text

### Tier 3 — Verification Required
8. **Secondary sources** (law review articles, treatises) — use for leads only, VERIFY
   underlying primary sources
9. **Wikipedia legal pages** — structure only, never cite

### Tier 4 — Subscription (Use When Provided)
10. **PACER** — docket entries, non-precedential opinions, local rules
11. **Westlaw/Lexis** — headnote searching, KeyCite, negative treatment

### Practice-Area Additions
- **FOIA**: USASpending.gov, SAM.gov/FPDS, and the target agency's FOIA reading room for
  background/scoping before drafting the request (see `references/foia.md`)
- **Family law**: the specific state's official statute portal and self-help/court-forms
  site are often the most current source for local procedural requirements

**403/404 Handling:** When free databases block access, use secondary sources to
reconstruct the proposition, flag every such citation with `[VERIFY BEFORE FILING]`, and
collect them in the verification checklist section of the final memo.

---

## Case Analysis Protocol

For each cited case, extract and record:

```
Case Name: [full name]
Citation: [reporter, court, year]
Binding Status: [BINDING / PERSUASIVE — specify why]
Holding (verbatim key quote): "..."
Source: [URL or PACER pull]
Verification Status: [CONFIRMED / VERIFY BEFORE FILING]
How opponent uses it: [brief description]
How we distinguish/counter: [brief description]
```

Always flag when the opponent (or the agency, in a FOIA denial) has mischaracterized a
case. Common patterns:
- Citing a case decided on a materially different procedural posture as if directly on
  point (e.g., an involuntary-petition case for debtor-bad-faith analysis; an interlocutory
  order treated as final for collateral estoppel)
- Citing non-precedential opinions as binding authority
- Citing a different circuit's standard without acknowledging a circuit split
- Citing a case for a proposition that is dicta, not holding
- (FOIA-specific) Invoking an exemption case for a broader withholding than that case
  actually supports, or skipping the foreseeable-harm showing entirely

---

## Statutory & Regulatory Verification Protocol

Before citing any statute or regulation:
1. Confirm the section exists in the official source — U.S. Code (`uscode.house.gov`) for
   federal statutes, `eCFR.gov` for current federal regulations, the state's official code
   site for state statutes
2. Confirm the section number matches the title/chapter scheme actually in force
3. Quote the verbatim text — never paraphrase a statute or regulation in an argument section

**Golden rule:** When an opponent (or an agency) cites a nonexistent or mis-numbered
provision (e.g., "28 U.S.C. § 1134(c)(2)" when § 1134 does not exist), document it
prominently. It goes first in the argument on that issue, before addressing the merits —
it signals the rest of the analysis wasn't carefully checked either.

---

## Final Memorandum Structure

The internal research memo (the input to `gen_pdf.py`) follows this flexible structure —
use every part that applies to the matter, drop what doesn't (a FOIA memo has no "judicial
profile" or "counterclaims" section; a custody memo has no "abstention" section):

```
## EXECUTIVE SUMMARY: [N] WINNING ARGUMENTS / KEY FINDINGS
  — numbered list, strongest to weakest
  — one short paragraph per argument
  — BOMBSHELL disclosures identified separately

## PART I: [FORUM] PROFILE  (motions/litigation only — judge/agency track record)
  — career trajectory or agency's public FOIA/enforcement track record
  — available rulings/precedent (PACER search, prior agency responses, etc.)
  — strategic implications table
  — immediate action items

## PART II–[N]: [ISSUE] ANALYSIS
  — Controlling Standard (with verbatim quote)
  — Affirmative evidence of client's position
  — Burden framework
  — Opposing authority distinguished (case-by-case, or exemption-by-exemption for FOIA)
  — Opponent's/agency's weakest arguments identified

## PART [N+1]: COUNTERCLAIMS / AFFIRMATIVE RELIEF  (if applicable)
  — Statutory violation analysis (e.g., § 362(k), fee-shifting under FOIA)
  — Sanctions/fees grounds

## PART [N+2]: FACTUAL RECORD CORRECTIONS
  — Date discrepancies in the opposing papers
  — Citation errors in the opposing papers
  — Mischaracterizations of the record below

## PART [N+3]: STRATEGIC SEQUENCING
  — Opening argument order / request structure
  — Which arguments to lead vs. hold in reserve
  — Approach tailored to the forum profile from Part I

## PART [N+4]: VERIFICATION CHECKLIST
  — Every VERIFY flag from all tracks, organized by: statute | case law | factual | procedural

## APPENDIX A: CONSOLIDATED AUTHORITY TABLE
  — Full case/statute list with binding/persuasive designation, organized by track

## APPENDIX B: FILE INDEX
  — Every output file with a one-line description
  — Every external document accessed and its key finding
```

---

## Writing Persuasively

### Argument Ordering Principle
Lead with the argument that is clearest and most procedurally prior. Typically:

1. **Procedural/threshold defects** (nonexistent statute, wrong proceeding type, missing
   exhaustion) — first
2. **Standard of law not met** (conduct/showing does not reach the required threshold) —
   second
3. **Factual record refutation** (the record is mischaracterized) — third
4. **Counterclaim/affirmative relief** — last, unless timing requires it first (e.g., a
   statute-of-limitations-sensitive claim must be preserved even if led with something else)

### Verbatim Quote Rule
Every controlling standard goes in verbatim with a pinpoint citation before any paraphrase.
A reader who argued these issues personally will notice inexact paraphrasing immediately.

### Distinguishing Cases
Structure each distinguishing argument as a numbered list:
```
[Opponent's case] is distinguishable on [N] independent grounds:
1. [Factual distinction — most concrete first]
2. [Legal distinction — different holding/issue]
3. [Procedural distinction — different posture]
...
```
Multiple independent grounds signal the distinction isn't strained.

### Burden Allocation
Always state explicitly who bears the burden and at what standard — check the relevant
practice-area reference file for the specific allocation (e.g., FOIA puts the burden on the
agency to sustain any withholding; § 1983 puts the initial burden on the plaintiff; PLRA
exhaustion is the defendant's burden to prove).

---

## Collateral Estoppel / Issue Preclusion Analysis Template

Cross-cutting tool — use whenever a party claims a prior proceeding already decided an
issue (this comes up in bankruptcy nondischargeability, criminal-to-civil preclusion,
and FOIA "prior litigation already settled this" arguments alike):

```
CE Element 1: Was the issue IDENTICAL?
  → State exact issue in prior proceeding
  → State exact issue now
  → Are they legally identical? Y/N + why

CE Element 2: Was the issue ACTUALLY LITIGATED?
  → Default/sanction entry? → generally NO (ministerial; no evidentiary hearing)
  → Interlocutory order? → generally NO (not final)
  → Privilege invocation (e.g., Fifth Amendment)? → generally NO (constitutionally
     protected; not bad-faith obstruction absent willful obstruction with a full and fair
     opportunity to litigate — see the bankruptcy reference for the Docteroff line)

CE Element 3: Was the issue ESSENTIAL to the judgment?
  → Could the court have reached the same result without deciding this issue?

CE Element 4: Was the party against whom CE is asserted a PARTY or in privity?

Conclusion: CE [APPLIES / DOES NOT APPLY] because element(s) [X] fail(s).
```

---

## Settlement / Release Analysis

Whenever a prior settlement or release exists between the parties:

1. Pull the full text of the release (verify scope language — "full release," "any current
   or future claims," carve-outs)
2. Map every claim in the current matter to the release scope
3. Identify any claim that falls within a broad "any current or future claims" clause
4. Analyze: res judicata / claim preclusion bar
5. Analyze: judicial estoppel (*New Hampshire v. Maine*, 532 U.S. 742 (2001) — three
   elements: clearly inconsistent positions, prior court accepted the earlier position,
   unfair advantage/detriment)
6. Analyze: candor to the tribunal — did opposing counsel disclose the release to the
   court/agency? (Check the jurisdiction's RPC 3.3 analog)
7. If undisclosed: flag separately as a candor violation AND an independent sanctions basis

---

## Pre-Filing / Pre-Submission Quality Checklist

Before anything is signed and filed or sent:

### Statutory & Regulatory Citations
- [ ] Every federal statute verified in the official U.S. Code
- [ ] Every federal regulation verified in the current eCFR
- [ ] Every state statute verified against the state's official code (watch for section/
      title transpositions)
- [ ] Every cited subsection exists and says what the filing says it says

### Case Law
- [ ] Every `[VERIFY BEFORE FILING]` flag resolved via Westlaw/PACER/official source
- [ ] Every non-precedential opinion labeled as such, not cited as binding authority
- [ ] Every "BINDING" designation confirmed (same jurisdiction, precedential status)
- [ ] Every circuit split (or state-court split) acknowledged where relevant
- [ ] Subsequent history checked (no reversed, overruled, or superseded authority)

### Factual Record
- [ ] Every date cross-checked against the docket/administrative record
- [ ] Every quote from an opinion, order, or agency letter pulled verbatim, no paraphrase
      in an argument section
- [ ] Any discrepancy in the opposing side's papers documented with an exhibit reference
- [ ] Client declarations/certifications reviewed for internal consistency

### Opposing Party's / Agency's Papers
- [ ] Every case the other side cites has actually been read (not just abstracted)
- [ ] Every statutory/regulatory citation by the other side confirmed to exist
- [ ] Any error documented and included in the introduction/lead argument
- [ ] Any procedural distinction preserved where required (e.g., an adversary proceeding
      vs. a motion; an administrative appeal vs. a lawsuit)

### Ethical
- [ ] Any settlement/release known to both parties disclosed where required
- [ ] No misrepresentation of the procedural history below
- [ ] No citation to a "judgment" or "determination" without disclosing its interlocutory
      or non-final character
- [ ] Candor review: is any material fact omitted that creates a misleading impression?

Also run the practice-area-specific checklist in the relevant `references/*.md` file (e.g.,
the FOIA requester-side drafting checklist, the § 523(a)(6) element checklist).

---

## Subagent Prompt Template

When launching a research subagent, include:

```
**Matter:** [Matter name/number, forum/agency]
**Deadline:** [Date, if any]
**Your track:** [Track name — e.g., "FOIA Exemption (b)(4) Analysis"]
**Controlling jurisdiction:** [e.g., D.C. Circuit / Third Circuit / [state]]
**Issue to research:** [Specific legal question]
**Opponent's/agency's position (verbatim or paraphrase):** [What they say]
**Our position:** [What we argue]
**Output file:** [Absolute path for output]
**Key cases/sources to start with:** [Any already identified]
**Sources to use:** CourtListener, Google Scholar, Justia (in that order), plus any
  practice-area-specific sources from the reference file
**Mark all unconfirmed citations [VERIFY BEFORE FILING]**
**Return:** Full memo with verbatim quotes, pinpoint citations, and binding/persuasive
  designation
```

---

## File Organization

```
matter-files/
  [matter-name]/
    README.md                    ← matter summary + folder map for subagents
    research-output/
      part1-[track].md           ← per-track subagent outputs
      part2-[track].md
      ...
      [doc-name]-analysis.md     ← per-document analysis subagent outputs
      FINAL-MEMO.md              ← master synthesis (primary internal deliverable)
      FINAL-MEMO.matter.json     ← cover-page data for gen_pdf.py (see PDF section)
      FINAL-MEMO.pdf             ← rendered deliverable
```

---

## Timing Protocol (Example: 24-Hour Deadline)

Scale hours to the actual deadline and track count — this is a worked example from a
same-day bankruptcy hearing, not a fixed schedule:

| Hour | Action |
|------|--------|
| 0    | Read all documents (parallel source pulls) |
| 0    | Launch all research tracks simultaneously |
| 0    | Main context: review existing matter documents while tracks run |
| 2-4  | Track outputs arrive; read each; flag anomalies for follow-up |
| 4    | Launch document-analysis subagents for major opposing/source filings |
| 6    | All track outputs confirmed written; begin synthesis |
| 8    | FINAL-MEMO.md written; verification checklist extracted |
| 10   | Commit and push all files |
| 10+  | Begin drafting the actual filing/letter from FINAL-MEMO |
| 20   | Pre-filing quality checklist; final-source verification of all [VERIFY] flags |
| 23   | Final review; no new research after this point |
| 24   | File / send |

For a small matter (e.g., a single FOIA request letter), collapse this to a few hours with
2-3 tracks; don't run the full ceremony for a small deliverable.

---

## PDF Output — Final Deliverable Step

After `FINAL-MEMO.md` is complete, generate a professional PDF. The cover page, banner
text, and footer disclaimer are **fully data-driven** — nothing case-specific is hardcoded
in the LaTeX template, so the same pipeline serves any practice area.

### Tools

```
.claude/skills/legal-research/gen_pdf.py               — main script
.claude/skills/legal-research/templates/legal-memo.tex — LaTeX template (generic)
```

### Dependencies (Linux/apt)

```bash
apt-get install -y --fix-missing pandoc texlive-latex-recommended \
  texlive-fonts-recommended texlive-latex-extra
```

### Usage

Create a `matter.json` file (see keys below, and worked examples in each
`references/*.md` file) alongside the memo, named `<memo-stem>.matter.json`, and it's
picked up automatically:

```bash
python3 .claude/skills/legal-research/gen_pdf.py \
  matter-files/[matter]/research-output/FINAL-MEMO.md \
  matter-files/[matter]/research-output/FINAL-MEMO.pdf
```

Or pass the matter file explicitly, or call `generate_pdf()` directly from Python with a
`matter` dict — see the module docstring in `gen_pdf.py` for the full key list.

### `matter.json` Keys

| Key | Purpose | Omit to... |
|---|---|---|
| `doc_title_line1` / `doc_title_line2` | Big cover-page title (2 lines) | fall back to "LEGAL / RESEARCH MEMORANDUM" |
| `banner_line1` / `banner_line2` / `banner_notice` | Red confidentiality banner on the cover | fall back to "ATTORNEY WORK PRODUCT / PRIVILEGED AND CONFIDENTIAL" |
| `header_banner` | Single-line banner repeated on every page header | fall back to a combined version of the above |
| `matter_label` / `matter_name` | e.g. "IN RE:" / "S. Bradley Mell" or "REQUESTER:" / "Erik Khan" | — required for a real caption |
| `forum_label` / `forum` | e.g. "Court:" / court name, or "Agency:" / agency name — supports `\n` for a 2-line value | — |
| `hearing_label` / `hearing` | e.g. "Hearing:" / date | omit the row entirely (leave both empty) |
| `presiding_label` / `presiding` | e.g. "Before:" / judge name | omit the row entirely (leave both empty) |
| `subject_label` / `subject` | Subject-matter line(s), supports `\n` | — |
| `distribution_label` / `distribution` | Distribution restriction line | fall back to "Legal Team — INTERNAL USE ONLY" |
| `footer_disclaimer` | Cover-page italic disclaimer paragraph | fall back to a generic work-product notice |
| `case_number` / `case_name_short` | Running header/footer on every page | fall back to placeholders |
| `pdf_title` / `pdf_author` / `pdf_subject` / `pdf_keywords` | PDF metadata | fall back to generic values |

Rows with an empty label or value (e.g., `hearing`/`presiding` on a FOIA memo, which has no
judge or hearing date) are automatically omitted from the cover page — no template editing
required.

### What the Pipeline Does

1. **Reads** FINAL-MEMO.md and the matter dict (JSON file or programmatic argument)
2. **Extracts citations** from the original text (before Unicode normalization):
   - Cases: `In re Name, Vol Rep Page (Court Year)` and `X v. Y, citation` patterns
   - Statutes/regulations: `11 U.S.C.`, `28 U.S.C.`, `5 U.S.C.`, `C.F.R.`, `N.J.S.A.`
     patterns
   - Rules: `Fed. R. Bankr./Civ./Crim./Evid./App. P.`, `N.J. Ct. R.`, `N.J. RPC` patterns
3. **Normalizes Unicode** → replaces `→`, `≠`, `§`, `—`, curly quotes, etc. with
   pdflatex-safe equivalents (math symbols use pandoc `$...$` delimiters)
4. **Pre-processes markdown** → strips the duplicate H1/classification header (already on
   the cover page), promotes H4 to H3, highlights `[VERIFY]` flags in amber
5. **Builds the Table of Authorities** and the **cover-page caption** as LaTeX fragments
   (both escaped and injected via `\input{}`, the same mechanism)
6. **Runs pandoc** with the template → pdflatex → PDF

### PDF Structure

| Section | Page numbering |
|---------|---------------|
| Cover page | Unnumbered |
| Table of Contents | Roman (i, ii, …) |
| Table of Authorities | Roman (continued) |
| Memo body | Arabic (1, 2, …) |

### Formatting Decisions

- **Font:** Times New Roman (mathptmx) — standard for legal documents
- **Margins:** 1 inch all sides; top/bottom 1.2 inch for header/footer room
- **Line spacing:** 1.25x — readable without being double-spaced
- **Blockquotes:** Left rule bar + italic — visual distinction for verbatim quotes
- **Section headers:** Uppercase, rule line under — standard internal memo style
- **VERIFY flags:** Amber/orange text with bold `[VERIFY BEFORE FILING]` label
- All confidentiality/privilege framing is controlled entirely by the `matter.json` banner
  fields — set them to something other than "ATTORNEY WORK PRODUCT" (e.g., "DRAFT — FOR
  CLIENT REVIEW") for deliverables headed outside privileged internal use, like a FOIA
  request letter draft.

### Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `\tightlist undefined` | Pandoc macro not in template | Confirm `\providecommand{\tightlist}{...}` is present in the template |
| `Unicode character X not set up` | Raw Unicode reaching pdflatex | Add to `UNICODE_SUBSTITUTIONS` in `gen_pdf.py` |
| `Missing $ inserted` near `\rightarrow` | Used `\(` in markdown; pandoc treats it as an escaped paren | Use pandoc math `$\rightarrow$` instead |
| Template `unexpected "$"` | Dollar sign in a LaTeX comment or command | In pandoc templates, `$` outside `$var$` syntax is invalid; escape or use `\(\)` |
| TOA has 0 statutes | Normalization ran before extraction | Always extract from raw_text before normalizing (already enforced in `gen_pdf.py`) |
| Long table cells overflow the margin | Wide pipe-table columns | Use narrower column labels; break long content across rows |
| Cover-page row shows up empty/misaligned | A label was set but the paired value left empty (or vice versa) | Both label and value must be non-empty for a row to render — set both or leave both blank |

### Adding New Unicode Characters

Edit `UNICODE_SUBSTITUTIONS` in `gen_pdf.py`. Rules:
- Math/comparison symbols: use `$\latex_name$` (pandoc math syntax)
- Typography: use plain text equivalents where possible (`---` for em dash)
- LaTeX text commands (`\S{}`, `\P{}`): only for symbols with dedicated commands
- Never use `\(` or `\)` for inline math in substitutions (pandoc treats `\(` as an escaped
  paren)
