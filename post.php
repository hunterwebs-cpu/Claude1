<?php
require __DIR__ . '/_seo.php';
require __DIR__ . '/_posts.php';

/* Server-render the article so crawlers that don't run JavaScript (and every
   reader on a slow phone) get the full text, title and metadata in the HTML. */
$slug = isset($_GET['slug']) ? (string) $_GET['slug'] : '';
$post = stf_load_post($slug);

if ($post) {
    list($published, $modified) = stf_post_dates($post);
    $title   = isset($post['title']) ? $post['title'] : 'Article';
    $excerpt = isset($post['excerpt']) ? $post['excerpt'] : '';
    $path    = stf_post_path($slug);
    $url     = stf_url($path);
    $cover   = !empty($post['cover']) ? ltrim($post['cover'], '/') : '';
    $byline  = implode('  ·  ', array_filter(array(
        isset($post['author']) ? $post['author'] : '',
        stf_fmt_date(isset($post['date']) ? $post['date'] : ''),
    )));
    $bodyHtml = stf_render_markdown($post['body']);

    $article = array(
        '@type'            => 'Article',
        '@id'              => $url . '#article',
        'headline'         => $title,
        'description'      => $excerpt,
        'image'            => array(stf_url($cover ?: STF_DEFAULT_IMAGE)),
        'author'           => array('@id' => STF_PERSON_ID, 'name' => 'Bilal Khan'),
        'publisher'        => array('@id' => STF_ORG_ID),
        'mainEntityOfPage' => $url,
        'isPartOf'         => array('@id' => STF_WEBSITE_ID),
        'inLanguage'       => 'en-US',
    );
    if (!empty($post['category'])) $article['articleSection'] = $post['category'];
    if ($published) {
        $article['datePublished'] = $published;
        $article['dateModified']  = $modified;
    }
    if (isset($post['author']) && $post['author'] !== 'Bilal Khan') {
        $article['author'] = array('@type' => 'Person', 'name' => $post['author']);
    }
} else {
    http_response_code(404);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
<?php if ($post):
    stf_meta(array(
        'title'       => stf_post_title_tag($post),
        'description' => $excerpt,
        'path'        => $path,
        'og_title'    => $title,
        'type'        => 'article',
        'image'       => $cover,
        'image_alt'   => $title,
        'extra_og'    => $published ? array(
            array('article:published_time', $published),
            array('article:modified_time', $modified),
        ) : array(),
    ));
    stf_jsonld(array(
        $article,
        stf_breadcrumbs(array(array('Home', ''), array('The Journal', 'blog.php'), array($title, $path))),
        stf_website_node(),
        stf_org_node(),
        stf_person_node(),
    ));
else:
    stf_meta(array(
        'title'       => 'Article not found | Surviving the Feds',
        'description' => 'That article could not be found. Browse every free guide in the Surviving the Feds Journal.',
        'noindex'     => true,
    ));
endif; ?>
  <meta name="theme-color" content="#0A0B0E" />  <?php require '_head.php'; ?>
</head>
<body>

<?php $stf_page = 'post'; require '_nav.php'; ?>

  <main>
    <article class="article" id="article-root">
<?php if (!$post): ?>
      <div class="article-header"><span class="eyebrow center">The Journal</span>
        <h1>Article not found</h1><p class="lead center">We couldn't find that article.</p>
        <div class="center" style="margin-top:28px;"><a class="btn btn--primary" href="blog.php">Back to the Journal</a></div></div>
<?php else: ?>
      <div class="container">
      <!-- Print sheet: <tfoot> repeats at the bottom of every printed page and
           reserves its own space, so body copy can never flow underneath it. -->
      <table class="print-sheet">
        <tfoot class="print-sheet-foot print-only">
          <tr><td>
            <div class="print-foot-inner">
              <span></span>
              <span class="print-foot-tag">Knowledge&nbsp;+&nbsp;Strength&nbsp;=&nbsp;Freedom&nbsp;&nbsp;·&nbsp;&nbsp;survivingthefeds.com</span>
              <img class="print-foot-logo" src="assets/img/logo-silver.png" alt="" />
              <p class="print-foot-legal">
                &copy; 2026 Surviving the Feds. You may print and share this document free of charge with anyone confined in any jail or prison. Charging money for it is not authorized.
              </p>
            </div>
          </td></tr>
        </tfoot>
        <tbody><tr><td>
        <!-- Logo: upper-left of the printed / saved PDF page -->
        <div class="print-brand print-only">
          <img src="assets/img/logo-silver.png" alt="Surviving the Feds" />
        </div>

        <header class="article-header">
          <span class="eyebrow center" id="a-cat"><?= h(!empty($post['category']) ? $post['category'] : 'Article') ?></span>
          <h1 id="a-title"><?= h($title) ?></h1>
          <p class="article-meta" id="a-meta"><?= h($byline) ?></p>
        </header>

        <!-- Download / print toolbar (hidden when printing) -->
        <div class="article-tools screen-only">
          <button class="btn btn--primary" type="button" data-print>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v8H6z"/></svg>
            Download / Print PDF
          </button>
          <span class="tools-hint">To mail to someone inside, choose <strong>“Save as PDF”</strong> or print directly.</span>
        </div>

        <div class="prose" id="a-body">
<?= $bodyHtml /* Markdown from content/blog via the CMS; raw HTML allowed, as marked.js did */ ?>
        </div>

        <!-- Book promo + Amazon CTA appended to the printed / saved PDF page -->
        <aside class="print-books print-only">
          <h2>Get the full field guide — from someone who lived it</h2>
          <p class="print-books-note">Most jails and prisons require books to be shipped <strong>directly from Amazon</strong>. A family member or supporter can order the paperback and have it sent straight to the facility.</p>

          <div class="print-book">
            <h3>Surviving Pretrial</h3>
            <p>The Ultimate Survival Guide to Being Busted &amp; Prosecuted by the Feds — the map most families never get. Covers arrest, detention, evaluating your attorney, what never to say on a recorded line, and how plea deals really work.</p>
            <p class="print-link">Order the paperback &rarr; <strong>amazon.com/dp/B0BT19Y3V8</strong></p>
          </div>

          <div class="print-book">
            <h3>The 2255 Motion Handbook</h3>
            <p>A Post-Conviction Relief Guide for Federal Inmates — the first guide of its kind. The exact steps to file, argue, and fight for your freedom after conviction, written so a non-lawyer can actually use it.</p>
            <p class="print-link">Order the paperback &rarr; <strong>amazon.com/dp/B0D8HQRJN8</strong></p>
          </div>

          <p class="print-disclaimer">Informational only — not legal advice. Always consult a licensed attorney about a specific case.</p>
        </aside>

        <div class="center screen-only" style="margin-top:56px; display:flex; gap:14px; justify-content:center; flex-wrap:wrap;">
          <a class="btn btn--ghost" href="blog.php">← Back to the Journal</a>
          <button class="btn btn--ghost" type="button" data-print>Download / Print PDF</button>
        </div>
        </td></tr></tbody>
      </table>
      </div>
<?php endif; ?>
    </article>

    <!-- CTA BAND -->
    <section class="section cta-band">
      <div class="container">
        <div>
          <span class="eyebrow center">Knowledge + Strength = Freedom</span>
          <h2>Don't face it blind.</h2>
          <p class="lead center">The books go deeper than any article can.</p>
          <div class="hero-actions" style="justify-content:center;">
            <a class="btn btn--primary" href="books.php">
              Explore the Books
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
            <a class="btn btn--ghost" href="calculators.php">Free Calculators</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->

<?php require '_footer.php'; ?>

</body>
</html>
