# Transcription: SORA Risk-Level Classification Package (Client-Provided Photos)

**Source:** 11 phone photos in the Google Drive folder "Sex offender classification" (within the `USA v Jeff Bernecky` case folder). The client, Jeffrey Bernecky, received these documents informally — **not through formal service of process** — from the New York State Board of Examiners of Sex Offenders and, separately, from the Monroe County Supreme & County Courts, in connection with an upcoming risk-level classification hearing under the New York Sex Offender Registration Act (SORA).

**This is a transcription only — not legal analysis.** No conclusions are drawn here about the significance of anything in these documents, the applicable law, or litigation strategy. That is reserved for separate, later work product.

**Method:** Each of the 11 Drive files was downloaded, decoded from base64, and corrected for EXIF orientation using `PIL.ImageOps.exif_transpose`. Several images were photographed sideways or upside-down relative to their EXIF tag and required additional manual rotation (noted below) before they could be read. Each corrected image was then read directly and transcribed by visual inspection — Google Drive's automatic OCR was **not** used or relied upon, consistent with this case file's established practice, because it has proven unreliable for this client's document photos. Illegible or uncertain text is flagged explicitly rather than guessed at.

**File-ID-to-content mapping** (filenames are phone photo-library numbers and do NOT reflect document order; order below was determined from letterhead, header fields, page-continuation numbering, and sentence continuity across images):

| Photo | Drive file ID | Content |
|---|---|---|
| 158.jpg | `15xZzTeZ694sqoYikTvL2aUkxqyzj-C7O` | Court hearing notice letter, p.1 |
| 159.jpg | `15SlWBlOJi24BZwtgtyi3RUmOzERhmCgt` | Court hearing notice, attached counsel-status form |
| 173.jpg | `1rdZ8JJ1aVSdvm1fLv0R5KA-N6UydqQiR` | Board of Examiners cover memo |
| 168.jpg | `1Gkn8suC2cIflVaK6Y99dIu4D9aWduPTp` | Risk Assessment Instrument (RAI) |
| 169.jpg | `1fEa3DDvCkWCV6MqviUg6Aynz6dkbA3Pl` | Case Summary, p.1 |
| 170.jpg | `1D8QF57JwMNqjEJAmjdCK05pQkJdowguC` | Case Summary, p.2 |
| 171.jpg | `1pQIAahrgi55VSVAMaiBfGMMUXoGAItIi` | Case Summary, p.3 |
| 172.jpg | `1V2SUwt_t9AftNY8PoYhsWOV9X3mtcEA5` | Case Summary, p.4 (mostly blank) |
| 174.jpg | `1RzhhMcz12PDkr-44uM9NW5rsDlsk0OpP` | Sex Offender Designation Form, p.1 |
| 175.jpg | `1_bjLkIbs4-4wTQpuZ9c5bdvUt01gb8Nd` | Sex Offender Designation Form, p.2 |
| 176.jpg | `1ODGyB_7NLgTgDBqN01D7xDt3WziJzLjo` | Sex Offender Designation Form, p.3 |

---

## Part 1: Document order — reasoning

These 11 photos represent **two separate documents from two separate senders**, mailed roughly a week apart, both concerning the same SORA classification hearing:

### Document A — Monroe County Supreme & County Courts hearing notice (2 photos: 158, 159)
Dated **July 30, 2026**. Letterhead is the NYS Unified Court System / Monroe County Supreme & County Courts. Photo 158 is the cover letter; its closing paragraph instructs Bernecky to "fill out the attached form, sign and return no later than 8/4/2026." Photo 159 is exactly that attached form — same letterhead, same "You are scheduled for a risk assessment on 9/11/2026" line, and a counsel-status checklist with signature/date blank. No page numbers appear, but the letter's own text ("the attached form") directly identifies 159 as its enclosure, and the RE: block on 159 ("Jeffrey T Bernecky / c/o VOA 175 Ward Street / Rochester NY 14605") matches the addressee block on 158.

### Document B — New York State Board of Examiners of Sex Offenders recommendation package (9 photos: 173, 168, 169–172, 174–176)
All bear the same NYSID# (OS6430), the same subject date of **July 23, 2026**, and originate from Board Examiner Renee Pizzo-Roy (her handwritten initials "RPR" appear on both the RAI assessor-signature line and the Designation Form's "1st Reviewer Initials" line). This document contains three distinguishable components, in what I believe — based on content, not on any visible staple/page-number sequence tying them together — is their logical order:

1. **Cover memo** (173): "Board Determination and Risk Level Recommendation," addressed directly to Bernecky at 175 Ward Street, Rochester. Its text ("Attached for your review is the risk level recommendation made by the Board... a statement of the reasons for the recommendations") describes exactly the two items that follow.
2. **Risk Assessment Instrument / RAI scoring worksheet** (168): a single sheet, laid out with two form-panels side by side, listing point values circled/X'd for each risk factor and yielding a Total Risk Factor Score of 70, plus an Overrides/Departure section.
3. **Case Summary** (169 → 170 → 171 → 172): a four-page narrative. Order among these four is established by direct sentence continuity — 169 ends mid-thought ("...evidence to indicate a past history of substance abuse; however, there is no"), and 170 begins to continue that thought was, on inspection, actually the reverse: **170 is the earlier page** — 169 is the SORA/offense-conduct narrative that leads into 170's personal-history narrative, which itself ends "...and there is evidence to indicate a past history of substance abuse; however, there is no" and 171 begins "evidence to indicate a more recent pattern of the daily use of marijuana and alcohol..." — a direct sentence continuation. 171 in turn ends mid-sentence ("...include that he was actively engaging in sex offender treatment at the time of the instant offense and he was") and 172 begins "under supervised release." — completing that sentence, then the rest of 172's page is blank.
4. **Sex Offender Designation Form** (174 → 175 → 176): a three-page checklist form. Order is established by each page's own "(Continued on the next page)" footer and by the form's printed section numbering (item 1 on 174, item 2 on 175, item 2 continued plus items 3–4 on 176).

