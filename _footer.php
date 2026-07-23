<?php // Shared footer partial ?>
  <!-- ============================================================ FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="assets/img/logo-silver.png" alt="Surviving the Feds" />
          <p>Knowledge + Strength = Freedom. Real answers about the federal system, from someone who lived it.</p>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <a href="index.php">Home</a>
          <a href="start-here.php">Command Center</a>
          <a href="calculators.php">Free Tools</a>
          <a href="about.php">About</a>
          <a href="books.php">The Books</a>
          <a href="blog.php">The Journal</a>
          <a href="is-my-lawyer-any-good.php">Is My Lawyer Any Good?</a>
        </div>
        <div class="footer-col">
          <h4>The Calculators</h4>
          <a href="start-here.php#guideline">Guideline Range</a>
          <a href="start-here.php#stats">Sentencing Statistics</a>
          <a href="start-here.php#fsa">FSA Time Credits</a>
          <a href="start-here.php#bop">BOP Security Level</a>
          <a href="start-here.php#refsheets">Reference Sheets</a>
        </div>
        <div class="footer-col">
          <h4>The Books</h4>
          <a href="https://www.amazon.com/Surviving-Pretrial-Ultimate-Survival-Prosecuted/dp/B0BT19Y3V8" target="_blank" rel="noopener">Surviving Pretrial</a>
          <a href="https://www.amazon.com/2255-Motion-Handbook-Post-Conviction-Surviving/dp/B0D8HQRJN8" target="_blank" rel="noopener">The 2255 Motion Handbook</a>
          <a href="https://www.amazon.com/dp/B0D471H5Z9" target="_blank" rel="noopener">The Series on Amazon</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year"><?= date('Y') ?></span> Surviving the Feds. All rights reserved.</span>
        <span>This site is for informational purposes only and does not constitute legal advice.</span>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js?v=<?= filemtime(__DIR__ . '/assets/js/main.js') ?>" defer></script>
