<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Surviving the Feds — Knowledge + Strength = Freedom</title>
  <meta name="description" content="When the federal government comes for someone you love, knowledge is the first line of defense. Free guides, books, and real answers from someone who served 20 years in federal prison." />
  <meta name="theme-color" content="#0A0B0E" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Surviving the Feds — Knowledge + Strength = Freedom" />
  <meta property="og:description" content="Real answers about the federal system, from someone who lived it. Built for families. Free, because you deserve it." />
  <meta property="og:image" content="https://survivingthefeds.com/assets/img/logo.png" />

  <!-- Structured data — helps AI search engines cite this site -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Surviving the Feds",
    "url": "https://survivingthefeds.com",
    "description": "Real-world knowledge about the federal criminal system, from someone who served 20 years in federal prison. Free guides, books, and resources for federal defendants and their families.",
    "founder": { "@type": "Person", "name": "Bilal Khan" },
    "sameAs": []
  }
  </script>
  <!-- First-time visitor routing: send new visitors to the Command Center -->
  <script>
    if (!localStorage.getItem('stf_visited')) {
      localStorage.setItem('stf_visited', '1');
      window.location.replace('start-here.php');
    }
  </script>
  <?php require '_head.php'; ?>
</head>
<body>

<?php $stf_page = 'home'; require '_nav.php'; ?>

  <main>

    <!-- ========================================================= HERO -->
    <section class="hero hero--statement">
      <div class="hero-statement-bg" aria-hidden="true"></div>
      <div class="container">
        <div class="hero-inner">

          <span class="eyebrow hero-eyebrow">What they hoped you'd never find.</span>

          <h1 class="hero-statement-h1">
            <span class="hsl-dim">It isn't<br>easy.</span>
            <em class="hsl-bright">But you can <span class="word-survive">survive</span> this.</em>
          </h1>

          <p class="hero-statement-deck">
            Before I was sentenced to <strong>20 years in federal prison,</strong> I was exactly where you are right now — no light, no answers, nowhere to turn. I built this from that place. Free. Because you deserve what I didn't have.
          </p>

          <div class="hero-actions hero-statement-actions">
            <a class="btn btn--primary" href="start-here.php">
              Command Center
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
            <a class="btn btn--ghost" href="blog.php">Read the Journal</a>
          </div>

          <p class="hero-statement-sub">No judgment. No agenda. Just the truth.</p>

        </div>
      </div>

      <div class="scroll-cue" aria-hidden="true">
        <span>Scroll</span>
        <span class="line"></span>
      </div>
    </section>

    <!-- ======================================================= MARQUEE -->
    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        <span class="marquee-item">No judgment here</span>
        <span class="marquee-item">You found the right place</span>
        <span class="marquee-item">The truth from inside</span>
        <span class="marquee-item">Free, because you deserve it</span>
        <span class="marquee-item">Knowledge is how you fight back</span>
        <span class="marquee-item">You are not alone</span>
        <!-- duplicate for seamless loop -->
        <span class="marquee-item">No judgment here</span>
        <span class="marquee-item">You found the right place</span>
        <span class="marquee-item">The truth from inside</span>
        <span class="marquee-item">Free, because you deserve it</span>
        <span class="marquee-item">Knowledge is how you fight back</span>
        <span class="marquee-item">You are not alone</span>
      </div>
    </div>

    <!-- ===================================================== TOOLS / SEO HUB -->
    <section class="section section--tools">
      <div class="container">

        <div class="sec-head" data-reveal>
          <span class="eyebrow eyebrow--clean">Federal Sentencing Tools</span>
          <h2>Free Federal Sentencing Calculators</h2>
          <p class="lead" style="margin-top:18px; max-width:62ch;">Five tools built from the data the government already has — guideline range, FSA time credits, BOP security level, national sentencing statistics, and printable reference sheets. No login. No charge.</p>
        </div>

        <div class="tool-rows" data-reveal data-delay="1">

          <a class="tool-row tool-row--guideline" href="calculators.php#tool-guideline">
            <svg class="tool-row-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3L3 9v12h18V9L12 3z"/><path d="M9 21V12h6v9"/></svg>
            <div class="tool-row-body">
              <strong>Federal Sentencing Guideline Range Calculator</strong>
              <span>Enter offense level and criminal history category. See the §5A sentencing table range immediately.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>

          <a class="tool-row tool-row--fsa" href="calculators.php#tool-fsa">
            <svg class="tool-row-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 3.5"/></svg>
            <div class="tool-row-body">
              <strong>First Step Act Time Credits Calculator (FSA)</strong>
              <span>Estimate earned time credits and projected release date. Every eligible day matters.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>

          <a class="tool-row tool-row--bop" href="calculators.php#tool-bop">
            <svg class="tool-row-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <div class="tool-row-body">
              <strong>BOP Security Level Calculator — Federal Prison Designation</strong>
              <span>Score the BP-337 custody factors. Find out what security level you're likely designated to.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>

          <a class="tool-row tool-row--stats" href="calculators.php#tool-stats">
            <svg class="tool-row-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="12" width="4" height="9"/><rect x="10" y="7" width="4" height="14"/><rect x="17" y="3" width="4" height="18"/></svg>
            <div class="tool-row-body">
              <strong>Federal Sentencing Statistics — USSC National Data</strong>
              <span>Data from 480,000+ federal cases. See what defendants with your charges actually received.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>

          <a class="tool-row tool-row--refsheets" href="calculators.php#tool-refsheets">
            <svg class="tool-row-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            <div class="tool-row-body">
              <strong>Federal Sentencing Reference Sheets — 7 Major Guidelines</strong>
              <span>Printable quick-reference cards for the most common federal offense guidelines.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>

        </div>

        <div class="center" style="margin-top:48px;" data-reveal data-delay="2">
          <a class="btn btn--primary" href="calculators.php">
            Build a Custom Defense Report
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a class="btn btn--ghost" href="calculators.php">All five free tools</a>
        </div>

      </div>
    </section>

    <!-- ================================================ CREDIBILITY STRIP -->
    <section class="cred-strip">
      <div class="container">
        <div class="cred-inner" data-reveal>
          <span class="cred-number" aria-hidden="true">20</span>
          <div class="cred-text">
            <p>Bilal Khan was sentenced to <strong>20 years</strong> in federal prison. He learned the system from inside it — and built this so you don't walk in blind, the way he once did.</p>
            <a class="btn btn--ghost" href="about.php">
              His story
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- ================================================= SINGLE TESTIMONIAL -->
    <section class="section testimonial-section">
      <div class="container">
        <blockquote class="testimonial-single" data-reveal>
          <div class="ts-stars" aria-label="5 out of 5 stars">★★★★★</div>
          <p>"I read this and sent it to my cousin who's just starting in the federal system. For the first time, we feel like there's a light at the end of the tunnel."</p>
          <cite>
            Matthew Clem
            <span>— Verified review · Surviving Pretrial</span>
          </cite>
        </blockquote>
      </div>
    </section>

    <!-- ======================================================= THE BOOKS -->
    <section class="section section--alt">
      <div class="container">
        <div class="sec-head" data-reveal>
          <span class="eyebrow">The Books</span>
          <h2>They have a playbook.<br><em class="display-italic">Now so do you.</em></h2>
          <p class="lead" style="margin-top:18px;">Two volumes in the <em>Surviving the Feds</em> series. Paperback and eBook on Amazon. Written for the person sitting at the kitchen table at midnight, trying to understand what just happened to their life.</p>
        </div>

        <div class="grid grid-2">
          <!-- Book 1 -->
          <article class="card home-book-card" data-reveal data-delay="1" style="display:flex; gap:28px; align-items:center;">
            <a class="book-cover-shell" href="books.php" style="flex:0 0 132px;" aria-label="Surviving Pretrial — view details">
              <img class="cover-img" src="assets/img/cover-pretrial.jpg" alt="Surviving Pretrial book cover by Bilal Khan" loading="lazy" />
            </a>
            <div>
              <div class="bc-series" style="color:var(--accent); font-family:var(--font-label); letter-spacing:.18em; text-transform:uppercase; font-size:.72rem; margin-bottom:8px;">Volume 1</div>
              <h3 style="font-size:1.35rem;">Surviving Pretrial</h3>
              <p style="color:var(--muted); font-size:.95rem; margin:10px 0 18px;">The map most families never get — arrest, detention, attorneys, and the decisions that shape everything that follows.</p>
              <a class="nav-link" style="padding-left:0; color:var(--accent);" href="books.php">Read more →</a>
            </div>
          </article>

          <!-- Book 2 -->
          <article class="card home-book-card" data-reveal data-delay="2" style="display:flex; gap:28px; align-items:center;">
            <a class="book-cover-shell" href="books.php" style="flex:0 0 132px;" aria-label="The 2255 Motion Handbook — view details">
              <img class="cover-img" src="assets/img/cover-2255.jpg" alt="The 2255 Motion Handbook book cover by Bilal Khan" loading="lazy" />
            </a>
            <div>
              <div class="bc-series" style="color:var(--accent); font-family:var(--font-label); letter-spacing:.18em; text-transform:uppercase; font-size:.72rem; margin-bottom:8px;">Volume 2</div>
              <h3 style="font-size:1.35rem;">The 2255 Motion Handbook</h3>
              <p style="color:var(--muted); font-size:.95rem; margin:10px 0 18px;">The first guide of its kind — the exact steps to file, argue, and fight for your freedom after conviction.</p>
              <a class="nav-link" style="padding-left:0; color:var(--accent);" href="books.php">Read more →</a>
            </div>
          </article>
        </div>

        <div class="center" style="margin-top:48px;" data-reveal>
          <a class="btn btn--primary" href="books.php">
            See both books
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
        </div>
      </div>
    </section>

    <!-- ================================================== JOURNAL TEASER -->
    <section class="section" id="journal-teaser">
      <div class="container">
        <div class="sec-head split-head" data-reveal>
          <div class="sh-head">
            <span class="eyebrow">The Journal</span>
            <h2>Straight answers to the questions keeping you up at night.</h2>
          </div>
          <p class="lead">Free guides and articles on federal procedure, defense strategy, and surviving the process — written in plain language. Every article is printable to mail inside.</p>
        </div>
        <div class="post-grid" id="home-posts" data-reveal data-delay="1">
          <!-- Populated by blog.js (latest 3). -->
        </div>
        <div class="center" style="margin-top:48px;" data-reveal>
          <a class="btn btn--ghost" href="blog.php">Read the Journal</a>
        </div>
      </div>
    </section>

  </main>

  <!-- ============================================================ FOOTER -->

<?php require '_footer.php'; ?>

  <script src="assets/js/blog.js?v=<?= filemtime(__DIR__ . '/assets/js/blog.js') ?>" defer></script>
</body>
</html>
