<?php // Shared <head> assets — include inside <head>, after page-specific meta ?>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <!-- Fonts requested from the HTML, not via @import inside styles.css, so the
       preload scanner discovers them immediately instead of after the CSS parse. -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Courier+Prime:wght@400;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" />

  <link rel="stylesheet" href="assets/css/styles.css?v=<?= filemtime(__DIR__ . '/assets/css/styles.css') ?>" />

  <!-- Tab icon — gold SF shield -->
  <link rel="icon" href="assets/img/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" href="assets/img/favicon-32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="assets/img/favicon-48.png" sizes="48x48" />
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon-180.png" />

  <!-- Google Analytics — last, so it never competes with CSS for bandwidth -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-T324SDSBV4"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-T324SDSBV4');
  </script>