I am **not fully certain** components 2–4 physically stapled/mailed in the order I've presented them (RAI, then Case Summary, then Designation Form) versus some other order, since no cross-referencing page numbers link them to each other or to the cover memo. I've ordered them by what each is: the cover memo names the RAI as "the risk level recommendation," and the Case Summary explicitly narrates and explains the RAI's scoring, so RAI-before-Case-Summary follows logically; the Designation Form addresses a legally distinct determination (Predicate Sex Offender/Sexually Violent Offender/Sexual Predator status) referenced in passing within the Case Summary, so it is placed last. Flagging this ordering as my best reconstruction, not a certainty.

Several images required manual rotation beyond the automatic EXIF correction because they were photographed in landscape orientation or upside down: photo 168 needed an additional 90° rotation; photo 171 needed an additional 180° rotation; photo 172 needed the same 180° correction.

---

## Part 2: Full transcription

### Document A — Monroe County Supreme & County Courts hearing notice

#### A-1 (photo 158) — Cover letter

> STATE OF NEW YORK
> Monroe County Supreme & County Courts
> 545 Hall of Justice
> Rochester, NY 14614
> Phone: 585-371-3758
> Fax: 585-371-3780
> www.nycourts.gov

> HON. WILLIAM K. TAYLOR
> Administrative Judge
> Seventh Judicial District

> LISA L. PRESTON
> Chief Clerk
>
> NICHOLAS SPRAGUE
> Deputy Chief Clerk

> July 30, 2026

> Jeffrey T Bernecky
> c/o VOA 175 Ward Street
> Rochester NY 14605

(The addressee block above is highlighted in yellow highlighter in the photo — an annotation on the physical document, not part of the original printed/typed text.)

> Dear Jeffrey T Bernecky,
>
> The Supreme & County Court of Monroe County has been notified of your conviction which requires that you be registered as a sex offender. To accomplish this, an appearance in court has been scheduled on 9/11/2026, at 11:30am, before the Hon. Karen Bailey Turner. The courtroom is located in the Hall of Justice, 99 Exchange Boulevard, Rochester, NY 14614.
>
> This proceeding is being held to determine whether you will be classified as a level 3 offender (risk of repeat offense is high), a level 2 offender (risk of repeat offense is moderate), or a level 1 offender (risk of repeat offense is low), or whether you will be designated as a sexual predator, a sexually violent offender or a predicate sex offender, which will determine how long you must register as a sex offender and how much information can be provided to the public concerning your registration. If you fail to appear at this proceeding, without sufficient excuse, it shall be held in your absence. Failure to appear may result in a longer period of registration or a higher level of community notification because you are not present to offer evidence or contest evidence offered by the district attorney.
>
> A copy of the recommendation received from the Board of Examiners of Sex Offenders and a statement of the reasons for the recommendations is enclosed and will be available at your court appearance.
>
> Upon registration and classification by the court, you will be required to register certain information with the New York State Division of Criminal Justice Services. Depending on your risk level, this information may be distributed to law enforcement agencies and may be available for public review.
>
> *You have the right to a hearing prior to the court determination on the recommended classification. You also have the right to have an attorney represent you in court. If you cannot afford to hire an attorney, one will be appointed to represent you. Whether you wish to have counsel appointed, or if you have hired your own attorney or an attorney has already been assigned, please fill out the attached form, sign and return no later than 8/4/2026.*
>
> Thank you for your cooperation.
>
> Sincerely,
>
> Heather Kennedy
>
> Court Clerk
>
> cc: Public Defender; District Attorney's Office; Judge

Note: the paragraph beginning "You have the right to a hearing..." appears in italics in the original. A small "2" is visible in the right margin near that paragraph, and another faint mark near the signature block — these appear to be incidental marks/creases rather than legible additional text; noted for completeness, not transcribed as content.

#### A-2 (photo 159) — Attached counsel-status form

> STATE OF NEW YORK
> Monroe County Supreme & County Courts
> 545 Hall of Justice
> Rochester, NY 14614
> Phone: 585-371-3758
> Fax: 585-371-3780
> www.nycourts.gov

> HON. WILLIAM K. TAYLOR
> Administrative Judge
> Seventh Judicial District
>
> LISA L. PRESTON
> Chief Clerk
>
> NICHOLAS SPRAGUE
> Deputy Chief Clerk

> RE:   Jeffrey T Bernecky
>       c/o VOA 175 Ward Street
>       Rochester NY 14605

(A small yellow highlighter mark appears next to the "RE:" line; its purpose is not evident from the photo.)

