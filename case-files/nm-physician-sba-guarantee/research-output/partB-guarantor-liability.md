# Track B: Effect of the LLC's Chapter 7 Filing on the Physician's Personal Guarantor Liability

**Prepared for:** Preliminary bankruptcy research memo — 82-year-old physician, 100% sole member of an LLC with SBA PPP/EIDL debt, personally guaranteed
**Scope:** Pure legal research (no code). Answers whether the LLC's Chapter 7 filing discharges or otherwise forces the guarantor into bankruptcy, and what happens next.
**Research date:** July 11, 2026

---

## BOTTOM LINE (for the memo's executive summary)

1. The LLC's Chapter 7 filing does **not** discharge the physician's personal guaranty and does **not** force him into personal bankruptcy. 11 U.S.C. § 524(e) is explicit that a debtor's discharge "does not affect the liability of any other entity" on the same debt.
2. Technically, the LLC — a non-individual — will not even receive a "discharge" as that term is used in the Code. Under 11 U.S.C. § 727(a)(1), only an individual debtor gets a Chapter 7 discharge. The LLC's Chapter 7 case will simply liquidate whatever assets exist, distribute proceeds to creditors, and close — leaving any unpaid balance legally uncollectible from the (now-defunct, asset-less) LLC, but not "discharged" in the technical statutory sense.
3. Practically, this distinction is close to academic for the physician: either way, the SBA/lender/servicer will look to him personally on the guaranty, and it can sue him directly in state or federal court (or pursue non-judicial federal collection tools) without any requirement that he file his own bankruptcy case.
4. Filing his own personal Chapter 7 or Chapter 13 is the guarantor's **voluntary** option if the guaranty debt becomes overwhelming — not a legal consequence that flows automatically from the LLC's bankruptcy.
5. An involuntary Chapter 7 filed by creditors against the physician himself is theoretically possible under 11 U.S.C. § 303 but requires a specific creditor count and claim thresholds; with a single creditor situation (SBA/one lender) it is very unlikely.

---

## 1. Core Principle: 11 U.S.C. § 524(e) — Discharge of the LLC Does Not Touch the Guarantor

### Statutory text (verbatim)

> **11 U.S.C. § 524(e):** "Except as provided in subsection (a)(3) of this section, discharge of a debt of the debtor does not affect the liability of any other entity on, or the property of any other entity for, such debt."

Verified consistently across secondary aggregators of the U.S. Code (Cornell LII, FindLaw, GovInfo excerpts, GovRegs) — the statutory language is uniform across all sources found. **Verification Status: CONFIRMED** (text corroborated by multiple independent code-reproduction sites; direct WebFetch to law.cornell.edu, govinfo.gov, and law.justia.com was blocked by network/proxy policy during this research session — counsel should pull the primary govinfo.gov PDF text directly before filing to eliminate any residual transcription risk). [VERIFY BEFORE FILING — confirm against the official govinfo.gov U.S. Code PDF]

### What it means here

Section 524(e) is the codification of the century-old common-law rule that a discharge is a **personal defense of the debtor**, not a satisfaction or extinguishment of the underlying debt. When the LLC's case concludes, the debt itself does not disappear — it simply becomes unenforceable *against the LLC*. Anyone else obligated on that same debt (a guarantor, co-borrower, or co-signer) remains on the hook exactly as if the LLC's bankruptcy had never happened.

### Cases applying § 524(e) to guarantor liability

