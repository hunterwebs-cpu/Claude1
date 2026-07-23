<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Article — Surviving the Feds</title>
  <meta name="description" content="An article from the Surviving the Feds Journal." />
  <meta name="theme-color" content="#0A0B0E" />  <?php require '_head.php'; ?>
</head>
<body>

<?php $stf_page = 'post'; require '_nav.php'; ?>

  <main>
    <article class="article" id="article-root">
      <div class="container">
        <!-- Logo: upper-left of the printed / saved PDF page -->
        <div class="print-brand print-only">
          <img src="assets/img/logo.png" alt="Surviving the Feds" />
        </div>

        <header class="article-header">
          <span class="eyebrow center" id="a-cat">The Journal</span>
          <h1 id="a-title">Loading…</h1>
          <p class="article-meta" id="a-meta"></p>
        </header>

        <!-- Download / print toolbar (hidden when printing) -->
        <div class="article-tools screen-only">
          <button class="btn btn--primary" type="button" data-print>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v8H6z"/></svg>
            Download / Print PDF
          </button>
          <span class="tools-hint">To mail to someone inside, choose <strong>“Save as PDF”</strong> or print directly.</span>
        </div>

        <div class="prose" id="a-body"></div>

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

        <!-- Catch phrase: centered running footer on every printed page -->
        <div class="print-running-foot print-only" aria-hidden="true">
          Knowledge&nbsp;+&nbsp;Strength&nbsp;=&nbsp;Freedom&nbsp;&nbsp;·&nbsp;&nbsp;survivingthefeds.com
        </div>

        <div class="center screen-only" style="margin-top:56px; display:flex; gap:14px; justify-content:center; flex-wrap:wrap;">
          <a class="btn btn--ghost" href="blog.php">← Back to the Journal</a>
          <button class="btn btn--ghost" type="button" data-print>Download / Print PDF</button>
        </div>
      </div>
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
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->

<?php require '_footer.php'; ?>

  <!-- Markdown renderer -->
  <script src="assets/js/post.js?v=15" defer></script>
</body>
</html>
