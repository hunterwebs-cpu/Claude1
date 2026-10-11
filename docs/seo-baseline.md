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

