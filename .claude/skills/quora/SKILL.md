---
name: quora
description: Answer Quora questions in Bilal Khan's voice — classifies each question as research-required, personal-experience, or mixed, researches and/or interviews Bilal accordingly, then drafts a short conversational answer ready to paste into Quora. Invoke with /quora.
---

# Quora Answer Skill
## Surviving the Feds — Q&A

This skill governs every answer Bilal posts on Quora. It is lighter-weight than
the Substack pipeline (`substack` skill) — most questions can go from prompt to
finished answer in one sitting. The one rule that never bends: don't write a
word of the answer until you know whether this question needs research, Bilal's
personal account, or both.

---

## ENTRY BEHAVIOR — what to do when /quora is invoked

**If a question is pasted with the command:** Go straight to Step 1 (Classify).

**If /quora is invoked with no question:** Ask Bilal to paste the question text
(and the Quora space/topic if he knows it — sometimes the framing of the space
changes what angle the answer should take).

---

## STEP 1 — Classify the question

Every question is one of three types. Decide before doing anything else.

**A. Personal-experience.** The honest answer only exists inside Bilal's own
years in the system. No amount of outside research substitutes for it — the
research would just be other people's speculation. These are the highest-value
answers because nobody else on Quora can write them.
> Example: *"If you stay quiet, mind your business, are polite, and do not
> interfere, will other inmates leave you alone? Will they still mess with you,
> beat you up, etc.?"* — this lives entirely in what Bilal has seen, at which
> facilities, over which years. Skip research. Go to Step 2B.

**B. Research-required.** The question is definitional, procedural, or general
knowledge — it has a correct factual answer that exists independent of Bilal's
experience. Still worth Bilal's voice and a personal angle where one genuinely
fits, but the backbone is accurate information, not memory.
> Example: *"What does a trust do?"* — a real, researchable, factual question.
> Go to Step 2A.

**C. Mixed.** The question has a factual/legal core (BOP policy, a legal
mechanism, a procedure) but the real value-add is what actually happens versus
what's on paper. Research the facts first, then bring them to Bilal to react to.
Go to Step 2C.

When in doubt, ask yourself: *if Bilal weren't a federal prisoner, could a good
generalist researcher still produce a solid answer?* If yes, it's A or A-leaning
B. If the answer is worthless without his firsthand account, it's A.

---

## STEP 2A — Research path (Type B)

Spawn a general-purpose research subagent:

> Research the following question thoroughly for a short Quora answer:
> **[QUESTION]**
>
> Context: the answer will be posted by Bilal Khan, a federal prisoner and
> author writing under "Surviving the Feds." Keep it tight — this informs a
> 150–500 word Quora answer, not an article.
>
> Return:
> 1. A plain-English, accurate answer to the question (2–4 sentences a smart
>    non-expert could act on).
> 2. Any common misconceptions worth correcting.
> 3. 2–4 places where Bilal's personal experience inside the federal system
>    could add real color or a concrete example — flag these as questions for
>    him, not assumptions.
> 4. Anything that needs a citation or verification before it's stated as fact.

After the subagent returns, read the brief. If it surfaced a genuine spot for
Bilal's personal experience, ask him those specific questions inline (keep it
to 1–3 quick questions — this is not a full interview). Otherwise go straight
to Step 3.

---

## STEP 2B — Personal-experience interview (Type A)

**Do not open with a checklist.** Start with an open brain dump:

> "[Restate the question in one line.] Just talk it through — whatever comes
> to mind, in whatever order. I'll ask follow-ups after."

Let Bilal answer in whatever shape it comes. Read the whole thing before
responding.

**Then follow up — only on what's actually missing.** Common gaps to check,
but only ask what the brain dump didn't already cover:

- **Concreteness:** Which facility/facilities is this true of? Does it vary by
  security level (camp vs. low vs. medium vs. USP)? Any exception that proves
  the rule — a specific time it didn't hold?
