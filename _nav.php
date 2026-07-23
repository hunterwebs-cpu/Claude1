<?php
// Shared navigation partial — include after setting $stf_page.
// Optional: $nav_cta_label, $nav_cta_href, $nav_cta_attrs for per-page CTA override.
$_cta_label = $nav_cta_label ?? 'Command Center';
$_cta_href  = $nav_cta_href  ?? 'start-here.php';
$_cta_attrs = $nav_cta_attrs ?? '';
function _stf_cur(string $page, string $current): string {
  return $page === $current ? ' aria-current="page"' : '';
}
$_p = $stf_page ?? '';
?>
  <!-- ========================================================= ANNOUNCEMENT -->
  <div class="site-announce">This site is always being improved. <strong>Check back regularly</strong> for new tools, guides, and updates.</div>

  <!-- ============================================================ HEADER -->
  <header class="site-header">
    <div class="container">
      <nav class="nav" aria-label="Primary">
        <a class="brand" href="index.php" aria-label="Surviving the Feds home">
          <img src="assets/img/logo.png" alt="Surviving the Feds" />
        </a>
        <div class="nav-links">
          <a class="nav-link" href="index.php"<?= _stf_cur($_p,'home') ?>>Home</a>
          <a class="nav-link" href="calculators.php"<?= _stf_cur($_p,'calculators') ?>>Free Tools</a>
          <a class="nav-link" href="books.php"<?= _stf_cur($_p,'books') ?>>The Books</a>
          <a class="nav-link" href="blog.php"<?= _stf_cur($_p,'blog') ?>>The Journal</a>
          <a class="nav-link" href="about.php"<?= _stf_cur($_p,'about') ?>>About</a>
        </div>
        <div class="nav-cta">
          <a class="btn btn--primary" href="<?= htmlspecialchars($_cta_href) ?>"<?= $_cta_attrs ?>>
            <?= htmlspecialchars($_cta_label) ?>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mega-menu">
            <span></span><span></span><span></span>
          </button>
        </div>
      </nav>
    </div>
  </header>

  <!-- Full-screen overlay mega-menu -->
  <div class="nav-overlay" id="mega-menu">
    <div class="overlay-menu">
      <a href="index.php"><span class="idx">01</span>Home</a>
      <a href="start-here.php"><span class="idx">02</span>Command Center</a>
      <a href="calculators.php"><span class="idx">03</span>Free Tools</a>
      <a href="books.php"><span class="idx">04</span>The Books</a>
      <a href="blog.php"><span class="idx">05</span>The Journal</a>
      <a href="about.php"><span class="idx">06</span>About</a>
    </div>
    <aside class="overlay-aside">
      <p class="eyebrow">Knowledge + Strength = Freedom</p>
      <p class="tagline-mini">We make sure the world has the information it needs to fight for its freedom.</p>
      <p class="contact-line">For inquiries:</p>
      <p class="contact-line"><a href="mailto:contact@survivingthefeds.com">contact@survivingthefeds.com</a></p>
    </aside>
  </div>
