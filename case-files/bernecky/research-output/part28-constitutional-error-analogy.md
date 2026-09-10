# Part 28 — The "Constitutional Error Survives an Otherwise-Applicable Procedural Bar" Analogy: Verification of Three Sub-Claims (Stat-Max/Plea Waiver; Cause-and-Prejudice; Rule 52(b) Plain Error)

**United States v. Jeffrey Bernecky, No. 6:18-CR-06018-DGL-MWP (W.D.N.Y.) — Second Circuit**
**Prepared:** 2026-08-19
**Prepared by:** Researcher (subagent)
**For:** Coordinator / Writer (drafting-round backlog only — not authorized for insertion in any draft)
**File reference:** `case-files/bernecky/research-output/part28-constitutional-error-analogy.md`

**Scope.** Client directive logged at `client-directives.md`, entries of 2026-08-17 ("TWO ITEMS FOR THE NEXT DRAFTING ROUND," item 2, and "MORE ITEMS FROM THE CLIENT'S READ OF v4," item 5). The client, correcting the v4 report's earlier framing, asks for verification of an **analogy**, not of on-point supervised-release authority. He does not assert — and this memo does not revisit — any claim that § 3583(e)(2)'s changed-circumstances requirement has a constitutional carve-out. That question was answered in the negative in the earlier pass (*Kunz* n.14 / *Villafane-Lozada*), that finding stands, and nothing below disturbs it. What is verified here are three propositions drawn from **other** areas of federal criminal procedure, offered as persuasive analogy for asking this Court to reach the Special Condition (g) polygraph/Fifth Amendment question now:

1. A sentence exceeding the statutory maximum remains challengeable notwithstanding an otherwise-valid appellate- or collateral-attack waiver in a plea agreement.
2. Such a claim survives the cause-and-prejudice standard that would otherwise bar a procedurally defaulted claim.
3. On plain-error review, courts of appeals apply Rule 52(b) differently — less exactingly — when the unpreserved error is of constitutional significance.

**Methodology and source discipline.** The matter's Google Drive folder was searched first (`fullText contains 'statutory maximum' and fullText contains 'appeal waiver'`; `fullText contains 'cause and prejudice'`) and, as anticipated in the directive, contains **nothing** on these three doctrines. The two Drive documents that surfaced with adjacent subject matter — "Research Memorandum: Section 2255 Appeal" (Drive ID `1QBX1C1VaJ6VMvA8XK1RfKn1hpe1RybF86Z7zY22Lq6w`) and "Supervised Release Search Condition Analysis" — are from unrelated matters, carry the numbered-footnote/AI-generated fingerprint this matter's practice has learned to distrust, and were **not** used as authority for anything in this memo.

Everything below was verified against primary or near-primary source text. Sources actually opened and read this session:

