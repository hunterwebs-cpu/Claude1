# Practice Reference — Bankruptcy

Loaded by the legal-research skill when the matter is a bankruptcy case (dismissal fights,
nondischargeability, abstention, automatic stay). Citations below are Third Circuit-flavored
(this module was built out during *In re Mell*, 26-16834-EJO (Bankr. D.N.J. 2026)) — treat
circuit-specific holdings as a starting map and confirm the controlling circuit before filing.

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

**Burden**: movant bears burden; debtor rebuts; burden shifts back under Tamecki.

---

## § 523(a)(6) Specific Checklist

Under Kawaauhau v. Geiger, 523 U.S. 57 (1998), the creditor must establish for EACH element:

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

**Purposeful infliction OR subjective certainty test**: In re Conte, 33 F.3d 303 (3d Cir. 1994).

**Burden**: creditor-plaintiff bears burden in the adversary proceeding, preponderance of the
evidence (Grogan v. Garner, 498 U.S. 279 (1991)).

**Core proceeding / exclusive jurisdiction**: In re Halper, 164 F.3d 830 (3d Cir. 1999).

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

**Threshold check**: Does the statute cited even exist? (§ 1134 does not exist; § 1334 does —
watch for opponents transposing digits in a citation.)

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

**Burden**: movant shows cause under § 362(d)(1); debtor shows no equity/necessity under
§ 362(d)(2). For § 362(k), debtor-plaintiff must prove all three elements above; good faith
is not a defense.

---

## Collateral Estoppel — Worked Bankruptcy Example

Apply the generic CE template in `SKILL.md` and note these bankruptcy-specific outcomes:

- Default/sanction entry → issue NOT actually litigated: In re Azeglio, 422 B.R. 490
  (Bankr. D.N.J. 2010)
- Discovery sanction under R. 4:23-5(a)(2) → NOT actually litigated (ministerial; no
  evidentiary hearing)
- Fifth Amendment invocation → NOT bad-faith obstruction; constitutionally protected.
  The Docteroff exception (In re Docteroff, 133 F.3d 210 (3d Cir. 1997)) requires WILLFUL
  OBSTRUCTION with a FULL AND FAIR OPPORTUNITY to litigate — mere invocation of privilege
  does not satisfy it.

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

---

## Suggested Track Breakdown for a Bankruptcy Opposition (6 tracks)

| Track | Scope |
|-------|-------|
| 1 | Judicial profile — judge's career, prior rulings, PACER orders |
| 2 | Primary dismissal standard (e.g. § 707(a)) + controlling circuit cases + factual rebuttal |
| 3 | Nondischargeability (§ 523(a)(6)) + collateral estoppel |
| 4 | Abstention (mandatory and permissive) + jurisdiction |
| 5 | Automatic stay — relief factors + § 362(k) counterclaim |
| 6 | Factual record reconstruction — state court errors, transfer analysis, sanctions |

This was demonstrated end-to-end in *In re Mell* (2026) under a 24-hour hearing deadline —
see the Timing Protocol in `SKILL.md` for the hour-by-hour breakdown.

## Sample Matter File for PDF Generation

```json
{
  "doc_title_line1": "INTERNAL LEGAL",
  "doc_title_line2": "RESEARCH MEMORANDUM",
  "banner_line1": "ATTORNEY WORK PRODUCT",
  "banner_line2": "PRIVILEGED AND CONFIDENTIAL",
  "banner_notice": "DO NOT DISTRIBUTE WITHOUT COUNSEL AUTHORIZATION",
  "header_banner": "ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL",
  "matter_label": "IN RE:",
  "matter_name": "S. Bradley Mell",
  "forum_label": "Court:",
  "forum": "United States Bankruptcy Court\nDistrict of New Jersey",
  "hearing_label": "Hearing:",
  "hearing": "July 16, 2026",
  "presiding_label": "Before:",
  "presiding": "Hon. Eamonn J. O'Hagan",
  "subject_label": "Subject:",
  "subject": "Opposition to Motion to Dismiss (Doc. 8);\nAutomatic Stay Relief; Mandatory Abstention",
  "distribution_label": "Distribution:",
  "distribution": "Legal Team — INTERNAL USE ONLY",
  "footer_disclaimer": "This memorandum constitutes attorney work product and is protected by the attorney-client privilege and work product doctrine. It is prepared solely for the use of counsel representing S. Bradley Mell in Case No. 26-16834-EJO. Unauthorized disclosure or distribution is strictly prohibited.",
  "case_number": "26-16834-EJO",
  "case_name_short": "In re Mell",
  "pdf_title": "Internal Legal Research Memorandum — In re Mell",
  "pdf_author": "Legal Team",
  "pdf_subject": "Opposition to Motion to Dismiss, 26-16834-EJO",
  "pdf_keywords": "bankruptcy, attorney work product, privileged"
}
```