- **Sourcing:** Is this direct personal experience, something he watched happen
  to someone else, or general reputation/rumor? Say so explicitly — never blur
  the three.
- **The naive misconception:** What does someone who's never been inside get
  wrong about this? What would they assume that's false?
- **The honest caveat:** Is there a "but" that a falsely-reassuring answer would
  omit? (e.g., staying quiet helps, but doesn't make you invisible; specific
  situations still find you.)

Ask in one small round — 2–5 questions, not a form. If an answer opens a new
thread worth pulling, pull it before moving to writing.

---

## STEP 2C — Mixed path (Type C)

Run Step 2A's research subagent first. Bring the brief back to Bilal the same
way Phase 3 of the `substack` skill does: *"The research says X — does that
match what you've actually seen? What's missing or wrong?"* Then fold in a
short version of the Step 2B gap-check for the personal layer.

---

## STEP 3 — Write the answer

Quora is not a blog post. Read `docs/VOICE.md` for the full voice spec, but
apply these deltas for this format:

**Answer the question in the first 1–2 sentences.** No scene-setting, no
epigraph, no wind-up. Quora readers (and Quora's own ranking) reward getting to
the point immediately. Everything after the opening supports or complicates
that direct answer.

**Length:** 150–500 words for most questions. Up to ~800 for a question with
real depth (like the inmate-conflict one) — but only if every sentence is
earning its place. Quora answers that ramble get skimmed and skipped.

**First-person, conversational register.** This reads like Bilal talking to
someone across a table, not like an article. Contractions are fine. It can be
looser than the blog voice — but the DNA is the same: short declaratives,
no hedging, no false comfort, specificity over abstraction (name the facility,
the situation, the actual outcome).

**No subheadings. No forced ALL CAPS.** Reserve caps for a genuine "don't get
this wrong" moment, and even then use it more sparingly than the blog — Quora's
register is a conversation, not a warning label. Most answers should have zero.

**Distinguish sourcing in the text itself** when it matters: "I've seen this
myself" vs. "I never saw this happen, but guys who tried it—" Don't blur the
two just for a cleaner narrative.

**No forced sign-off, no bio block, no CTA.** Quora carries Bilal's profile and
credentials separately. Only mention the books if a reader would genuinely want
to go deeper on that exact topic (a legal-mechanism question, not a
personal-experience one) — one line, no pitch, easy to cut if Bilal doesn't
want it that time.

**End on the real answer, not a flourish.** It's fine to end on a plain,
slightly blunt closing line if that's how the thought actually ends. Don't
manufacture a literary close.

---

## STEP 4 — Save and deliver

1. Save the answer to `content/quora/[slug].md` with light frontmatter:
   ```
   ---
   question: "[full question text]"
   type: personal | research | mixed
   date: YYYY-MM-DD
   ---
   ```
2. Show Bilal the answer as plain text, ready to copy straight into Quora — no
   extra formatting, no markdown syntax that Quora's editor won't render as
   intended (use plain bold/italic only if Quora's editor supports it; when
   unsure, keep it plain text).
3. Ask if he wants it committed. Don't commit and push without him confirming
   — unlike the blog/Substack pipeline, these are quick and he may want to post
   several before ever touching git.

---

## Quality checklist — before showing the draft

- [ ] Direct answer lands in the first 1–2 sentences
- [ ] Length fits the question (150–500 typical; 800 ceiling for real depth)
- [ ] First-person, conversational — reads like a table conversation, not an article
- [ ] No subheadings; ALL CAPS used zero or once, only if truly earned
- [ ] Sourcing distinguished where it matters (saw it himself vs. heard about it)
- [ ] No false comfort — the honest caveat is in there if one exists
- [ ] Book mention (if present at all) is one line and genuinely on-topic — not a reflex
- [ ] No reference to Bilal's offense type or case charges
- [ ] Saved to `content/quora/[slug].md` with frontmatter
