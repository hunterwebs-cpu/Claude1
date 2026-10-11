# Surviving the Feds — Full Site Specification

Authoritative build/design reference for **survivingthefeds.com**. Subagents and
contributors should follow this exactly so every page stays consistent. For a fast
orientation use the project skill (`.claude/skills/surviving-the-feds/SKILL.md`);
this document is the deep reference.

> The site has **two distinct design systems**:
> 1. **Main brand** (dark, defiant) — `assets/css/styles.css`. Used by home, books,
>    about, blog, post, is-my-lawyer.
> 2. **Crisis sub-brand** (the "Emergency Room") — `assets/css/start.css`, a
>    self-contained system used ONLY by `start-here.php`. Different fonts, palette,
>    reset, and `--cr-*` tokens. **Never** mix the two. This spec documents the
>    MAIN brand; for Start Here, read `start.css` + `start-here.php` directly.

---

## 1. Tech & conventions

- **Hand-coded PHP pages** (shared `_head.php`/`_nav.php`/`_footer.php`/`_seo.php`
  includes) + CSS + vanilla JS. **No build step, no framework, no Composer.**
- **Everything a crawler needs is in the server HTML.** Titles, meta, canonical,
  OG/Twitter and JSON-LD are emitted in PHP via `_seo.php`; articles and the
  Journal list are rendered by PHP. JavaScript only enhances.
- **Hosting/deploy:** Hostinger, auto-deploys from GitHub `main`. Work on branch
  `claude/surviving-feds-site-5n4cmc`, then fast-forward `main` and push (goes live
  in ~1 min). Never force-push `main`; if it diverges (parallel sessions happen),
  rebase onto `origin/main`.
- **Cache busting:** HTML is `no-cache` via `.htaccess`; CSS/JS are long-cached.
  `styles.css`, `main.js` and `blog.js` use `?v=<?= filemtime(...) ?>` and bust
  themselves; for any ref still on a hand-set `?v=N`, **bump it** in the same change.
- **Local preview:** `php -S localhost:8080` from repo root. It ignores `.htaccess`,
  so open `.php` URLs directly (`/sitemap.php` rather than `/sitemap.xml`).
- **Images:** optimize before commit (Pillow). Hero/background JPGs ≤ ~1920px wide,
  progressive, q≈82–88. Use `loading="lazy"` on below-the-fold `<img>`.
- **Icons:** inline SVG only (stroke style, 24×24 viewBox, `stroke-width` 1.8–2).
  **No emoji as UI icons.**
- **Accessibility:** visible focus, `aria-label` on icon-only buttons, alt text on
  meaningful images, color contrast ≥ 4.5:1 for body text, honor
  `prefers-reduced-motion` (global rule already disables animations/reveals).

---

## 2. Design tokens (main brand — `:root` in styles.css)

| Token | Value | Use |
|-------|-------|-----|
| `--bg` | `#0A0B0E` | page background (near-black) |
| `--bg-2` | `#0E1014` | alt sections (`.section--alt`, `.promise`) |
| `--surface` | `#14171D` | cards |
| `--surface-2` | `#1B1F27` | elevated/hover cards, code |
| `--border` | `#262B34` | hairlines |
| `--border-2` | `#353C48` | stronger borders |
| `--text` | `#F3F4F6` | headings / primary |
| `--text-soft` | `#D3D7DD` | body copy (warm light grey) |
| `--muted` | `#9AA2AC` | secondary/labels |
| `--faint` | `#5B626D` | footnotes |
| `--accent` | `#E87722` | **brand orange** — CTAs, highlights |
| `--accent-deep` | `#B85A14` | darker orange |
| `--accent-glow` | `rgba(232,119,34,.42)` | button shadow/glow |
| `--gold` | `#C9D0D8` | **silver/steel** metallic accent (sparingly) |
| `--max` | `1240px` | container width |
| `--max-narrow` | `760px` | reading width |
| `--radius` / `--radius-sm` | `14px` / `8px` | corners |
| `--ease` / `--ease-out` | cubic-beziers | motion |
| z-index | `--z-nav:100`, `--z-overlay:200`, `--z-top:300` | layering scale |

**Brand palette = black + orange + silver** (from the logo). Changing `--accent`
re-skins the whole main site.

---

## 3. Typography

- **Display / headings:** `Fraunces` (serif). Weights 300–700; 300 used for the
  light "deck" intros. `--font-display`.
- **Labels / eyebrows / meta:** `Oswald` (condensed), uppercase, wide tracking.
  `--font-label`.
- **Body:** `Hanken Grotesk` (do **not** use Inter). `--font-body`. Base 17px,
  line-height 1.78, slight negative tracking, ligatures on.
