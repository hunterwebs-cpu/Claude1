<?php // Shared <head> assets — include inside <head>, after page-specific meta ?>
  <link rel="icon" href="assets/img/logo.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="assets/css/styles.css?v=<?= filemtime(__DIR__ . '/assets/css/styles.css') ?>" />
