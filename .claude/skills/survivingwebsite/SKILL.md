---
name: survivingwebsite
description: Build, edit, and extend the Surviving the Feds website (survivingthefeds.com) in this repo — its pages, custom design system, free guides/blog, and deployment. Use whenever working on this project: homepage, Start Here, Books, About, the Journal, the "Is My Lawyer Any Good" page, the planned free guides, styling, copy, or pushing changes live.
---

# Surviving the Feds — Project Handbook

A premium, hand-coded site (PHP includes + CSS + vanilla JS, no build step) for
the brand **Surviving the Feds** by author **Bilal Khan**. Tagline:
**Knowledge + Strength = Freedom.** The mission: put real, lived federal-system
knowledge into the hands of defendants and their families — for free — and sell
the two books. Founder is "present but understated."

> **Full reference spec:** `docs/SITE-SPEC.md` — read it before building or editing
> pages (exact tokens, components, page structures, conventions). This file is the
> quick-start; SITE-SPEC.md is authoritative.

## Hard rules (do not violate)
1. **Never fabricate quotes from the books.** Only use book text the user has
   supplied/approved. Marketing lines must NOT be attributed to the book. If a
   quote's source is unverified, attribute it to the brand ("Surviving the Feds"),
   not the book.
2. **Not legal advice.** All guidance is general, lived-experience information.
   Keep the disclaimer on every page; phrase rights/procedure generally
   ("generally," "in most cases").
3. **The "Jesus / engine of justice" line on Start Here is intentional** and
   stays (the user's reasoning: revered across beliefs as the most honest person,
   so if even he can't get you out, get comfortable). Don't soften it.
4. **Don't reuse the main-site template skeleton for pages that are meant to feel
   different.** Start Here is deliberately bespoke (see below).
5. Keep everything **responsive** and respect `prefers-reduced-motion`. No emojis
   as icons — use inline SVG.
6. **Content must be in the server-rendered HTML.** Articles are rendered by PHP
   (`post.php` + `_posts.php` + vendored `lib/Parsedown.php` + `lib/ParsedownExtra.php`
   for footnotes) so Google and AI
   crawlers that don't run JavaScript (OAI-SearchBot, ChatGPT-User,
   Claude-SearchBot, PerplexityBot) see the full text. `<title>`, meta
   description, canonical, Open Graph/Twitter and JSON-LD are set **in PHP** via
   `_seo.php` (`stf_meta()`, `stf_jsonld()`) — never with JavaScript, and never
   leave a "Loading…" placeholder in the HTML. JS may only enhance content that
   is already there. Article `<title>` format: `[Primary keyword]: [Hook] |
   Surviving the Feds` — set the optional `seoTitle` frontmatter field when the
   display title doesn't already fit it. Use the `article` skill for all
   article editing/creation work.

## Repo & deployment
- Dev branch: **`claude/surviving-feds-site-5n4cmc`**. Work here, then fast-forward
  **`main`** and push. **`main` auto-deploys** to Hostinger (GitHub app integration),
  so a push to main = live in ~a minute. No manual upload.
- Workflow each change: edit → **bump the `?v=N` cache query** on changed CSS/JS
  refs across all HTML (HTML itself is no-cache via `.htaccess`) → commit on dev →
  `git checkout main && git merge --ff-only <dev> && git push origin main` →
  `git checkout <dev>`.
- Local preview: `php -S localhost:8080` from repo root (PHP's dev server ignores
  `.htaccess`, so open `.php` URLs directly; `/sitemap.xml` is `sitemap.php`).
  Images optimized with Pillow (`pip install pillow`).
- `.htaccess` sets HTML to no-cache, static assets long-cache, blocks `/.git`.
- `styles.css`, `main.js` and `blog.js` are cache-busted automatically with
  `?v=<?= filemtime(...) ?>`. Any ref still using a hand-set `?v=N` (e.g.
  `glossary.css?v=1`, `start.css`) must be incremented by hand when that file changes.

## File map
- `index.php` — dark cinematic homepage (hero photo, mission, books teaser,
  reviews, founder teaser, services-coming-soon, journal teaser, CTA).
- `start-here.php` — the **crisis "Emergency Room" sub-brand**: a completely
  separate trade dress from the rest of the site. **Self-contained
  `assets/css/start.css`** (its own reset + `--cr-*` tokens; does NOT depend on
  styles.css). Fonts **Zilla Slab + DM Sans + Caveat**; slate/cool-grey canvas,
  deep-teal accent, aged-parchment intro **letter overlay** (`#cr-letter`), a
  minimal crisis header (`.cr-header`, not the main nav), triage + "command center"
  sections, `assets/img/shield-sf.svg`. Classes are `cr-`-prefixed. **Read
  start.css + start-here.php before editing**; do NOT impose main-site components on it.
- `books.php` — both books with real covers + Amazon links + a real review each.
- `about.php` — Bilal Khan founder story + "taught law to fellow inmates" + S.B.M. testimonial.
- `is-my-lawyer-any-good.php` — podcast + 6-point lawyer checklist (from the book).
- `blog.php` (index) + `post.php` (single, `?slug=`); posts in `content/blog/*.md`
  (Markdown + YAML frontmatter). Both pages render server-side from `_posts.php`
  (frontmatter parsing, listing, Markdown via `lib/Parsedown.php` +
  `lib/ParsedownExtra.php`, which renders `[^n]` footnotes under the article's
  `## Endnotes` heading; references whose definition is only a `[VERIFY]` note
  are dropped with it). `blog.php` outputs the list as real `<a href>` links;
  `blog.js` only enhances: it opens articles in the split-pane reader using the
  body `post.php` rendered, so both views are identical. `content/posts.php` is the JSON index
  `blog.js` falls back to; `content/posts.json` is the last-resort static list.
  Unknown slugs return a real 404 + noindex.