```
Case Name: Republic Supply Co. v. Shoaf
Citation: 815 F.2d 1046 (5th Cir. 1987)
Binding Status: PERSUASIVE (Fifth Circuit; not binding outside the 5th Cir., but widely cited nationally as the leading case on § 524(e) and guarantors)
Holding (verbatim key quote): "[Section] 524(e) does not by its specific words preclude the discharge of a guaranty when it has been accepted and confirmed as an integral part of a plan of reorganization."
Note: This case arose in Chapter 11 (not Chapter 7) and involved a confirmed reorganization plan that *expressly* released the guarantor by its terms; the Fifth Circuit gave that express plan release res judicata effect. It is useful here mainly to show the narrow exception (an express, court-approved release as part of a Chapter 11 plan) — which is inapplicable to a Chapter 7 liquidation case with no plan and no express guarantor release. It confirms, a contrario, that absent such an express release mechanism, § 524(e) leaves guarantor liability untouched.
Source: Multiple secondary summaries (Dechert "Guaranties in Bankruptcy: A Primer II"; FindLaw Corporate Counsel summary "No Release of Loan Guaranty Under Confirmed Plan's General Release Provision"); direct opinion text at law.resource.org/pub/us/case/reporter/F2/815/815.F2d.1046.86-1541.html (WebFetch to this URL was blocked by network policy during this session)
Verification Status: VERIFY BEFORE FILING — pull full opinion text via Westlaw/Lexis or CourtListener before citing to confirm exact quote and pin cite.
```

```
Case Name: Underhill v. Royal (Royal Insurance Co.)
Citation: 769 F.2d 1428 (9th Cir. 1985) [some secondary sources cite 769 F.2d 1426 — pin cite/page needs verification]
Binding Status: PERSUASIVE (9th Circuit)
Holding (as reported by secondary sources): The Ninth Circuit read the "broad" language of § 524(e) to mean the discharge "does not affect the liability of any other entity," and held the bankruptcy court lacked power to discharge or release the liability of a non-debtor. Frequently cited as foundational authority (alongside § 524(e)'s text) for the proposition that a bankruptcy discharge cannot be extended to release a non-debtor guarantor absent an express statutory exception.
Source: Secondary summaries only (Southern California Law Review, "953 Without Exception? The Ninth Circuit's Evolving Stance"); direct case text not independently retrieved in this session due to WebFetch network-policy blocks on openjurist.org, law.resource.org, and courtlistener.com.
Verification Status: VERIFY BEFORE FILING — retrieve and independently confirm the exact citation (1426 vs. 1428), pin cite, and quoted language via CourtListener, Google Scholar, or Westlaw before use in any filing.
```

```
Case Name: In re Walker
Citation: 927 F.2d 1138 (10th Cir. 1991)
Binding Status: PERSUASIVE (10th Circuit)
Holding (as reported by secondary sources): While § 524(a)(2) enjoins actions to hold the discharged debtor personally liable, § 524(e) "permits a creditor to bring or continue an action directly against the debtor for the purpose of establishing the debtor's liability when establishment of that liability is a prerequisite to recovery from another entity" — illustrating that § 524(e) preserves creditors' rights against non-debtor third parties (there, a state recovery fund) notwithstanding the primary debtor's discharge.
Source: Secondary summary (vLex case abstract; general search aggregation). Full text not independently retrieved due to WebFetch blocks.
Verification Status: VERIFY BEFORE FILING — pull full opinion via CourtListener/Westlaw before citing; confirm this case truly involves guarantor-type liability rather than solely an insurance/recovery-fund fact pattern (it is somewhat analogous but not a pure guaranty case, so it should be cited for the general § 524(e) principle rather than as a guaranty-specific holding).
```

### Additional widely-cited secondary framing (non-case, but useful for the memo narrative)

- "A discharge granted a debtor has no effect on the liability of a third-party co-debtor or guarantor of a discharged debt." — recurring formulation across multiple practitioner sources (Nolo, AllLaw, bankruptcy-specialist firm blogs) summarizing the settled, essentially undisputed application of § 524(e) to guarantors. This point is not genuinely contested in the case law nationally — courts uniformly hold guarantors remain liable after the primary obligor's discharge; the only live circuit splits concern the different question of whether a *Chapter 11 plan* may affirmatively enjoin third-party claims against a non-debtor (the "non-debtor release" controversy — see *Purdue Pharma*, *Dow Corning*, *A.H. Robins* line of cases), which is not applicable to a straight Chapter 7 liquidation with no plan.