> You are scheduled for a risk assessment on 9/11/2026, at 11:30am, before the Hon. Karen Bailey Turner
>
> Please check the appropriate line below:
>
> _____ I wish to have counsel appointed
>
> _____ I have hired counsel to represent me. Counsel's name_____________________________
>
> _____ I have counsel already assigned to me. Counsel's name_____________________________
>
> Signed: _____________________________ Date: _____________________
>
> *Please return this form to: Monroe Supreme and County Courts*
>
> *Attn: Heather Kennedy*
>
> *545 Hall of Justice*
>
> *Rochester, NY 14614*

None of the checkboxes/blanks on this form are filled in in the photograph — it is blank/unexecuted as photographed.

---

### Document B — NYS Board of Examiners of Sex Offenders recommendation package

#### B-1 (photo 173) — Board cover memo

> [Logo: outline of New York State] NEW YORK STATE — Board of Examiners of Sex Offenders

> KATHY HOCHUL                    MICHELE L. HARRINGTON
> Governor                        Chairperson

> TO:      JEFFREY BERNECKY
>          175 WARD STREET
>          ROCHESTER, NY 14605
>
> FROM:    NYSID# OR BOARD ID #:  OS6430
>          BOARD EXAMINER, RENEE PIZZO-ROY [handwritten initials, appear to read "RPR"]
> RE:      Board Determination and Risk Level Recommendation
> DATE:    7/23/2026

> Pursuant to the New York State Sex Offender Registration Act, the Board of Examiners of Sex Offenders has reviewed your conviction in another jurisdiction and has determined that you are required to register with the New York State Sex Offender Registry. If you haven't already, you will receive a registration form for completion and signature from the New York State Division of Criminal Justice Services Sex Offender Registry or, if you are under supervision, from your supervising officer.
>
> Attached for your review is the risk level recommendation made by the Board. The Board has also forwarded its risk level recommendation to the Court and District Attorney in the jurisdiction in which you currently reside.
>
> **Please note that all relevant information considered by the Board has been forwarded to the Court.** At least 20 days prior to the determination proceeding, the Court will send you notification of the date of the hearing. You will be advised of the right to be represented by counsel at the hearing and that counsel will be appointed if it is determined that you are financially unable to retain counsel.
>
> *This is the final decision of the Board of Examiners of Sex Offenders. If you are aggrieved by this final decision, you may commence a proceeding for judicial review in accordance with Article 78 of the Civil Practice Law and Rules.*

Note: this memo addresses Bernecky at "175 Ward Street, Rochester, NY 14605" — without the "c/o VOA" prefix used on the court's letter to the same address.

Note: faint text is visible bleeding through from what appears to be the reverse side of this page (show-through from printing on the back), but it is not legible and is not part of this page's content.

#### B-2 (photo 168) — Sex Offender Registration Act Risk Assessment Instrument (RAI)

Header fields:

> Offender Name: JEFFREY BERNECKY
> NYSID #: OS6430
> Indictment #: _______ (blank)
> DIN: _______ (blank)
> RISK LEVEL: 3 (handwritten)
> Assessor's Signature: [illegible cursive signature]
> Date: [handwritten, appears to read "7/23/26"]

**I. CURRENT OFFENSE(S)**

| Risk Factor | Value | Marked | Score |
|---|---|---|---|
| 1. Use of Violence — Used forcible compulsion | +10 | | |
| — Inflicted physical injury | +15 | | |
| — Armed with a dangerous instrument | +30 | | **0** |
| 2. Sexual Contact with Victim — Contact over clothing | +5 | | |
| — Contact under clothing | +10 | | |
| — Sexual intercourse, deviate sexual intercourse or aggravated sexual abuse | +25 | | **0** |
| 3. Number of Victims — Two | +20 | | |
| — Three or more | +30 | | **0** |
| 4. Duration of offense conduct with victim — Continuing course of sexual misconduct | +20 | | **0** |
| 5. Age of victim — 11 through 16 | +20 | | |
| — 10 or less, 63 or more | +30 | **X** | **30** |
| 6. Other victim characteristics — Victim suffered from mental disability or incapacity or from physical helplessness | +20 | | **0** |
| 7. Relationship with victim — Stranger or established for purpose of victimizing or professional relationship | +20 | | **0** |

**II. CRIMINAL HISTORY**

| Risk Factor | Value | Marked | Score |
|---|---|---|---|
| 8. Age at first sex crime — 20 or less | +10 | | **0** |
| 9. Number and nature of prior crimes — Prior history/no sex crimes or felonies | +5 | | |
| — Prior history/non-violent felony | +15 | | |
| — Prior violent felony, sex crime or endangering welfare of a child | +30 | **X** | **30** |
| 10. Recency of prior felony or sex crime — Less than 3 years | +10 | **X** | **10** |
| 11. Drug or Alcohol abuse — History of abuse | +15 | | **0** |

**COLUMNS 1-11 SUBTOTAL: 70**

**III. POST-OFFENSE BEHAVIOR**

| Risk Factor | Value | Marked | Score |
|---|---|---|---|
| 12. Acceptance of Responsibility — Not accepted responsibility | +10 | | |
| — Not accepted responsibility/refused or expelled from treatment | +15 | | **0** |
| 13. Conduct while confined/supervised — Unsatisfactory | +10 | | |
| — Unsatisfactory with sexual misconduct | +20 | | **0** |

**IV. RELEASE ENVIRONMENT**

