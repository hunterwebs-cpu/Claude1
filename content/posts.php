<?php
/* ============================================================================
   SURVIVING THE FEDS — Auto post index
   Lists every Markdown file in /content/blog/ and returns their slugs as JSON.
   This lets new posts created in the CMS appear on the site automatically,
   with no manifest to maintain by hand.

   Requires PHP (Hostinger supports it out of the box). If PHP is unavailable,
   the site automatically falls back to the static /content/posts.json file.
   ========================================================================== */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-cache, must-revalidate');

/* Returns each post's frontmatter, not just its slug, so listing pages can
   render cards from ONE request instead of fetching every full article. */
$dir = __DIR__ . '/blog';
$posts = array();

if (is_dir($dir)) {
    foreach (glob($dir . '/*.md') as $file) {
        $fh  = fopen($file, 'r');
        $raw = $fh ? fread($fh, 2048) : '';   // frontmatter lives at the top
        if ($fh) fclose($fh);

        $meta = array('slug' => basename($file, '.md'));
        if (preg_match('/^---\s*\n(.*?)\n---/s', $raw, $m)) {
            foreach (explode("\n", $m[1]) as $line) {
                $i = strpos($line, ':');
                if ($i === false) continue;
                $k = trim(substr($line, 0, $i));
                $v = trim(trim(substr($line, $i + 1)), "\"'");
                if ($k !== '') $meta[$k] = $v;
            }
        }
        $posts[] = $meta;
    }
}

usort($posts, function ($a, $b) {
    return strcmp(isset($b['date']) ? $b['date'] : '', isset($a['date']) ? $a['date'] : '');
});

echo json_encode($posts);