- *Hunter v. United States*, No. 24–1063 — **full slip opinion PDF downloaded from supremecourt.gov and text-extracted locally** (syllabus, majority, all four separate writings' captions). This is the single most important source in the memo and it was read directly.
- *United States v. Sofsky*, 287 F.3d 122 (2d Cir. 2002) — full opinion text from `law.resource.org` (Public.Resource.Org's F.3d archive).
- *United States v. Gomez-Perez*, 215 F.3d 315 (2d Cir. 2000) — full opinion text from `law.resource.org`.
- *United States v. Torres*, 901 F.2d 205 (2d Cir. 1990) — full opinion text from `law.resource.org`.
- *United States v. Thomas*, 274 F.3d 655 (2d Cir. 2001) (en banc) — full opinion text from `law.resource.org`.
- *United States v. Marcus*, 560 U.S. 258 (2010) — full opinion text from Cornell LII.
- *United States v. Cotton*, 535 U.S. 625 (2002); *Puckett v. United States*, 556 U.S. 129 (2009); *Dretke v. Haley*, 541 U.S. 386 (2004); *Bousley v. United States*, 523 U.S. 614 (1998) — Cornell LII opinion pages.
- *United States v. Frady*, 456 U.S. 152 (1982) — FindLaw's reproduction of the U.S. Reports text.
- *Spence v. Superintendent, Great Meadow Corr. Facility*, 219 F.3d 162 (2d Cir. 2000); *United States v. Reeves* (2d Cir. 2010); *Dowell v. United States* (7th Cir. 2012) — FindLaw reproductions of the opinions.
- Brandon Hasbrouck, *Saving Justice: Why Sentencing Errors Fall Within the Savings Clause, 28 U.S.C. § 2255(e)*, 108 Geo. L.J. 287 (2019) — PDF downloaded and text-extracted; used as a **secondary source for case leads only**, per the secondary-sources-first sequencing, never as authority.

Sources that could **not** be opened this session (recurring in this matter): `law.justia.com` and `supreme.justia.com` (HTTP 403), CourtListener opinion pages and its REST API (HTTP 202 empty / 401 unauthenticated), Google Scholar (redirects to a sign-in interstitial), OpenJurist (403), Leagle (paywall truncation at the first paragraph). Where a passage below rests on one of those, or on a commercial database's rendering, it is flagged and appears again in the NOT VERIFIED section.

**No attorney marketing site was used for anything.** One institutional blog (Federal Defenders of New York, Second Circuit Blog) was used solely as a *lead* to case names, each of which was then run down independently.

---

## I. Introduction and Roadmap

This memo answers three questions with three different answers, and the differences matter.

**Sub-claim 1 is CONFIRMED, and it is now stronger and more directly useful to this matter than the client's own framing assumed.** Two months ago — on June 18, 2026 — the Supreme Court decided *Hunter v. United States*, 608 U.S. \_\_\_ (2026), an 8–1 decision by Justice Kagan holding that an appeal waiver is unenforceable when enforcing it would work a "miscarriage of justice." The Court then gave three illustrative categories, and the **second** of them is "a sentence infected with a blatant constitutional error, such as when a judge takes account of a constitutionally impermissible factor (like race) **or imposes a constitutionally infirm condition of supervised release**." That is not merely the client's analogy confirmed; it is the Supreme Court, this summer, naming an unconstitutional supervised-release condition as a paradigm case of an error too serious to be left standing behind an otherwise-valid procedural bar. Nothing else found in this research is worth as much to the motion.

**Sub-claim 2 is NOT CONFIRMED in the form the client stated it, and part of what is out there cuts the other way.** No authority was located holding that a claim the sentence exceeds the statutory maximum is exempt from, or gets a softened version of, the cause-and-prejudice showing. The Supreme Court's actual teaching runs the other direction: *Frady* holds that Rule 52(b)'s comparatively forgiving plain-error standard is displaced on collateral review by cause-and-prejudice, and *Frady*'s own claim was a constitutional one; *Bousley* applied ordinary procedural default to a constitutional claim. There **is** real doctrine in the neighborhood — § 2255(a)'s text, *Hill v. United States*'s "complete miscarriage of justice" cognizability threshold, and the Second Circuit's *Spence* "actual innocence of a noncapital sentence" gateway — but each of those is a different doctrinal move than the one the client described, and the closest-fitting line of authority (the § 2255(e) savings-clause cases treating an above-the-lawful-maximum sentence as a "fundamental defect") was largely knocked out by *Jones v. Hendrix* in 2023. The honest report is: the instinct is pointing at something real, but the doctrinal label the client attached to it does not survive checking.

**Sub-claim 3 is NOT CONFIRMED as stated; the modern rule is close to the opposite of the client's framing, and the Second Circuit in particular has been reversed for doing exactly what the client describes.** There is a genuine Second Circuit sentence saying that "errors of constitutional magnitude will be noticed more freely under the plain error rule than less serious errors" — *United States v. Torres*, 901 F.2d 205 (2d Cir. 1990) — but it is pre-*Olano*, it is a quotation from a 1977 Fifth Circuit case, the *Torres* panel itself immediately walked it back in the next paragraph, and in *United States v. Marcus*, 560 U.S. 258 (2010), the Supreme Court reversed the Second Circuit precisely for applying a relaxed plain-error standard to a constitutional (due-process/*ex post facto*-type) claim. Two narrower kernels of the client's point do survive and are usable: (a) the open question whether **structural** errors — a category that is entirely constitutional — automatically satisfy plain error's third prong; and (b) the Second Circuit's **own, still-cited relaxation of Rule 52(b) for unpreserved supervised-release conditions** under *United States v. Sofsky*, 287 F.3d 122, 125–26 (2d Cir. 2002). The *Sofsky* line is triggered by lack of notice and by the error being a sentencing error — **not** by constitutional significance — but it is a real, in-circuit, in-context example of an ordinarily rigid procedural standard bending, and it is a better fit for this matter than the proposition the client asked me to confirm.

Scope limitations discovered along the way: (i) *Hunter* is a **direct-appeal** waiver case; the Court did not address collateral-attack waivers, and the sub-claim-1 authority for collateral-attack waivers comes from the Seventh Circuit, not the Second; (ii) *Hunter* was decided after this matter's prior research passes and therefore does not appear anywhere in the existing part1–part27 memos, MASTER-OUTLINE.md, or MOTION-v4.md — it should be considered for the motion independent of whether the analogy argument is ever used.

---

## II. Issues and Summary Conclusions

**Issue 1.** Does a knowing and voluntary waiver of appeal (or of collateral attack) in a plea agreement bar a defendant's claim that the sentence imposed exceeds the statutory maximum — and, more generally, is there a recognized category of errors so serious that an otherwise-valid waiver will not be enforced against them?

> **Conclusion: CONFIRMED, at the Supreme Court level, as of June 18, 2026.** *Hunter v. United States*, 608 U.S. \_\_\_, No. 24–1063 (2026) (Kagan, J.). "An agreement not to appeal a sentence is unenforceable when it would result in a miscarriage of justice — meaning, when it would leave in place the kind of egregious error that would bring the judicial system into disrepute." Slip op. at 1 (syllabus, Held). A sentence exceeding the statutory maximum is the Court's **first** illustration; a "constitutionally infirm condition of supervised release" is expressly named within the **second**. Slip op. at 12. Second Circuit law is placed by *Hunter* in the majority camp via *United States v. Riggi*, 649 F.3d 143, 148 (2d Cir. 2011). For **collateral-attack** waivers the confirming authority is Seventh Circuit, not Second: *Keller v. United States*, 657 F.3d 675, 681 (7th Cir. 2011).

**Issue 2.** Is a claim that the sentence exceeds the statutory maximum excused from — or treated more leniently under — the "cause and actual prejudice" showing that otherwise excuses a procedural default on collateral review?

> **Conclusion: NOT CONFIRMED as framed. CONFIRMED in a materially different form, with one adjacent line of authority now abrogated.** No case was located holding that a stat-max claim is exempt from cause-and-prejudice. What the case law actually supplies is three different things: (a) § 2255(a) makes "in excess of the maximum authorized by law" an enumerated ground for relief, so the claim clears the *cognizability* threshold of *Hill v. United States*, 368 U.S. 424, 428 (1962), that ordinary guideline-misapplication claims fail; (b) the Second Circuit recognizes an **alternative** gateway — actual innocence of a noncapital sentence — that operates *instead of* cause-and-prejudice, *Spence v. Superintendent*, 219 F.3d 162 (2d Cir. 2000), a minority position the Supreme Court pointedly declined to endorse in *Dretke v. Haley*, 541 U.S. 386 (2004); and (c) the savings-clause cases treating a sentence "exceed[ing] that permitted by law" as a "miscarriage of justice," e.g., *Brown v. Caraway*, 719 F.3d 583, 587–88 (7th Cir. 2013), and *United States v. Wheeler*, 886 F.3d 415, 429 (4th Cir. 2018), were superseded by *Jones v. Hendrix*, 599 U.S. 465 (2023). Adverse authority the Writer must know about: *United States v. Frady*, 456 U.S. 152 (1982), and *Bousley v. United States*, 523 U.S. 614 (1998), both apply the ordinary default framework to constitutional claims.

**Issue 3.** Do courts of appeals apply Rule 52(b)'s four-part plain-error standard less exactingly when the unpreserved error is constitutional in nature?

> **Conclusion: NOT CONFIRMED as framed; the modern Supreme Court rule is materially contrary, and the Second Circuit was reversed in 2010 for the very practice described.** *United States v. Marcus*, 560 U.S. 258 (2010), rejected the Second Circuit's relaxed standard for an unpreserved constitutional claim and said flatly that the constitutional "rights at issue in this case … do not differ significantly in importance from the constitutional rights at issue in other cases where we have insisted upon a showing of individual prejudice." *United States v. Cotton*, 535 U.S. 625 (2002), applied ordinary plain error to a forfeited *Apprendi* claim that had produced a sentence above the otherwise-applicable statutory maximum and **denied relief** at the fourth prong. Two narrower kernels survive: the reserved structural-error question (*Olano*, 507 U.S. at 735; *Johnson*, 520 U.S. at 469; *Cotton*, 535 U.S. at 632; *Puckett*, 556 U.S. at 140–41), and the Second Circuit's *Sofsky* relaxation for unpreserved supervised-release conditions, 287 F.3d at 125–26 — the latter keyed to **notice**, not to constitutional significance.

---

## III. Facts Relevant to the Research (stated objectively, including unknowns)

1. Mr. Bernecky is serving a term of supervised release imposed in W.D.N.Y. under Judgment, Dkt. No. 28. The pending motion is under 18 U.S.C. § 3583(e)(2) to modify conditions.
2. **Unknown / not established for purposes of this memo:** whether Mr. Bernecky's own plea agreement contains an appellate or collateral-attack waiver, and if so what it covers. The case file materials reviewed for this memo do not establish it. **This matters**: the analogy below can be presented without any assertion about his own waiver, and — because a waiver's existence and scope is exactly the sort of fact the government would correct — nothing in the eventual draft should assume one either way absent confirmation from the Judgment and plea documents.
3. **Not applicable, and this is favorable:** nothing in this research suggests Mr. Bernecky's sentence exceeds any statutory maximum. The stat-max cases are being used purely as analogical material about how procedural bars behave, not as a claim about his sentence.
4. Special Condition (g) — the compelled-answer polygraph structure — is the condition the constitutional argument targets. The § 3583(e)(2) motion is a district-court modification proceeding, not a direct appeal and not a § 2255 motion. **This is the central structural weakness of the analogy** and is discussed candidly in Part VII.
5. The polygraph timing argument in MOTION-v4.md currently rests on an actual changed circumstance, not on any constitutional carve-out. That is unaffected by anything here.

---

## IV. Discussion — Issue 1: The Stat-Max/Plea-Waiver Proposition

### A. The rule, as of two months ago: *Hunter v. United States*

The controlling authority is now a Supreme Court decision handed down **June 18, 2026**, well after the last research pass in this matter. It postdates every part1–part27 memo and does not appear in MOTION-v4.md.

*Hunter v. United States*, No. 24–1063, 608 U.S. \_\_\_ (2026). Kagan, J., delivered the opinion of the Court, joined by Roberts, C.J., and Alito, Sotomayor, Gorsuch, Kavanaugh, Barrett, and Jackson, JJ. Gorsuch, J., filed a concurrence joined by Sotomayor and Jackson, JJ.; Kavanaugh, J., filed a concurrence joined by Alito and Barrett, JJ.; Barrett, J., filed a concurrence; Thomas, J., dissented alone. Argued March 3, 2026.

**The holding, verbatim from the syllabus:**

> "**Held:** An agreement not to appeal a sentence is unenforceable when it would result in a miscarriage of justice—meaning, when it would leave in place the kind of egregious error that would bring the judicial system into disrepute. Pp. 5–14."

**The corresponding sentence in the opinion of the Court (slip op. 11):**

> "We thus approve the majority view among the courts of appeals that an appeal waiver is unenforceable when it would result in a miscarriage of justice. That rule, properly understood and applied, sets a high bar: The waiver may be set aside only if the sentence is marred by the kind of egregious error that would bring the judicial system into disrepute. The error must be obvious—not one a judge could reasonably make. And it must be of the type that would undermine public confidence in the judiciary."

**The three illustrative categories (slip op. 12) — read this passage in full, because its second category is directly about this matter:**

> "The nature of the miscarriage-of-justice limit precludes any attempt to list all the situations in which it will overcome an appeal waiver. Extreme cases, after all, are hard to anticipate before they happen. But a few examples of the kinds of errors we mean—the kind that would bring the judiciary into disrepute—may provide guidance to lower courts. First, a defendant may appeal a sentence exceeding what the relevant statute allows—most commonly, a term of years above the maximum prescribed. See, e.g., Kim, 988 F. 3d, at 810–811, and n. 1; supra, at 10. Second, a defendant may appeal a sentence that is infected with a blatant constitutional error, such as when a judge takes account of a constitutionally impermissible factor (like race) or imposes a constitutionally infirm condition of supervised release (like barring a defendant from becoming pregnant). See, e.g., United States v. Elliott, 264 F. 3d 1171, 1173 (CA10 2001); supra, at 11. And third, a defendant may appeal if his sentence was imposed without 'some minimum of civilized procedure' as in, yes, the 'twelve orangutans' case—or less extravagantly, one in which the judge refused to hold a hearing consonant with basic principles of law. United States v. Adkins, 743 F. 3d 176, 192–193 (CA7 2014); see United States v. Behrens, 375 U. S. 162, 165–166 (1963). These examples are just examples, not intended to be exclusive, but they serve to illustrate the high bar a defendant must surmount to overcome an appeal waiver."

**The reasoning the client's analogy actually wants** — the Court's explanation of *why* a party-created bar yields — is at slip op. 10–11 and in the syllabus at 2–3:

> "Because that is so, the standard for enforcing appeal waivers implicates the interests not only of the plea agreement's parties, but also of the judiciary. If a court always enforces appeal waivers regardless of the kind or degree of error tainting a sentence, the judicial system's integrity may come into question."

and, from the opinion of the Court (slip op. 10–11):

> "The Government's maximalist position first runs into the scenario that even the Fifth Circuit will not tolerate: when a judge imposes on a defendant who has signed an appeal waiver a sentence beyond what the relevant statute allows. … Suppose, for example, that a judge sentences a misdemeanant to life in prison, when the applicable law caps a prison term at one year. If an appellate court had to dismiss the resulting appeal, it would call into doubt the judicial system's very attachment to law."

**Validation:** *Hunter* was decided June 18, 2026. It vacated and remanded to the Fifth Circuit. It is the freshest possible authority and cannot have been overruled. The slip opinion carries the standard "subject to formal revision before publication in the United States Reports" notice, so pin cites should be given as slip-opinion pages until the U.S. Reports pagination issues. The Justia reporting of the volume as 608 U.S. \_\_\_ is consistent with the slip opinion's own running head ("Cite as: 608 U. S. \_\_\_ (2026)").

### B. That the stat-max exception pre-existed *Hunter* — and was universal

*Hunter*'s significance for the analogy is not that it *created* the stat-max exception; it is that it confirmed the exception at the Supreme Court level **and enlarged the surrounding category**. Before *Hunter*, the Fifth Circuit — the **most** waiver-enforcing circuit in the country, the one whose rule *Hunter* rejected as too narrow — already recognized only two exceptions, one of which was a sentence exceeding the statutory maximum. From the *Hunter* syllabus (slip op. 2, describing the decision below):

> "…under Circuit precedent the 'general rule' that appeal waivers are enforceable has only two exceptions: when the waiver was tainted by ineffective assistance of counsel and when the sentence exceeded the statutory maximum."

The Fifth Circuit cases are *United States v. Barnes*, 953 F.3d 383, 388–389 (5th Cir. 2020), and *United States v. White*, 307 F.3d 336, 339 (5th Cir. 2002), both cited in the *Hunter* opinion at slip op. 4; the operative reasoning is quoted by the *Hunter* Court from *United States v. Kim*, 988 F.3d 803, 810 n.1 (5th Cir. 2021), which declined to enforce an appeal waiver in such a case because of "the legal truism that a court must not impose a sentence" that is "unauthorized by law."

**This is the strongest possible form of the client's point on sub-claim 1**: the stat-max exception is the one thing that survived even in the circuit that recognized almost nothing else, and the Supreme Court used it as its lead example.

The majority ("miscarriage of justice") circuits are collected in *Hunter*'s footnote 1 (slip op. 4–5): *United States v. Boudreau*, 58 F.4th 26, 33 (1st Cir. 2023); *United States v. Khattak*, 273 F.3d 557, 562 (3d Cir. 2001); *United States v. Smith*, 134 F.4th 248, 261 (4th Cir. 2025); *United States v. Andis*, 333 F.3d 886, 891–892 (8th Cir. 2003) (en banc); *United States v. Wells*, 29 F.4th 580, 583 (9th Cir. 2022); *United States v. Holzer*, 32 F.4th 875, 886 (10th Cir. 2022); *United States v. Guillen*, 561 F.3d 527, 531–532 (D.C. Cir. 2009).

### C. Second Circuit law

**The Second Circuit is placed in the majority camp by *Hunter* itself.** Footnote 1 closes: "see also United States v. Riggi, 649 F. 3d 143, 148 (CA2 2011) (adopting a differently framed but substantively similar exception)." That is the Supreme Court's own characterization of Second Circuit law, and it is quotable as such.

*Riggi*'s framing, as best it can be recovered, is that "[a] violation of a fundamental right warrants voiding an appeal waiver," and that the "exceptions to the presumption of the enforceability of a waiver … occupy a very circumscribed area of our jurisprudence." **[VERIFY]** — the *Riggi* opinion text itself could not be opened this session; that sentence was recovered from a commercial database's rendering (vLex) and independently corroborated by a search-result excerpt, which is **(b)**-tier, not **(a)**-tier. Before the sentence is quoted in any filing, the slip opinion or F.3d text must be read. The "very circumscribed area" phrase, however, **is** independently confirmed at (a)-tier: it originates in *Gomez-Perez* (below) and was read there in full.

The canonical Second Circuit statement of the exceptions is *United States v. Gomez-Perez*, 215 F.3d 315 (2d Cir. 2000), read in full this session:

> "In some cases, a defendant may have a valid claim that the waiver of appellate rights is unenforceable, such as when the waiver was not made knowingly, voluntarily, and competently, see United States v. Ready, 82 F.3d 551, 556-57 (2d Cir. 1996), when the sentence was imposed based on constitutionally impermissible factors, such as ethnic, racial or other prohibited biases, see Jacobson, 15 F.3d at 22-23, when the government breached the plea agreement, see Rosa, 123 F.3d at 98 …, or when the sentencing court failed to enunciate any rationale for the defendant's sentence, thus 'amount[ing] to an abdication of judicial responsibility subject to mandamus.' Yemitan, 70 F.3d at 748."

> "These exceptions to the presumption of the enforceability of a waiver, however, occupy a very circumscribed area of our jurisprudence."

**Two things must be said honestly about *Gomez-Perez*, and the second helps.**

*First, the adverse point:* that enumerated list does **not** include a sentence exceeding the statutory maximum. Nor did any Second Circuit case located in this research say in terms that a waiver does not bar a stat-max claim. If the Writer states flatly that "the Second Circuit holds a plea waiver does not bar a claim that the sentence exceeds the statutory maximum," that sentence will not survive a check. The correct statement is that *Hunter* now supplies that rule as binding Supreme Court law in every circuit, and that the Second Circuit's own pre-*Hunter* framework was already "substantively similar" by the Supreme Court's own reckoning.

*Second, the helping point:* *Gomez-Perez* expressly disclaims exhaustiveness, and does so in language that is itself useful:

> "This being so, our above recitation of cases representing prior circumstances in which we have held waivers unenforceable should in no way be considered exhaustive."

and, earlier in the same opinion, the court directed counsel preparing an *Anders* brief to address

> "any issues implicating a defendant's constitutional or statutory rights that either cannot be waived, or cannot be considered waived by the defendant in light of the particular circumstances."

That last clause — a Second Circuit court, in 2000, contemplating a category of constitutional and statutory rights that simply "cannot be waived" — is the in-circuit hook for the client's analogy, and it was read in the actual opinion text.

**Validation of *Gomez-Perez*:** still routinely cited in the Second Circuit for the "very circumscribed area" formulation, including in *United States v. Lewis*, No. 14-4552-cr (2d Cir. 2017), read this session. No indication of reversal or abrogation; *Hunter* supplements rather than displaces it. **[VERIFY]** — no commercial citator (Shepard's/KeyCite) was available this session; validation here rests on later opinions found citing the case approvingly, which is a weaker substitute and should be redone before filing.

### D. Collateral-attack waivers — Seventh Circuit, not Second

*Hunter* is an appeal-waiver case. The Court did not address waivers of collateral attack, and the sub-claim-1 authority for those comes from elsewhere. The cleanest statement located, quoted verbatim by the Seventh Circuit in *Dowell v. United States*, No. 10–2912 (7th Cir. 2012) (read this session):

> "There are only limited instances when we will not enforce a knowing and voluntary waiver of direct appeal or collateral review, including when the sentence exceeds the statutory maximum, when the plea or court relies on a constitutionally impermissible factor like race, or when counsel is ineffective in the negotiation of the plea agreement." *Keller v. United States*, 657 F.3d 675, 681 (7th Cir. 2011).

**[VERIFY]** — *Keller*'s own text was not opened; the quotation and pin cite come from *Dowell*'s reproduction of it, which is a court opinion quoting a court opinion (better than a treatise, short of reading *Keller* itself).

Second Circuit law on collateral-attack waivers runs the other way on the facts of the cases located — *Sanford v. United States*, 841 F.3d 578 (2d Cir. 2016), and *Cook v. United States* (2d Cir. 2023/2024) both **enforced** collateral-attack waivers — but neither involved a stat-max claim, so neither is contrary authority on this point. **[VERIFY]** — neither *Sanford* nor *Cook* was read in full; they are noted here only so the Writer knows the terrain and does not overclaim.

### E. Counter-authority the Writer must anticipate

- **Thomas, J., dissenting** in *Hunter* would have enforced the waiver categorically. A single dissent does not weaken the holding, but the government will emphasize that the Court called the standard "a high bar."
- **Kavanaugh, J., concurring** (joined by Alito and Barrett, JJ.) wrote separately for the express purpose of insisting on the narrowness of the exception: "The Court's opinion sets a 'high bar' … The Court describes the exception as applying in 'extreme cases' to sentencing errors that are 'egregious' and 'obvious' and that 'undermine public confidence in the judiciary.'" He then stated his disagreement with Justice Gorsuch's broader reading. **Three Justices signed a concurrence whose only purpose was to keep the exception narrow.** Any draft that presents *Hunter* as a generous, open-ended constitutional escape hatch will be met with that concurrence.
- ***Hunter* did not decide whether Hunter won.** The Court expressly declined to say whether the mandatory-medication condition met the standard, remanding to the Fifth Circuit. Slip op. 13–14. So *Hunter* establishes the category; it does not establish that a challenged supervised-release condition clears it.

---

## V. Discussion — Issue 2: Cause and Prejudice

### A. What the client's framing would require, and why it fails

The claim as stated is that a stat-max challenge "can even survive the cause and prejudice test." Read strictly, that would mean either (i) such a claim is exempt from the cause-and-prejudice requirement, or (ii) a relaxed version applies. **No authority was located for either proposition, and the Supreme Court authority located points the other way.**

**The controlling adverse case is *United States v. Frady*, 456 U.S. 152 (1982)** — and it is adverse in a way that is specifically damaging to the client's broader intuition, because *Frady*'s claim **was** constitutional (a due-process challenge to a malice jury instruction), and the Court's answer was to impose a **stricter**, not looser, standard on collateral review:

> "the 'plain error' standard is out of place when a prisoner launches a collateral attack" (456 U.S. at 164);

> "to obtain collateral relief a prisoner must clear a significantly higher hurdle than would exist on direct appeal" (456 U.S. at 166–67);

> "to obtain collateral relief based on trial errors to which no contemporaneous objection was made, a convicted defendant must show both (1) 'cause' excusing his double procedural default, and (2) 'actual prejudice'" (456 U.S. at 167–68).

**[VERIFY]** — the *Frady* text was read through FindLaw's reproduction of the U.S. Reports, not from a court-issued PDF; the three pin cites above are FindLaw's and should be confirmed against 456 U.S. before quotation.

***Bousley v. United States*, 523 U.S. 614 (1998)** compounds the problem. Bousley's claim was that his guilty plea was not knowing and intelligent — a core constitutional claim — and the Court still applied ordinary default analysis:

> "Where a defendant has procedurally defaulted a claim by failing to raise it on direct review, the claim may be raised in habeas only if the defendant can first demonstrate either 'cause' and actual 'prejudice,' … or that he is 'actually innocent.'"

Taken together, *Frady* and *Bousley* stand for a proposition directly at odds with the general shape of the client's instinct: **the constitutional character of a claim does not, by itself, loosen a procedural-default bar.**

### B. What *is* real in this neighborhood — three distinct doctrines, none of them the one described

**(1) Cognizability, not default: § 2255(a) and *Hill*.** Section 2255(a) makes "that the sentence was in excess of the maximum authorized by law" an **enumerated statutory ground** for relief. That is why an above-the-max sentence clears the cognizability threshold of *Hill v. United States*, 368 U.S. 424, 428 (1962) — the requirement of "a fundamental defect which inherently results in a complete miscarriage of justice" — that ordinary guideline-misapplication claims do not. **This is a genuine and citable point, and it is probably the real source of the client's instinct.** But it answers a different question than default: it answers *whether the claim can be heard at all if it gets past the default rules*, not *whether the default rules apply*. Conflating the two is exactly the framing error the directive asked me to guard against.

**(2) An alternative gateway, not a softened test: actual innocence of a noncapital sentence.** The Second Circuit is one of the few circuits to hold that the "actual innocence" gateway — which operates **instead of** cause-and-prejudice, not as a relaxed version of it — reaches noncapital sentencing. *Spence v. Superintendent, Great Meadow Correctional Facility*, 219 F.3d 162 (2d Cir. 2000):

> "Accordingly, we hold that in these circumstances, the actual innocence exception applies to the sentencing phase of a noncapital trial."

The *Spence* court restated the ordinary framework as a two-path structure: a defaulted claim is barred unless the petitioner can "(1) show cause for the default and actual prejudice" or "(2) demonstrate that failure to consider the federal claim will result in a 'fundamental miscarriage of justice.'"

**This is genuinely favorable material for the analogy** — a Second Circuit holding that an ordinarily-applicable procedural bar gives way where the underlying defect goes to the justice of the sentence itself — but it comes with two hard limits. First, it is about *innocence of a sentencing predicate*, not about a sentence exceeding a statutory cap. Second, the Supreme Court **declined to adopt it**. In *Dretke v. Haley*, 541 U.S. 386 (2004), the Court was "asked … to extend the actual innocence exception to procedural default of constitutional claims challenging noncapital sentencing error," noted a "growing divergence of opinion in the Courts of Appeals," and expressly did not decide the question, holding instead that a court "must first address all nondefaulted claims for comparable relief." Anyone citing *Spence* must be ready for *Dretke*. **[VERIFY]** — *Spence* and *Dretke* were read through FindLaw and Cornell LII respectively; pin cites within them were not captured and must be added before any quotation is used.

**(3) A line that once said exactly this, and is now largely gone.** The closest thing in the reports to "an above-the-lawful-maximum sentence overcomes an otherwise-applicable collateral bar" was the § 2255(e) savings-clause jurisprudence. *Brown v. Caraway*, 719 F.3d 583, 587–88 (7th Cir. 2013), held that "a miscarriage of justice occurs when a federal prisoner's sentence 'exceed[s] that permitted by law'"; *Hill v. Masters*, 836 F.3d 591, 599 (6th Cir. 2016), and *United States v. Wheeler*, 886 F.3d 415, 429 (4th Cir. 2018), were to like effect. **Those cases have been superseded.** *Jones v. Hendrix*, 599 U.S. 465 (2023) (Thomas, J.), held that "[s]ection 2255(e) does not allow a prisoner asserting an intervening change in interpretation of a criminal statute to circumvent AEDPA's restrictions on second or successive § 2255 motions by filing a § 2241 habeas petition."

**This is precisely why the citator step exists.** Those three case names are exactly what a search for the client's proposition surfaces first; all three would have been cited confidently; all three would have been wrong. They are recorded here so that nobody in this matter cites them later without the *Jones v. Hendrix* caveat. (Source note: the three case leads came from the Hasbrouck Georgetown Law Journal article, a secondary source, and are reported here at that tier — the underlying opinions were **not** read. **[VERIFY]**. The *Jones v. Hendrix* holding, by contrast, was confirmed independently.)

### C. Bottom line on Issue 2

The accurate statement, if this ever goes into a draft, is something like: *a claim that the sentence exceeds the statutory maximum is one of the few sentencing claims Congress made cognizable on collateral review by name, 28 U.S.C. § 2255(a), and the only category of sentencing error courts have consistently described as a "complete miscarriage of justice" in the sense Hill requires.* That is defensible. **"It survives cause and prejudice" is not**, and should not be written.

---

## VI. Discussion — Issue 3: Rule 52(b) and Constitutional Error

### A. There is a real Second Circuit sentence saying what the client says

*United States v. Torres*, 901 F.2d 205 (2d Cir. 1990), read in full this session:

> "In making this assessment, 'we are reminded that errors of constitutional magnitude will be noticed more freely under the plain error rule than less serious errors, and that a closer scrutiny may also be appropriate "when the failure to preserve the precise grounds for error is mitigated by [an objection] on related grounds."' United States v. Brown, 555 F.2d 407, 420 (5th Cir.1977) (quoting United States v. Meadows, 523 F.2d 365, 368 n. 3 (5th Cir.1975))…"

**Four qualifications, all of which appear in the same opinion or in later Supreme Court authority, and all of which the government would find immediately:**

1. It is a **quotation from the Fifth Circuit's 1977 decision in *Brown***, not an original Second Circuit formulation.
2. It is **pre-*Olano***. *United States v. Olano*, 507 U.S. 725 (1993), supplied the four-part framework that governs today; *Torres* predates it by three years and does not apply it.
3. **The *Torres* panel walked it back in the very next paragraph:**

   > "As the Civelli formulation makes clear, however, the plain error doctrine is to be used sparingly. … Despite the inclination to invoke the doctrine more freely where constitutional error might otherwise pass without correction, furthermore, it is established that an ex post facto challenge to a jury instruction can be waived."

   The panel invoked the proposition and then declined to give it effect, in an *ex post facto* context — the same context in which the Second Circuit was later reversed.
4. **[VERIFY] the pin cite.** The Public.Resource.Org text of *Torres* carries no star pagination. The page is commonly given as 901 F.2d at 228; that figure comes from the Solicitor General's merits brief in *Marcus*, an advocacy document, not from the reporter. Confirm against F.2d before quoting.

### B. The modern rule, and the Second Circuit's own reversal

***United States v. Marcus*, 560 U.S. 258 (2010)**, read in full, is the case that ends this argument in its broad form. The Second Circuit had held that an unpreserved constitutional error required reversal if there were "any possibility, no matter how unlikely," that the jury convicted on preenactment conduct. The Supreme Court's response:

> "This standard is irreconcilable with our 'plain error' precedent."

And on whether the constitutional character of the right changes the calculus (slip op.; 560 U.S. at 266–67):

> "In any event, however Marcus' claim is labeled, we see no reason why this kind of error would automatically 'affect substantial rights' without a showing of individual prejudice."

> "Moreover, while the rights at issue in this case are important, they do not differ significantly in importance from the constitutional rights at issue in other cases where we have insisted upon a showing of individual prejudice."

And on the fourth prong:

> "In cases applying this fourth criterion, we have suggested that, in most circumstances, an error that does not affect the jury's verdict does not significantly impugn the 'fairness,' 'integrity,' or 'public reputation' of the judicial process."

***United States v. Cotton*, 535 U.S. 625 (2002)**, read this session, is the closest thing in the reports to a direct test of the client's combined intuition — a **constitutional** (*Apprendi*) error that produced a sentence **above the otherwise-applicable statutory maximum**, unpreserved. The Court applied ordinary Rule 52(b) analysis and **denied relief** at the fourth prong, because the evidence of drug quantity was "overwhelming" and "essentially uncontroverted." If constitutional significance softened Rule 52(b), *Cotton* would have come out the other way.

***Puckett v. United States*, 556 U.S. 129 (2009)**, read this session, confirms that the Court has repeatedly reserved — never adopted — the only genuinely constitutional-specific relaxation on offer:

> "This Court has several times declined to resolve whether 'structural' errors … automatically satisfy the third prong of the plain-error test."

### C. The two kernels that do survive

**(1) Structural error.** The reserved question is real and is entirely a constitutional-error question, since every recognized structural error is a constitutional one. The reservations are collected in *Marcus* itself: *Puckett*, 556 U.S. at 140–41; *Cotton*, 535 U.S. at 632; *Johnson v. United States*, 520 U.S. 461, 469 (1997); *Olano*, 507 U.S. at 735. But *Marcus* also states the limit: structural errors are "a very limited class" affecting the "framework within which the trial proceeds," and "if the defendant had counsel and was tried by an impartial adjudicator, there is a strong presumption that any other errors that may have occurred" are not structural. A sentencing-condition challenge is a poor candidate for this category.

**(2) The Second Circuit's *Sofsky* relaxation — the finding most worth carrying forward.** *United States v. Sofsky*, 287 F.3d 122 (2d Cir. 2002), read in full this session, is a real, in-circuit, **supervised-release-condition** case in which the Second Circuit declined to apply Rule 52(b) with full rigor:

> "Accordingly, although the Government is correct that plain error review applies, it appears that in the sentencing context there are circumstances that permit us to relax the otherwise rigorous standards of plain error review to correct sentencing errors."

> "In the pending appeal, the challenged condition of supervised release was not recommended in the PSR, and Sofsky had no prior knowledge that it would be imposed. Both because the alleged error relates only to sentencing and because Sofsky lacked prior notice, we will entertain his challenge without insisting on strict compliance with the rigorous standards of Rule 52(b)."

The Second Circuit restated and applied this in *United States v. Reeves* (2d Cir. 2010) (read this session): "The government does not contest that, even though Reeves did not object to the challenged condition at sentencing, we apply a relaxed plain error review here because he did not receive prior notice of the condition and the error relates only to sentencing."

**Be precise about what this is and is not.** The *Sofsky* trigger is (a) lack of prior notice of the condition and (b) the error being a sentencing error. It is **not** constitutional significance. Presenting it as a constitutional-error doctrine would misstate it. But as an example of the proposition the client is actually driving at — *an ordinarily rigid procedural standard bends when the underlying defect is serious enough and the defendant had no fair chance to raise it* — it is better in every respect than *Torres*: it is post-*Olano*, it is about supervised-release conditions specifically, and it is the Second Circuit's own.

**(3) A third line, noted for completeness and flagged as uncertain.** The Second Circuit has also applied a "modified plain error rule" shifting the burden of persuasion on prejudice to the Government where "the source of the alleged error is a supervening judicial decision that alters 'a settled rule of law in the circuit.'" *United States v. Thomas*, 274 F.3d 655 (2d Cir. 2001) (en banc), read in full this session, describing *United States v. Santiago*, 238 F.3d 213, 215 (2d Cir. 2001), and *United States v. Viola*, 35 F.3d 37, 42 (2d Cir. 1994). **But *Thomas* expressly reserved its continuing vitality**, noting the Government's contention that *Johnson v. United States*, 520 U.S. 461 (1997), had "implicitly overruled" it, and holding: "We need not address the continuing vitality of our modified plain error jurisprudence in this case, because … the defendant here prevails under ordinary plain error review." **[VERIFY]** — the current status of the Second Circuit's modified-plain-error rule after *Cotton* (2002) and *Marcus* (2010) was **not** determined in this research and should not be assumed. Like *Sofsky*, this rule's trigger is a change of law, not constitutional significance.

### D. Contemporary check

The most recent Second Circuit data point found: *United States v. McCrone*, No. 22-3178(L) (2d Cir. July 21, 2026), holding that a "continue to take any prescribed medications" condition of supervised release is plainly erroneous absent medically grounded, on-the-record findings of necessity under § 3583(d)(1) and an express § 3583(d)(2) finding. The panel applied **ordinary** plain error, acknowledged that compelled medication implicates "a substantial liberty interest," and resolved the case on statutory grounds while expressly leaving the constitutional questions open. **[VERIFY]** — *McCrone* is reported here from a Federal Defenders blog summary used as a lead; the opinion was **not** read, and the docket number, date, and holding all require confirmation before use. It is included because, if accurate, it is both (i) further evidence that the Second Circuit does not soften Rule 52(b) for constitutionally-inflected conditions, and (ii) potentially valuable to this matter on its own terms, given that the Bernecky judgment's conditions include treatment requirements.

---

## VII. Conclusion — Which Side Has the Better Argument, and How Confident

**Issue 1 — the client is right, and *Hunter* makes him more right than he knew.** High confidence. *Hunter v. United States* is two months old, is an 8–1 Supreme Court holding, and its second illustrative miscarriage-of-justice category names "a constitutionally infirm condition of supervised release" in terms. For an argument that a constitutional defect in a supervised-release condition is the kind of thing courts do not leave standing behind a procedural bar, this is as good as authority gets. The only qualifications are the ones the Court itself and three concurring Justices supplied: the bar is high, the error must be obvious, and *Hunter* did not decide that any particular condition clears it.

**Issue 2 — the client is wrong as stated, and the correction is not cosmetic.** High confidence. The framing "survives the cause-and-prejudice test" does not correspond to any located holding, and *Frady* and *Bousley* — both constitutional claims subjected to ordinary default analysis — make the general premise unsafe. What is true is narrower and belongs to a different doctrine (cognizability under § 2255(a) and *Hill*), plus a separate and contested gateway (*Spence*, unendorsed in *Dretke*). The savings-clause cases that once said something close to the client's proposition are gone after *Jones v. Hendrix*.

**Issue 3 — the client is wrong as stated, and the Second Circuit is the circuit that got reversed for it.** High confidence on the general proposition; moderate confidence on the surviving kernels. *Torres* really does contain the sentence, but it is pre-*Olano*, borrowed, and self-limited; *Marcus* is a Supreme Court reversal of the Second Circuit for exactly this move; *Cotton* is a worked example of a constitutional error producing an above-the-max sentence and still losing on plain error. The recoverable material is (a) the reserved structural-error question, and (b) *Sofsky*'s relaxation — which is real and in-context but keyed to notice, not to the Constitution.

**The structural weakness of the analogy as a whole, stated plainly because the Writer needs it before drafting.** Every confirmed instance of a bar yielding to a constitutional claim — *Hunter*, *Sofsky*, the structural-error reservation — involves an **appellate court** deciding how much rigor to give a **judge-made or party-made** procedural rule in a proceeding where the court's own institutional integrity is implicated. *Hunter*'s reasoning is explicit about this: the waiver yields because "the courts are too enmeshed in its approval and implementation to escape responsibility for such results." Section 3583(e)(2)'s changed-circumstances requirement is a different animal: it is a limit derived from the modification statute and circuit precedent on a **district court's** authority to revisit its own judgment, and no court has an institutional-integrity interest in relaxing it. A judge who reads the analogy carefully will see that gap. The analogy is therefore usable as **rhetorical reinforcement** for a timing argument that already stands on its own changed-circumstances footing — it is not a substitute for that footing, and it should not be positioned as one.

---

## VIII. Recommendations

1. **Bring *Hunter v. United States* into this matter regardless of what happens to the analogy argument.** It is a June 2026 Supreme Court decision that names an unconstitutional supervised-release condition as a paradigm miscarriage of justice, and it postdates every research pass in this file. At minimum it belongs in the Fifth Amendment/polygraph section as an expression of how seriously the Supreme Court treats constitutionally infirm supervised-release conditions. Consider whether it also bears on any other section. **Client decision required — this memo does not authorize any drafting.**
2. **If the analogy is used, build it on *Hunter*, not on Rule 52(b).** Sub-claim 3 in its stated form cannot be written without inviting a *Marcus* citation in the government's response. Sub-claim 1 can be written as stated and then some.
3. **Substitute *Sofsky* for *Torres* wherever the plain-error point is made.** *Sofsky*, 287 F.3d at 125–26, gives the Second Circuit relaxing Rule 52(b) for an unpreserved supervised-release condition, in the client's own circuit, post-*Olano*, with verbatim language confirmed at (a)-tier this session. Describe its trigger accurately (lack of notice; sentencing-only error), not as a constitutional-significance rule.
4. **Do not write "survives cause and prejudice."** If a collateral-review point is wanted at all, the safe form is that Congress made an above-the-maximum sentence an enumerated § 2255(a) ground and that it is the paradigm "complete miscarriage of justice" under *Hill*.
5. **Never cite *Brown v. Caraway*, *Hill v. Masters*, or *United States v. Wheeler* in this matter without the *Jones v. Hendrix* caveat.** They surface first on any search of this topic and they are no longer good law for the proposition they are cited for.
6. **Confirm before any of this is filed:** (a) whether Mr. Bernecky's plea agreement contains an appellate or collateral-attack waiver and what it covers; (b) the *Riggi* text at 649 F.3d 148; (c) the *Torres* pin cite at 901 F.2d 228 if that sentence is used at all; (d) *McCrone*'s docket number, date, and holding; (e) the current vitality of the Second Circuit's modified-plain-error rule; and (f) a real citator run on every case in this memo.
7. **Consider whether *McCrone* deserves its own research pass.** If the summary is accurate, a July 2026 Second Circuit decision requiring individualized, on-the-record findings before a treatment-adjacent condition may be imposed is potentially significant to this motion independent of the analogy question.

---

## IX. NOT VERIFIED

Listed explicitly so that none of it can quietly read as settled to the next reader.

1. **The *Riggi* sentence** — "A violation of a fundamental right warrants voiding an appeal waiver," attributed to 649 F.3d at 148 — was recovered from a commercial database rendering (vLex) and a corroborating search excerpt. **The opinion text was not opened.** CourtListener returned an empty body; Justia, FindLaw's *Riggi* page, OpenJurist, and Google Scholar were all inaccessible this session; Public.Resource.Org's F.3d archive does not reach volume 649. *Hunter*'s footnote-1 characterization of *Riggi* ("adopting a differently framed but substantively similar exception") **is** (a)-tier, because it was read in the slip opinion.
2. **The *Torres* pin cite (901 F.2d at 228).** The quotation itself is (a)-tier — read in the full opinion text. The page number is not; it comes from the Solicitor General's *Marcus* merits brief.
3. **The *Frady* pin cites (456 U.S. at 164, 166–67, 167–68).** Quotations and pages come from FindLaw's reproduction of the U.S. Reports, not from a court-issued document.
4. **The *Keller* quotation and pin cite (657 F.3d at 681).** Read as quoted inside *Dowell v. United States* (7th Cir. 2012); *Keller* itself was not opened.
5. **Pin cites within *Spence* and *Dretke*.** Both opinions were read for holding, but no internal page numbers were captured; the block quotations above should not be given pin cites until confirmed.
6. ***Brown v. Caraway*, 719 F.3d 583, 587–88 (7th Cir. 2013); *Hill v. Masters*, 836 F.3d 591, 599 (6th Cir. 2016); *United States v. Wheeler*, 886 F.3d 415, 429 (4th Cir. 2018).** Case names, cites, and parentheticals come from the Hasbrouck Georgetown Law Journal article — a secondary source. None of the three opinions was read. They appear in this memo only to be flagged as superseded.
7. ***United States v. McCrone*, No. 22-3178(L) (2d Cir. July 21, 2026).** Reported from a Federal Defenders of New York blog summary used as a lead. Docket number, date, panel, holding, and standard of review are all unconfirmed.
8. **The current vitality of the Second Circuit's "modified plain error" rule.** *Thomas* (2001) expressly reserved it. Whether *Cotton* (2002) or *Marcus* (2010) has since settled the question was not researched.
9. **Whether any Second Circuit decision has applied *Hunter* yet.** Searched; none found. Two months is short, and the absence of a hit is not proof of absence.
10. **Whether the Second Circuit has ever squarely held that an appeal waiver does not bar a stat-max claim.** Searched across multiple formulations; **no such Second Circuit holding was located.** *Gomez-Perez*'s enumerated list does not include it. This is a genuine gap, and the memo does not paper over it: after *Hunter* the rule binds the Second Circuit as Supreme Court law, but it should not be attributed to the Second Circuit's own pre-*Hunter* case law.
11. **No commercial citator (Shepard's/KeyCite) was available.** Every validation statement in this memo rests on later opinions found citing the case, or on the case's recency. That is a weaker method than the malpractice case law contemplates (*Gosnell*, *Cimino*, *Meadowbrook*, *Pravic*), and a real citator run must precede any filing.
12. **Mr. Bernecky's own plea agreement.** Whether it contains an appellate or collateral-attack waiver, and what that waiver covers, was not established from the case file and is treated throughout as unknown.