| Risk Factor | Value | Marked | Score |
|---|---|---|---|
| 14. Supervision — Release with specialized supervision | 0 | | |
| — Release with supervision | +5 | | |
| — Release without supervision | +15 | | **0** |
| 15. Living/employment situation — Living or employment inappropriate | +10 | | **0** |

**COLUMNS 12-15 SUBTOTAL: 0**
**COLUMNS 1-11 SUBTOTAL: 70**
**TOTAL RISK FACTOR SCORE (add 2 subtotals): 70**

Below the total-score box, the printed numerals "**X   2   3**" appear (an "X" printed/marked before "2" and "3"). I am not fully certain what this notation is indicating in relation to the boxed Level table beside it — transcribing as observed without interpreting its significance:

> Level 1 (low) = 0 to +70
> Level 2 (moderate) = +75 to +105
> Level 3 (high) = +110 to +300
>
> Note: The Sex Offender Registration Act requires the court or Board of Examiners of Sex Offenders to consider any victim impact statement in determining a sex offender's level of risk.

**A. Overrides** (If any override is circled, offender is presumptively a Level 3)

> **X** 1. Offender has a prior felony conviction for a sex crime
>
>    2. Offender inflicted serious physical injury or caused death
>
>    3. The offender has made a recent threat that he will reoffend by committing a sexual or violent crime
>
>    4. There has been a clinical assessment that the offender has a psychological, physical, or organic abnormality that decreases ability to control impulsive sexual behavior

**B. Departure**

> 1. A departure from the risk level is warranted
>
>    [ ] Yes    [X] No
>
> 2. If yes, circle the appropriate risk level    1    2    3
>
> 3. If yes, explain the basis for departure (See Summary)

#### B-3 (photos 169–172) — Case Summary

Each page carries the header:

> RE:   JEFFREY BERNECKY
>       NYSID #: OS6430
>
> DATE: 7/23/2026
> _____________________________
>
> CASE SUMMARY

**Page 1 (photo 169):**

> This assessment is based upon a review of the inmate's file which may include but is not limited to the pre-sentence investigation, prior criminal history and post-offense behavior.
>
> Jeffrey Bernecky is a 38-year-old (DOB: 6/03/1988) Predicate Sex Offender who was convicted by guilty plea in the U.S. District Court for the Western District of New York of Possession of Child Pornography Involving Prepubescent Minors Following a Prior Conviction for Possessing and Distribution of Child Pornography, in violation of 18 USC §§ 2252A(a)(5)(B), and 2252A(b)(2), on February 15, 2018. He was sentenced to 120 months in the United States Bureau of Prisons (BOP) to be followed by 10 years of supervised release. This sentence was imposed concurrently with his sentence imposed for the violation of supervised release under Docket No 6:11CR06045-001 for which he was sentenced to 60 months in the BOP. On June 18, 2026, the Board of Examiners of Sex Offenders (the "Board") was notified that he was residing in Monroe County, New York. However, after Mr. Bernecky's notification letter from the Board was returned, his letter was resent on June 23, 2026, to the correct address which is at a reentry facility where he has access to the community. As a resident of New York, he is required to register as a sex offender for this enumerated federal offense.
>
> According to the Federal Presentence Investigation Report (PSR) revised on April 26, 2011, the Sentencing Memorandum filed on June 7, 2018, the Criminal Complaint filed on December 22, 2017, and the Indictment filed on February 15, 2018, the instant offense took place on or about December 8, 2017 and involved Mr. Bernecky at the age of 29 knowingly possessing images and videos of child pornography depicting male children as young as 8 years old. The videos and images had been shipped and transported in the affecting interstate and foreign commerce via the Internet. The offense was detected during a routine home inspection by his supervising United States Probation Officer (USPO). During the inspection the USPO observed a white Samsung smartphone on Mr. Bernecky's desk next to his bed. When questioned, Mr. Bernecky initially reported that the phone belonged to a co-worker who had asked him to charge the phone overnight. He was going to return it to the co-worker the next day. When the USPO took possession of the cellular phone with the intent to following Mr. Bernecky to his place of employment to return the phone to its owner, Mr. Bernecky admitted that the phone was his. He reported that he had asked another person to purchase it for him approximately two weeks prior. He acknowledged that he was aware that he could not possess the phone without permission from the United States Probation Office. When asked if it contained contraband, Mr. Bernecky admitted that it contained "child porn" and reported that he downloaded the images from "the Tor network." At that time, the phone was seized by the USPO.
>
> A forensic review of the phone revealed that it contained approximately 200 images and 25 videos of child pornography. One video depicted an approximate 8-year-old boy that was performing oral sex on an adult male. Another video over 23 minutes in length depicted two prepubescent boys approximately 10 years old lying on a bed fully clothed. They appeared to be watching something on the computer and then they removed their clothes while staring at the camera. They began manipulating their penises until they became erect. One of the boys performed oral sex on the other and later in the video they engaged in anal sex.
>
> When interviewed for the PSR, Mr. Bernecky advised that the account set forth in the factual basis of the plea agreement accurately reflected his conduct in the instant offense.

Note: the document as photographed states the PSR was "revised on April 26, 2011" in the same sentence that cites the 2018 Sentencing Memorandum, 2017 Criminal Complaint, and 2018 Indictment for the instant offense. This date is transcribed exactly as printed; it was verified by zooming into the image and is not a transcription error on my part. I flag the apparent inconsistency (2011 date grouped with 2017–2018 filings) as something present in the source document, without speculating on its cause.

