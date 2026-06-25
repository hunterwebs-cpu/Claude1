---
name: legal-research
description: Full-stack legal research workflow for bankruptcy opposition papers. Covers parallel subagent architecture, source prioritization, six-part memo structure, synthesis into a final memorandum, citation verification protocol, pre-filing quality checks, and automatic PDF generation (cover page + TOC + Table of Authorities + formatted body via pandoc/pdflatex). Demonstrated in In re S. Bradley Mell, 26-16834-EJO (Bankr. D.N.J. 2026).
---

# Legal Research Skill — Bankruptcy Opposition Papers

Use this skill whenever tasked with producing comprehensive legal research for a bankruptcy
motion response. The workflow runs six parallel research tracks through dedicated subagents,
synthesizes them into a structured final memorandum, and delivers a court-ready opposition
package. Demonstrated end-to-end in In re Mell (2026), producing research on § 707(a),
§ 523(a)(6), mandatory abstention, stay relief, automatic stay violations, and factual
record reconstruction under a 24-hour hearing deadline.

---

## The Master Architecture: Six-Track Parallel Research

The core insight: a single opponent motion rarely turns on one issue. Break research into
**six independent tracks** and run them simultaneously through subagents. Each subagent
has a focused scope, writes its own output file, and does not depend on the others.

### Track Assignments

| Track | Scope | Output File |
|-------|-------|-------------|
| SA1 | Judicial profile — judge's career, prior rulings, PACER orders | `part1-judge-ohagan.md` |
| SA2 | Primary § 707(a) / dismissal standard (controlling circuit cases + factual rebuttal) | `part2-707a.md` |
| SA3 | § 523(a)(6) / nondischargeability + collateral estoppel | `part3-523a6.md` |
| SA4 | Abstention (mandatory and permissive) + jurisdiction | `part4-abstention.md` |
| SA5 | Automatic stay — relief factors + § 362(k) counterclaim | `part5-stay.md` |
| SA6 | Factual record reconstruction — state court errors, transfer analysis, sanctions | `part6-factual.md` |

Plus two document-analysis subagents (one per major opposing document) and one synthesis
agent (main context) that reads all six parts and produces FINAL-MEMO.md.

### When to Add More Subagents

Spawn an additional subagent whenever:
- A source document exceeds ~50K characters (MTD brief, appellate opinion)
- A Drive document requires authentication that conflicts with another subagent's session
- A new bombshell finding (e.g., the settlement) warrants isolated deep-dive analysis

---

## Research Source Priority Stack

Run sources in this order; stop at the first reliable result per proposition.

### Tier 1 — Authoritative Free Sources
1. **CourtListener** (`courtlistener.com/opinion/`) — full text, citation counts, subsequent history
2. **Google Scholar** (`scholar.google.com/scholar_case?q=...`) — fast federal circuit search
3. **Justia US Law** (`law.justia.com/cases/federal/`) — reliable for SCOTUS and circuits

### Tier 2 — Official Sources (Slower, More Reliable)
4. **GovInfo.gov** — regulations, statutory text, Federal Register
5. **Congress.gov** — statute text and amendments

### Tier 3 — Verification Required
6. **Secondary sources** (law review articles, treatises) — use for leads only, VERIFY underlying
7. **Wikipedia legal pages** — structure only, never cite

### Tier 4 — Subscription (Use When Provided)
8. **PACER** — docket entries, non-precedential opinions, local rules
9. **Westlaw/Lexis** — headnote searching, KeyCite, negative treatment

**403/404 Handling:** When free databases block access, use secondary sources to reconstruct
the proposition, flag every such citation with `[VERIFY BEFORE FILING]`, and collect them
in the verification checklist section of FINAL-MEMO.

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

Always flag when the opponent has mischaracterized a case. Common patterns:
- Citing an INVOLUNTARY petition case for debtor-bad-faith analysis (see Murray)
- Citing non-precedential opinions as binding authority (see IOP 5.7 in Third Circuit)
- Citing a different circuit's standard without acknowledging circuit split
- Citing a case for a proposition that is dicta, not holding

