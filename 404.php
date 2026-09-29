<?php http_response_code(404); header('X-Robots-Tag: noindex, follow'); ?><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Page not found | Surviving the Feds</title>
  <meta name="robots" content="noindex, follow" />
  <meta name="theme-color" content="#0A0B0E" />
  <?php require '_head.php'; ?>
</head>
<body>
<?php $stf_page = '404'; require '_nav.php'; ?>
  <main id="main">
    <section class="section">
      <div class="container center">
        <span class="eyebrow center">404</span>
        <h1>That page isn't here.</h1>
        <p class="lead center">It may have moved. These will get you where you need to go.</p>
        <div class="hero-actions" style="justify-content:center;">
          <a class="btn btn--primary" href="/start-here.php">Start Here</a>
          <a class="btn btn--ghost" href="/journal">Read the Journal</a>
          <a class="btn btn--ghost" href="/calculators.php">Free Calculators</a>
          <a class="btn btn--ghost" href="/books.php">Books</a>
        </div>
      </div>
    </section>
  </main>
<?php require '_footer.php'; ?>
</body>
</html>