- **Headings** `h1/h2/h3` are Fraunces 600, tight line-height, `letter-spacing:-.01em`.
  Sizes use `clamp()` (responsive).
- **`.lead`** = larger intro paragraph. **`.lead.deck`** = elegant light-Fraunces
  serif "deck" for page intros (use on the first intro paragraph of each page).
- Hero headline highlight: `.hl-feds` (dims) + `.hl-now` (orange gradient that
  paints in left-to-right via `now-reveal` ≈2.7s). Keep smooth, not typewriter.

---

## 4. Layout primitives

- `.container` (max 1240, 28px gutter) · `.container.narrow` (760) · `.center`.
- `.section` (vertical padding `clamp(58px,6vw,104px)`) · `.section--alt` (bg-2).
- `.grid` + `.grid-2` / `.grid-3` (responsive, collapse on narrow).
- `.split` — 2-col `1fr 1fr`, 64px gap, centered (founder/reassurance blocks).
- `.sec-head` — section header block (eyebrow + h2 + optional `.lead`).
  Modifier **`.sec-head.split-head`** → editorial 2-col (heading left / lead right)
  at ≥1000px; wrap heading in `.sh-head`. Prefer split-head to fill desktop width.

---

## 5. Component inventory (main brand)

**Buttons** — `.btn` base; `.btn--primary` (orange, white text, glow, magnetic
hover via main.js), `.btn--ghost` (outline → orange on hover), `.btn--gold`
(silver). Include a trailing arrow SVG; it slides on hover.

**Header / nav** — `.site-header` (fixed; `.scrolled` adds blur + shrinks logo).
`.nav` › `.brand` (logo `img`, 64px → 52px scrolled) · `.nav-links` (`.nav-link`,
underline-on-hover, `aria-current="page"` for active) · `.nav-cta` (primary button
+ `.nav-toggle` hamburger). Full-screen overlay menu `.nav-overlay#mega-menu`
(`.overlay-menu` numbered links `01–05` via `.idx`, `.overlay-aside` with tagline +
contact). main.js toggles `body.menu-open`.

**Hero (photo)** — `.hero.hero--photo` › `.hero-photo` (bg image) + `.hero-scrim`
(layered gradient + orange glow) + `.container` › `.hero-content` (`.equation`
chip, `h1`, `.lead`, `.hero-actions`, `.hero-trust`). `.scroll-cue` bottom.
min-height 86svh.

**Interior page hero** — `.page-hero` › `.ph-bg` + `.ph-scrim` + container
(`.eyebrow`, `h1`, `.ph-sub`). Used by books/about/is-my-lawyer.

**Marquee** — `.marquee` › `.marquee-track` of `.marquee-item` (duplicate the set
for a seamless loop; pauses on hover).

**Promise strip** — `.promise` › `.promise-grid` (4-up) of `.promise-item`
(SVG + strong + span).

**Cards** — `.card` (+ `.card--feature` top-accent on hover). Inner: `.card-num`,
`.icon-wrap` (svg), `h3`, `p`. Lay out in `.grid.grid-3` / `.grid-2`.

**Stats** — `.stats` (3-up) › `.stat` (`.num` with `data-count` for animated
counters, `.label`). (Defined; optional.)