---

## Statutory Verification Protocol

Before citing any statute:
1. Confirm the section exists in the official U.S. Code (`uscode.house.gov`)
2. Confirm the section number matches the chapter and title scheme
3. Quote the verbatim text — never paraphrase a statute in an argument section

**Golden rule:** When an opponent cites a nonexistent statute (e.g., "28 U.S.C. § 1134(c)(2)"
when § 1134 does not exist), document it prominently. It goes first in the opposition's
argument on that issue, before addressing the merits.

---

## FINAL-MEMO.md Structure

The synthesis memo follows this ten-part structure:

```
## EXECUTIVE SUMMARY: [N] WINNING ARGUMENTS
  — numbered list, strongest to weakest
  — one short paragraph per argument
  — BOMBSHELL disclosures identified separately

## PART I: JUDICIAL PROFILE
  — career trajectory
  — available rulings (PACER search: suffix "-[initials]")
  — strategic implications table
  — immediate action items

## PART II–[N]: ARGUMENT [X] — [ISSUE] FAILS
  — Controlling Standard (with verbatim quote)
  — Affirmative evidence of client's position
  — Burden framework
  — Opposing cases distinguished (case-by-case)
  — Opponent's weakest arguments identified

## PART [N+1]: COUNTERCLAIMS / AFFIRMATIVE RELIEF
  — § 362(k) violation analysis (if applicable)
  — Sanctions grounds (Rule 9011 / § 1927 / RPC)

## PART [N+2]: FACTUAL RECORD CORRECTIONS
  — Date discrepancies in opponent's papers
  — Citation errors in opponent's papers
  — Mischaracterizations of record below

## PART [N+3]: STRATEGIC SEQUENCING
  — Opening argument order
  — Which arguments to lead vs. hold in reserve
  — Oral argument approach by judge profile

## PART [N+4]: VERIFICATION CHECKLIST
  — Every VERIFY flag from all six parts
  — Organized by: statute | case law | factual | procedural

## APPENDIX A: CONSOLIDATED AUTHORITY TABLE
  — Full case list with binding/persuasive designation
  — Organized by argument track

## APPENDIX B: FILE INDEX
  — Every output file with one-line description
  — Every Drive document accessed and its key finding
```

---

## Writing the Opposition

### Argument Ordering Principle
Lead with the argument that is clearest and most procedurally prior. In bankruptcy
opposition, typically:

