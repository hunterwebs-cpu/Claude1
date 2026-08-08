---
name: substack
description: Write and deliver a "Surviving the Feds: Dispatches from the Inside" Substack article for Bilal Khan's column on Doug Passon's Substack. Full 4-phase pipeline — topic discovery, deep research, targeted interview, write and deliver. Invoke with /substack.
---

# Substack Dispatch Skill
## Surviving the Feds: Dispatches from the Inside

This skill governs every article written for Bilal Khan's guest column on Doug Passon's Substack. Follow the phases in order. Do not skip research. Do not begin writing until the interview is complete. Do not deliver until the .docx is generated and verified.

---

## ENTRY BEHAVIOR — What to do when /substack is invoked

**If the user says `/substack` with no topic specified:**
1. Read `content/substack/topic-pipeline.md`
2. Check whether "## THIS WEEK'S RESEARCH RESULTS" contains actual research entries (not just the placeholder text)
3. **If fresh research results exist:** Present them as a numbered list and ask Bilal to pick one. Then go to Phase 2.
4. **If no results yet (placeholder only):** Immediately spawn the Phase 1 research subagent (instructions below). Do NOT list the committed pipeline topics as choices — those are already assigned and are not for selection.

**If the user specifies a topic, or arrives with something he witnessed:** Skip Phase 1 entirely. Go straight to Phase 2 and ask him to tell you what happened. Do not research first. Do not present him with a brief. Let him talk.

**The default assumption is that Bilal already knows this subject.** Ask whether he wants research before running any. On most topics the honest answer is no.

---

## THE PIPELINE — 4 PHASES

```
PHASE 1: Topic Discovery    → AUTOMATED (weekly Routine, runs headlessly, no human present)
         Only used when Bilal has no story in hand. Saves a ranked report
         to content/substack/topic-pipeline.md, commits, pushes, STOPS.
         ↓
PHASE 2: The Account        → Bilal tells what happened. This is the article.
         ONE round of follow-ups, maximum. Nothing else happens first.
         ↓
PHASE 3: Verification       → runs SILENTLY in the background, narrow scope:
         confirm names/dates/citations, and confirm any rule a family
         would act on. Bilal never has to read this.
         ↓
PHASE 4: Write & Deliver    → write from his account, one redline, .docx, deliver
```

**The center of gravity is Bilal's account, not the research.** The column exists to give readers a glimpse of life inside a low-security federal prison, told through events, with practical tips for getting settled. The scene is the product. Law and data are seasoning, and a dispatch can carry very little of either and still be excellent.

**Do NOT open with a research phase.** An earlier version of this skill researched first and then interviewed Bilal about the findings. The result was a legal argument with his story bolted on, and it cost six rounds of him stripping out citations, severity tables, and procedural posture he had never asked for. If a draft reads like a law review article with anecdotes, the pipeline ran backwards.

**Deep research is CONDITIONAL.** Run it only when Bilal says he does not know a subject well, or when the piece turns on a rule he has not worked with. He has fourteen years inside and litigates from his cell — on most topics he is the better source, and research merely catches up to him. Ask before spending a phase on it.

**If the article takes more than one redline from Bilal, the process failed, not the draft.** He should talk once and correct once. Anything more means the writing started from the wrong material.

**To start an article:** Open a new Claude Code session, type `/substack`, and tell Claude which topic from `content/substack/topic-pipeline.md` you want to develop.

**The Routine prompt lives at:** `content/substack/routine-prompt.md` — paste this into the Routine's prompt field at `claude.ai/code/routines`.

---

## PHASE 1 — Topic Discovery

**When to run:** When `/substack` is invoked with no topic AND the pipeline file has no fresh research results. Goal: surface what the audience is actively searching for so articles meet real demand, not just assumed interest.

**Spawn a general-purpose research subagent** with this brief:

> Research what people are actively searching for and asking about in the federal prison and federal criminal justice space. This is for a Substack column called "Surviving the Feds: Dispatches from the Inside" — first-person dispatches by a federal prison veteran currently incarcerated at FCI Fort Dix, writing for families of federal defendants and people navigating the federal system.
>
> Search across:
> - Reddit (r/legaladvice, r/federal, r/WhiteCollarCrime, r/Prison, r/AskLawyers) — what questions are families and defendants actually asking?
> - Quora and similar Q&A platforms — what are the most-viewed questions about federal prison life, BOP procedures, inmate rights?
> - Existing Substack publications in the criminal justice niche — what are they covering and what gaps exist? (Check: Prisons Prose & Protest, Sentences: Writings About Mass Incarceration, JustImpact, The Marshall Project's Life Inside)
> - News coverage of federal prison conditions — what's generating audience engagement right now?
> - Google autocomplete and "People Also Ask" signals for terms like "federal prison," "BOP," "federal inmate rights," "federal sentencing," "prison conditions"
>
> Return a ranked list of 6–10 article ideas, each containing:
> 1. The topic and the specific angle that's underserved
> 2. Evidence of audience demand (what you found and where)
> 3. What existing coverage misses — the gap this column can fill
> 4. Whether this author's profile (14+ years inside, active litigator, Marine veteran) gives him unique standing on this topic
> 5. A draft title (first-person, 13–17 words, no question mark)
>
> Do not suggest topics already covered: infrastructure/Fort Dix is complete. Disability accommodations, retaliatory transfer, administrative remedies, and First Step Act are in the pipeline.

**After the subagent returns:** Present the ranked list to Bilal. Let him choose or redirect. His instinct about what readers need overrides the algorithm — the research surfaces demand, he decides what's worth his voice.

---

## OPTIONAL — Deep Research (only when Bilal doesn't know the subject)

**When to run:** Only when Bilal says he is not well versed in the topic, or the piece turns on a rule he has not personally worked with. **Ask him first.** Do not run this by default and do not run it before he has told you the story.

**When NOT to run it:** Anything drawn from what he has lived — how a unit runs, what staff actually do, how men behave, what happens after a report. He is the primary source. Research on those topics produces a brief that mostly gets thrown away and an article that argues instead of showing.

If you do run it, the brief below is heavy. Cut it down to the two or three questions that actually matter for this piece.

**Spawn a general-purpose research subagent** with this brief (fill in [TOPIC]):

> Research the following topic thoroughly for a Substack dispatch article: **[TOPIC]**
>
> Context: First-person column by a federal prison veteran at FCI Fort Dix. Audience is families of federal defendants and people navigating the federal system. The article must provide something they cannot get from existing coverage — the insider view.
>
> Research and report on:
>
> 1. **Existing coverage audit** — What has already been written about this? List 5–10 sources (news, Substack, advocacy orgs, government reports). Assess each: what angle does it take, who wrote it, and what does it miss?
>
> 2. **Factual framework** — Key facts, statistics, BOP policies, CFR citations, program statements, and relevant case law. Flag which are verified and which need confirmation. Do not present uncertain facts as established.
>
> 3. **The official story vs. likely reality** — What does the BOP/government say about this topic? Based on known reporting and advocacy documentation, where does that diverge from lived experience inside?
>
> 4. **Common misconceptions** — What do families and defendants most commonly get wrong about this topic? What assumptions does existing coverage make that may be false?
>
> 5. **The gap** — What specific angle, detail, or insight is missing from everything you found that someone currently inside the BOP could uniquely provide?
>
> 6. **Targeted interview questions** — 8–12 specific questions for the author, framed around the gaps the research found. Examples of the right format:
>    - "The BOP's official policy says X — does that match what you've seen at Fort Dix and other facilities?"
>    - "Most coverage focuses on Y — what does coverage miss about the reality of Z?"
>    - "Nobody is writing about [specific angle] — is that something you have direct experience with?"
>    - "The research found [statistic/claim] — does that track with your experience, and what would you add or correct?"
>
> Return the full research brief. Flag every factual claim that will need verification before publication.

**After the subagent returns:** Read the brief before interviewing Bilal. The interview questions in the brief replace the generic Round 1–4 questions in Phase 3 for this specific article. The research brief is the interview prep sheet.

---

## PHASE 2 — The Account

**When to run:** First. Before research, before any brief, before you have an angle. Goal: get the event out of Bilal's head in his own words. This is the article; everything after it is support.

**Open with the story, not with questions.** "Tell me what happened — what you saw, what it looked like, what people did." Then get out of the way and let him write.

**Then ONE round of follow-ups. One.** Only ask what you genuinely cannot get anywhere else:

- Sequence — what happened first, and what came after
- Sensory detail — what it looked like, sounded like, who was standing where
- Who did what, and how he knows (saw it himself / compound talk / staff said it / read it)
- What the tips are — see below

**Do not ask him to react to statistics.** Do not ask him to confirm a research finding. Do not send twelve questions. He is typing on a monitored prison email system where every message costs him real effort; a long question list is expensive and mostly produces material that never runs.

**Where the tips come from: him.** He is a litigator with fourteen years inside who has watched families make every mistake there is. Ask directly — "what do you tell someone whose son is dealing with this?" — and take the answer as the section. Much of it will not be verifiable, and that is expected. Write it as his experience (see THE SOURCING RULE). Verify only the pieces a reader would act on as a rule: a citation, a deadline, a form, a right.

**Sourcing questions to always ask:**
- How do you know this — saw it, heard it, read it?
- Anything you cannot or should not include, given where you are?

**The interview is conversational and conducted inline — not delegated to a subagent.** It requires follow-up based on Bilal's answers.

### Using the Research Brief

Lead with what the research found, then ask Bilal to respond to it:

- "The research shows [finding]. What does your experience say?"
- "Existing coverage says [claim]. Is that accurate from inside? What's missing?"
- "Nobody seems to be writing about [gap]. Is that something you've seen?"
- "The official BOP position is [X]. What's the reality on the ground?"
- "The research flagged [statistic/policy] — can you confirm that's accurate, or does it need correction?"

This is not a generic interview. It is a targeted correction and enrichment session based on what the research already found.

### Standing Interview Questions (Every Article)

These apply regardless of topic:

**Sourcing:**
- How do you know what you know? (direct observation, inmate accounts, staff statements, documents?) Be explicit — the article must distinguish rumor from documented fact.
- Is there anything you cannot or should not include given your situation?

**Personal authority:**
- Does your facility history (Doña Ana, Torrance, Maricopa, FDC Philly, Fort Dix, Big Spring, Lewisburg) give you a comparative angle on this topic?
- Have you personally litigated anything related to this topic, or helped someone else do so?

**Actionable layer:**
- What is the specific procedure, form number, program statement, or law the reader needs?
- What happens if they miss the deadline or skip the process?
- What is the most common mistake people make on this?

**Corrections gate:**
- Any numbers, dates, dimensions, or official statements to confirm before we write?
- Anything in the research brief that was flatly wrong?

### Interview Mechanics

- Conduct in rounds of 5–7 questions. Do not send 20 questions at once.
- Read Bilal's answers fully before asking the next round. Follow-up beats a preset list.
- When an answer opens a new thread, pull that thread before moving on.
- Note what Bilal explicitly says he wants to add, change, or remove — those are editorial directives, not suggestions.

---

## PHASE 4 — Write and Deliver

### Column Identity

**Publication:** Doug Passon's Substack (guest column)
**Column name:** Surviving the Feds: Dispatches from the Inside
**Author:** Bilal Khan
**Voice:** First-person, written FROM inside FCI Fort Dix
**Audience:** Family members of federal defendants, people navigating or anticipating the federal system, engaged citizens following criminal justice issues

This is not a legal journal. It is not a policy brief. It is a dispatch — one person with 14+ years inside the federal system telling readers what they need to know, from where he is right now.

---

### Platform Rules (Research-Backed — Do Not Guess)

From analysis of 94,000+ Substack posts and the Marshall Project's "Life Inside" standard.

**Length:** 900–1,400 words. Top-50 Substack publications average 871 words. 1,600–1,800 is defensible for a high-stakes piece; not routine.

**Title:** First-person, 13–17 words, no question marks. Titles with "I" or "My" outperform all others by ~30%. Question marks suppress subscriber conversion. Model: *"I Reported the Condemned Building to an Associate Warden. She Agreed. The Bleachers Are Still There."*

**Subtitle (6–10 words):** This becomes the email preview text — the second line every subscriber sees before deciding to open. Model: *"Nine years inside Fort Dix. Here's what federal neglect actually looks like."*

**Opening:** Single vivid scene. In medias res. No preamble. One sentence or a short 2-sentence paragraph. Reader drop-off spikes at the 25% scroll mark when the opening fails.

**Paragraphs:** 2–3 sentences maximum. One sentence is fine. One idea per paragraph. Front-load the point.

**Subheadings:** None in narrative sections — use horizontal dividers (`---`) instead. Acceptable for the actionable section only. Never more than 2–4 if used at all.

**Ending:** (1) Literary close echoing the opening → (2) Direct question to comment section → (3) Sign-off → (4) Bio block.

**Write for email first.** Most subscribers read in their inbox. No load-bearing hyperlinks — everything important lives in the prose.

---

### Voice

Full spec in `docs/VOICE.md`. Dispatch adaptations:

**First-person throughout.** Bilal as narrator. Reader sees the world through his eyes. Pivot to "you" only in the actionable section.

**Earned profanity.** Marks the exact moment of institutional failure or life-altering stakes. Not decoration. Not removed for squeamishness.

**ALL CAPS: once per article maximum, and only if earned.** The one procedural point that, if missed, causes irreversible harm. Format: `WARNING: [STATEMENT IN FULL CAPS]`

**This slot is optional. If no verified do-or-die fact exists, leave it out.** An empty slot in a template is not a prompt to invent something to fill it. A fabricated warning in a piece families rely on is worse than no warning at all. Both drafts of the Fort Dix officer dispatch failed here: one asserted that a PREA allegation dies on transfer, the other that a man moved for his protection never gets moved back. Neither is true. Neither came from Bilal or from any source. Both were written because the template had a hole in it.

**Specificity is the credibility.** Name the facilities, the forms, the laws, the program statements. Abstract claims land nowhere. Specific ones land everywhere.

**No false comfort.** If hard, say hard. If the system's solution is worse than the problem, say that.

---

### Bilal's Credibility Profile

Do not invent or extrapolate beyond these facts.

- Incarcerated May 9, 2012 — present. FCI Fort Dix. Projected release July 2028.
- United States Marine Corps veteran.
- Facilities in order: Doña Ana County (Las Cruces, NM) → Torrance County/CoreCivic (Estancia, NM) → Otero County (days) → FTC Oklahoma City → FDC Philadelphia → FCI Fort Dix (Aug 2016) → Lower Buckeye Jail/Maricopa County (Dec 2016–Jun 2017, Arpaio's jails, state IAD writ) → FCI Fort Dix (Jun 2017–May 2025) → FCI Big Spring TX → USP Lewisburg + FTC Oklahoma City (transit, twice) → FCI Fort Dix (Oct 2025–present).
- *Khan v. Barela* — 10th Circuit; pretrial detention rights; settled.
- Filed habeas corpus petitions from inside, including one challenging a 30-year BOP APA violation regarding sentence calculation.
- Sued BOP for retaliatory transfer to Big Spring; Cole Schotz pro bono; government transferred him back to Fort Dix — believed exceedingly rare or unique in BOP history. Settlement: government must show cause and give notice before any future transfer. Public record, FOIA-able.
- Helped inmates win sentence reductions, immediate releases, civil suits. *U.S. v. Marshall*: 25+ years → 8 years via §2255.
- Taught BOP case managers to correctly calculate First Step Act credits.
- Author: *Surviving Pretrial* and *The 2255 Motion Handbook* (Surviving the Feds Series, Amazon).
- **Do not reference offense type or case charges — ever.**

---

### THE SOURCING RULE — read this before writing a single sentence

Every factual sentence in a dispatch must trace to one of exactly two places:

1. **Bilal said it** in the interview, or
2. **A verified source** confirmed it — statute, regulation, published opinion, agency report, or news reporting you actually read.

**If a sentence traces to neither, cut it.** Not soften it, not hedge it — cut it. There is no third category. "It follows logically," "this is how prisons work," and "any reader would assume" are not sources.

**The rule is about attribution, not verifiability.** Most of what makes this column worth reading is Bilal's experience, and most of that cannot be cited to anything. That is fine — it is the product. What matters is that each kind of claim is written as what it is:

| Kind of claim | How it must be written |
|---|---|
| What Bilal watched, did, or concluded over fourteen years | First person, as his experience. "What I have watched happen is…" "They will tell you X. What actually happens is Y." |
| What compound talk says | Named as rumor, explicitly. |
| A rule, right, deadline, form, or citation a family will act on | Verified against the source, or it does not go in. |

**The failure is never "Bilal said something I could not verify."** The failure is a writer *inventing* a claim, or taking lived experience and dressing it up as a rule. "In my experience the SHU is where they put you first and sort it out later" is publishable. "Protective segregation is permanent" is a fabricated rule wearing a fact's clothes.

When Bilal's experience contradicts the regulation, **print both** — that gap is frequently the whole point of the piece. Do not resolve it by deleting his half.

This is the failure mode that has cost the most rework, and it is seductive because invented claims are usually *plausible* and always *convenient*. They arrive precisely when a paragraph needs a beat, a warning slot needs filling, or a contrast needs sharpening. Real examples from the Fort Dix officer dispatch, each caught by Bilal after it was written:

| Invented | Reality |
|---|---|
| "If he is transferred before he files, he has lost it." | 28 C.F.R. § 115.63 — the receiving facility must notify within 72 hours and the original facility must investigate. Transfer waives nothing. |
| "She went on **paid** administrative leave." | No source said paid. Bilal watched her keep working, moved away from inmates. |
| "ONCE HE IS MOVED, HE DOES NOT GET MOVED BACK." | Invented outright. Contradicted Bilal's own account that the institution later began asking men first. |
| "That is not a sex offender unit, but…" | Rebutting a question no reader asked. Describe what a thing *is*. |

**A specific trap: institutional practice.** Claims about what BOP "always" or "never" does, how staff "typically" respond, or what "happens next" are the easiest things to invent and the hardest for a reader to check. Bilal is the source for those. Ask him; do not reason your way to them.

**A second trap: sharpening a contrast.** When an asymmetry is the point, there is pressure to make each side more extreme than the record supports. "He went to the SHU, she kept working" is true and devastating. "Paid administrative leave" was neither.

### Handling Bilal's raw text

He writes fast, on a monitored prison email system, with no ability to revise comfortably. His messages contain typos, dropped words, and phonetic mangling.

- **Never render a transcription artifact as prose.** A draft once published the phrase "others will be far the otherwise" verbatim. It is not a sentence. He meant officers who go far in the *other* direction — extremely nice, trying to please.
- **When a phrase is unclear, ask him.** Do not guess at meaning and do not quietly drop the sentence. One question costs a minute; a wrong guess costs his credibility.
- **Preserve his diction, fix his typing.** "Give a shit," "thrown to the wolves," "a shot" for an incident report — keep. Misspellings and dropped words — fix silently.

### Writing about named living people

Dispatches often turn on a real person facing real charges.

- Anything about a charged person traces to **published reporting** or **Bilal's direct observation** — never to inference, and never to compound rumor presented as fact.
- **Keep consequences conditional.** "A conviction makes her a registered sex offender," not "she will register."
- **Never merge two people.** If the material contains a man whose hair was braided and a different man in the case, they are two men. A title once implied they were the same person.
- Bilal decides whether to name anyone. Ask; do not assume public reporting settles it.

---

### Article Structure Template

```
[TITLE — first-person, 13–17 words, no question mark]
[SUBTITLE — 6–10 words, adds urgency the title couldn't carry]

By Bilal Khan
*Surviving the Feds: Dispatches from the Inside*

---

[OPENING — single vivid scene, 1–2 short paragraphs, ends on tension]

---

[BODY — narrative prose, dividers between major sections, 2–5 sections]
[Short paragraphs. Specific detail. No abstraction. No subheadings.]

---

[ACTIONABLE SECTION — **What you can actually do about this**]
[Specific procedures, form numbers, deadlines, program statements]
[OPTIONAL — WARNING: ALL CAPS DEADLINE OR CRITICAL POINT]
[Include ONLY if a verified do-or-die fact exists. Never invent one to fill this line.]

---

[LITERARY CLOSE — 2–4 short paragraphs echoing the opening image or line]

---

[COMMENT PROMPT — italic, one direct question to the audience]

---

Be Well, Stay Safe, and Survive the Feds,
~Bilal

---

*Bilal Khan has been incarcerated in the federal system since May 2012.
He is a United States Marine Corps veteran and the author of* Surviving
Pretrial *and* The 2255 Motion Handbook*, both available on Amazon under
the Surviving the Feds Series. This column reflects personal experience
and is not legal advice.*
```

---

### Quality Checklist — Gate Before Generating .docx

**Run the sourcing audit first. It gates everything below.**

- [ ] **Every factual sentence traces to Bilal or to a verified source.** Walk the draft line by line and name the source for each claim out loud. Any sentence you cannot source gets cut, not hedged.
- [ ] **No invented institutional practice** — nothing about what BOP "always," "never," or "typically" does that Bilal did not say
- [ ] **The ALL CAPS warning, if present, states a verified fact** — and is absent entirely if no such fact exists
- [ ] **No transcription artifacts from Bilal's raw text** rendered as prose
- [ ] **Two different people are never merged into one**, in the title or the body
- [ ] **Consequences for charged people stated conditionally** ("a conviction makes her…")
- [ ] **Word count verified by script, not estimated** — run the counter and read the number

- [ ] Title: first-person, 13–17 words, no question mark
- [ ] Subtitle: 6–10 words, adds urgency beyond the title
- [ ] Opening: single scene, no preamble, lands in the first sentence
- [ ] Paragraphs: 2–3 sentences max throughout; no walls of text
- [ ] Word count: 900–1,400 words
- [ ] No subheadings in narrative sections; dividers only
- [ ] ALL CAPS used at most once, on a genuine do-or-die point
- [ ] Earned profanity present where it lands; not sanded off, not gratuitous
- [ ] Actionable section present with specific forms, procedures, deadlines
- [ ] No load-bearing hyperlinks — all critical info is in the prose
- [ ] Literary close echoes the opening
- [ ] Comment question present before sign-off
- [ ] Sign-off and bio block present
- [ ] No reference to offense type or charges
- [ ] Inmate rumor explicitly distinguished from documented fact
- [ ] Research brief claims that needed verification were verified or flagged
- [ ] Source file saved to `content/substack/[slug].md`

---

### Delivery Workflow

**Step 1:** Save source file to `content/substack/[slug].md`

**Step 2:** Generate .docx
```bash
python3 scripts/dispatch_wordcount.py content/substack/[slug].md   # gate: must PASS
python3 scripts/substack_to_docx.py content/substack/[slug].md
```

**Step 3:** Verify .docx structure
```bash
python3 -c "
from docx import Document
doc = Document('content/substack/[slug].docx')
for i, p in enumerate(doc.paragraphs[:15]):
    if p.text.strip(): print(f'{i:03d} | {repr(p.text[:70])}')
"
```
Confirm: PUBLISHER CHECKLIST header at top, title and subtitle present, article begins cleanly after the separator.

**Step 4:** Commit and push
```bash
git add content/substack/[slug].md content/substack/[slug].docx
git commit -m "Add Substack dispatch: [short description]"
git push
```

**Step 5:** Deliver .docx to user via SendUserFile.

---

### What the .docx Gives Doug

Doug opens one Word document:
- **Shaded blue cover block** (NOT the article): title, subtitle, column tag, guest author instruction
- **Article body** below the separator: bold, italic, horizontal rules, and WARNING text render correctly when pasted into Substack's editor

Doug's workflow: open → read checklist → paste → done.

---

## Subagent Architecture Summary

| Task | Who does it | Notes |
|---|---|---|
| Topic discovery | General-purpose subagent | Phase 1; only when Bilal has no story in hand |
| The account | Main agent, inline | Phase 2; cannot be delegated. Comes FIRST. |
| Deep research | General-purpose subagent | Optional. Only when Bilal says he doesn't know the subject — ask him. |
| Verification | General-purpose subagent | Phase 3; runs silently in background. Names, dates, and any rule a reader would act on. Bilal never reads it. |
| Writing | Main agent | No writing subagent |
| Word-count gate | Bash tool, inline | `scripts/dispatch_wordcount.py` — must PASS before .docx |
| .docx generation | Bash tool, inline | `scripts/substack_to_docx.py` |

Do NOT re-research Substack platform mechanics — that is baked into this document. Only re-research if Substack announces significant format or algorithm changes.

---

## Article Pipeline

| # | Topic | Status | Notes |
|---|---|---|---|
| 1 | Infrastructure — Fort Dix | ✅ Complete | `fort-dix-infrastructure-condemned.md` |
| 2 | BOP Disability Accommodations Program Statement | Queued | Teased in article #1; Bilal has used it successfully |
| 3 | The Retaliatory Transfer | Queued | Full story: TRO, Cole Schotz, chambers conference, settlement, return |
| 4 | Administrative Remedies: Your Only Real Power | Queued | BP-8 through BP-11; the record is the foundation |
| 5 | The First Step Act: What You're Actually Getting | Queued | Credits, halfway house, supervised release trap |
| 6 | Doug's second requested topic | TBD | Confirm with Bilal |
| 7+ | Phase 1 research will surface additional topics | Research-driven | Run Phase 1 when pipeline runs low |
