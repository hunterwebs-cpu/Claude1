# Surviving the Feds — Go-Live & Owner's Guide

This is the plain-English guide to launching the site, changing it, and
publishing blog posts. No coding required for day-to-day use.

---

## 1. What this site is

A fast, static website (plain HTML/CSS/JavaScript) — meaning it loads quickly,
costs almost nothing to host, and works on any host including **Hostinger**.

| Page | File | What it is |
|------|------|------------|
| Home | `index.html` | Brand, mission, books teaser, founder, journal teaser |
| The Books | `books.html` | Showcase of both books with Amazon links |
| The Journal | `blog.html` | Lists all articles |
| Article | `post.html` | Displays a single article |
| Dashboard | `admin/` | Where you log in to write posts |
| Articles | `content/blog/*.md` | The actual blog posts |
| Styling | `assets/css/styles.css` | All the colors, fonts, layout |
| Behavior | `assets/js/*.js` | Menus, animations, blog loading |

---

## 2. Put it live on Hostinger

**Option A — File Manager (simplest):**
1. Log in to Hostinger → **hPanel** → **File Manager**.
2. Open the `public_html` folder (this is your website's root).
3. Upload **everything in this project** into `public_html` (keep the folder
   structure: `assets/`, `content/`, `admin/`, and all the `.html` files).
   The easiest way is to upload a ZIP of the project and "Extract" it inside
   `public_html`.
4. Visit your domain — the site is live.

**Option B — Git deployment (keeps the site in sync with GitHub):**
Hostinger supports deploying straight from a GitHub repo on most plans
(hPanel → **Website** → **GIT**). Point it at this repository and the branch
your live site should track (e.g. `main`). After that, anything published
through the dashboard auto-deploys. Hostinger's docs walk through the exact
screens.

**Point the domain:** In hPanel, make sure `survivingthefeds.com` is attached
to this hosting plan (Domains → add/point). If the domain is registered
elsewhere, set its nameservers to Hostinger's (shown in hPanel).

> Tip: enable the free SSL certificate in hPanel so the site loads on
> `https://`.

---

## 3. Make it yours (quick edits)

**Swap in the real logo:** Replace `assets/img/logo.svg` (and
`assets/img/emblem.svg` for the favicon) with your official artwork. Keep the
same filenames and the whole site updates automatically. SVG or PNG both work
— if PNG, just point the `<img>` tags to the new filename.

**Change the accent color to match the logo:** Open
`assets/css/styles.css`, find the `:root` block near the top, and edit:
```css
--accent:      #E63946;  /* main brand color (buttons, highlights) */
--accent-deep: #9E1B26;
--gold:        #E0B43B;  /* premium gold used sparingly */
```
Change those hex values and the entire site re-skins. That's the only place
you need to touch.

**Update the contact email:** The site uses a placeholder
`contact@survivingthefeds.com`. Find-and-replace it across the `.html` files
with your real address (it appears in the menu, footer, and overlay).

---

## 4. Publish blog posts (the dashboard)

The dashboard lives at **`https://survivingthefeds.com/admin/`**. You log in
with GitHub, write in a clean editor, and hit **Publish**. Each post is saved
as a file in `content/blog/` and appears on the site automatically.

### One-time setup: connect the login

Because the site isn't hosted on Netlify, the dashboard needs a small, free
"login helper" (an OAuth app) so GitHub can authorize you. You set this up
**once**:

1. **Create a GitHub OAuth App.** GitHub → Settings → Developer settings →
   **OAuth Apps** → *New OAuth App*. Set the callback URL to your login
   helper's address (from the next step). Note the **Client ID** and
   **Client Secret**.
2. **Deploy a free OAuth helper.** The community provides ready-made ones you
   deploy in a couple of clicks on **Cloudflare Workers**, **Vercel**, or
   **Netlify** (search "Decap CMS GitHub OAuth provider"). You paste in the
   Client ID and Secret from step 1. You'll get a URL like
   `https://stf-oauth.yourname.workers.dev`.
3. **Tell the dashboard about it.** Open `admin/config.yml`, find the
   commented `base_url` line under `backend:`, uncomment it, and set it to your
   helper's URL. Re-upload `config.yml`.

After that, going to `/admin/` → "Login with GitHub" just works, for you and
anyone you grant repo access.

> If you'd rather skip OAuth entirely, you can host **just this site** on
> Netlify's free tier (point your Hostinger domain at it). Then the dashboard
> login is one click with no helper needed. Both approaches are fine — this is
> purely about where the site files live.

### Writing a post

1. Go to `/admin/`, log in.
2. Click **Journal Articles → New Article**.
3. Fill in Title, Date, Category, Excerpt, optional Cover Image, and the Body.
4. Hit **Publish**. Done — it shows up on the Journal page.

### Adding a post by hand (no dashboard)

You can also just drop a Markdown file into `content/blog/`. Copy an existing
one (e.g. `the-first-48-hours.md`), rename it (the filename becomes the URL
slug), and edit the top section + text. On Hostinger (which runs PHP) it
appears automatically. On hosts without PHP, also add the new filename
(without `.md`) to `content/posts.json`.

---

## 5. How the blog finds posts (for reference)

- On Hostinger, `content/posts.php` lists the articles automatically, so new
  posts show up with zero extra steps.
- If PHP isn't available, the site falls back to the static list in
  `content/posts.json`.
- You normally never touch either of these — the dashboard and PHP handle it.

---

## 6. Good to know

- **Not legal advice:** every page carries the disclaimer; keep it.
- **Performance & accessibility:** the site respects reduced-motion settings,
  uses real SVG icons (no emojis), and is responsive from phone to desktop.
- **SEO:** `robots.txt` and `sitemap.xml` are included — update the URLs in
  `sitemap.xml` if you add pages.
- **Lead capture:** intentionally none yet (per your call). When you're ready,
  a contact form or newsletter signup can be added cleanly.
