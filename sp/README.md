# Surviving Pretrial — sp.survivingthefeds.com

The sales/landing site for **Surviving Pretrial** by Bilal Khan (Surviving the Feds, Vol. 1).
Hand-coded static HTML/CSS/JS, no build step. This folder is designed to become the root of
its **own GitHub repo**, connected to the `sp` subdomain on Hostinger.

## Pages
- `index.html` — the landing page (hero, road-ahead timeline, all 5 real Amazon reviews,
  Kindle Instant Preview embed, author, vs-Busted comparison, FAQ, CTAs).
- `first-72-hours.html` — free family crisis guide (the SEO ranking page for arrest queries).
- `busted-by-the-feds.html` — honest comparison vs. the jailhouse classic (purchase-intent capture).

## Deploying (Hostinger + GitHub, one time)
1. **Create the repo**: new GitHub repo (e.g. `surviving-pretrial-site`), push the contents
   of this folder to its root on branch `main`.
2. **Create the subdomain** in hPanel: Websites → Dashboard → Subdomains → add `sp`.
   DNS is automatic (Hostinger nameservers); free SSL auto-installs — verify it, then enable
   **Force HTTPS**.
3. **Connect the repo**: subdomain's dashboard → Advanced → Git → "Continue with GitHub",
   authorize the Hostinger GitHub App for the new repo, branch `main`.
   ⚠️ **Set the deploy directory to the sp subdomain's document root** — the field defaults
   to the main site's `public_html`. The two sites' directories must not overlap.
4. Every push to `main` now auto-deploys.

## After first deploy (SEO checklist)
- [ ] Google Search Console: if survivingthefeds.com is a **Domain property**, sp. is already
      covered — submit `https://sp.survivingthefeds.com/sitemap.xml` there. Otherwise add sp.
      as its own property.
- [ ] Bing Webmaster Tools: import from GSC, submit the sitemap. (Bing's index feeds ChatGPT.)
- [ ] IndexNow: generate a key at bing.com/indexnow, commit the `{key}.txt` file to this repo
      root, then ping `https://api.indexnow.org/indexnow?url=https://sp.survivingthefeds.com/&key={key}`
      after each deploy.
- [ ] Main site: add followed links to sp. from books.html, Start Here, and the Journal
      (varied anchors: "Surviving Pretrial", "read the first pages free", "the first 72 hours guide").
- [ ] Analytics (optional): GoatCounter (free) or Plausible — add their snippet before
      `</body>` on all three pages. `sp.js` already fires per-button `data-cta` events to
      either one automatically. Avoid GA4 (heavy).
- [ ] Verify rich results: search.google.com/test/rich-results on all three URLs.

## Conventions
- Cache busting: bump `?v=N` on `sp.css` / `sp.js` references in **all three HTML files**
  whenever CSS/JS change (HTML itself is no-cache via `.htaccess`).
- All Amazon links: `target="_blank" rel="sponsored noopener"` + a `data-cta` label.
  If you join Amazon Associates, append your tag to every Amazon URL for commission + tracking.
- Fonts are self-hosted in `assets/fonts/` (Fraunces, Hanken Grotesk, IBM Plex Mono).
- **Never fabricate quotes from the book or reviews.** Review text on these pages is verbatim
  from the live Amazon listing (captured 2026-07-03).
- The on-page book excerpt (planned) must stay under 10% of the book (~54 pages) to comply
  with KDP Select exclusivity. The embedded Kindle preview is Amazon-served and always safe.

## Amazon facts (as of 2026-07-03)
- Kindle `B0BTCDLWN8`: $24.99, free on Kindle Unlimited, 541 pp, pub 2023-01-29.
- Paperback `B0BT19Y3V8`: ⚠️ buy box showed $74.95 / "from $45.43" — verify the KDP listing
  is in stock at your intended list price (reseller buy-box risk).
- Rating: 5.0★, 9 ratings, 5 written reviews (all quoted on the site).
- Add-to-cart URL (paperback only; digital items can't be carted):
  `https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B0BT19Y3V8&Quantity.1=1`
