<?php
/* Generated sitemap — the Journal is read straight from content/blog/, so a new
   article is in the sitemap the moment it is published. Static pages carry a
   hand-maintained lastmod: bump it when a page's content meaningfully changes
   (do not use file mtimes; every deploy resets them and search engines learn to
   ignore the date). */
require __DIR__ . '/_content.php';
header('Content-Type: application/xml; charset=utf-8');
header('Cache-Control: public, max-age=3600');

$static = array(
    array('/',                          '2026-09-29', '1.0'),
    array('/start-here.php',            '2026-09-29', '0.9'),
    array('/books.php',                 '2026-09-29', '0.9'),
    array('/calculators.php',           '2026-09-29', '0.9'),
    array('/journal',                   '2026-09-29', '0.8'),
    array('/is-my-lawyer-any-good.php', '2026-09-29', '0.7'),
    array('/glossary.php',              '2026-09-29', '0.6'),
    array('/about.php',                 '2026-09-29', '0.6'),
);

echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
foreach ($static as $u) {
    echo '  <url><loc>' . stf_h(stf_abs($u[0])) . '</loc><lastmod>' . $u[1] . '</lastmod><priority>' . $u[2] . '</priority></url>' . "\n";
}
foreach (stf_posts() as $p) {
    $mod = $p['updated'] ?? ($p['date'] ?? '');
    echo '  <url><loc>' . stf_h(stf_abs(stf_url($p['slug']))) . '</loc>' . ($mod ? '<lastmod>' . stf_h($mod) . '</lastmod>' : '') . '<priority>0.7</priority></url>' . "\n";
}
echo '</urlset>' . "\n";
