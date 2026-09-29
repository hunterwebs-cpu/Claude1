# Surviving the Feds

The official brand site for **Surviving the Feds** — *Knowledge + Strength = Freedom.*

A fast, responsive, static website with a built-in publishing dashboard for the
blog. Dark, bold, defiant theme. No build step required.

## Structure

```
index.html          Home (mission, books teaser, founder, journal teaser)
books.html          The Books — Surviving Pretrial + The 2255 Motion Handbook
blog.php            The Journal: /journal (index) and /journal/<slug> (article), server-rendered
post.php            Legacy URL: 301s to /journal/<slug>
_content.php        Journal helpers (frontmatter, Markdown -> HTML, SEO helpers)
sitemap.php         Generates /sitemap.xml from content/blog
admin/              Decap CMS publishing dashboard (/admin)
content/blog/*.md   Blog posts (Markdown + frontmatter)
content/posts.php   Legacy JSON post index (no longer used by the site)
assets/css/         styles.css — all theming via CSS variables
assets/js/          main.js (UI + outbound book-click tracking), blog.js (in-page article swap)
assets/img/         logo.svg, emblem.svg (swap with official artwork)
```

## Quick start (local preview)

```bash
# from the project root
python3 -m http.server 8080
# then open http://localhost:8080
```
The blog loads posts over HTTP, so preview via a local server (not by opening
the file directly).

## Going live & publishing

See **[DEPLOY.md](DEPLOY.md)** — full plain-English guide for Hostinger,
swapping the logo/colors, and using the publishing dashboard.

## Customize

- **Accent color / theme:** edit the `:root` variables at the top of
  `assets/css/styles.css`.
- **Logo:** replace `assets/img/logo.svg` and `assets/img/emblem.svg`.
- **Contact email:** find-and-replace `contact@survivingthefeds.com`.

---
*Informational only — not legal advice.*
