# SEO / AI-crawler baseline — survivingthefeds.com

Captured **2026-10-11** from the **live site**, fetching every URL in the live
`sitemap.xml` with `curl -A "Mozilla/5.0 (compatible; OAI-SearchBot/1.0)"` — i.e.
the raw HTML a crawler that does not run JavaScript receives. Word count = visible
text after removing `<script>`, `<style>`, `<noscript>`. JSON-LD types come from
parsing every `application/ld+json` block (all blocks parsed on every page).

## Before (live site, 2026-10-11)

| URL | HTTP | `<title>` | Meta description | Canonical | `<h1>` | Words | JSON-LD @types | OG / Twitter |
|---|---|---|---|---|---|---|---|---|
| `/` | 200 | Federal Sentencing Calculators & Survival Guides — Surviving the Feds | When the federal government comes for someone you love, know… | yes | It isn't easy. But you can survive this. | 835 | WebSite, Organization, Person | OG / summary_large_image |
| `/start-here.php` | 200 | Start Here — Surviving the Feds | You landed in the right place. This is where people in the f… | yes | **none** | 8220 | WebPage | OG / **no Twitter** |
| `/calculators.php` | 200 | Free Federal Sentencing Calculators \| Surviving the Feds | Free federal sentencing calculators: guideline range, FSA Fi… | yes | Federal Sentencing Calculators — Built for the people who need them. | 1218 | WebPage, FAQPage | OG / **no Twitter** |
| `/books.php` | 200 | Books — Surviving the Feds | The Surviving the Feds book series by Bilal Khan. Surviving … | **none** | **none** | 1871 | **none** | **no OG** / **no Twitter** |
| `/blog.php` | 200 | The Journal \| Surviving the Feds | Plain-language guides on federal criminal procedure, defense… | **none** | Loading… | 300 | **none** | **no OG** / **no Twitter** |
| `/glossary.php` | 200 | Federal Criminal Law Glossary — Plain Language \| Surviving the Feds | Plain-language definitions of the federal criminal law terms… | yes | The Federal System, Translated. | 2471 | DefinedTermSet | OG / **no Twitter** |
| `/about.php` | 200 | About Bilal Khan — Surviving the Feds | Bilal Khan navigated the federal system firsthand and taught… | **none** | Bilal Khan | 481 | **none** | **no OG** / **no Twitter** |
| `/is-my-lawyer-any-good.php` | 200 | Is My Lawyer Any Good? — Surviving the Feds | How to tell whether your federal defense attorney is actuall… | **none** | Is My Lawyer Any Good? | 592 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=how-to-use-pacer` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=the-first-step-act` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=your-rights-in-pretrial-detention` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=understanding-the-plea-deal` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=federal-sentencing-what-drives-the-numbers` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=the-first-48-hours` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=staying-connected-calls-mail-visits` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=is-my-lawyer-any-good` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |
| `/post.php?slug=what-is-a-2255-motion` | 200 | Article — Surviving the Feds | An article from the Surviving the Feds Journal.… | **none** | Loading… | 374 | **none** | **no OG** / **no Twitter** |

Every `post.php?slug=…` URL returned the same 374 words of chrome: title
"Article — Surviving the Feds", the generic description, `<h1>Loading…</h1>`, an
empty article body and no canonical. `blog.php` had `<h1>Loading…</h1>` and no
`<a href>` to any article. An unknown slug (`post.php?slug=nope-xyz`) returned **200**.

### Bot access (live, 2026-10-11, requests from this sandbox, not from the bots' own IP ranges)

| User agent | `/` | `/blog.php` | `/post.php?slug=how-to-use-pacer` |
|---|---|---|---|
| GPTBot/1.1 | **429** | **429** | **429** |
| OAI-SearchBot/1.0 | 200 | 200 | 200 |
| ChatGPT-User/1.0 | 200 | 200 | 200 |
| Claude-SearchBot/1.0 | 200 | 200 | 200 |
| ClaudeBot/1.0 | 200 | 200 | 200 |
| PerplexityBot/1.0 | 200 | 200 | 200 |
| Googlebot/2.1 | 200 | 200 | 200 |

