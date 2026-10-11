<?php
/* ============================================================================
   SURVIVING THE FEDS — Journal post helpers (shared)
   Used by post.php (single article), blog.php (article list),
   content/posts.php (JSON index for blog.js) and sitemap.php.

   Posts are Markdown files in content/blog/<slug>.md with YAML-style
   frontmatter (title, date, category, author, excerpt, cover, optional
   seoTitle / updated). Decap CMS writes them; nothing here needs a manifest.
   ========================================================================== */

if (!defined('STF_POSTS_DIR')) define('STF_POSTS_DIR', __DIR__ . '/content/blog');

/** Strip YAML-style quotes from a scalar value. */
function stf_unquote($v)
{
    $v = trim($v);
    $n = strlen($v);
    if ($n >= 2 && $v[0] === '"' && $v[$n - 1] === '"') {
        return stripcslashes(substr($v, 1, -1));               // "…\"…"
    }
    if ($n >= 2 && $v[0] === "'" && $v[$n - 1] === "'") {
        return str_replace("''", "'", substr($v, 1, -1));     // '…''…'
    }
    return $v;
}

/**
 * Split a post into [meta, body]. Handles `key: value` (quoted or bare) and the
 * folded / literal block scalars (`>-`, `|`) that Decap emits for long text.
 */
function stf_parse_frontmatter($raw)
{
    $raw  = str_replace("\r\n", "\n", $raw);
    $meta = array();
    $body = $raw;
    if (!preg_match('/^---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)(.*)$/s', $raw, $m)) {
        return array($meta, $body);
    }
    $body  = $m[2];
    $lines = explode("\n", $m[1]);
    for ($i = 0, $n = count($lines); $i < $n; $i++) {
        if (!preg_match('/^([A-Za-z0-9_-]+)\s*:\s*(.*)$/', $lines[$i], $kv)) continue;
        $key = $kv[1];
        $val = trim($kv[2]);
        if (preg_match('/^([>|])[+-]?$/', $val, $blk)) {
            $parts = array();
            while ($i + 1 < $n && ($lines[$i + 1] === '' || preg_match('/^\s/', $lines[$i + 1]))) {
                $parts[] = trim($lines[++$i]);
            }
            $val = $blk[1] === '>' ? trim(preg_replace('/\s+/', ' ', implode(' ', $parts)))
                                   : rtrim(implode("\n", $parts));
        } else {
            $val = stf_unquote($val);
        }
        $meta[$key] = $val;
    }
    return array($meta, $body);
}

/** Slugs are lowercase letters, digits and hyphens only. */
function stf_valid_slug($slug)
{
    return is_string($slug) && preg_match('/^[a-z0-9-]+$/', $slug) === 1;
}

/** A YYYY-MM-DD date string, or '' if the value isn't one. */
function stf_iso_date($v)
{
    return (is_string($v) && preg_match('/^\d{4}-\d{2}-\d{2}/', $v, $m)) ? $m[0] : '';
}

/** Load one post (meta + body + slug), or null if the slug is invalid / missing. */
function stf_load_post($slug)
{
    if (!stf_valid_slug($slug)) return null;
    $file = STF_POSTS_DIR . '/' . $slug . '.md';
    if (!is_file($file)) return null;
    list($meta, $body) = stf_parse_frontmatter((string) file_get_contents($file));
    $meta['slug'] = $slug;
    $meta['body'] = $body;
    return $meta;
}

/** Every post's frontmatter (no body), newest first. */
function stf_list_posts()
{
    $posts = array();
    foreach (glob(STF_POSTS_DIR . '/*.md') ?: array() as $file) {
        $slug = basename($file, '.md');
        if (!stf_valid_slug($slug)) continue;
        list($meta) = stf_parse_frontmatter((string) file_get_contents($file));
        $meta['slug'] = $slug;            // the filename is the real slug
        $posts[] = $meta;
    }
    usort($posts, function ($a, $b) {
        $c = strcmp(isset($b['date']) ? $b['date'] : '', isset($a['date']) ? $a['date'] : '');
        return $c !== 0 ? $c : strcmp($a['slug'], $b['slug']);
    });
    return $posts;
}

/** Published date and last-modified date (frontmatter `updated`, else `date`). */
function stf_post_dates(array $p)
{
    $pub = stf_iso_date(isset($p['date']) ? $p['date'] : '');
    $mod = stf_iso_date(isset($p['updated']) ? $p['updated'] : '');
    if ($mod === '' || $mod < $pub) $mod = $pub;
    return array($pub, $mod);
}

