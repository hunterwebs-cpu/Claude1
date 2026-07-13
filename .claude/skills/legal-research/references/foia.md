# Practice Reference — FOIA / Public Records

Loaded by the legal-research skill for federal FOIA requests, administrative appeals, and
FOIA litigation. For state-court public-records analogs (state FOIA/open-records acts,
which vary widely), treat this module as a structural template and verify the specific
state statute — do not assume federal standards transfer.

---

## Statutory & Regulatory Framework

- **5 U.S.C. § 552** — FOIA itself, as amended by the OPEN Government Act of 2007 and the
  FOIA Improvement Act of 2016 (added the "foreseeable harm" standard and a 25-year sunset
  on the deliberative-process privilege).
- **Agency-specific implementing regulations** — every agency has its own FOIA regs; for
  DOJ components (including the Bureau of Prisons), see **28 C.F.R. Part 16**, Subpart A.
  Always cite the requester's regulation, not just the statute.
- **DOJ Office of Information Policy (OIP)** — issues government-wide FOIA guidance;
  administers DOJ's own appeals. `justice.gov/oip`, `foia.gov`.

---

## Required Elements of a Proper Request (5 U.S.C. § 552(a)(3))

1. **Reasonably describes** the records sought — specific enough that a professional
   agency employee familiar with the subject could locate them with a reasonable amount
   of effort. Cite award/solicitation/case numbers, date ranges, and named custodians
   where known; vague "all documents relating to X" requests invite an "unduly
   burdensome" denial.
2. Follows the agency's **published procedural regulations** (addressing, required
   certifications, format).
3. Sent to the **correct component** — for BOP records this is the BOP's FOIA/Privacy Act
   Section (or DOJ's centralized eFOIA portal, which routes to the correct component).

---

## Fee Categories (5 U.S.C. § 552(a)(4)(A); 28 C.F.R. § 16.10)

| Category | Search fees | Review fees | Duplication |
|---|---|---|---|
| Commercial use | Yes | Yes | Yes, no free pages |
| News media / educational or noncommercial scientific institution | No | No | First 100 pages free |
| All other requesters (individuals, general public) | First 2 hrs free, then yes | No | First 100 pages free, then yes |

State your category explicitly in the request — the agency defaults to the most
expensive category if you don't.

---

## Fee Waiver Standard (5 U.S.C. § 552(a)(4)(A)(iii))

Available to **any** requester regardless of fee category. Must show disclosure:

1. Concerns "the operations or activities of the government";
2. Is "likely to contribute significantly to public understanding" of those operations —
   the contribution must be more than of interest to the requester alone;
3. Would inform a **reasonably broad audience**, not just the requester;
4. Is **not primarily in the requester's commercial interest**;
5. The requester's ability/intent to convey the information to the public (having a
   platform — a blog, a media outlet, an advocacy organization, a newsletter — strengthens
   this showing but is not strictly required of an individual requester).

