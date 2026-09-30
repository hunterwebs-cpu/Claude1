# Drafts (not published)

Files here are **not** on the site. `_content.php` only reads `content/blog/`, and this folder is
blocked from web access by `.htaccess`. Nothing here can go live by accident.

To publish a draft: Bilal reviews it, replaces every `[VERIFY...]` and the epigraph placeholder with
a checked quotation, removes the `draft: true` and the `<!-- DRAFT ... -->` header, then move the file
into `content/blog/`. It appears in the Journal and the sitemap automatically.

Per `docs/VOICE.md`: an unverified epigraph must never run, and the voice must be Bilal's. These drafts
use only facts checked against primary sources (cited in each endnote) and only personal details already
in `docs/VOICE.md` or his published book text. Anything else is marked for him.

## Status (2026-09-30)
The four full article drafts were withdrawn. They contained advice and wording that did not match the books,
and there is no way to check them against the books from here. They remain in git history (commit f6d62b0 and
the following commits) if anyone wants to look. What is kept: `verified-facts.md` (primary-source facts only)
and `tier1-briefs.md` (proposed topics and outlines, with the rule that lawyer guidance is Bilal's decision).
