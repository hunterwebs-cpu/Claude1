/* ============================================================================
   SURVIVING THE FEDS — Core interactions
   Sticky nav, full-screen mega-menu, scroll reveals, animated counters.
   Vanilla JS, no dependencies. Honors prefers-reduced-motion.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Sticky header state --------------------------------------------- */
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 40);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- Full-screen overlay menu ---------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var overlay = document.querySelector('.nav-overlay');
  function closeMenu() {
    document.body.classList.remove('menu-open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  if (overlay) {
    overlay.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });

  /* ---- Scroll reveal --------------------------------------------------- */
  var revealEls = document.querySelectorAll('[data-reveal]');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Animated counters ----------------------------------------------- */
  var counters = document.querySelectorAll('[data-count]');
  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    if (reduceMotion) { el.textContent = prefix + target + suffix; return; }
    var start = null, dur = 1600;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = target % 1 === 0 ? Math.floor(eased * target) : (eased * target).toFixed(1);
      el.textContent = prefix + val + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { animateCount(entry.target); cio.unobserve(entry.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(animateCount);
  }

  /* ---- Print / Save-as-PDF buttons ------------------------------------- */
  document.querySelectorAll('[data-print]').forEach(function (btn) {
    btn.addEventListener('click', function () { window.print(); });
  });

  /* ---- Footer year ----------------------------------------------------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---- Hero typewriter ("But you" only — char by char)
         "can get through this." is in .hl-em and revealed by CSS clip-path
         so background-clip:text stays intact. Only text nodes and <br>
         directly inside .hsl-bright are processed here. --------------- */
  (function initTypewriter() {
    var line = document.querySelector('.hsl-bright');
    if (!line) return;

    if (reduceMotion) { line.style.opacity = '1'; return; }

    line.style.opacity = '1';

    var delay = 580;   // ms before first char
    var charMs = 42;   // ms per character
    var brPause = 195; // pause at the line break

    Array.from(line.childNodes).forEach(function (node) {
      if (node.nodeType === 3) { // text node ("But you")
        var chars = Array.from(node.textContent);
        if (!chars.length) return;
        var frag = document.createDocumentFragment();
        chars.forEach(function (ch) {
          var s = document.createElement('span');
          s.className = 'tw-char';
          s.textContent = ch;
          s.style.setProperty('--tw-delay', delay + 'ms');
          delay += charMs;
          frag.appendChild(s);
        });
        node.parentNode.replaceChild(frag, node);
      } else if (node.nodeType === 1 && node.tagName === 'BR') {
        delay += brPause; // .hl-em clip-path uses CSS timing, not delay var
      }
      // .hl-em is left untouched — CSS handles its reveal
    });
  }());

  /* ---- Magnetic hover on primary buttons (subtle) ---------------------- */
  if (!reduceMotion && window.matchMedia('(pointer:fine)').matches) {
    document.querySelectorAll('.btn--primary').forEach(function (btn) {
      btn.addEventListener('mousemove', function (e) {
        var r = btn.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.18;
        var y = (e.clientY - r.top - r.height / 2) * 0.18;
        btn.style.transform = 'translate(' + x + 'px,' + (y - 3) + 'px)';
      });
      btn.addEventListener('mouseleave', function () { btn.style.transform = ''; });
    });
  }
})();