/** "June 20, 2026" — same format blog.js / post.js used. */
function stf_fmt_date($iso)
{
    $d = stf_iso_date($iso);
    if ($d === '') return (string) $iso;
    $t = DateTime::createFromFormat('!Y-m-d', $d);
    return $t ? $t->format('F j, Y') : $d;
}

/** <title> text: `seoTitle` if set (format "[Keyword]: [Hook]"), else the title. */
function stf_post_title_tag(array $p)
{
    $t = !empty($p['seoTitle']) ? $p['seoTitle'] : (isset($p['title']) ? $p['title'] : 'Article');
    return $t . ' | Surviving the Feds';
}

function stf_post_path($slug)
{
    return 'post.php?slug=' . rawurlencode($slug);
}

/**
 * Remove print/layout markers and unresolved editor notes before rendering.
 * A straight port of stripMarkers() from the old post.js / blog.js.
 */
function stf_strip_markers($md)
{
    $rules = array(
        '/^\[LOGO:[^\]]*\]\s*$/m'              => '',
        '/^\[ORANGE RULE LINE[^\]]*\]\s*$/m'   => '',
        '/^\[HEADSHOT:[^\]]*\]\s*$/m'          => '',
        '/^\[SIGNATURE IMAGE[^\]]*\]\s*$/m'    => '',
        '/^\[TWO-BOOK FOOTER[^\]]*\]\s*$/m'    => '',
        '/^\[PRINT:[^\]]*\]\s*$/m'             => '',
        '/^>?\s*\[VERIFY:[^\]]*\]\s*$/m'       => '',
        '/^\[\^\d+\]:\s*\[VERIFY[^\]]*\]\s*$/m' => '',
        '/\[VERIFY:[^\]]*\]/'                  => '',
        '/\[VERIFY\]/'                         => '',
        '/\[LOGO:[^\]]*\]/'                    => '',
        '/\[ORANGE RULE LINE[^\]]*\]/'         => '',
        '/\[HEADSHOT:[^\]]*\]/'                => '',
        '/\[SIGNATURE IMAGE[^\]]*\]/'          => '',
        '/\[TWO-BOOK FOOTER\]/'                => '',
        '/^\[[^\]]*\.(png|jpg|jpeg|webp|gif)\]\s*$/im' => '',
        '/\n{4,}/'                             => "\n\n\n",
    );
    $md = preg_replace(array_keys($rules), array_values($rules), $md);

    // A footnote whose definition was removed above (it was only a [VERIFY]
    // note) must not leave a dangling [^n] reference in the text.
    preg_match_all('/^\[\^([^\]\s]+)\]:/m', $md, $defs);
    $defined = array_flip($defs[1]);
    return preg_replace_callback('/\[\^([^\]\s]+)\](?!:)/', function ($m) use ($defined) {
        return isset($defined[$m[1]]) ? $m[0] : '';
    }, $md);
}

/** Markdown → HTML with vendored Parsedown + ParsedownExtra (lib/, MIT) — Extra adds footnotes. */
function stf_render_markdown($md)
{
    require_once __DIR__ . '/lib/Parsedown.php';
    require_once __DIR__ . '/lib/ParsedownExtra.php';
    $pd   = new ParsedownExtra();   // fresh instance: Extra's footnote counter isn't reset by text()
    $html = $pd->text(stf_strip_markers($md));

    // Extra appends footnotes at the very end. If the article has its own
    // "Endnotes"/"Notes" heading, put the list under it instead of leaving
    // that heading empty above the book footer.
    if (preg_match('#\n?<div class="footnotes">\s*<hr />\s*(<ol>.*</ol>)\s*</div>\s*$#s', $html, $fn, PREG_OFFSET_CAPTURE)
        && preg_match('#<h2>(?:Endnotes|Notes|Footnotes)</h2>#i', $html, $h2, PREG_OFFSET_CAPTURE)
        && $h2[0][1] < $fn[0][1]) {
        $list = "\n<div class=\"footnotes\">\n" . $fn[1][0] . "\n</div>";
        $html = substr($html, 0, $fn[0][1]);
        $at   = $h2[0][1] + strlen($h2[0][0]);
        $html = substr($html, 0, $at) . $list . substr($html, $at);
    }
    return $html;
}