Re-tested GPTBot at 18:56–18:58 UTC: `/` returned 429 five times out of five,
15 s apart (`server: hcdn`, no `Retry-After`); `/robots.txt` returned 429 once,
then 200 twice. The block comes from Hostinger's CDN edge, not from `robots.txt`
(which allows all). Because these requests came from a sandbox IP rather than
OpenAI's published GPTBot ranges, it can't be proven that real GPTBot is
blocked. The setting to check is in hPanel (CDN / bot protection); hosting
config was intentionally left untouched.

### Other live findings

- Hostinger rewrites every file's mtime on each deploy: all 9 `content/blog/*.md`
  report `Last-Modified: Sun, 09 Aug 2026 21:55:12 GMT` — the moment of the last
  deploy, even for files unchanged since 2026-08-07. `filemtime()` therefore
  cannot be used for `dateModified` or sitemap `lastmod`.
- The CDN re-encodes images (e.g. `assets/img/pacer/pacer_google_result.jpg`:
  341 KB in the repo, 223 KB served).
- Extension-less URLs (`/about`) return 200 with the same content as `/about.php`
  (no redirect) — canonical tags are what consolidate them.


## After (branch `claude/seo-server-render`, 2026-10-11)

Same crawler and user agent, run against `php -S localhost:8080` on the branch
(PHP's dev server ignores `.htaccess`, so `.php` URLs were hit directly; the
`.htaccess` rules — `/sitemap.xml` → `sitemap.php`, `_*.php` and `lib/` → 403 —
were checked separately under Apache 2.4 with the real `.htaccess`). Canonicals
point at `https://survivingthefeds.com/…`.