**Practice note:** Because this is a Chapter 7 (not Chapter 11) case with no reorganization plan, the "non-debtor release" line of cases (which concerns whether a plan may enjoin claims against guarantors) is not directly implicated — there is no plan and no possibility of an injunction protecting the physician. The straightforward § 524(e) rule applies without any exception or wrinkle: nothing in the LLC's Chapter 7 case will touch his guaranty liability.

---

## 2. Does the LLC Even Get a "Discharge" in Chapter 7? No — Only Individuals Do

### Statutory text (verbatim)

> **11 U.S.C. § 727(a)(1):** "The court shall grant the debtor a discharge, unless— (1) the debtor is not an individual;" [remainder of subsection (a) lists other grounds (2)–(12), inapplicable here]

Verified consistently across Cornell LII, FindLaw, uscode.house.gov, and multiple secondary summaries. **Verification Status: CONFIRMED** (consistent across all independent sources found; primary-source WebFetch was blocked by network policy this session — recommend pulling the govinfo.gov PDF directly before filing). [VERIFY BEFORE FILING against the official U.S. Code text]

### What this means practically

- A corporation, partnership, or LLC that files Chapter 7 is **liquidated only** — its assets are collected and distributed by the trustee, and the case is then closed. It **never receives a discharge**, because § 727(a)(1) categorically bars discharge for any debtor that "is not an individual."
- Legislative history (House Report on the Bankruptcy Reform Act of 1978, reflected in numerous secondary summaries of § 727's history) explains that Congress deliberately eliminated corporate/partnership Chapter 7 discharges (which had been permitted, though rarely used, under prior law) specifically "to avoid trafficking in corporate shells and in bankrupt partnerships." The policy: a corporate shell with no assets and no ongoing business has nothing left to protect via discharge, and allowing a discharge would create an opportunity for abuse (e.g., resurrecting/reselling a "clean" shell entity).
- Practical consequence: any debt the LLC could not pay from its liquidated assets simply remains **legally owed by the LLC** (now an empty, defunct entity with no ability to ever pay it) — it is not "discharged" in the Bankruptcy Code's technical sense, it's just uncollectible in practice because there is no one and nothing left to collect from. The debt is not erased from existence; it has merely lost its only source of recovery (the LLC's assets, which are now gone).
- This is why the distinction matters for the physician: the SBA's claim against the LLC doesn't get wiped out by a magic "discharge" order — it becomes worthless against the LLC purely because the LLC will have no more assets and no more legal existence to collect from. The claim against **him** as guarantor is entirely unaffected by any of this and remains fully collectible.

### Supporting sources

```
Source Type: Secondary/treatise-style summary (widely and consistently corroborated across multiple independent legal-publisher summaries of § 727)
Key Point: "Unlike an individual debtor, a non-individual debtor does not achieve a discharge of its debts following liquidation; discharge of liability is only available to individual debtors." Additional formulation found: "In a chapter 7 case, a discharge is only available to individual debtors, not to partnerships or corporations... a corporation or partnership in a chapter 7 case is liquidated only and never receives a discharge. After liquidation, any dissolution of the corporation or partnership... must be effectuated under state law, since the [Bankruptcy] Code does not provide for dissolution of corporations or partnerships."
Source: Legislative-history-based summaries appearing consistently across Cornell LII Wex, FindLaw, and practitioner commentary (e.g., "Why Corporations and LLCs Should NOT File Chapter 7" — Mediat Bankry; "Life after death for Chapter 7 corporate debtors?" — Lexology)
Verification Status: VERIFY BEFORE FILING — for a formal filing, cite directly to the House Report (H.R. Rep. No. 95-595, 95th Cong., 1st Sess. 384 (1977)) reprinted in the historical/legislative notes to § 727, available via govinfo.gov or a Westlaw/Lexis legislative history search, rather than relying on secondary paraphrase.
```

```
Case Name: In re Kabbage Inc.
Citation: Bankr. D. Del. (2023) [exact docket/reporter citation not independently confirmed this session]
Binding Status: PERSUASIVE (Delaware bankruptcy court; not controlling outside that district, and note this was a Chapter 11 case, not Chapter 7)
Holding (as reported by secondary source): Addressed whether liquidating corporate debtors could obtain a "de facto discharge" through broad injunctive/exculpation provisions in a Chapter 11 liquidating plan, and held that permanent injunctions functionally equivalent to a discharge are impermissible for non-individual (corporate) liquidating debtors — reinforcing that entities cannot obtain the functional equivalent of a § 727 discharge by other means.
Source: Lexology summary ("Life after death for Chapter 7 corporate debtors? What remains after a corporate liquidation")
Verification Status: VERIFY BEFORE FILING — locate full opinion and exact citation via CourtListener or Westlaw; this is Chapter 11, so use only as supporting/contextual authority for the "no functional discharge for entities" point, not as direct Chapter 7 authority.
```

---

## 3. Creditors Can Sue the Guarantor Directly — No Requirement That He Also File Bankruptcy

Multiple consistent secondary sources confirm:

- Once SBA honors its guarantee to the lender and becomes the creditor (or once the participating lender itself pursues collection), it (or its servicer/collection counsel, or ultimately the U.S. Treasury via cross-servicing) sends demand letters to, and can sue, **any personal guarantor directly** — this does not require and is not contingent upon the guarantor filing his own bankruptcy case.
- "In most cases, just ceasing operations is sufficient" for the SBA/lender to pursue the guarantor; the LLC's bankruptcy filing is not a legal prerequisite to suing the guarantor, though as a practical matter a formal Chapter 7 liquidation of the LLC (confirming there is nothing left to recover from the entity) often *triggers* or accelerates the decision to pursue the guarantor.
- The federal government generally has a **six-year statute of limitations** to sue and obtain a judgment on a defaulted SBA debt (28 U.S.C. § 2415 context, as referenced in practitioner sources) — but critically, non-judicial federal collection tools (Treasury offset of tax refunds/Social Security, administrative wage garnishment (AWG) under 13 C.F.R. § 140.11, credit bureau reporting, etc.) are **not** subject to that same limitations period once the debt has been referred to Treasury for cross-servicing, and can continue indefinitely until paid or settled.
- **Key point for the memo:** the guarantor filing his own bankruptcy is entirely his own **choice** — a defensive/proactive option available to him if and when the guaranty debt becomes unmanageable — not something the LLC's Chapter 7 case forces upon him or automatically triggers.

```
Source: "SBA Collection Rights Extend Far Beyond Just Suing You" (bankruptcysoapbox.com)
Key Points: "The federal government does not need a judgment to exercise powerful collection actions that usually require one" — SBA/Treasury can garnish wages without first suing, similar to IRS authority. 13 C.F.R. § 140.11 governs administrative wage garnishment limits and challenge procedures. Treasury offset (tax refunds, Social Security) has no apparent time limit, unlike the ability to sue for a judgment, which is time-barred after a set period. [VERIFY BEFORE FILING — confirm current 13 C.F.R. Part 140 citation and cross-servicing/Treasury Offset Program authority (31 U.S.C. § 3716 et seq.) directly against eCFR/govinfo.gov]
Verification Status: VERIFY BEFORE FILING — this is a secondary/practitioner source; confirm underlying regulatory citations (13 C.F.R. Part 140; 31 C.F.R. Part 285 Treasury offset regulations) directly against eCFR before relying on them in any filing.
```

---

## 4. The Guarantor's Options Once Pursued on the Personal Guaranty

### (a) Pay / negotiate a direct settlement
Straightforward — pay the demanded amount or negotiate a reduced lump-sum or payment-plan settlement directly with the SBA, its servicer, or (if referred) Treasury/DOJ.

### (b) SBA Offer in Compromise (OIC)
- The relevant SBA process is an **Offer in Compromise**, using **SBA Form 1150** (Offer in Compromise) together with **SBA Form 770** (Financial Statement of Debtor) or a business financial statement.
- Substantive OIC criteria (per SBA post-servicing/liquidation guidance, summarized in secondary sources): the offered amount must bear "a reasonable relationship to the estimated net present value of the projected amount of recovery available through enforced collection"; the borrower/guarantor must fully disclose financial capacity; the borrower must have ceased operations and liquidated all business collateral; the participating lender must agree; and the source of settlement funds must be identified.
- **Citation correction/verification needed:** The task materials suggested "13 C.F.R. § 140" as a possible OIC citation — that appears to be incorrect; 13 C.F.R. Part 140 concerns SBA's administrative debt collection/wage garnishment procedures, not the Offer in Compromise program itself. The OIC program is governed by SBA internal **SOP 50 57 (Loan Servicing and Liquidation)**, and 13 C.F.R. Part 120, Subpart E (Servicing, Liquidation, and Debt Collection Litigation of 7(a) and 504 loans) is the more relevant regulatory subpart (e.g., 13 C.F.R. § 120.520 governs SBA's purchase of the guaranteed portion from the lender upon default). Note also: **lenders/CDCs cannot compromise or release any claim against a guarantor without SBA's prior written approval** — meaning the guarantor's OIC negotiation, once the SBA has purchased/owns the guaranteed claim, generally runs through SBA (or its Treasury-cross-serviced collection agent) directly, not the original lender.
- [VERIFY BEFORE FILING — confirm current SOP number/revision (SOP 50 57 has had multiple revisions, e.g., 50 57 3) and the precise current CFR citations directly on ecfr.gov and sba.gov before advising the client, since SBA COVID-era loan servicing/OIC guidance has been updated multiple times since 2020.]
- If the SBA approves an OIC, the guarantor's personal guaranty on that loan is released upon payment of the agreed compromise amount.

### (c) Suretyship / guarantor defenses — largely waived
- SBA's standard guaranty instrument, **SBA Form 148 (Unconditional Guarantee)** (used for all SBA 504 loans, and commonly for 7(a) loans as well, either in SBA's own form or a lender's substantially similar form), contains an extensive **Section 6 "Rights, notices, and defenses that Guarantor waives"** provision — the guarantor waives, "to the extent permitted by law," essentially all of the traditional common-law suretyship defenses (e.g., notice of default, changes to the underlying loan terms, release of collateral, etc.).
- Practical implication: the physician should not expect to have much room to contest the guaranty's enforceability on classic suretyship-defense grounds; his practical options are financial/negotiated (settlement, OIC) or bankruptcy-based (his own filing), not litigation defenses on the merits of the guaranty itself. [VERIFY BEFORE FILING — obtain and review the actual signed guaranty instrument for this specific loan, since it may be a lender's own form rather than SBA Form 148/148L, with potentially different (broader or narrower) waiver language; also confirm which underlying loan program (PPP vs. EIDL) is at issue, since EIDL loans over $200,000 typically require a personal guaranty via a different mechanism (SBA loan documents/UCC, not necessarily Form 148), while PPP loans generally did NOT require personal guarantees at all (PPP was largely non-recourse to owners absent fraud/certain misuse) — this distinction is critical and should be independently verified against the client's actual loan documents.]

### (d) The guarantor's own Chapter 7 or Chapter 13
- This is the guarantor's affirmative, voluntary choice, not a legal requirement flowing from the LLC's case.
- If the physician's own eventual bankruptcy filing becomes necessary to discharge the guaranty debt, standard Chapter 7 eligibility (means test, etc.) and — critically — **exemption planning** (state vs. federal exemptions, homestead, retirement accounts, etc.) become central concerns. This ties directly to whatever exemption-focused track is covering asset protection in this five-track research effort; that analysis should be read together with this memo before advising the client whether/when his own filing makes sense.
- Note: an SBA loan personally guaranteed and reduced to a deficiency after the LLC's failed collateral liquidation is ordinary unsecured (or partially secured, if the guaranty was collateralized separately, e.g., by a lien on the physician's personal residence or other assets pledged as additional collateral — verify from loan documents) debt, generally dischargeable in the guarantor's own Chapter 7 absent a specific exception under 11 U.S.C. § 523 (e.g., fraud in obtaining the loan under § 523(a)(2), which the SBA has pursued in some COVID-loan-fraud contexts — a search flagged that the SBA "may file an Adversary Proceeding under 11 U.S.C. § 523(a)(2)(B)... requesting the... court find the SBA loan non-dischargeable because the debtor obtained the loan fraudulently"). [VERIFY BEFORE FILING — this fraud/nondischargeability risk should be separately assessed based on the actual facts of how the PPP/EIDL loan was obtained and represented; not addressed further in this track.]

