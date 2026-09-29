<?php
/* ============================================================================
   THE JOURNAL — index and articles, rendered on the server.
   /journal        -> article list + welcome pane
   /journal/<slug> -> the same layout with the article already in the reader

   The article text, <title>, description, canonical and schema are all in the
   initial HTML (no JavaScript needed), so search and AI crawlers can read them.
   Legacy URLs (blog.php, blog.php?slug=, post.php?slug=) 301 to the clean ones.
   ========================================================================== */
require __DIR__ . '/_content.php';

$req_path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/';
$slug     = $_GET['slug'] ?? '';
$slug     = is_string($slug) ? strtolower($slug) : '';

// Legacy URL -> clean URL (only when the visitor did NOT arrive via /journal).
if (strpos($req_path, '/journal') !== 0) {
    $to = stf_valid_slug($slug) ? stf_url($slug) : '/journal';
    header('Location: ' . $to, true, 301);
    exit;
}

$post = null;
$not_found = false;
if ($slug !== '') {
    $post = stf_post($slug);
    if ($post === null) {
        $not_found = true;
        http_response_code(404);
    }
}
$all_posts = stf_posts();

if ($post) {
    $page_title = stf_seo_title($post);
    $page_desc  = stf_meta_description($post);
    $canonical  = stf_abs(stf_url($post['slug']));
    $og_image   = stf_image_url($post);
} elseif ($not_found) {
    $page_title = 'Article not found | Surviving the Feds';
    $page_desc  = 'That article could not be found. Browse the free federal case guides in The Journal.';
    $canonical  = stf_abs('/journal');
    $og_image   = stf_abs('/assets/img/og-home.jpg');
} else {
    $page_title = 'Federal Case Guides: Plain-English Answers | Surviving the Feds';
    $page_desc  = 'Guides on federal indictments, bail, plea deals, sentencing, the PSR, and 2255 motions. Written by someone who lived it. Free, no email required.';
    $canonical  = stf_abs('/journal');
    $og_image   = stf_abs('/assets/img/og-home.jpg');
}
?><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title><?= stf_h($page_title) ?></title>
  <meta name="description" content="<?= stf_h($page_desc) ?>" />
  <link rel="canonical" href="<?= stf_h($canonical) ?>" />
<?php if ($not_found): ?>
  <meta name="robots" content="noindex, follow" />
<?php endif; ?>
  <meta name="theme-color" content="#0A0B0E" />
  <meta property="og:site_name" content="Surviving the Feds" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="<?= $post ? 'article' : 'website' ?>" />
  <meta property="og:title" content="<?= stf_h($post ? ($post['seo_title'] ?? $post['title']) : $page_title) ?>" />
  <meta property="og:description" content="<?= stf_h($page_desc) ?>" />
  <meta property="og:url" content="<?= stf_h($canonical) ?>" />
  <meta property="og:image" content="<?= stf_h($og_image) ?>" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="<?= stf_h($post ? ($post['seo_title'] ?? $post['title']) : $page_title) ?>" />
  <meta name="twitter:description" content="<?= stf_h($page_desc) ?>" />
  <meta name="twitter:image" content="<?= stf_h($og_image) ?>" />
<?php if ($post): ?>
  <meta property="article:published_time" content="<?= stf_h($post['date'] ?? '') ?>" />
  <meta property="article:modified_time" content="<?= stf_h($post['updated'] ?? ($post['date'] ?? '')) ?>" />
  <meta property="article:author" content="<?= stf_h($post['author'] ?? 'Bilal Khan') ?>" />
  <script type="application/ld+json">