**Page 2 (photo 170):**

> Regarding his personal life, Mr. Bernecky has never been married, and he has not fathered any children. At the time of the instant offense, he was residing with his mother since his release from a halfway house in July 2016 and he had resided there at the time of his prior sex crime. Additionally, he was engaging in treatment for individuals who commit sex crimes.
>
> The Board reviewed Mr. Bernecky's e-Justice Criminal History Report, the PSR, and the Board's Case Summary dated January 19, 2016, his criminal history at the age of 23 on January 17, 2012, when he was convicted by guilty plea of Distribution of Child Pornography, in violation of 18 U.S.C. § 2252A(a)(1), and Possession of Child Pornography, in violation of 18 U.S.C. § 2252A(a)(5)(B), in the U.S. District Court for the Western District of New York. He was sentenced to 60 months in the BOP and 180 months of supervised release. His supervision commenced on July 7, 2016, and he committed the instant offense less than two years later. Therefore, he will be scored for recency. This prior offense involved Mr. Bernecky distributing and possessing images of child pornography. Specifically, he shared over 62,000 files that included numerous images and video files with names indicative of child pornography. Further investigation revealed he possessed approximately 8,811 videos containing child pornography and child erotica which included 10-year-old boys and images that portrayed sadistic of masochistic conduct or other depictions of violence. When interviewed by special agents at his residence on July 7, 2010, he admitted to using the peer-to-peer file sharing program to download videos from other users. He stated that the average age of the children he downloaded was between 10 and 12 years old. He stated that he could not help what he was doing, and he wished he could change it. He stated that a couple of years ago he took pictures of his 13-year-old cousin, clothed, and acknowledged being sexually attracted to him. He also admitted to going on BlogTV.com on the Junior Section because he thought it was safe since it was in Israel and believed they could not prosecute. He added that he used a desktop recorder to record children he viewed on webcam engaging in sexual acts. He added that he always knew there was danger in everything he did. He stated that when guys started sending him pictures, that was when he started collecting child pornography. He stated he looked at the child pornography so he could masturbate to it and he stored his collection on an external hard drive. He admitted to trading a lot of child pornography through the peer-to-peer network and stated that if he did not have something to look at (child pornography), he might be tempted to do something (have sexual contact with an actual child). He is registered as a Level II risk with no designation on the New York State Registry for this offense.
>
> There are inconsistencies in what Mr. Bernecky reported relating to his use of alcohol and drugs. During the PSR interview, Mr. Bernecky reported the use of alcohol beginning at the age of 21 with his last use at the age of 28. He drank maybe once a week that consisted of one drink with dinner. He tried marijuana a couple of times when he was 21 years old and denied any other drug use. He has never engaged in substance abuse treatment. While under supervision, he submitted to five random drug screens which were negative for all substances. During an evaluation at Endeavor on August 8, 2016, he reported the occasional use of marijuana beginning when he was approximately 21 or 22 years old. He stated, "I think it affected my daily life, but I was more prone to seek out pornography and child pornography when I was high." It is unclear if the outcome of this evaluation determined the need for substance abuse treatment at Endeavor. Notably, prior to the instant offense and upon his initial entry into the BOP, he reported the daily use of alcohol and marijuana and the rare use of hallucinogens during the year prior to his arrest for his first sex crime. Based on his self-report there was a correlation between his use of marijuana and viewing images of child pornography and there is evidence to indicate a past history of substance abuse; however, there is no

**Page 3 (photo 171):**

> evidence to indicate a more recent pattern of the daily use of marijuana and alcohol or that he was under the influence of either substance when he committed the instant offense. Therefore, he will not be scored for this factor. The Court may wish to reassess this factor based in evidence presented at the time of the SORA hearing and adjust his score if necessary.
>
> It is unknown whether Mr. Bernecky participated in sex offender treatment while in the BOP. He is mandated to engage in treatment as a condition of his supervised release. He is credited with accepting responsibility based on his guilty plea and the anticipated engagement in treatment while supervised. Notably, at the time he committed the instant offense he was involved in treatment for individuals who commit sex crimes at Endeavor that included weekly group treatment and monthly individual sessions. During the 2016 evaluation he denied a current attraction to children and stated, "I feel like I felt stuck in my younger age, I don't think I ever moved." In May 2017 a sexual history polygraph re-test was completed due to a failed sexual history polygraph from an apparent misunderstanding of sexual contact. During the pretest interview, he listed two individuals with whom he had sexual contact with that included a 12-year-old boy when he was 18 years old and a 9-year-old boy when he was 16 years old. He reported that he worked at a camp for children and while in the day camp bus in 2005, the 9-year-old tried to sit on his lap and in 2007, the 12-year-old sat down on his back at the after-school program he worked at. He reported that these instances caused him to become sexually aroused. Thereafter, no deception was indicated in the sexual history polygraph. Prior to the re-test, he admitted to his counselor that he was sexually attracted to children, but he could never hurt a child. Following his re-test examination his counselor reported that Mr. Bernecky took accountability for his actions and showed insight into his offending behavior, his arousal to children, and the risks associated to the possibility to reoffending. He was engaging in phase two of treatment when he committed the instant offense. During this time, he identified stress as a trigger for deviant fantasies. In July 2017, he reported fighting with his mother more, but he was asserting his desires in a healthy way. He also reported a decrease in masturbation, partially due to his new medication and his moods. When he had deviant fantasies, they involved past child pornography stories he read. Throughout the following months, he continued to report decreased deviant fantasies and masturbation.
>
> His conduct while confined in the BOP and while residing in the reentry facility is considered satisfactory, absent any information to the contrary.
>
> Mr. Bernecky is scored on the Risk Assessment Instrument (RAI) for possessing images of child pornography depicting children under the age of 11 (30 points). He is further scored for his prior felony sex crime (30 points), and for the recent nature of the instant offense to his prior sex crime (10 points).
>
> Mr. Bernecky is assessed as a Level I (Low) risk. However, pursuant to the New York State Sex Offender Registration Act Risk Assessment Guideline and Commentary, the fact that Mr. Bernecky has a prior felony sex crime conviction automatically results in a presumptive Risk Level III, as this provides compelling evidence that he poses a serious risk to public safety that is not captured by scoring alone. Therefore, he is considered a Level III (High) risk, and no departure is recommended as prior detection, sanction and treatment have not deterred his conduct. Additionally, as outlined in the Board's June 1, 2012, Position Statement (attached), a Level III risk is warranted based on the fact that he has demonstrated the inability to manage his sexual urges and returned to seeking out images of child pornography. Other concerning factors