---

## 5. Could Creditors Force the Physician Into an Involuntary Bankruptcy? (11 U.S.C. § 303)

### Statutory framework (verbatim, key portions)

> **11 U.S.C. § 303(b)(1):** An involuntary case may be commenced "by three or more entities, each of which is either a holder of a claim against such person that is not contingent as to liability or the subject of a bona fide dispute as to liability or amount, or an indenture trustee representing such a holder, if such noncontingent, undisputed claims aggregate at least $10,000 more than the value of any lien on property of the debtor securing such claims held by the holders of such claims..."

> **11 U.S.C. § 303(b)(2):** "if there are fewer than 12 such holders, excluding any employee or insider of such person and any transferee of a transfer that is voidable under section 544, 545, 547, 548, 549, or 724(a) of this title, by one or more of such holders that hold in the aggregate at least $10,000 of such claims..."

**Verification Status: CONFIRMED** for the underlying statutory structure and the base $10,000 figure (which Congress set in the original statute and which is then periodically adjusted for inflation under 11 U.S.C. § 104). [VERIFY BEFORE FILING against the official U.S. Code text at govinfo.gov]

### Current inflation-adjusted dollar figure

- The base statutory figure of $10,000 is adjusted every three years under § 104. Sources consistently confirm the figure was **$18,600** for petitions filed **April 1, 2022 – March 31, 2025**.
- Sources indicate the figure was adjusted again effective **April 1, 2025** to **$21,050** (some sources render this in slightly different combinations of language, but consistently land on the $21,050 figure for the April 2025–March 2028 triennial period). Because the current date is July 2026, **$21,050 is the applicable current aggregate-claim threshold**, not $18,600 as suggested in the task prompt.
- [VERIFY BEFORE FILING — confirm the exact current figure and effective date directly against the Judicial Conference / Federal Register inflation-adjustment notice for 11 U.S.C. § 104, or the current text of 11 U.S.C. § 303 as codified with the adjustment note, since secondary sources showed some inconsistency in exact figures and this number changes automatically every three years by operation of law.]