<?= json_encode(array(
      '@context' => 'https://schema.org',
      '@graph' => array(
        array(
          '@type' => 'Article',
          '@id' => $canonical . '#article',
          'headline' => $post['title'] ?? '',
          'description' => $page_desc,
          'image' => $og_image,
          'datePublished' => $post['date'] ?? '',
          'dateModified' => $post['updated'] ?? ($post['date'] ?? ''),
          'inLanguage' => 'en-US',
          'articleSection' => $post['category'] ?? 'Article',
          'mainEntityOfPage' => $canonical,
          'author' => array('@type' => 'Person', 'name' => $post['author'] ?? 'Bilal Khan', 'url' => stf_abs('/about.php')),
          'publisher' => array('@type' => 'Organization', 'name' => 'Surviving the Feds', 'url' => STF_SITE . '/',
                               'logo' => array('@type' => 'ImageObject', 'url' => stf_abs('/assets/img/logo-silver.png'))),
        ),
        array(
          '@type' => 'BreadcrumbList',
          'itemListElement' => array(
            array('@type' => 'ListItem', 'position' => 1, 'name' => 'Home', 'item' => STF_SITE . '/'),
            array('@type' => 'ListItem', 'position' => 2, 'name' => 'The Journal', 'item' => stf_abs('/journal')),
            array('@type' => 'ListItem', 'position' => 3, 'name' => $post['title'] ?? '', 'item' => $canonical),
          ),
        ),
      ),
    ), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG) ?>

  </script>
<?php endif; ?>
  <?php require '_head.php'; ?>
</head>
<body class="journal-page<?= $post || $not_found ? ' journal-reading' : '' ?>">

<?php $stf_page = 'blog'; require '_nav.php'; ?>

  <!-- JOURNAL COMMAND CENTER -->
  <div class="journal-layout">

    <!-- LEFT: Article list -->
    <aside class="journal-sidebar">
      <div class="journal-sidebar-head">
        <span class="eyebrow">The Journal</span>
        <h2 class="journal-sidebar-title">Guides &amp; Articles</h2>
        <p class="journal-sidebar-sub">Straight talk about the federal system. No bullshit, no false hope.</p>
      </div>
      <nav class="journal-nav" id="post-list" aria-label="Articles">
<?php if (!$all_posts): ?>
        <p style="color:var(--muted);padding:16px 24px;font-size:.9rem;">No articles yet — check back soon.</p>
<?php endif; ?>
<?php foreach ($all_posts as $p): ?>
        <a class="journal-item<?= ($post && $post['slug'] === $p['slug']) ? ' journal-item--active' : '' ?>" href="<?= stf_h(stf_url($p['slug'])) ?>" data-slug="<?= stf_h($p['slug']) ?>"<?= ($post && $post['slug'] === $p['slug']) ? ' aria-current="page"' : '' ?>>
          <span class="journal-item-cat"><?= stf_h($p['category'] ?? 'Article') ?></span>
          <span class="journal-item-title"><?= stf_h($p['title'] ?? $p['slug']) ?></span>
          <span class="journal-item-date"><?= stf_h(stf_fmt_date($p['date'] ?? '')) ?></span>
        </a>
<?php endforeach; ?>
      </nav>
    </aside>

    <!-- RIGHT: Reader -->
    <section class="journal-reader" id="journal-reader" aria-live="polite">

      <!-- Welcome / no-article state -->
      <div class="journal-welcome<?= ($post || $not_found) ? ' is-hidden' : '' ?>" id="journal-welcome">
        <div class="journal-welcome-inner">
          <span class="eyebrow center">The Journal</span>
          <h2>Real knowledge.<br>No bullshit.</h2>
          <p class="lead">Select an article from the list to begin reading. Every guide is free — no email required, no paywall.</p>
        </div>
      </div>

      <!-- Article reader -->
      <article class="journal-article" id="journal-article"<?= ($post || $not_found) ? '' : ' hidden' ?>>

        <!-- Mobile: back to list -->
        <button class="journal-back-btn btn btn--ghost" type="button" id="journal-back">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          All Articles
        </button>

        <!-- Print logo (print-only) -->
        <div class="print-brand print-only" style="padding:0 28px;">
          <img src="/assets/img/logo.png" alt="Surviving the Feds" />
        </div>

        <header class="journal-article-head">
<?php if ($not_found): ?>
          <span class="eyebrow center" id="jr-cat">The Journal</span>
          <h1 id="jr-title">Article not found</h1>
          <p class="article-meta" id="jr-meta"></p>
<?php else: ?>
          <span class="eyebrow center" id="jr-cat"><?= stf_h($post['category'] ?? 'Article') ?></span>
          <h1 id="jr-title"><?= stf_h($post['title'] ?? '') ?></h1>
          <p class="article-meta" id="jr-meta"><?= stf_h(implode('  ·  ', array_filter(array(
              $post['author'] ?? '',
              $post ? stf_fmt_date($post['date'] ?? '') : '',
              $post ? stf_read_minutes($post['body']) . ' min read' : '',
          )))) ?></p>
