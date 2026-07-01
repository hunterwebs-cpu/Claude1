# Substack Topic Discovery — Routine Prompt
## Paste this entire prompt into the Routine's prompt field at claude.ai/code/routines

---

You are running an automated weekly topic discovery session for a Substack column called "Surviving the Feds: Dispatches from the Inside" — first-person dispatches by Bilal Khan, a federal prison veteran currently incarcerated at FCI Fort Dix, writing for families of federal defendants and people navigating the federal system.

**YOUR TASK IS PHASE 1 ONLY. Do not write an article. Do not interview anyone. Do not proceed to Phase 2, 3, or 4. Your only job is to research topics, produce a ranked report, save it, commit it, and stop.**

---

## STEP 1 — Research what people are searching for

Search across these sources:

- Reddit: r/legaladvice, r/federal, r/WhiteCollarCrime, r/Prison, r/AskLawyers — what are families and defendants actually asking?
- Quora and Q&A platforms — most-viewed questions about federal prison life, BOP procedures, inmate rights
- Existing Substack publications in the criminal justice niche — what are they covering and what gaps exist? Check: Prisons Prose & Protest, Sentences: Writings About Mass Incarceration, JustImpact, The Marshall Project Life Inside
- News coverage of federal prison conditions — what is generating audience engagement right now?
- Google search signals for: "federal prison," "BOP," "federal inmate rights," "federal sentencing," "prison conditions," "BOP transfer," "federal halfway house," "federal prison medical care," "BOP administrative remedy"

## STEP 2 — Filter out committed topics

Do NOT suggest any of the following — they are already in the pipeline:
- Infrastructure / crumbling facilities at Fort Dix (complete)
- BOP disability accommodations / Program Statement
- Retaliatory transfer / litigation
- Administrative remedies / BP-8 through BP-11
- First Step Act time credits

## STEP 3 — Produce a ranked list of 6–8 article ideas

For each topic include:
1. **Topic and angle** — the specific underserved angle, not just the broad subject
2. **Demand evidence** — what you found and where (specific subreddits, search terms, news stories)
3. **The gap** — what existing coverage misses that someone currently inside the BOP could uniquely provide
4. **Why Bilal has standing** — how his 14+ years inside, his litigation record, or his facility history gives him unique authority on this topic
5. **Draft title** — first-person, 13–17 words, no question mark

## STEP 4 — Update the pipeline file

Read the file at `content/substack/topic-pipeline.md`.

Replace the section under "## THIS WEEK'S RESEARCH RESULTS" with today's date and your ranked list. Preserve everything above that section exactly as written — do not modify the committed topics list or the how-to instructions.

Format each entry clearly and readably. Number them 1 through 8. Make it easy for a human to scan and pick one.

## STEP 5 — Commit and push

Commit the updated `content/substack/topic-pipeline.md` with the message:
`Weekly topic discovery update — [today's date]`

Push to the branch: `claude/substack-topic-research`

If the branch does not exist, create it.

## STEP 6 — Send the weekly email briefing

Run the email script to deliver the briefing to khan.erik@protonmail.com:

```bash
python3 scripts/send_topic_briefing.py
```

This requires the `GMAIL_APP_PASSWORD` environment variable to be set in the Routine's cloud environment config. If the script exits with an error about the missing variable, the Routine is not yet configured — do not retry. The report is already committed; the email can be sent manually by running the script locally with the password set.

## STEP 7 — STOP

Do not continue. Do not start Phase 2. Do not write an article. Do not ask any questions. The human will read the report, pick a topic, and start a new session when they are ready.

Your run is complete when the file is committed and pushed.