- `_seo.php` — shared `<title>`/meta/canonical/OG/Twitter (`stf_meta()`) and the
  JSON-LD entity graph (`stf_jsonld()`, Organization `#org`, Person `#bilal`,
  WebSite `#website`). Every page uses it, so the @ids never drift.
- `sitemap.php` — generated sitemap, served at `/sitemap.xml` via `.htaccess`.
  Static pages are listed in it; posts are added automatically. lastmod comes from
  frontmatter (`updated`, else `date`) — not filemtime, which Hostinger resets on
  every deploy.
- `admin/` — Decap CMS (publish dashboard); needs GitHub OAuth setup (see DEPLOY.md).
- `assets/css/styles.css` — global design system + tokens. `assets/css/start.css` —
  Start Here bespoke layout only.
- `assets/js/main.js` — sticky nav, overlay mega-menu, scroll reveals (`[data-reveal]`,
  `data-delay`), counters, print buttons (`[data-print]`).
- `assets/img/` — `logo.png` (badge), `cover-pretrial.jpg`, `cover-2255.jpg`,
  `bilal-khan.jpg` (headshot), `photos/` (courtroom, guard-tower, walkway, handcuffs,
  defendant-judge), `uploads/` (CMS).
- `robots.txt`, `sitemap.php`, `DEPLOY.md`, `README.md`.

## Design system
**Brand colors (logo): black + orange + silver.** Tokens live in `:root` in
styles.css. Dark theme: `--bg #0A0B0E`, `--accent #E87722` (orange), silver greys.
**Fonts:** `Fraunces` (display serif), `Oswald` (condensed labels/eyebrows),
`Hanken Grotesk` (body — replaced Inter; do not use Inter). Body copy is tuned
warm/light/airy (line-height ~1.78, subtle negative tracking) for a premium read.
Intro paragraphs use the **`.lead.deck`** class (light Fraunces serif "deck").

Dark-site components: `.btn`/`.btn--primary`/`.btn--ghost`, `.eyebrow`,
`.sec-head.split-head` (editorial two-col header), `.card.card--feature`,
`.hero--photo` (full-bleed photo hero), `.quote-band`, `.page-hero`, `.marquee`,
`.promise`, reviews, `.cta-band--photo`, `.book-photo`/`.cover-img`.

Hero headline effect: `.hl-feds` dims while `.hl-now` ("Now so do you.") paints in
left-to-right (gradient orange, `now-reveal` ~2.7s) — keep it smooth, not typewriter.

**Start Here is its own world** — see file-map note above. It is the "Emergency
Room" crisis sub-brand in `start.css` (`--cr-*` tokens, Zilla Slab/DM Sans/Caveat,
teal + parchment), intentionally NOT the dark brand recolored. Treat it as a
separate design system; don't mix the main `styles.css` components into it.

## Book / brand facts
- **Surviving Pretrial** (Vol 1): paperback ASIN `B0BT19Y3V8`, Kindle `B0BTCDLWN8`.
- **The 2255 Motion Handbook** (Vol 2): paperback `B0D8HQRJN8`, Kindle `B0D9FXJHZZ`.
- Series page: `B0D471H5Z9`. Both 5★ on Amazon; real reviews are used on home/books.
- Podcast: Set for Sentencing — "Is My Lawyer Any Good?"
  `https://setforsentencing.com/podcast/surviving-pretrial-vol-1-is-my-lawyer-any-good/`
- The feds' playbook is named in copy: the **Manual for United States Attorneys**.
- Contact placeholder: `contact@survivingthefeds.com` (swap when real one given).

## Roadmap / open items
- **8 free in-depth guides + a PACER guide** — each its own page AND feeding Start
  Here; all free. Topics families search (covered ✓ / planned): find someone ✓,
  money on books ✓, bail/detention hearing, charges & sentencing exposure,
  talking to / visiting an inmate, finding & judging a lawyer ✓ (lawyer page),
  reading a PACER docket, plea/cooperation & stages. Each links back to Start Here.
- **Finish the user's "interview"** (his locating/first-week notes were cut off) —
  build guides in his voice; do not invent legal specifics.
- **Tablet pass** (deferred until desktop is locked).
- **Warm hopeful image** for Start Here's "You are not alone" band (placeholder in place).
- **SEO**: "Busted by the Feds" is the $200 incumbent competitor — a fair comparison
  article + real "vs Busted" reviews + Book/FAQ structured data are the wedge (user
  said "not yet"). FAQ JSON-LD already on Start Here.
- Founder section still has one brand-voice pull-quote (not a book quote) — fine.

## Style of working with this user
He has real web instincts and strong taste — wants a custom, expensive, NON-template
feel; flag template-y reuse before it ships. He's on Android, deploys via GitHub
auto-deploy. Confirm genuine choices, but act on clear direction. Keep replies tight
(long sessions hit context limits).