| URL | HTTP | `<title>` | Canonical | `<h1>` (first) | Words before → after | JSON-LD @types | Twitter card |
|---|---|---|---|---|---|---|---|
| `/` | 200 | Federal Sentencing Calculators & Survival Guides — Surviving the Feds | yes | It isn't easy. But you can survive this. | 835 → **1019** | WebSite, Organization, Person | summary_large_image |
| `/start-here.php` | 200 | Start Here — Surviving the Feds | yes | **none** | 8220 → **8220** | WebPage | **none** |
| `/calculators.php` | 200 | Free Federal Sentencing Calculators \| Surviving the Feds | yes | Federal Sentencing Calculators — Built for the people who need them. | 1218 → **1218** | WebSite, Organization, Person, WebPage, FAQPage | summary |
| `/books.php` | 200 | Books — Surviving the Feds | yes | **none** | 1871 → **1871** | BookSeries, Book, Book, BreadcrumbList, Person, Organization, WebSite | summary_large_image |
| `/blog.php` | 200 | The Journal \| Surviving the Feds | yes | Guides & Articles | 300 → **711** | CollectionPage, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/glossary.php` | 200 | Federal Criminal Law Glossary — Plain Language \| Surviving the Feds | yes | The Federal System, Translated. | 2471 → **2471** | DefinedTermSet | summary |
| `/about.php` | 200 | About Bilal Khan — Surviving the Feds | yes | Bilal Khan | 481 → **481** | ProfilePage, BreadcrumbList, Person, Organization, WebSite | summary_large_image |
| `/is-my-lawyer-any-good.php` | 200 | Is My Lawyer Any Good? — Surviving the Feds | yes | Is My Lawyer Any Good? | 592 → **592** | WebPage, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=how-to-use-pacer` | 200 | How to Use PACER to Follow Your Federal Case \| Surviving the Feds | yes | How to Use PACER to Follow Your Federal Case | 374 → **5794** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=the-first-step-act` | 200 | The First Step Act: What It Actually Gets You \| Surviving the Feds | yes | The First Step Act: What It Actually Gets You | 374 → **3869** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=your-rights-in-pretrial-detention` | 200 | Your Rights in Pretrial Federal Detention \| Surviving the Feds | yes | Your Rights in Pretrial Federal Detention | 374 → **4074** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=understanding-the-plea-deal` | 200 | Understanding the Plea Deal: What It Is, What It Costs, and When to Take It \| Surviving the Feds | yes | Understanding the Plea Deal: What It Is, What It Costs, and When to Take It | 374 → **1353** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=federal-sentencing-what-drives-the-numbers` | 200 | Federal Sentencing 101: What Drives the Numbers \| Surviving the Feds | yes | Federal Sentencing 101: What Drives the Numbers | 374 → **1427** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=the-first-48-hours` | 200 | The First 48 Hours After a Federal Arrest \| Surviving the Feds | yes | The First 48 Hours After a Federal Arrest | 374 → **976** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=staying-connected-calls-mail-visits` | 200 | Staying Connected: Calls, Mail, Email, and Visits in Federal Custody \| Surviving the Feds | yes | Staying Connected: Calls, Mail, Email, and Visits in Federal Custody | 374 → **1508** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=is-my-lawyer-any-good` | 200 | Is My Lawyer Actually Any Good? 7 Questions That Reveal the Truth \| Surviving the Feds | yes | Is My Lawyer Actually Any Good? 7 Questions That Reveal the Truth | 374 → **947** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |
| `/post.php?slug=what-is-a-2255-motion` | 200 | What Is a 2255 Motion — and Who Can File One? \| Surviving the Feds | yes | What Is a 2255 Motion — and Who Can File One? | 374 → **964** | Article, BreadcrumbList, WebSite, Organization, Person | summary_large_image |

Bad slugs (`nope-not-real`, `../posts`, `How-To-Use-Pacer`, empty, `a b`) → **404**
with `<meta name="robots" content="noindex, follow">` and no canonical (was 200).
"Loading…" occurrences in raw HTML: **0** on every page (was 1 on `blog.php` and
on every post). Every JSON-LD block parses; no placeholders.

### Summary

| Check | Before | After |
|---|---|---|
| Posts with a unique, article-specific `<title>` | 0 / 9 | 9 / 9 |
| Posts whose raw HTML contains the full article text | 0 / 9 | 9 / 9 (verbatim match against the old marked.js render) |
| Posts with `<h1>` = article title | 0 / 9 | 9 / 9 |
| Pages with a canonical tag | 4 / 17 | 17 / 17 |
| Pages with Twitter tags | 1 / 17 | 16 / 17 (Start Here untouched) |
| Crawlable `<a href>` links to posts on `blog.php` | 0 | 9 (+ 4 on the homepage) |
| Book structured data | none | BookSeries + 2 × Book (paperback + Kindle editions) |
| Sitemap | hand-maintained | generated; new CMS posts appear automatically |
| Unknown slug | 200 + "Loading…" | 404 + noindex |

Note: `start-here.php` is out of scope and unchanged — it has a canonical,
`og:title`/`og:description`/`og:image` and WebPage JSON-LD, but no `og:url`,
`og:type`, Twitter tags or `<h1>`.

### Rendering parity (Playwright, Chromium, 2026-10-11)

Live site vs branch, all 9 posts + `blog.php` + `blog.php?slug=the-first-48-hours`:

- **JS-rendered article text**: identical character counts on all 9 posts; same
  `document.title` and H1s; no console or page errors.
- **Full-page desktop screenshots (1440 px)**: 8 / 9 posts pixel-identical.
  `how-to-use-pacer` differs only inside its embedded screenshots, because the
  Hostinger CDN serves re-encoded JPEGs (341 KB in the repo, 223 KB live).
- **Print / Save-as-PDF (Letter)**: same page count for every page (e.g. PACER
  30 = 30, First Step Act 12 = 12), identical extracted text, and every
  rasterised page pixel-identical except PACER pp. 11, 16 and 21 (the same
  re-encoded images).
- **`blog.php`**: with excerpts hidden, the sidebar is pixel-identical to live at
  1440 px and 390 px. The only visible change is the new two-line excerpt under
  each title (required so the list carries title, excerpt and date).
- **Interaction**: a plain click opens the article in the reader (URL becomes
  `?slug=…`, item marked active); Ctrl/Cmd-click opens `post.php?slug=…` in a
  new tab; Back returns to the list; with JavaScript disabled, clicking follows
  the link to the server-rendered article.

Screenshots: `docs/seo-screenshots/` (left = live, right = branch).