### Practical bottom line for this client

- **Requirements to force an involuntary Chapter 7 on the physician:** (1) if he has 12 or more creditors (excluding insiders/employees), it takes **3 or more** petitioning creditors joining the petition; if fewer than 12 total creditors, it takes only **1 or more**; (2) each petitioning creditor's claim must be **non-contingent** and **not the subject of a bona fide dispute**; and (3) the aggregate qualifying claims must exceed the value of any securing collateral by at least the current inflation-adjusted threshold (approx. **$21,050** as of mid-2026, subject to verification).
- **Applied here:** This appears to be fundamentally a single-creditor (or small handful of creditors — SBA/lender, possibly plus ordinary personal debts) situation. Since it takes **three or more** creditors to force an involuntary petition once a debtor has 12+ creditors, and the SBA/lender alone cannot single-handedly do so unless the physician has fewer than 12 total creditors, an involuntary Chapter 7 against him personally is **legally possible in the abstract but practically unlikely** here — it would require the SBA/servicer to recruit at least two other creditors with qualifying non-contingent, undisputed claims to join a petition, which is an unusual and aggressive step rarely taken by SBA/Treasury collection functions in practice (they overwhelmingly rely on lawsuits, judgments, administrative wage garnishment, and Treasury offset rather than involuntary bankruptcy petitions).
- Counsel should advise the client this risk is real but low-probability, and should be monitored rather than treated as a driving factor in near-term planning — unless discovery reveals the physician has fewer than 12 total creditors (in which case the SBA alone, as a single creditor holding a non-contingent, undisputed claim exceeding ~$21,050, could theoretically file an involuntary petition unilaterally).