**Founder** — `.split` › `.founder-card` (`.founder-portrait` img or `.initials`,
`.founder-plate`) + `.founder-bio` (p's + `.pull-quote`). Keep founder understated.

**Books** — `.book` (cover-shell + `.book-meta`); on Books page use real cover
`<img class="book-photo">` (3D tilt). `.book-meta`: `.vol`, h3, `.subtitle`,
`p`, `.formats` (`.format-pill`), `.book-actions` (buttons). Per-book real review:
`.book-quote` (`.stars` + p + `.bq-cite`). Home teaser covers use `.cover-img`.

**Reviews** — `.reviews-grid` (3-up) › `.review` (`.stars` ★, blockquote, `cite`
+ `.src`). Use **real Amazon reviews only**.

**Quote band** — `.quote-band` › `.qb-photo` + `.qb-scrim` + blockquote + `.qb-cite`
(cinematic full-width pull quote over a photo).

**CTA band** — `.cta-band` (gradient) or `.cta-band--photo` (`.cta-photo` +
`.cta-scrim`). Centered eyebrow + h2 + lead + button.

**Callout** — `.callout` (left-accent info box, svg + p).

**Footer** — `.site-footer` › `.footer-grid` (brand + 3 cols) + `.footer-bottom`
(© with `#year` auto-filled by main.js, + disclaimer). Keep nav/footer identical
across all main-brand pages.

**Article / blog** — `.article` › `.article-header` (h1, `.article-meta`),
`.article-tools` (print buttons), `.prose` (rendered markdown). `.post-grid` /
`.post-card` for listings. Print: `.print-only` + `@media print` produces a clean
mailable PDF (logo top-left, book CTA + Amazon ASINs, running tagline footer).

**Scroll reveal** — add `data-reveal` (and optional `data-delay="1..4"`) to any
element; main.js fades/translates it in on scroll (IntersectionObserver).

---

## 6. Pages & section order

All main-brand pages share the **same header, overlay menu, and footer** (5 nav
items: Home · Start Here · The Books · The Journal · About; set `aria-current` on
the active one; overlay idx 01–05).

- **`index.php`** (home): photo hero → marquee → promise strip → mission (split
  header + 3 feature cards) → books teaser (2 covers) → reviews (3) → quote band →
  founder teaser (subtle, links to About) → "what's coming" services (3 soon cards)
  → journal teaser (`#home-posts`, latest 3) → photo CTA band.
- **`books.php`**: page hero → Book 1 (`.book-section` w/ faint bg photo) → divider
  → Book 2 → disclaimer callout → series CTA.
- **`about.php`**: page hero → story split (headshot) → teaching credential
  (split header + 3 cards) → testimonial quote band → mission CTA.
- **`is-my-lawyer-any-good.php`**: page hero → intro `.lead.deck` + book callout →
  podcast card → 6-point checklist → CTA. (Checklist drawn from the book.)
- **`blog.php`**: sidebar list (`#post-list`, server-rendered `<a>` links) + JS reader pane.
- **`post.php`**: server-renders the `?slug=` article into `.prose`; print/PDF toolbar.
- **`start-here.php`**: CRISIS SUB-BRAND — separate system (see top note).

---

## 7. Blog / free-guides system

- Posts/guides = Markdown files in `content/blog/<slug>.md` with YAML frontmatter:
  `title`, `date` (YYYY-MM-DD), `category`, `author`, `excerpt`, optional `cover`,
  then the body.
- Rendering: `_posts.php` parses frontmatter, lists posts and renders Markdown
  with vendored `lib/Parsedown.php`; `post.php`, `blog.php`, the homepage cards and
  `sitemap.php` all use it. Optional frontmatter: `seoTitle` (the `<title>` when
  the display title doesn't fit `[Keyword]: [Hook]`) and `updated` (YYYY-MM-DD,
  drives `dateModified` and sitemap `lastmod`).
- `content/posts.php` returns the same list as JSON for `blog.js`;
  `content/posts.json` is the static fallback array of slugs.
- Decap CMS at `/admin` (GitHub backend; OAuth setup in `DEPLOY.md`).
- **Planned:** 8 free in-depth guides + a PACER guide, each its own page/article and
  cross-linked from Start Here. All free.

---

## 8. Content & voice (non-negotiable)

- **Author:** Bilal Khan. **Brand line:** *Knowledge + Strength = Freedom.*
- **Never fabricate quotes from the books.** Only use supplied/approved book text.
  Don't attribute marketing copy to the book; attribute brand lines to "Surviving
  the Feds."
- **Not legal advice.** Keep the disclaimer; phrase rights/procedure generally.
- Voice: plain, direct, lived-experience, defiant-but-caring. No jargon, no false
  hope. Custom feel — avoid template-y repetition; flag it before shipping.
- **Book facts:** Surviving Pretrial — paperback `B0BT19Y3V8`, Kindle `B0BTCDLWN8`.
  The 2255 Motion Handbook — paperback `B0D8HQRJN8`, Kindle `B0D9FXJHZZ`. Series
  `B0D471H5Z9`. Podcast: Set for Sentencing, "Is My Lawyer Any Good?". The feds'
  playbook = the **Manual for United States Attorneys**.

---

## 9. Responsive

Mobile-first review at 375 / 768 / 1024 / 1440. Key main-brand breakpoints:
≤1000px (split-head stacks), ≤980px (grids → 2-col, splits stack, overlay 1-col),
≤760px (nav → hamburger, grids → 1-col, hero padding). Never allow horizontal
scroll. The user reviews primarily on Android — test narrow widths.

---

## 10. Definition of done (per change)

1. Matches tokens/components above (or extends them deliberately, documented here).
2. Responsive at the four widths; no horizontal scroll; reduced-motion safe.
3. Real SVG icons; real content (no fabricated quotes); disclaimer where relevant.
4. `?v=` bumped if CSS/JS changed.
5. Committed on the dev branch, fast-forwarded to `main`, pushed (auto-deploys).
6. Spot-check live (hard refresh / incognito).
