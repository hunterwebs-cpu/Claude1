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

$dir = __DIR__ . '/blog';
$slugs = array();

if (is_dir($dir)) {
    foreach (glob($dir . '/*.md') as $file) {
        $slugs[] = basename($file, '.md');
    }
}

echo json_encode($slugs);