**Page 4 (photo 172):**

> include that he was actively engaging in sex offender treatment at the time of the instant offense and he was under supervised release.

Below this single line, the rest of the page is blank as photographed — no signature block, additional text, or further content is visible on this page.

#### B-4 (photos 174–176) — Sex Offender Designation Form

**Page 1 (photo 174):**

> SEX OFFENDER DESIGNATION FORM
>
> Offender Name: JEFFREY BERNECKY
> NYSID #: OS6430          1ST Reviewer Initials: [handwritten, appears to read "RPR"]
>
> The following is the Board of Examiners of Sex Offenders' recommendation pursuant to Section 168-l of Article 6-C of the NYS Correction Law as to whether the offender shall be designated a Sexually Violent Offender, Predicate Sex Offender, or Sexual Predator as defined in subdivision seven of Section 168-a or whether the offender does not fit any of those categories due to his conviction. The District Attorneys may also use this form for recommendations to the Court pursuant to their authority under Correction Law 168-d(3).
>
> Please check all that apply:
>
> 1. [ ] Sexually Violent Offender - a sex offender who has been convicted of a sexually violent offense defined in Correction Law section 168-a (3).
>
> Please check which conviction(s) apply, also please indicate whether the conviction was for an attempt at an offense:
>
> Attempt
> ___  ___  130.35 - Rape 1°
> ___  ___  130.50 - Sodomy 1°/Criminal Sexual Act 1°
> ___  ___  130.53 - Persistent sexual abuse
> ___  ___  130.65 - Sexual Abuse 1°
> ___  ___  130.65-a - Aggravated sexual abuse 4°
> ___  ___  130.66 - Aggravated sexual abuse 3°
> ___  ___  130.67 - Aggravated sexual abuse 2°
> ___  ___  130.70 - Aggravated sexual abuse 1°
> ___  ___  130.75 - Course of sexual conduct against a child 1°
> ___  ___  130.80 - Course of sexual conduct against a child 2°
> ___  ___  130.90 - Facilitating a sex offense with a controlled substance
> ___  ___  130.95 - Predatory sexual assault
> ___  ___  130.96 - Predatory sexual assault against a child
> ___  ___  A conviction of an offense in any other jurisdiction which includes all of the essential elements of any listed felony provided for above, or conviction of a felony in any other jurisdiction for which the offender is required to register as a sex offender in the jurisdiction which the conviction occurred.
> ___  ___  A conviction of, or a conviction for an attempt to commit, any provision of a sexually violent offense as set forth in Corr. Law § 168-a(3)(a) committed or attempted as a hate crime defined in Penal Law § 485.05 (specify offense)_____________
> ___  ___  A conviction of, or a conviction for an attempt to commit, any provision of a sexually violent offense as set forth in Corr. Law § 168-a(3)(a) committed or attempted as a crime of terrorism pursuant to Penal Law § 490.25 (specify offense)_____________
>
> (Continued on the next page)

None of the blanks on this page are filled in; checkbox 1 is unchecked. In the bottom-left corner of the page, small print reads "12/07/2010" — this appears to be a form-revision date printed on the blank template itself, not a date entered by the Board for this case.

**Page 2 (photo 175):**

