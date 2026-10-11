<?php
/* ============================================================================
   SURVIVING THE FEDS — XML sitemap (served at /sitemap.xml via .htaccess)
   Static pages are listed below; every content/blog/*.md post is added
   automatically, so articles published from the CMS appear with no edits here.

   lastmod: posts use frontmatter `updated` (else `date`). Static pages get no
   lastmod — Hostinger rewrites every file's mtime on each deploy, so filemtime()
   would claim every page changed whenever anything is pushed.
   ========================================================================== */
require __DIR__ . '/_seo.php';
require __DIR__ . '/_posts.php';

$static = array(
    '',                           // homepage
    'start-here.php',
    'calculators.php',
    'books.php',
    'blog.php',
    'glossary.php',
    'about.php',
    'is-my-lawyer-any-good.php',
);

$posts  = stf_list_posts();
$newest = '';
$urls   = array();
foreach ($posts as $p) {
    list(, $mod) = stf_post_dates($p);
    if ($mod > $newest) $newest = $mod;
    $urls[] = array(stf_url(stf_post_path($p['slug'])), $mod);
}
foreach (array_reverse($static) as $path) {
    // The Journal index changes whenever a post is published or updated
    array_unshift($urls, array(stf_url($path), $path === 'blog.php' ? $newest : ''));
}

header('Content-Type: application/xml; charset=utf-8');
header('Cache-Control: no-cache, must-revalidate');
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
foreach ($urls as $u) {
    echo '  <url><loc>' . htmlspecialchars($u[0], ENT_XML1 | ENT_QUOTES, 'UTF-8') . '</loc>'
       . ($u[1] ? '<lastmod>' . $u[1] . '</lastmod>' : '') . "</url>\n";
}
echo "</urlset>\n";