<?php endif; ?>
          <div class="journal-tools screen-only">
            <button class="btn btn--primary" type="button" data-print>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v8H6z"/></svg>
              Download / Print PDF
            </button>
            <span class="tools-hint">Choose <strong>"Save as PDF"</strong> to mail to someone inside.</span>
          </div>
        </header>

        <div class="prose" id="jr-body"><?php
  if ($not_found) {
      echo '<p>We couldn\'t find that article. It may have moved. <a href="/journal">Browse all Journal guides</a> or <a href="/start-here.php">start here</a>.</p>';
  } elseif ($post) {
      echo stf_render_markdown($post['body']);
  }
?></div>

<?php if ($post): ?>
        <!-- Keep reading: real crawlable links to related guides -->
        <nav class="screen-only" aria-label="More from the Journal" style="margin-top:48px;padding-top:28px;border-top:1px solid var(--border);">
          <h2 style="font-size:1.15rem;margin:0 0 14px;">More from the Journal</h2>
          <ul style="list-style:none;margin:0;padding:0;display:grid;gap:10px;">
<?php $shown = 0; foreach ($all_posts as $p): if ($p['slug'] === $post['slug'] || $shown >= 4) continue; $shown++; ?>
            <li><a href="<?= stf_h(stf_url($p['slug'])) ?>"><?= stf_h($p['title'] ?? $p['slug']) ?></a></li>
<?php endforeach; ?>
          </ul>
        </nav>
<?php endif; ?>

        <!-- Print: book promos -->
        <aside class="print-books print-only" style="padding:0 28px;">
          <h2>Get the full field guide — from someone who lived it</h2>
          <p class="print-books-note">Most jails and prisons require books to be shipped <strong>directly from Amazon</strong>. A family member or supporter can order the paperback and have it sent straight to the facility.</p>
          <div class="print-book">
            <h3>Surviving Pretrial</h3>
            <p>The Ultimate Survival Guide to Being Busted &amp; Prosecuted by the Feds. Covers arrest, detention, evaluating your attorney, what never to say on a recorded line, and how plea deals really work.</p>
            <p class="print-link">Order the paperback &rarr; <strong>amazon.com/dp/B0BT19Y3V8</strong></p>
          </div>
          <div class="print-book">
            <h3>The 2255 Motion Handbook</h3>
            <p>A Post-Conviction Relief Guide for Federal Inmates. The exact steps to file, argue, and fight for your freedom after conviction.</p>
            <p class="print-link">Order the paperback &rarr; <strong>amazon.com/dp/B0D8HQRJN8</strong></p>
          </div>
          <p class="print-disclaimer">Informational only — not legal advice. Always consult a licensed attorney about a specific case.</p>
        </aside>

        <!-- Print running foot -->
        <div class="print-running-foot print-only" aria-hidden="true">
          Knowledge&nbsp;+&nbsp;Strength&nbsp;=&nbsp;Freedom&nbsp;&nbsp;·&nbsp;&nbsp;survivingthefeds.com
        </div>

        <!-- In-reader CTA (screen-only) -->
        <section class="journal-cta screen-only">
          <div class="journal-cta-inner">
            <span class="eyebrow center">Go deeper</span>
            <h2>The books go where the articles can't.</h2>
            <p class="lead center">Every article here is a starting point. The books are the full field guide — written by someone who spent 20 years navigating the system you're in right now.</p>
            <div class="hero-actions" style="justify-content:center;">
              <a class="btn btn--primary" href="/books.php">
                Explore the Books
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
              </a>
              <a class="btn btn--ghost" href="/start-here.php">Start Here</a>
              <a class="btn btn--ghost" href="/calculators.php">Free Calculators</a>
            </div>
          </div>
        </section>

      </article>

    </section>

  </div>

  <script src="/assets/js/blog.js?v=<?= filemtime(__DIR__ . '/assets/js/blog.js') ?>" defer></script>
</body>
</html>
