---
name: quora
description: Research and draft Quora answers on legal/constitutional issues for the author's blog, in his right-of-center-libertarian voice. Either-or entry — give a topic and go straight to research and interview, or let the skill scour Quora for a high-buzz legal topic in the author's wheelhouse. Full pipeline — topic discovery (optional), deep legal research, targeted interview, write and deliver as a copy-paste-ready formatted document. Invoke with /quora.
---

# Quora Skill

This skill governs every Quora answer written for the author's blog. It exists because a single real engagement (the Maryland Community Trust Act / Supremacy Clause piece) proved out the whole pipeline: parallel legal research, an iterative interview that pulled out the author's actual voice and stakes, and a hard lesson that Quora's paste box eats markdown, so delivery must be a real formatted document.

Follow the phases in order. Do not start writing until the interview is done. Do not deliver chat-pasted markdown — always deliver a formatted file.

---

## ENTRY BEHAVIOR — What to do when /quora is invoked

This is an **either-or opener**. Read what the user gave you and pick a path:

**Path A — Topic given.** The user supplies a question or topic at invocation (e.g. "/quora does X law violate the Y clause"). Skip Phase 1 entirely. Go straight to Phase 2 (deep research), then Phase 3 (interview). Research and interview happen back-to-back in the same sitting — don't make the user wait a phase boundary to start talking.

**Path B — No topic.** The user invokes /quora with nothing else, or says something like "I don't have an idea." Run Phase 1: scour Quora (and adjacent signals) for a legal/constitutional topic in the author's wheelhouse that's likely to generate real engagement. Present a ranked shortlist. Let the user pick, then proceed to Phase 2.

**Shortcut — user arrives with a story.** If the user opens with a personal anecdote or a thing they just witnessed ("I saw X happen," "I know a guy who..."), skip straight to Phase 3 with that story as the seed, then loop back to Phase 2 to fact-check and contextualize it. The story is often the actual hook — don't bury it under a research phase first.

---

## THE PIPELINE — 4 PHASES

```
PHASE 1: Topic Discovery   → OPTIONAL, only when no topic was given
                              Subagent scours Quora + adjacent signals for a
                              high-buzz legal/constitutional angle in the
                              author's wheelhouse. Returns a ranked shortlist.
                              ↓
PHASE 2: Deep Research     → Parallel subagents (legal-research skill method,
                              scaled down) research the statute/case/doctrine.
                              ↓
PHASE 3: Interview         → Main agent interviews the author inline: personal
                              stake, anecdotes, framing, what to cut, what to push.
                              ↓
PHASE 4: Write & Deliver   → Main agent writes the piece, runs the quality gate,
                              converts to a real formatted document, delivers it.
```

---

## PHASE 1 — Topic Discovery (only when no topic given)

**Goal:** find a legal/constitutional question that's (a) actually generating engagement right now and (b) squarely in the author's wheelhouse — federalism, Supremacy Clause and preemption, anti-commandeering, immigration enforcement mechanics, Fourth Amendment/warrant law, gun rights, DOJ-vs-state fights, criminal justice — not just any trending news story.

**Spawn a general-purpose research subagent** with this brief:

