<?php
/* ============================================================================
   SURVIVING THE FEDS — Journal content helpers (server-side)

   Reads content/blog/*.md, parses the YAML-ish frontmatter, and renders the
   Markdown body to HTML ON THE SERVER, so the title, description, canonical,
   schema and full article text are in the raw HTML that Google and AI crawlers
   (most of which do not run JavaScript) actually receive.

   Underscore-prefixed files are blocked from direct web access by .htaccess.
   Written for PHP 7.4+ (Hostinger).
   ========================================================================== */

/* mbstring is on virtually every host, but a missing extension must not take the
   Journal down: fall back to byte-safe equivalents. */
if (!function_exists('mb_strlen'))   { function mb_strlen($s)                 { return strlen($s); } }
if (!function_exists('mb_substr'))   { function mb_substr($s, $a, $l = null)  { return $l === null ? substr($s, $a) : substr($s, $a, $l); } }
if (!function_exists('mb_strrpos'))  { function mb_strrpos($h, $n)            { return strrpos($h, $n); } }

if (!defined('STF_SITE')) define('STF_SITE', 'https://survivingthefeds.com');
if (!defined('STF_CONTENT_DIR')) define('STF_CONTENT_DIR', __DIR__ . '/content/blog');

/* Slugs are lowercase words joined by hyphens. Anything else is rejected before
   it can touch the filesystem. */
function stf_valid_slug($slug): bool {
    return is_string($slug) && preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/', $slug) === 1;
}

/* Split a raw .md file into frontmatter (array) and body (string). */
function stf_parse_post(string $raw, string $slug): array {
    $meta = array('slug' => $slug);
    $body = $raw;
    $raw  = preg_replace('/^\xEF\xBB\xBF/', '', $raw);   // strip a UTF-8 BOM
    if (preg_match('/^---\s*\n(.*?)\n---\s*\n?(.*)$/s', $raw, $m)) {
        $body = $m[2];
        foreach (explode("\n", $m[1]) as $line) {
            $i = strpos($line, ':');
            if ($i === false) continue;
            $k = trim(substr($line, 0, $i));
            $v = trim(trim(substr($line, $i + 1)), "\"'");
            if ($k !== '') $meta[$k] = $v;
        }
    }
    $meta['slug'] = $slug;   // the filename is the source of truth, not the frontmatter
    $meta['body'] = $body;
    return $meta;
}

/* One article by slug, or null if it doesn't exist. */
function stf_post($slug): ?array {
    if (!stf_valid_slug($slug)) return null;
    $file = STF_CONTENT_DIR . '/' . $slug . '.md';
    if (!is_file($file)) return null;
    $raw = file_get_contents($file);
    if ($raw === false) return null;
    return stf_parse_post($raw, $slug);
}

/* Every article (frontmatter + body), newest first. Cached per request. */
function stf_posts(): array {
    static $cache = null;
    if ($cache !== null) return $cache;
    $cache = array();
    foreach (glob(STF_CONTENT_DIR . '/*.md') ?: array() as $file) {
        $slug = basename($file, '.md');
        if (!stf_valid_slug($slug)) continue;
        $raw = file_get_contents($file);
        if ($raw === false) continue;
        $cache[] = stf_parse_post($raw, $slug);
    }
    usort($cache, function ($a, $b) {
        return strcmp($b['date'] ?? '', $a['date'] ?? '');
    });
    return $cache;
}

/* Port of the old client-side stripMarkers(): removes print/layout markers and
   unresolved [VERIFY] editor notes so they never reach the public page. */