```
Source: 11 U.S.C. § 303 (Cornell LII, uscode.house.gov, FindLaw — text consistent across all)
Source: LegalClarity, "11 USC 303: Creditor Requirements for Involuntary Bankruptcy"
Source: Cullen and Dykman LLP, "Involuntary Petitions in Bankruptcy: A Brief Update"
Verification Status: Statutory structure CONFIRMED; current dollar figure VERIFY BEFORE FILING against the official Judicial Conference/Federal Register triennial adjustment notice.
```

---

## Summary Table

| Question | Answer | Confidence |
|---|---|---|
| Does the LLC's Ch. 7 discharge release the guarantor? | No — § 524(e) expressly preserves guarantor liability | High (statutory text confirmed + multiple persuasive cases) |
| Does the LLC even get a "discharge" in Ch. 7? | No — only individuals get a § 727 discharge; LLC case is liquidation-only, ending in case closure, not discharge | High (statutory text confirmed) |
| Must the guarantor file his own bankruptcy because the LLC filed? | No — entirely voluntary/optional on his part | High |
| Can SBA/servicer sue him directly without his own BK filing? | Yes | High |
| Can SBA pursue him via non-judicial means (offset, garnishment)? | Yes, and largely without the 6-year suit limitations period applying | Medium-High (secondary sources; verify CFR cites) |
| Can he negotiate an OIC directly with SBA? | Yes, via SBA Form 1150 process under SOP 50 57 framework | Medium (verify current SOP revision/CFR cites) |
| Does he have strong suretyship defenses? | Unlikely — SBA Form 148 (if used) broadly waives them | Medium (verify actual signed guaranty document) |
| Could creditors force him into involuntary bankruptcy? | Theoretically possible under § 303, but requires multiple qualifying creditors (or a single creditor if fewer than 12 total) and is rare/unlikely in a single-major-creditor scenario | High on the law; fact-dependent on his total creditor count |

---

## Research Limitations / Notes on Methodology

- **WebFetch to primary-source case-law and statute repositories (courtlistener.com, law.cornell.edu, law.justia.com, openjurist.org, law.resource.org, govinfo.gov, en.wikipedia.org) was blocked throughout this session by the environment's outbound network/proxy policy** (confirmed via the proxy status endpoint, which logged repeated "gateway answered 403 to CONNECT (policy denial or upstream failure)" entries for these hosts). This is a session/infrastructure limitation, not a substantive research gap — it means case holdings and statutory text below were sourced through WebSearch result snippets (which frequently include verbatim quoted statutory/case language pulled from these same primary sources) rather than through direct primary-document retrieval and verification.
- **Every citation and quote in this memo should be independently re-verified against the primary source (Westlaw, Lexis, CourtListener, or govinfo.gov) before any filing**, per the flags above. The statutory text of §§ 524(e), 727(a)(1), and 303(b) is corroborated by enough independent, mutually-consistent secondary reproductions that it can be relied upon with high confidence for preliminary research purposes; the specific case pin cites (especially *Underhill v. Royal*'s exact page citation) and the current SBA SOP number/CFR citations for the OIC program carry more uncertainty and are flagged accordingly.
