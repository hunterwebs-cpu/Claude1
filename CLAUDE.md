# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

**Surviving the Feds** — a static brand/content site for a federal criminal defense book publisher. No build step, no framework, no npm. Pure HTML/CSS/vanilla JS deployed to Hostinger (PHP available) or any static host.

Live site: `survivingthefeds.com`

## Local preview

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

The blog requires an HTTP server — opening `index.html` directly via `file://` will break post loading.

## Architecture

### No build pipeline

There is no bundler, transpiler, or package manager. Edit files directly; changes are live on reload. All JS is ES5-compatible vanilla.

### Page structure

Each `.html` file is self-contained with inline `<style>` for critical CSS and `<link>` to `assets/css/styles.css`. Pages share the same nav/footer markup copied across files — there is no templating engine.

### Blog system

- **Posts** are Markdown files in `content/blog/*.md` with YAML frontmatter (`title`, `date`, `category`, `excerpt`, `coverImage`).
- **On Hostinger (PHP):** `content/posts.php` auto-discovers all `.md` files in the directory — new posts appear automatically.
- **On non-PHP hosts:** `content/posts.json` is the fallback manifest; new posts must be added to it manually.
- `blog.js` fetches the post list and renders the journal index.
- `post.js` reads `?slug=` from the URL, fetches the corresponding `.md`, parses frontmatter, renders Markdown, and injects it into `post.html`.

### Theming

All design tokens live in the `:root` block at the top of `assets/css/styles.css`:

```css
--accent: #E63946;
--accent-deep: #9E1B26;
--gold: #E0B43B;
```

Changing these values reskins the entire site.

### CMS / publishing dashboard

`admin/` contains a [Decap CMS](https://decapcms.org/) setup:
- `admin/config.yml` — defines collections, fields, and the GitHub backend
- `admin/index.html` — loads the CMS UI
- Login requires a GitHub OAuth app + OAuth helper (see `DEPLOY.md §4`)

### JS files

| File | Responsibility |
|------|---------------|
| `assets/js/main.js` | Sticky nav, full-screen overlay menu, scroll-reveal (`[data-reveal]`), animated counters (`[data-count]`) |
| `assets/js/blog.js` | Fetches post list, renders journal index cards |
| `assets/js/post.js` | Fetches + renders individual posts from Markdown |

All JS honors `prefers-reduced-motion`.

## Skills available in this repo

Project-level skills are in `.claude/skills/` and load automatically in Claude Code on the web:

- **survivingwebsite** — primary skill for this project; use for all site work
- **article** — writing/editing Journal articles (`content/blog/*.md`)
- **frontend** — visual design and UI decisions
- **uxui** — UI/UX patterns, color palettes, typography
- **legal-research** — bankruptcy/federal legal research with PDF generation

## Deployment

See `DEPLOY.md` for full deployment instructions. Short version: zip the repo root and upload to `public_html` on Hostinger, or use Hostinger's Git deployment pointed at `main`.

`sitemap.xml` and `robots.txt` are static — update `sitemap.xml` manually when adding new pages.