> 2. [X] Predicate Sex Offender - a sex offender who has been convicted of an offense set forth in subdivision 2 or 3 of Correction Law Section 168-a when the offender has been previously convicted of an offense set forth in subdivision 2 or 3 of Section 168-a, regardless of the date of the prior conviction and regardless of whether the offender was required to register for the previous conviction.
>
> Please identify below the offender's previous qualifying conviction(s) as well as the offender's current qualifying conviction, also please indicate whether the conviction was for an attempt at an offense:
>
> Current  Previous  Attempt
> ___  ___  ___  120.70 - Luring a child
> ___  ___  ___  130.20 - Sexual Misconduct
> ___  ___  ___  130.25 - Rape 3°
> ___  ___  ___  130.30 - Rape 2°
> ___  ___  ___  130.35 - Rape 1°
> ___  ___  ___  130.40 - Criminal Sexual Act 3°/Sodomy 3°
> ___  ___  ___  130.45 - Criminal Sexual Act 2°/Sodomy 2°
> ___  ___  ___  130.50 - Criminal Sexual Act 1°/Sodomy 1°
> ___  ___  ___  130.52 - Forcible touching (victim<18 years old)
> ___  ___  ___  130.53 - Persistent sexual abuse
> ___  ___  ___  130.55 - Sexual abuse 3° (victim<18 years old)
> ___  ___  ___  130.60 - Sexual Abuse 2°
> ___  ___  ___  130.65 - Sexual Abuse 1°
> ___  ___  ___  130.65-a - Aggravated sexual abuse 4°
> ___  ___  ___  130.66 - Aggravated sexual abuse 3°
> ___  ___  ___  130.67 - Aggravated sexual abuse 2°
> ___  ___  ___  130.70 - Aggravated sexual abuse 1°
> ___  ___  ___  130.75 - Course of sexual conduct against a child 1°
> ___  ___  ___  130.80 - Course of sexual conduct against a  child 2°
> ___  ___  ___  130.90 - Facilitating a sex offense with a controlled substance
> ___  ___  ___  130.91 - Sexually motivated felony
> ___  ___  ___  130.95 - Predatory sexual assault
> ___  ___  ___  130.96 - Predatory sexual assault against a child
> ___  ___  ___  *135.05 - Unlawful Imprisonment 2°
> ___  ___  ___  *135.10 - Unlawful Imprisonment 1°
> ___  ___  ___  *135.20 - Kidnapping 2°
> ___  ___  ___  *135.25 - Kidnapping 1°
> ___  ___  ___  230.04 - Patronizing a prostitute 3° (victim <17 years old)
> ___  ___  ___  230.05 - Patronizing a prostitute 2°
> ___  ___  ___  230.06 - Patronizing a prostitute 1°
> ___  ___  ___  230.30 (2) - Promoting prostitution 2°
> ___  ___  ___  230.32 - Promoting prostitution 1°
> ___  ___  ___  230.33 - Compelling prostitution
> ___  ___  ___  230.34 - Sex trafficking
> ___  ___  NA  235.22 - Disseminating indecent material to minors 1°
> ___  ___  ___  **250.45(2),(3)and(4) - Unlawful surveillance 2°
> ___  ___  ___  250.50 - Unlawful surveillance 1°
> ___  ___  ___  255.25 - Incest 3°
> ___  ___  ___  255.26 - Incest 2°
> ___  ___  ___  255.27 - Incest 1°
> ___  ___  ___  Article 263 offenses - Sexual Performance by a Child
>
> ___  ___  ___  Conviction/Attempt to commit any provision of 130.52 or 130.55 of the Penal Law regardless of age of victim and the offender has previously been convicted of: (i) a sex offense listed in Correction Law § 168-a (2), or (ii) a sexually violent offense listed in Correction Law § 168-a (3), or (iii) any of the provisions of § 130.52 or § 130.55 of the penal law or an attempt thereof.
>
> (Continued on the next page)

Checkbox 2 ("Predicate Sex Offender") is marked with an X. The only entry on this page with anything written in a blank is the "235.22 - Disseminating indecent material to minors 1°" line, where "NA" is handwritten in the Attempt column; all other lines on this page are unmarked.

**Page 3 (photo 176):**

> **X**  **X**  ___  A conviction of any of the provisions of 18 U.S.C. 2251, 18 U.S.C. 2251A, 18 U.S.C. 2252, 18 U.S.C. 2252A, 18 U.S.C. 2260, 18 U.S.C 2422(b), 18 U.S.C. 2423 or 18 U.S.C. 2425, provided the elements of such crime of conviction are substantially the same as those which are part of such offense as of March 11, 2002.
>
> ___  ___  ___  A conviction of an offense in any other jurisdiction which includes all of the essential elements of any such crime provided for in Corr. Law § 168-a (2) (a), (b), or (c) or any such felony as provided for in Corr. Law § 168-a(3)(a), or a conviction of a felony in any other jurisdiction for which the offender is required to register as a sex offender in that jurisdiction in which the conviction occured.
>
> ___  ___  ___  A conviction of, or a conviction for an attempt to commit any provision of an offense as set forth in Corr. Law § 168-a(2) or (3) committed or attempted as a hate crime as defined in Penal Law § 485.05 (specify offense)_____________
>
> ___  ___  ___  A conviction of, or a conviction for an attempt to commit any provision of an offense as set forth in Corr. Law § 168-a(2) or (3) committed or attempted as a crime of terrorism pursuant to Penal Law § 490.25 (specify offense)_____________
>
> (*) 135.05, 135.10, 135.20, 135.25 - the victim must be less than 17 years old and the offender must not be the parent of the victim
>
> (**) 250.45(2), (3), (4) - A registerable offense unless the trial court finds that registration would be unduly harsh and inappropriate. Please note that an attempt to commit this offense does not require registration.
>
> 3. [ ] Sexual Predator - a sex offender who has been convicted of a sexually violent offense defined in Correction Law Section 168-a (3) and who suffers from a mental abnormality or personality disorder that makes him or her likely to engage in predatory sexually violent offenses.
>
> 4. [ ] None of the above.

On this page, the "Current" and "Previous" columns are both marked with an X on the federal-statute line (18 U.S.C. §§ 2251, 2251A, 2252, 2252A, 2260, 2422(b), 2423, 2425); the "Attempt" column on that line is blank. No other lines on this page are marked. Checkboxes 3 and 4 are both unmarked.