1. **Procedural/threshold defects** (nonexistent statute, wrong proceeding type) — first
2. **Standard of law not met** (debtor's conduct does not reach the threshold) — second
3. **Factual record refutation** (opponent mischaracterizes what actually happened) — third
4. **Counterclaim/affirmative relief** (opponent violated the stay, deserves sanctions) — last
   unless timing requires it first (e.g., § 362(k) willfulness must be preserved)

### Verbatim Quote Rule
Every controlling standard goes in verbatim with a pinpoint citation before any paraphrase.
Judges who argued these motions personally (like a former USAO bankruptcy counsel) will
notice inexact paraphrasing immediately.

### Distinguishing Cases
Structure each distinguishing argument as a numbered list:
```
[Opponent's case] is distinguishable on [N] independent grounds:
1. [Factual distinction — most concrete first]
2. [Legal distinction — different holding/issue]
3. [Procedural distinction — different posture]
...
```
This signals to the court that the distinction is not strained — multiple independent
bases each independently suffice.

### Burden Allocation
Always state explicitly who bears the burden and at what standard. In bankruptcy:
- § 707(a) dismissal: movant bears burden; debtor rebuts; burden shifts back under Tamecki
- § 523(a)(6): creditor-plaintiff bears burden in adversary proceeding (preponderance, Grogan)
- Stay relief: movant shows cause (§ 362(d)(1)); debtor shows no equity/necessity (§ 362(d)(2))
- § 362(k): debtor-plaintiff must prove three elements; good faith not a defense

---

## Collateral Estoppel Analysis Template

For any case where the opponent claims a prior judgment establishes an element:

```
CE Element 1: Was the issue IDENTICAL?
  → State exact issue in prior proceeding
  → State exact issue now
  → Are they legally identical? Y/N + why

CE Element 2: Was the issue ACTUALLY LITIGATED?
  → Default/sanction entry? → NO (In re Azeglio, 422 B.R. 490 (Bankr. D.N.J. 2010))
  → Discovery sanction under R. 4:23-5(a)(2)? → NO (ministerial; no evidentiary hearing)
  → Interlocutory order? → NO (not final)
  → Fifth Amendment invocation? → NO (constitutionally protected; not bad-faith obstruction
     per Docteroff, 133 F.3d 210 (3d Cir. 1997) — Docteroff exception requires WILLFUL
     OBSTRUCTION with FULL AND FAIR OPPORTUNITY, not mere invocation of privilege)

CE Element 3: Was the issue ESSENTIAL to the judgment?
  → Could the court have reached the same result without deciding this issue?

CE Element 4: Was the party against whom CE is asserted a PARTY or in privity?

Conclusion: CE [APPLIES / DOES NOT APPLY] because element(s) [X] fail(s).
```

---

## § 523(a)(6) Specific Checklist

Under Kawaauhau v. Geiger, 523 U.S. 57 (1998), the creditor must establish for EACH
element:

- [ ] **Willful injury**: Debtor desired to cause the specific injury (not just the act)
      — *not* inferred from the nature of the act; *not* satisfied by recklessness
- [ ] **Malicious injury**: Without just cause or excuse
- [ ] **Actually litigated**: Every element was contested and decided in prior proceeding
- [ ] **Final judgment**: Not interlocutory, not a sanction default, not a consent order
- [ ] **Adversary proceeding**: Filed under Fed. R. Bankr. P. 7001(6) (§ 523(a)(6) is
      NOT self-executing in a motion to dismiss)
- [ ] **Subjective intent evidence**: What specific evidence shows the debtor's mental state?

If the opponent cannot check every box with citations to the record, the § 523(a)(6)
claim fails at threshold.

---

## Settlement / Release Analysis

Whenever a pre-petition settlement exists between the parties:

1. Pull full text of the release (verify "full release from beginning of time" language)
2. Map every claim in the current motion to the release scope
3. Identify any claim that falls within "any current or future claims" language
4. Analyze: res judicata / claim preclusion bar
5. Analyze: judicial estoppel (New Hampshire v. Maine, 532 U.S. 742 (2001) — three elements)
6. Analyze: RPC 3.3(a)(5) — did moving counsel disclose the release to the court?
7. If undisclosed: flag separately as candor violation AND independent sanctions basis

---

## Automatic Stay Violation Template (§ 362(k))

```
Element 1: STAY IN EFFECT
  → Bankruptcy petition filed: [date/time]
  → Relevant § 362(a) subsection(s): [list which apply]

Element 2: DEBTOR HAD KNOWLEDGE OF FILING
  → Under In re University Medical Center, 973 F.2d 1065 (3d Cir. 1992):
     knowledge of the filing (not knowledge of the stay) is sufficient
  → Evidence of knowledge: [ECF notice / email / service / court call]
  → Date knowledge established: [date]

Element 3: ACT WAS INTENTIONAL
  → Under In re Lansaw, 853 F.3d 657 (3d Cir. 2017): intentional act ≠ intent to violate stay
  → Describe act: [specific action taken]
  → Date of act: [date — must be AFTER knowledge established]
  → Good faith not a defense: In re Aleckna, 2021 WL 4097155 (3d Cir. 2021)

Relief Available:
  → § 362(k)(1): actual damages + costs + attorneys' fees (MANDATORY)
  → § 362(k)(1): punitive damages if "egregious" or "deliberate disregard" (DISCRETIONARY)
  → § 362(k)(2): individual debtor only for emotional distress (medical evidence helpful
     but not required where conduct is "patently egregious" per Lansaw at 670)

Joint and Several: Firm and individual attorney both liable
  → Cite In re Shaw (Bankr. D.N.J.) [obtain full citation from PACER]
```

---

## § 707(a) Opposition Quick Reference

**Controlling standard** (BINDING, 3d Cir. 2000):
> "Dismissal based on lack of good faith should be confined carefully and is generally
> utilized only in those egregious cases that entail concealed or misrepresented assets
> and/or sources of income, lavish lifestyles and intention to avoid a large single debt
> based upon conduct akin to fraud, misconduct or gross negligence."
> In re Tamecki, 229 F.3d 205, 207 (3d Cir. 2000).

**Ability to pay** (BINDING, 3d Cir. 2007):
> "A debtor's ability to repay is not in and of itself sufficient proof of bad faith."
> In re Perlin, 497 F.3d 364, 369 (3d Cir. 2007).

**Affirmative good faith showing**:
- Full and complete schedules (detail is the credibility)
- Multiple creditors (not a two-party dispute in bankruptcy clothing)
- Legitimate discharge purpose
- Disclosed assets / no concealment

**Distinguishing eve-of-trial cases** (In re Myers, 491 F.3d 120 (3d Cir. 2007)):
Myers is Ch. 13, not Ch. 7. Myers involved: (1) violation of existing court order;
(2) Ch. 13 ineligibility; (3) state court had already announced its ruling; (4) underlying
debt was fraudulent conveyance. None of these typically present in Ch. 7 civil litigation cases.

---

## Mandatory Abstention Checklist (§ 1334(c)(2))

Stoe v. Flaherty, 436 F.3d 209 (3d Cir. 2006) five-element test — ALL must be met:

- [ ] Element 1: Timely motion
- [ ] Element 2: Proceeding based on state law claim NOT arising under title 11 or in a
      case under title 11 → **FAILS for § 523(a)(6)** (expressly arises under title 11)
- [ ] Element 3: Absent § 1334, no federal jurisdiction → **FAILS** if § 157(b)(2)(I)
      core proceeding exists (bankruptcy court has exclusive jurisdiction)
- [ ] Element 4: Action already commenced in state forum capable of timely adjudication
      → **FAILS** if state court action was dismissed before petition filed
- [ ] Element 5: State forum of appropriate jurisdiction exists

**Threshold check**: Does the statute cited even exist? (§ 1134 does not exist; § 1334 does.)

---

## Pre-Filing Quality Checklist

Before the opposition is signed and filed:

### Statutory Citations
- [ ] Every statute verified in official U.S. Code
- [ ] Every state statute verified (watch for Title transpositions — e.g., N.J.S.A. 21:58D
      vs. 2A:58D)
- [ ] Every cited subsection exists and says what the brief says it says

### Case Law
- [ ] Every [VERIFY BEFORE FILING] flag resolved via Westlaw/PACER
- [ ] Every non-precedential opinion labeled as such and not cited as binding authority
- [ ] Every "BINDING" designation confirmed (same circuit, precedential)
- [ ] Every circuit split acknowledged where relevant
- [ ] Subsequent history checked (no reversed or overruled authority)

### Factual Record
- [ ] Every date cross-checked against docket entries
- [ ] Every quote from court opinions pulled verbatim (no paraphrase in argument sections)
- [ ] Any discrepancy between dates in opponent's papers documented with exhibit reference
- [ ] Client declarations/certifications reviewed for consistency with schedule filings

### Opponent's Papers
- [ ] Every case opponent cites has been read (not just abstracted)
- [ ] Every statutory citation by opponent confirmed to exist
- [ ] Any error documented and included in opposition's introduction
- [ ] Adversary proceeding vs. motion distinction preserved where required (e.g., § 523)

### Ethical
- [ ] Any settlement/release known to both parties disclosed to the court
- [ ] No misrepresentation of the procedural history of the state court case
- [ ] No citation to "judgment of liability" without disclosing interlocutory characterization
- [ ] RPC 3.3 review: Is any "material fact" omitted that creates a misleading impression?

---

## Subagent Prompt Template

When launching a research subagent, include:

```
**Case:** [Case name, number, court]
**Hearing:** [Date, judge]
**Your track:** [Track name — e.g., § 707(a) Analysis]
**Controlling circuit:** [e.g., Third Circuit]
**Issue to research:** [Specific legal question]
**Opponent's argument (verbatim or paraphrase):** [What they say]
**Our position:** [What we argue]
**Output file:** [Absolute path for output]
**Key cases to start with:** [Any already identified]
**Sources to use:** CourtListener, Google Scholar, Justia (in that order)
**Mark all unconfirmed citations [VERIFY BEFORE FILING]**
**Return:** Full memo with verbatim quotes, pinpoint citations, and binding/persuasive designation
```

---

## File Organization

```
case-files/
  [case-name]/
    README.md                    ← case summary + folder map for subagents
    research-output/
      part1-judge-[initials].md  ← SA1 judicial profile
      part2-[primary-issue].md   ← SA2 primary argument
      part3-[issue].md           ← SA3
      part4-[issue].md           ← SA4
      part5-[issue].md           ← SA5
      part6-factual.md           ← SA6 factual reconstruction
      [doc-name]-analysis.md     ← Per-document analysis subagents
      FINAL-MEMO.md              ← Master synthesis (FINAL DELIVERABLE)
```

---

## Timing Protocol (24-Hour Deadline Example)

| Hour | Action |
|------|--------|
| 0    | Read all documents (parallel Drive/PACER pulls) |
| 0    | Launch all 6 SA tracks simultaneously |
| 0    | Main context: review existing case documents while SAs run |
| 2-4  | SA outputs arrive; read each; flag anomalies for follow-up |
| 4    | Launch document-analysis SAs for major opponent filings |
| 6    | All SA outputs confirmed written; begin synthesis |
| 8    | FINAL-MEMO.md written; verification checklist extracted |
| 10   | Commit and push all files |
| 10+  | Begin drafting the actual court filing from FINAL-MEMO |
| 20   | Pre-filing quality checklist; Westlaw verification of all [VERIFY] flags |
| 23   | Final review; no new research after Hour 20 |
| 24   | File |

---

## PDF Output — Final Deliverable Step

After FINAL-MEMO.md is complete and all research is synthesized, generate a professional
PDF for distribution to the legal team. This is the final step of every engagement.

### Tools

```
.claude/skills/legal-research/gen_pdf.py       — main script
.claude/skills/legal-research/templates/legal-memo.tex — LaTeX template
```

### Dependencies (Linux/apt)

```bash
apt-get install -y --fix-missing pandoc texlive-latex-recommended \
  texlive-fonts-recommended texlive-latex-extra
```

### Usage

```bash
python3 .claude/skills/legal-research/gen_pdf.py \
  case-files/[matter]/research-output/FINAL-MEMO.md \
  case-files/[matter]/research-output/FINAL-MEMO.pdf
```

### What the Pipeline Does

1. **Reads** FINAL-MEMO.md
2. **Extracts citations** from original text (before any Unicode normalization):
   - Cases: `In re Name, Vol Rep Page (Court Year)` and `X v. Y, citation` patterns
   - Statutes: `11 U.S.C.`, `28 U.S.C.`, `N.J.S.A.` patterns
   - Rules: `Fed. R. Bankr. P.`, `N.J. Ct. R.`, `N.J. RPC` patterns
3. **Normalizes Unicode** → replaces `→`, `≠`, `§`, `—`, curly quotes, etc. with
   pdflatex-safe equivalents (math symbols use pandoc `$...$` delimiters)
4. **Pre-processes markdown** → strips duplicate H1/classification header (already on
   cover page), promotes H4 to H3, highlights `[VERIFY]` flags in amber
5. **Builds Table of Authorities** as a LaTeX section (cases / statutes / rules)
6. **Runs pandoc** with custom LaTeX template → pdflatex → PDF

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
- **Header:** ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL (red, every page)
- **Footer:** Shortened case name (left) | page number (center)
- **Blockquotes:** Left rule bar + italic — visual distinction for verbatim legal quotes
- **Section headers:** Uppercase, rule line under — standard internal memo style
- **VERIFY flags:** Amber/orange text with bold `[VERIFY BEFORE FILING]` label
- **Confidentiality:** No firm name on header/footer; cover page carries all classification

### Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `\tightlist undefined` | Pandoc macro not in template | Add `\providecommand{\tightlist}{...}` |
| `Unicode character X not set up` | Raw Unicode reaching pdflatex | Add to UNICODE_SUBSTITUTIONS in gen_pdf.py |
| `Missing $ inserted` near `\rightarrow` | Used `\(` in markdown; pandoc treats as escaped paren | Use pandoc math `$\rightarrow$` instead |
| Template `unexpected "$"` | Dollar sign in LaTeX comment or command | In pandoc templates, `$` outside `$var$` syntax is invalid; use `\(\)` or escape |
| TOA has 0 statutes | Normalization ran before extraction | Always extract from raw_text before normalizing |
| Long table cells overflow margin | Wide pipe table columns | Use narrower column labels; break long content across rows |

### Adding New Unicode Characters

Edit `UNICODE_SUBSTITUTIONS` in `gen_pdf.py`. Rules:
- Math/comparison symbols: use `$\latex_name$` (pandoc math syntax)
- Typography: use plain text equivalents where possible (`---` for em dash)
- LaTeX text commands (`\S{}`, `\P{}`): only for symbols with dedicated commands
- Never use `\(` or `\)` for inline math in substitutions (pandoc treats `\(` as escaped paren)

### Customizing for a New Matter

To adapt for a different case, change the `generate_pdf()` call arguments:

```python
generate_pdf(
    input_md=Path("case-files/[matter]/research-output/FINAL-MEMO.md"),
    output_pdf=Path("case-files/[matter]/research-output/FINAL-MEMO.pdf"),
    case_number="26-XXXXX-XXX",
    case_name_short="In re [Name]",
    memo_date="June 25, 2026",
)
```

The cover page case details are hardcoded in the template's `\begin{titlepage}` block.
For a new matter, edit `legal-memo.tex` lines for IN RE, Case No., Court, Hearing,
Before, Subject, and Date — or convert these to pandoc template variables.

---

## Key Third Circuit Bankruptcy Standards (Quick Reference)

| Issue | Standard | Citation |
|-------|----------|----------|
| § 707(a) bad faith | "Egregious cases" only | Tamecki, 229 F.3d 205 (3d Cir. 2000) |
| § 707(a) ability to pay | Insufficient alone | Perlin, 497 F.3d 364 (3d Cir. 2007) |
| § 523(a)(6) willful | Must desire the specific injury | Kawaauhau, 523 U.S. 57 (1998) |
| § 523(a)(6) test | Purposeful infliction OR subj. certainty | Conte, 33 F.3d 303 (3d Cir. 1994) |
| CE "actually litigated" | Narrow; default insufficient | Docteroff, 133 F.3d 210 (3d Cir. 1997) |
| Mandatory abstention | Five elements, all required | Stoe v. Flaherty, 436 F.3d 209 (3d Cir. 2006) |
| § 362(k) willfulness | Knowledge of filing + intentional act | Lansaw, 853 F.3d 657 (3d Cir. 2017) |
| § 362(k) good faith | Not a defense | Aleckna, 2021 WL 4097155 (3d Cir. 2021) |
| § 362(k) knowledge std | Filing only (not stay) | Univ. Medical Ctr., 973 F.2d 1065 (3d Cir. 1992) |
| § 523 dischargeability burden | Preponderance | Grogan v. Garner, 498 U.S. 279 (1991) |
| § 523 = core proceeding | Exclusive BK jurisdiction | Halper, 164 F.3d 830 (3d Cir. 1999) |
| § 1927 sanctions | Willful bad faith required | Baker Industries, 764 F.2d 204 (3d Cir. 1985) |