> Find legal/constitutional topics likely to generate high engagement on Quora, for a blog author who writes from a right-of-center libertarian, "constitution over party" point of view. His recurring interests: federalism and the Supremacy Clause, anti-commandeering doctrine, immigration enforcement fights between states and the federal government, Fourth Amendment and warrant distinctions, Second Amendment federalism, and DOJ-vs-state litigation.
>
> Search across:
> - Quora itself (site:quora.com searches for the topic areas above) — which questions have unusually high answer counts, views, or recent activity?
> - Current news on state-vs-federal legal fights (DOJ lawsuits against states or vice versa, new state legislation restricting or expanding cooperation with federal agencies, recent circuit or SCOTUS rulings touching federalism)
> - Reddit (r/law, r/supremecourt, r/politics) and Google "People Also Ask" for the same topic areas, as a secondary signal of what people are actually confused about or arguing over
>
> Return a ranked list of 5–8 candidate topics, each with:
> 1. The specific question or angle (phrased as a real Quora-style question)
> 2. Evidence of buzz — what you found and where
> 3. Why it fits this author's wheelhouse and voice specifically (not just "it's legal news")
> 4. The core legal tension in one sentence (what makes it genuinely contestable, not a settled question nobody's arguing about)

**After the subagent returns:** present the shortlist as a numbered list. Let the author pick or redirect — his read on what's worth his voice overrides the algorithm.

---

## PHASE 2 — Deep Research

**Goal:** get the underlying law right before anyone starts writing a word. Do not let voice or virality considerations touch this phase — it is pure fact-finding.

**Use the `legal-research` skill's methodology, scaled down.** That skill is built for six-track bankruptcy court filings — do not run the full six-track/PDF pipeline. Instead:

- Spawn 2–4 parallel `general-purpose` research subagents (not six), each scoped to one piece: e.g. (1) the actual statute/bill text and its current legal status, (2) the controlling constitutional doctrine and its leading cases, (3) any narrower legal wrinkle that needs its own deep dive (e.g. a specific circuit split, a specific doctrinal distinction).
- Apply the same source-priority stack: CourtListener → Google Scholar → Justia for case law; official government sites (state legislature bill-tracking pages, GovInfo, Congress.gov) for statutory text; secondary sources (news, advocacy orgs) only for context and leads, always flagged.
- Each subagent reports back with pinpoint citations, verbatim key quotes, and a `[VERIFY]` flag on anything it couldn't confirm from a primary source.
- Skip the PDF-generation and court-filing formatting entirely — this is a research memo for fact-checking a general-audience piece, not a filing.
- **Always try to identify the current news hook** — is there active litigation, a recent bill signing, a public statement from an official? That's usually the actual reason the topic is hot, and it belongs in the opening of the piece, not buried.

**After the subagents return:** synthesize into a short internal brief — what the law actually says, what the controlling doctrine holds, and where (if anywhere) the honest answer is "this part is genuinely contested," not "here's my hot take." Identify 3–5 gaps or tensions that only the author's personal read or experience can resolve — those become the interview questions.

---

## PHASE 3 — Interview

**Conducted inline, conversationally — never delegated to a subagent.** This is where the piece gets its actual voice, not just its facts.

### Standing questions (ask a relevant subset every time, in rounds of 4–6, not all at once)

**Personal stake:**
- Do you have a personal story, case, or firsthand encounter that illustrates this? (This is often the single strongest thing in the piece — see the wrongfully-detained-citizen story from the Maryland piece.)
- Is there a specific detail — a dollar figure, a distance, a timeline — that you're not 100% certain of? Flag it now so it gets hedged ("roughly," "about") before publication instead of after someone challenges it in the comments.

**Framing:**
- How hard do you want the self-ID/soapbox close this time — front and center, a brief mention, or skip it entirely for this one?
- Is there a concrete policy proposal or compromise you want to pitch, instead of just picking a side? (The masks-for-bodycams trade in the Maryland piece is the model: acknowledge a legitimate concern on each side, propose an actual trade.)
- Is there a steelman you want included — a real cost or downside on the other side that's honest to admit, even though it complicates the argument? (The ER-cost-of-illegal-immigration paragraph is the model — conceding a real point makes the rest of the piece more credible, not less.)

**Corrections:**
- Anything in the research brief that conflicts with something you know firsthand?
- Anything from a prior draft's structure you want cut because it's no longer load-bearing? (Full Faith and Credit got cut entirely once it stopped being central — don't be precious about sunk sections.)

**Mechanics:**
- Any link the reader should be able to click to verify this themselves (bill text, docket number, statute)?

Read each answer fully before the next round. When an answer opens a new thread — a story, a correction, a strong opinion — pull that thread before moving on to the next standing question. What the author explicitly says to add, cut, or change is an editorial directive, not a suggestion to weigh.

---

## PHASE 4 — Write & Deliver

### Voice

- **Right-of-center libertarian, Constitution-first.** The author voted for Trump and generally supports the administration's direction, but the throughline of every piece is that constitutional limits on power apply regardless of which party is exercising it. Do not soften this into both-sidesism — it's a specific, stated position: pick a rule, apply it consistently, regardless of team jersey.
- **Written from the author to a public Quora audience — never to an assistant.** Every sentence must read as if a stranger on Quora is seeing it for the first time. Never write "you raised earlier" or otherwise reference the private conversation that produced the piece. If a common misconception needs correcting (like the Full Faith and Credit Clause point), frame it as "a common instinct is to reach for X" — a reader's likely assumption, not something "you" personally said.
- **Concede real costs honestly.** If there's a legitimate cost or downside to the position the piece is defending, say so plainly before making the counterpoint. This is a credibility move, not a hedge.
- **Distinguish the real thing from its strawman.** When the topic is adjacent to a genuinely bad-faith version of itself (e.g., non-cooperation with civil detainers vs. physically obstructing federal agents), spell out the distinction explicitly rather than letting the piece get lumped in with the strawman.
- **Prefer a concrete policy trade over a rhetorical win.** Where the topic allows it, close the substantive section with an actual proposal, not just "the other side is wrong."

### Structure (adapt, don't force every section into every piece)

1. **Hook** — the actual news peg (a lawsuit, a bill signing, a public fight) in 2–3 sentences. Not a dry thesis statement.
2. **What the thing actually is/does** — plain-language summary of the law/ruling/policy at issue, with a link to the primary source so readers can check it themselves.
3. **The core doctrine** — the controlling legal framework, with real case names, holdings, and pinpoint quotes from Phase 2 research. Never paraphrase a holding when a verbatim quote is available.
4. **The honest complication** — the part that's genuinely contested or a closer call, stated plainly. Every piece should have one of these; a piece with no real complication reads as partisan cheerleading.
5. **Historical or educational deep-dive** (when it earns its place) — the "why" behind a doctrine, not just the "what." The writs-of-assistance/Fourth Amendment history in the Maryland piece is the model: it makes an abstract legal rule feel like it was fought for.
6. **Personal stakes** — the anecdote from Phase 3, if there is one. This is usually what makes a piece memorable rather than merely correct.
7. **The steelman / cost concession** — the honest "this isn't free" or "this is a fair concern" paragraph.
8. **Distinguishing the strawman**, if applicable.
9. **A concrete policy proposal**, if the author has one.
10. **Soapbox close** — self-ID, the consistency argument, a Federalist Papers or similarly weighty quote if it fits naturally (don't force one in). End on the "pick a rule, apply it consistently" register, adjusted to how hard Phase 3 said to lean into it.
11. **Direct comment prompt** — a specific question tied to the piece's genuinely contested point, not a generic "thoughts?"

### Quality Gate — check before generating the delivery file

- [ ] Primary source (bill, statute, case, docket number) linked or cited with a real citation
- [ ] Every case holding or quote checked against the Phase 2 research, not invented or misremembered
- [ ] Opens on a real hook, not a thesis statement
- [ ] At least one honest steelman/cost-concession present
- [ ] No sentence addresses the reader as if replying to something said privately — audience is Quora at large
- [ ] Personal anecdote figures hedged ("roughly," "about") wherever the author flagged uncertainty in Phase 3
- [ ] The real thing is explicitly distinguished from its nearest bad-faith strawman, if one exists
- [ ] Ends with a specific, non-generic comment-prompt question
- [ ] Author had final say on how hard the self-ID/soapbox close leans in

### Delivery — Quora does not accept pasted markdown

This is the hard lesson from the first run: Quora's answer box does not detect `**bold**` or `## headers` — it pastes them as literal symbols. **Always deliver a document with real formatting already applied, not a markdown file and not raw chat text.**

**Default: an `.rtf` file**, since it opens natively in Word, Google Docs, TextEdit, and WordPad on any platform, and copying from any of those preserves bold/italic/headings when pasted into Quora.

RTF conventions that worked (reuse this template rather than reinventing it each time):

```
{\rtf1\ansi\ansicpg1252\deff0\nouicompat
{\fonttbl{\f0\froman\fcharset0 Times New Roman;}{\f1\fswiss\fcharset0 Arial;}}
{\colortbl ;\red28\green27\blue25;\red43\green69\blue112;}
\viewkind4\uc1\pard\sa240\sl276\slmult1\f0\fs24

\pard\sa280\f0\fs40\b [TITLE]\b0\fs24\par

[body paragraph]\par

\cf2\b\fs30 [Section Heading]\cf1\b0\fs24\par

[body paragraph with \b bold\b0  and \i italic\i0  inline]\par

{\li480 \bullet \b [Bold lead-in]:\b0  [rest of bullet].\par}

\li720\i "[block quote text]"\i0\li0\par
}
```

- Bold: `\b ... \b0`. Italic: `\i ... \i0`. Section headers: `\cf2\b\fs30 ... \cf1\b0\fs24`.
- Bullets: literal `\bullet` inside an `\li480`-indented brace group, one per item.
- Block quotes (e.g. Federalist Papers excerpts): `\li720\i "..." \i0\li0`.
- **ANSI-safe substitutions are mandatory** — this encoding does not tolerate curly quotes, em dashes, or section symbols reliably:
  - em dash `—` → ` -- `
  - curly quotes `" " ' '` → straight `" '`
  - section sign `§` / `§§` → `Section` / `Sections`
  - ellipsis `…` → `...`
- Links: write the full URL as plain visible text (e.g. `https://mgaleg.maryland.gov/...`) rather than an RTF hyperlink field — simpler and more reliably preserved across editors than `{\field{\*\fldinst HYPERLINK ...}}`.

**Fallback: an HTML artifact with a "Copy article" button** (contenteditable selection + `execCommand('copy')`, falling back to the Clipboard API) is a nicer experience when it works, but the artifact link 404'd for the author once already — treat the `.rtf` as the default and only build the HTML version if specifically asked, or as a bonus alongside the `.rtf`, never as the only deliverable.

**Steps:**
1. Save the markdown source to `content/quora/[slug].md` (source of truth, easy to diff and re-edit).
2. Hand-author the matching `.rtf` at `content/quora/[slug].rtf` following the template above — do not attempt to build an automated markdown→RTF converter; the escaping rules are simple enough to apply directly and a hand-written RTF is easier to debug than a converter script.
3. Deliver the `.rtf` via `SendUserFile`, with a caption summarizing what changed since the last version if this is a revision.
4. Only commit/push these files if the author asks — this is personal blog content, not necessarily meant to live in a shared repo history by default.

---

## Author Voice & Stance Profile

Do not invent or extrapolate beyond what the author has actually said across sessions. Update this list as new interviews add confirmed facts.

- Right-of-center libertarian; voted for Trump; generally supportive of the administration's direction.
- Strong, specific disagreement with the federal government pressuring or bullying state/local jails and officers into doing federal immigration enforcement work — "you can't have it both ways" (immigration is exclusively federal *and* states must help enforce it).
- Believes a warrant issued by an actual Article III judge/magistrate must be honored; does not consider an ICE administrative detainer/warrant equivalent, and wants that distinction explained on the merits (Fourth Amendment probable-cause/neutral-magistrate requirement), not hand-waved.
- Supports immigration law being enforced — fairly and safely — against people actually here unlawfully. This is not an open-borders position; it's a due-process-first position.
- Has personal proximity to the federal criminal justice system and has witnessed U.S. citizens wrongly detained/delayed by ICE/BOP due to inadequate identity verification — treats this as a serious, non-hypothetical harm, not a rhetorical device.
- Fiscally conservative: opposes unfunded federal mandates that push enforcement costs onto state/local budgets; sees "make the level of government that owns the policy pay for it" as a small-government principle, not a partisan one.
- Prefers concrete bipartisan policy trades over "all-or-none" partisan trench warfare — wants pieces to end with an actual proposal where one is available, not just a rhetorical win.
- Comfortable citing the Federalist Papers (Madison, Nos. 45 and 51 used so far) and anti-commandeering doctrine (Printz, New York v. United States, Murphy v. NCAA) to argue that constitutional limits must bind regardless of which party currently holds power.
- Hard rule: articles are authored **from him to the public**, never addressed to an assistant or referencing the private conversation that produced them.

---

## Subagent Architecture Summary

| Task | Who does it | Notes |
|---|---|---|
| Topic discovery (Phase 1) | `general-purpose` subagent | Only when no topic was given; run in foreground, present shortlist |
| Deep research (Phase 2) | 2–4 parallel `general-purpose` subagents | Scaled-down `legal-research` methodology; run in parallel, foreground |
| Interview (Phase 3) | Main agent, inline | Conversational; cannot be delegated |
| Writing (Phase 4) | Main agent | No writing subagent |
| RTF authoring | Main agent, by hand | Follow the template in Phase 4; no converter script |

Do not re-research Quora platform mechanics or RTF escaping rules from scratch each time — both are documented above. Only redo that research if Quora changes its paste behavior or a new formatting failure surfaces.