---

## Part 3: Structured summary of key facts

**Senders and dates**
- **Document A:** Monroe County Supreme & County Courts (NYS Unified Court System, Seventh Judicial District), dated **July 30, 2026**. Signed by Heather Kennedy, Court Clerk.
- **Document B:** New York State Board of Examiners of Sex Offenders, dated **July 23, 2026**. Cover memo signed/initialed by Board Examiner Renee Pizzo-Roy; RAI signed by an assessor whose signature is illegible in cursive, dated "7/23/26"; Designation Form initialed "1ST Reviewer Initials" (appears to read "RPR").

**Hearing date**
- **September 11, 2026, at 11:30 a.m.**, before the Hon. Karen Bailey Turner, in the Hall of Justice, 99 Exchange Boulevard, Rochester, NY 14614 (per both the court letter and the attached counsel-status form).

**Risk level sought / scoring**
- The Board's RAI shows a Total Risk Factor Score of **70**, built from: Age of victim "10 or less, 63 or more" (+30); prior violent felony/sex crime or endangering welfare of a child (+30); recency of prior felony/sex crime, less than 3 years (+10). All other RAI categories scored 0.
- A raw score of 70 falls within the RAI's own printed "Level 1 (low) = 0 to +70" range, and the Case Summary states in so many words that "Mr. Bernecky is assessed as a Level I (Low) risk" on the point scale.
- However, RAI **Override 1** is marked ("Offender has a prior felony conviction for a sex crime"), which the form states makes the offender "presumptively a Level 3." The RAI's "RISK LEVEL:" field is filled in as **3**, and the Case Summary states the Board is recommending he "is considered a Level III (High) risk, and no departure is recommended."
- The Sex Offender Designation Form marks **"2. Predicate Sex Offender"** as applicable (box checked, and the federal child-pornography statute line — 18 U.S.C. §§ 2251, 2251A, 2252, 2252A, 2260, 2422(b), 2423, 2425 — is marked X in both the "Current" and "Previous" columns). Neither "1. Sexually Violent Offender," "3. Sexual Predator," nor "4. None of the above" is checked.

**Federal presentence report (PSR) excerpts**
- The Case Summary (Document B, pages 169–172) is a **narrative document written by the Board**, not a photocopy of actual PSR pages. It repeatedly references and paraphrases "the Federal Presentence Investigation Report (PSR)" and other charging documents (Sentencing Memorandum filed June 7, 2018; Criminal Complaint filed December 22, 2017; Indictment filed February 15, 2018) as its sources, and separately references "the PSR" from the 2012 case and "the Board's Case Summary dated January 19, 2016."
- Content the Case Summary attributes to the PSR/case record includes: the instant offense conduct (the December 8, 2017 home inspection, the Samsung smartphone, Bernecky's admissions to USPO, the "Tor network" statement, the forensic review finding ~200 images/25 videos including descriptions of two specific videos); the prior 2012 federal conviction facts (distribution/possession of child pornography, ~62,000 shared files, ~8,811 videos, admissions to special agents in a 2010 interview about downloading habits, the BlogTV.com and webcam-recording admissions, the 13-year-old cousin photo admission); substance-use history; sex-offender-treatment history including the 2016 Endeavor evaluation, 2017 polygraph re-test, and named contacts with two minors (a 12-year-old when Bernecky was 18, and a 9-year-old when Bernecky was 16) described as occurring in 2005 and 2007.
- **No pinpoint citation format (e.g., "PSR at ___") appears anywhere in these photographed pages.** The Case Summary refers to its sources by document type and filing/revision date only ("According to the Federal Presentence Investigation Report (PSR) revised on April 26, 2011..."), not by page number.
- The instant-offense docket number is not stated in the Case Summary; the only federal docket number given is **6:11CR06045-001**, identified as the docket for the *prior* case's supervised-release violation that ran concurrently with the instant sentence.

**Deadlines**
- The counsel-status form (Document A-2) must be signed and returned **no later than August 4, 2026**, per the cover letter's instruction, to Attn: Heather Kennedy, 545 Hall of Justice, Rochester, NY 14614.
- Appearance at the classification hearing is required on **September 11, 2026**; the letter states that failure to appear "without sufficient excuse" will result in the proceeding being held in Bernecky's absence and may result in a longer registration period or higher notification level.

**Other procedural details visible in the documents**
- NYSID #: **OS6430** (used consistently across all Board documents).
- Indictment # and DIN fields on the RAI are both blank.
- Court contact: phone 585-371-3758, fax 585-371-3780, www.nycourts.gov.
- The court letter is copied ("cc:") to: Public Defender; District Attorney's Office; Judge.
- The Board's cover memo states that "at least 20 days prior to the determination proceeding, the Court will send you notification of the date of the hearing," and that the Board's decision is stated to be final, appealable only via an Article 78 proceeding in the CPLR.
- The Board's cover memo also states the Board "has also forwarded its risk level recommendation to the Court and District Attorney in the jurisdiction in which you currently reside."
- Bernecky's address is given as "c/o VOA 175 Ward Street, Rochester NY 14605" on the court documents, and as "175 Ward Street, Rochester, NY 14605" (no "c/o VOA" prefix) on the Board's cover memo.
- The Case Summary references an earlier Board "Position Statement" dated **June 1, 2012**, described as "attached," which is not among these 11 photographs.
