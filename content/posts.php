<?php
/* ============================================================================
   SURVIVING THE FEDS — Auto post index
   Lists every Markdown file in /content/blog/ and returns their frontmatter as
   JSON, so listing pages can render cards from ONE request and new CMS posts
   appear automatically with no manifest to maintain by hand.

   Parsing lives in /_posts.php, shared with post.php, blog.php and sitemap.php.
   If PHP is unavailable, blog.js falls back to the static /content/posts.json.
   ========================================================================== */
require __DIR__ . '/../_posts.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-cache, must-revalidate');

echo json_encode(stf_list_posts());