function stf_strip_markers(string $md): string {
    $rules = array(
        '/^\[LOGO:[^\]]*\]\s*$/m',
        '/^\[ORANGE RULE LINE[^\]]*\]\s*$/m',
        '/^\[HEADSHOT:[^\]]*\]\s*$/m',
        '/^\[SIGNATURE IMAGE[^\]]*\]\s*$/m',
        '/^\[TWO-BOOK FOOTER[^\]]*\]\s*$/m',
        '/^\[PRINT:[^\]]*\]\s*$/m',
        '/^>?\s*\[VERIFY:[^\]]*\]\s*$/m',
        '/^\[\^\d+\]:\s*\[VERIFY[^\]]*\]\s*$/m',
        '/\[VERIFY:[^\]]*\]/',
        '/\[VERIFY\]/',
        '/\[LOGO:[^\]]*\]/',
        '/\[ORANGE RULE LINE[^\]]*\]/',
        '/\[HEADSHOT:[^\]]*\]/',
        '/\[SIGNATURE IMAGE[^\]]*\]/',
        '/\[TWO-BOOK FOOTER\]/',
        '/^\[[^\]]*\.(png|jpg|jpeg|webp|gif)\]\s*$/im',
    );
    $md = preg_replace($rules, '', $md);
    return preg_replace("/\n{4,}/", "\n\n\n", $md);
}

/* Markdown -> HTML. Footnotes, tables and raw HTML are supported (the author's
   content is trusted: it comes from the repo, not from visitors). */
function stf_render_markdown(string $md): string {
    static $parser = null;
    if ($parser === null) {
        // Vendored Parsedown 1.7.x predates PHP 8.4 and emits E_DEPRECATED notices;
        // they are harmless, so keep them out of the page.
        $old = error_reporting(error_reporting() & ~E_DEPRECATED);
        require_once __DIR__ . '/_lib/Parsedown.php';
        require_once __DIR__ . '/_lib/ParsedownExtra.php';
        $parser = new ParsedownExtra();
        $parser->setSafeMode(false);
        error_reporting($old);
    }
    $old  = error_reporting(error_reporting() & ~E_DEPRECATED);
    $html = $parser->text(stf_strip_markers($md));
    error_reporting($old);

    // Articles are served from /journal/<slug>, so relative asset and page links
    // written for the site root must become root-relative.
    $html = preg_replace('/(src|href)="(assets|content)\//', '$1="/$2/', $html);
    $html = preg_replace('/href="([a-z0-9-]+\.php)/', 'href="/$1', $html);
    // Lazy-load images inside articles.
    $html = preg_replace('/<img(?![^>]*\bloading=)/', '<img loading="lazy" decoding="async"', $html);
    return $html;
}

function stf_h($s): string {
    return htmlspecialchars((string)$s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function stf_url(string $slug): string {
    return '/journal/' . rawurlencode($slug);
}

function stf_abs(string $path): string {
    return STF_SITE . $path;
}

function stf_fmt_date(?string $iso): string {
    if (!$iso) return '';
    $t = strtotime($iso . ' 00:00:00 UTC');
    return $t ? gmdate('F j, Y', $t) : $iso;
}

/* Title used in <title>. Uses seo_title when set (the plain-language,
   keyword-first version), otherwise the article title. */
function stf_seo_title(array $post): string {
    $t = trim($post['seo_title'] ?? '') !== '' ? $post['seo_title'] : ($post['title'] ?? 'Article');
    return $t . ' | Surviving the Feds';
}

/* Meta description: an explicit `description` wins; else the excerpt, cut on a
   word boundary so it is not truncated mid-sentence by the search engine. */
function stf_meta_description(array $post): string {
    $d = trim($post['description'] ?? '');
    if ($d === '') $d = trim($post['excerpt'] ?? '');
    if (mb_strlen($d) <= 160) return $d;
    $cut = mb_substr($d, 0, 157);
    $sp  = mb_strrpos($cut, ' ');
    if ($sp !== false && $sp > 100) $cut = mb_substr($cut, 0, $sp);
    return rtrim($cut, " ,;:.—-") . '…';
}

/* Absolute URL for the article's social/schema image. */
function stf_image_url(array $post): string {
    $img = trim($post['cover'] ?? '');
    if ($img === '') return stf_abs('/assets/img/og-home.jpg');
    if (preg_match('#^https?://#', $img)) return $img;
    return stf_abs('/' . ltrim($img, '/'));
}

/* Rough reading time for the byline (words / 220 wpm, minimum 1). */
function stf_read_minutes(string $md): int {
    $words = str_word_count(strip_tags(stf_strip_markers($md)));
    return max(1, (int)round($words / 220));
}