Draft the waiver request as an affirmative narrative addressing each factor, not a bare
assertion. Tie factor (2) to a *specific* gap in the public record (e.g., "no public
source currently discloses [X]; the requested records are the only way to verify [Y]").

---

## Expedited Processing Standard (5 U.S.C. § 552(a)(6)(E); 28 C.F.R. § 16.5(e)(1) for DOJ)

Compelling-need categories (DOJ's regulation is representative; other agencies mirror it
with minor variation — [VERIFY BEFORE FILING] against the specific agency's own 16.5-style
regulation):

(i) Failure to obtain the records on an expedited basis "could reasonably be expected to
    pose an imminent threat to the life or physical safety of an individual";
(ii) An "urgency to inform the public about actual or alleged federal government
     activity," if the request is made by "a person primarily engaged in disseminating
     information" — this prong is why journalists/bloggers/advocacy orgs have an easier
     path than a one-off individual requester; an individual can still qualify by
     describing a concrete, ongoing publication/dissemination practice;
(iii) The loss of substantial due process rights;
(iv) For DOJ specifically, a matter of "widespread and exceptional media interest" raising
     questions affecting public confidence in government integrity — [VERIFY this prong's
     exact text and whether the target agency's regs include it].

Requires a **certification "true and correct to the best of my knowledge and belief"**
of the facts supporting expedition — this is a statutory formality, include the exact
phrase. Agencies must decide the expedition request itself within 10 calendar days.

---

## Standard Timeline

- **20 business days** to issue a determination from date of receipt (§ 552(a)(6)(A)(i)).
- One **10-business-day extension** allowed for "unusual circumstances" (§ 552(a)(6)(B));
  agency must notify the requester in writing and offer an opportunity to narrow the
  request or negotiate an alternative time frame.
- Missed deadline → **constructive exhaustion**: requester may treat administrative
  remedies as exhausted and proceed straight to litigation (§ 552(a)(6)(C)(i)), though in
  practice most requesters still file an appeal first to build the record and sometimes
  get faster voluntary release.
- Agencies commonly run **simple / complex / expedited multi-track queues** — ask which
  track the request was assigned in the acknowledgment letter.

---

## Exemptions Quick Reference (5 U.S.C. § 552(b))

| Exemption | Covers | Notes |
|---|---|---|
| (b)(1) | Classified national security info | Rare outside intelligence/defense agencies |
| (b)(2) | Internal personnel rules/practices | Narrowed sharply by *Milner v. Dep't of Navy*, 562 U.S. 562 (2011) — rejected "High 2" withholding of non-personnel records |
| (b)(3) | Info exempted by another statute | Statute must require withholding with no discretion, or set particular withholding criteria |
| (b)(4) | Trade secrets & confidential commercial/financial info | **Directly relevant to contract pricing requests.** *Food Marketing Institute v. Argus Leader Media*, 588 U.S. 427 (2019) lowered the bar: info need only be "customarily and actually treated as private" by the submitter — the pre-2019 "competitive harm" test is gone. Expect a contractor to invoke this over rate schedules/pricing. Counter-argument: pricing charged to a **captive, government-controlled population with no market choice** is a materially different posture than ordinary competitive-bid pricing, and the public interest in what a monopoly government vendor charges a dependent population is unusually high — make that argument explicitly, and separately demand segregability (see below) so non-pricing deliverables terms aren't swept in by a blanket (b)(4) claim. |
| (b)(5) | Deliberative process / attorney work-product / attorney-client privilege (interagency memos) | Does not cover purely factual material or the agency's *final* opinions/policies (*NLRB v. Sears, Roebuck & Co.*, 421 U.S. 132 (1975)); 2016 amendment sunsets deliberative-process withholding after 25 years |
| (b)(6) | Personal privacy (personnel/medical files) | Requires balancing individual privacy against the public interest in disclosure |
| (b)(7) | Law enforcement records, six subparts: (A) interference with proceedings, (B) fair trial, (C) unwarranted privacy invasion, (D) confidential sources, (E) techniques/procedures, (F) life/safety | **(7)(E) is the BOP's likely basis for withholding security-sensitive tablet/kiosk system details** (e.g., network architecture, monitoring capability, contraband-detection methods) — anticipate this and pre-concede it isn't sought, which narrows the dispute to the commercial/deliverables terms |
| (b)(8) | Bank examination reports | Rare outside financial regulators |
| (b)(9) | Geological/geophysical well data | Rare |

**Segregability**: the agency must release all "reasonably segregable" non-exempt portions
of a record — it cannot withhold an entire document because part of it is exempt
(§ 552(b), final clause).

**Foreseeable harm standard**: since the 2016 amendment, the agency must also show that
disclosure would harm an interest the exemption is designed to protect — merely showing
information technically fits an exemption category is no longer sufficient
(5 U.S.C. § 552(a)(8)(A)).

---

## Administrative Appeal

- Required if the request is denied in whole/part, deemed "no responsive records," or a
  fee/fee-waiver determination is disputed.
- For DOJ components: **90 calendar days** from the date of the response letter to appeal,
  to DOJ's Office of Information Policy (28 C.F.R. § 16.9). Confirm the specific window in
  the denial letter — it controls over the general regulation if different.
- Appeal must be in writing, identify the request/response by tracking number, and state
  the grounds (exemption-by-exemption, if disputing withholding).
- Agency must respond within 20 business days (§ 552(a)(6)(A)(ii)), same extension rules
  as the initial request.
- **Exhaustion of the administrative appeal is a prerequisite to suit** against most
  agencies (including DOJ components) absent constructive exhaustion.

---

## Litigation

- **Venue**: requester's residence, principal place of business, where the records are
  located, or the District of Columbia (§ 552(a)(4)(B)).
- **De novo review**; the agency bears the burden to sustain any withholding.
- **Vaughn index**: an itemized index describing each withheld document/redaction and the
  exemption claimed, in enough detail for adversarial testing (*Vaughn v. Rosen*, 484 F.2d
  820 (D.C. Cir. 1973)).
- **Fees/costs**: available if the requester "substantially prevailed," including under a
  "catalyst theory" where the lawsuit prompted voluntary disclosure even without a court
  order (§ 552(a)(4)(E), post-2007 OPEN Government Act).

---

## Requester-Side Drafting Checklist

- [ ] Records reasonably described — dates, subject matter, specific record types,
      award/solicitation/contract numbers
- [ ] Correct component/address identified
- [ ] Fee category stated
- [ ] Fee waiver request with an affirmative 5-factor showing (if seeking one)
- [ ] Expedited processing certification, sworn "true and correct" (if seeking one)
- [ ] Format/production preference stated (electronic, searchable PDF, native format,
      rolling/interim production if volume is large)
- [ ] Segregability reminder ("release all reasonably segregable non-exempt portions")
- [ ] Foreseeable-harm reminder (agency must show harm, not just exemption-category fit)
- [ ] Request for a Vaughn-style log of any withholdings, even pre-litigation
- [ ] Statement of willingness to consult/narrow scope with the FOIA officer (helps avoid
      an "unduly burdensome" denial and often speeds processing)
- [ ] Cross-reference to any related prior FOIA requests/tracking numbers for continuity

---

## Template Structure — FOIA Request Letter

1. Requester identity + contact info + fee category
2. Statutory citation (5 U.S.C. § 552) + the agency's specific implementing regulation
3. Numbered, specific description of records sought
4. Fee waiver showing (if applicable)
5. Expedited processing certification (if applicable)
6. Format/production preference
7. Segregability & foreseeable-harm reminder
8. Response-deadline reminder (20 business days) + request for rolling production if delay
   is likely
9. Signature

## Template Structure — Administrative Appeal Letter

1. Identify the original request (tracking number, date filed, date of response)
2. State the specific determination being appealed (full denial / partial withholding /
   fee category / fee waiver denial / adequacy-of-search / "no records")
3. For each withheld exemption: argue why it doesn't apply, or why segregable portions
   were improperly withheld, or why foreseeable harm wasn't shown
4. For adequacy-of-search disputes: identify specific record types/custodians/systems the
   agency's search description suggests it did not check
5. Request a Vaughn index if none was provided
6. State the appeal deadline was met (calculate and show the date math)

---

## Key Cases (verify pinpoint cites before filing)

- *Food Marketing Institute v. Argus Leader Media*, 588 U.S. 427 (2019) — (b)(4) standard
- *Milner v. Dep't of Navy*, 562 U.S. 562 (2011) — narrowed (b)(2)
- *Dep't of Justice v. Reporters Comm. for Freedom of the Press*, 489 U.S. 749 (1989) —
  FOIA's "core purpose" is shedding light on what the government is up to; privacy/public
  interest balancing
- *NLRB v. Sears, Roebuck & Co.*, 421 U.S. 132 (1975) — deliberative-process vs. final
  opinion distinction
- *Vaughn v. Rosen*, 484 F.2d 820 (D.C. Cir. 1973) — Vaughn index requirement
- *Nat'l Archives & Records Admin. v. Favish*, 541 U.S. 157 (2004) — survivor privacy
  balancing under (b)(7)(C)

---

## Suggested Track Breakdown for a FOIA Matter

Unlike bankruptcy motion practice, a FOIA engagement is usually too small for six parallel
subagents. Typical shape:

| Track | Scope |
|---|---|
| 1 | Background research — confirm the correct agency component, prior public reporting, any related contract/procurement records already public (USASpending, SAM.gov, FPDS) so the request is precisely scoped |
| 2 | Draft the request letter — description of records, fee category, waiver/expedite showing |
| 3 (later) | Track the response deadline; if denied/partial, draft the administrative appeal |

Scale up to more tracks only if the matter involves parallel requests to multiple agencies
or components, or heads toward litigation (add a track for the Vaughn index challenge and
one for venue/exhaustion analysis).
