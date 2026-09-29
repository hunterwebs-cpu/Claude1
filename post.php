<?php
/* Legacy article URL (post.php?slug=...). Articles now live at /journal/<slug>,
   rendered on the server by blog.php. Permanently redirect old links, bookmarks
   and search-engine entries there. */
require __DIR__ . '/_content.php';
$slug = $_GET['slug'] ?? '';
$slug = is_string($slug) ? strtolower($slug) : '';
header('Location: ' . (stf_valid_slug($slug) ? stf_url($slug) : '/journal'), true, 301);
exit;
