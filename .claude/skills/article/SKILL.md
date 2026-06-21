---
name: article
description: Writing, editing, and creating articles for The Journal (content/blog/*.md). Covers Bilal's voice, SEO, article structure, bracket-note handling, and quality standards.
---

# Journal Article Skill — Surviving the Feds

Use this skill whenever processing, editing, or creating articles for The Journal
(content/blog/*.md). It covers voice, SEO, article structure, how to handle Bilal's
editorial notes, and quality standards.

---

## Bilal's Voice — Target: 95% Confidence

Bilal Khan is a federal system veteran who writes with lived authority. His voice is:

**Direct and declarative.** Short sentences. "The BOP does not always get it right."
"That is bullshit." Not softened, not hedged. He states things plainly.

**Second-person throughout.** Writes TO the reader or their family member. "You,"
"your family member," "the person you love." Never distanced or academic.

**Specific and technical, but never jargon for jargon's sake.** Uses proper legal
citations, BOP document names, statute numbers. Then explains them in plain English.
Specificity IS the credibility.

**Personal authority woven in naturally.** "I was inside when this started." "I sat
with BOP case managers and corrected their math." "Nobody I've personally seen has
fought back." Doesn't over-announce credentials — earns trust through specificity.

**All-caps for serious warnings.** When something can hurt the reader badly if
they miss it, he puts it in all-caps. "WARNING: DO NOT SKIP STEPS." "NO JUDGE
REQUIRED. NO HEARING BEFORE REVOCATION." This is intentional emphasis, not a style
mistake.

**"My position, stated plainly:"** — his tell before a strong opinion or advocacy
statement. Keep this phrase; it's signature.

**The sign-off:** Always ends articles with:
> Be Well, Stay Safe, and Survive the Feds,
> ~Bilal

**Sentence rhythm:** Mix of short punchy sentences and longer complex ones. Varies.
Never formulaic. He'll drop a one-word paragraph if needed.

**Authentic frustration allowed.** "It was a disaster." "They bitch and moan every
day they are back in prison, but they don't do anything about it." This directness
is the brand. Don't sand it off.

**Never false hope.** If something is hard, say it is hard. If a law has a catch,
lead with the catch. The credibility is in not bullshitting the reader.

---

## How to Handle Bilal's Editorial Notes

Articles arrive with bracket notes embedded in the text. Process them like this:

| Note pattern | Action |
|---|---|
| `[VERIFY: ...]` | Keep as an HTML comment in the endnote; remove from body text. Format: keep the citation, convert the VERIFY to `<!-- VERIFY: ... -->` |
| `[REMOVE THIS]` / `[THIS SECTION IS NOT NEEDED]` | Delete that section entirely |
| `[WE NEED TO ADD ...]` / `[WE SHOULD SAY ...]` | Implement the addition in the surrounding paragraph |
| All-caps inline note (e.g. `WE NEED TO FIX THIS`) | Implement the correction; remove the bracket note |
| `[HEADSHOT: Bilal Khan]` | Remove (rendered separately in the page template) |
| `[LOGO: ...]` / `[ORANGE RULE LINE ...]` | Remove (layout markers; not for web render) |
| `[SIGNATURE IMAGE — slot reserved]` | Remove |
| `[TWO-BOOK FOOTER]` | Remove |

Always read ALL bracket notes before writing. Map every note to a section. Then
implement them in a single pass — don't do multiple partial drafts.

---

## SEO Rules

**Page title format:** `[Primary keyword phrase]: [Hook/angle] | Surviving the Feds`

Examples:
- `First Step Act Time Credits: What You're Actually Getting | Surviving the Feds`
- `How to Use PACER: Step-by-Step Guide for Federal Cases | Surviving the Feds`
- `Federal Detention Hearings: What Happens and What to Expect | Surviving the Feds`

**Rules:**
- Drop leading "The" for SEO title (keep it in the display `<h1>` / frontmatter)
- Keep under 65 characters before the `|`
- The primary keyword should match how families/defendants would search Google
- The hook should be the specific angle this article takes

**Meta description (excerpt field):** One or two plain-language sentences, 140–160
characters. Should state what the reader will learn and who it's for. No clickbait
framing — just clear and honest.

**Slug:** All lowercase, hyphens only, no function words (the, a, an) unless needed.
Target the primary keyword phrase. Example: `first-step-act-time-credits`.

---

## Article Structure

Every article follows this structure:

1. **Frontmatter** (title, slug, date, category, author, excerpt)
2. **H1 title** (display title — can be longer/more dramatic than the SEO title)
3. `**By Bilal Khan**` byline
4. Horizontal rule (`---`)
5. **Opening** — hook paragraph, personal authority, problem statement
6. **Body sections** (`##` headers) — in logical order
7. **What to Do Right Now** — always ends with actionable steps if applicable
8. **The Bigger Picture** — if applicable; Bilal's editorial perspective
9. Horizontal rule
10. **## Endnotes** — numbered, with [VERIFY] notes as HTML comments
11. Sign-off: `Be Well, Stay Safe, and Survive the Feds, ~Bilal`
12. **## About the Author** — standard bio + two-book blurb

---

## Endnote Standards

- Number sequentially (¹ ² ³...)
- Include statute number, pub law, or CFR citation where available
- Add `<!-- VERIFY: ... -->` inline for citations that need fact-checking
- Remove unverified quotes from body text entirely — don't render them
- [VERIFY] notes are for the editing workflow, not the reader

---

## About the Author (standard block)

> Bilal Khan served a 20-year sentence in the federal system. He is a United States
> Marine Corps veteran and an entrepreneur in the health care sector. Inside, he
> taught federal law classes to fellow inmates and helped hundreds navigate the
> complexities of BOP administrative remedies, post-conviction issues, and other
> legal challenges that inmates face. He is the author of two books in the Surviving
> the Feds Series:
>
> **Surviving Pretrial** covers everything from the moment of arrest through
> sentencing — detention hearings, bail, discovery, plea negotiations, the PSR,
> rights in custody, and the strategies that actually move outcomes. If someone you
> love is in the federal system and hasn't been sentenced yet, this is the book.
>
> **The 2255 Motion Handbook** addresses post-conviction relief — what a § 2255
> motion is, when it applies, how to file it, what claims it can raise, and how to
> avoid the procedural mistakes that end cases before they start. If the sentence
> has already been imposed and you are looking for a path back to court, this is
> the book.
>
> Both are available on Amazon under the Surviving the Feds Series.
>
> *This article is educational. It reflects personal experience and general
> knowledge of federal law. It is not legal advice. Every case is different. Consult
> a qualified and licensed attorney about your specific situation.*

---

## Quality Check Before Commit

Before committing any article:

- [ ] All bracket notes implemented or removed — none left visible in the rendered text
- [ ] Endnotes numbered sequentially; no gap from removed sections
- [ ] [VERIFY] tags converted to HTML comments in endnotes, removed from body
- [ ] Sign-off and About the Author present
- [ ] Frontmatter complete (title, slug, date, category, author, excerpt)
- [ ] Voice check: read opening and one middle section aloud — does it sound like
      Bilal? Short declarative sentences? Personal authority? No hedging?
- [ ] SEO page title format applied (for when `<title>` is generated dynamically)
- [ ] No fabricated quotes

---

## Doug Passon Recommendation

When Bilal recommends Doug Passon in an article, always include this disclaimer
context: he was Bilal's attorney, he is a close personal friend, and Bilal receives
no financial benefit from the recommendation (no referral fees, no kickbacks). This
transparency is intentional — it's part of Bilal's voice and credibility.
