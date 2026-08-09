/* ============================================================================
   SURVIVING THE FEDS — Core interactions
   Sticky nav, full-screen mega-menu, scroll reveals, animated counters.
   Vanilla JS, no dependencies. Honors prefers-reduced-motion.
   ========================================================================== */
(function () {
  'use strict';

  /* NodeList.forEach is missing on older Android/Safari. Without this shim the
     first .forEach() below throws, the whole IIFE aborts, and every
     [data-reveal] section stays hidden — i.e. a blank page below the hero. */
  if (window.NodeList && !NodeList.prototype.forEach) {
    NodeList.prototype.forEach = Array.prototype.forEach;
  }

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Sticky header state --------------------------------------------- */
  var header = document.querySelector('.site-header');
  var announce = document.querySelector('.site-announce');
  function onScroll() {
    if (!header) return;
    /* Snap the header to the top exactly as the announcement bar scrolls away */
    var threshold = announce ? announce.offsetHeight - 6 : 40;
    header.classList.toggle('scrolled', window.scrollY > threshold);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- Full-screen overlay menu ---------------------------------------- */
  var toggle  = document.querySelector('.nav-toggle');
  var overlay = document.querySelector('.nav-overlay');
  var mainEl  = document.querySelector('main');
  var footEl  = document.querySelector('.site-footer');

  /* Make the page behind the overlay unreachable by tab and screen readers */
  function setInert(on) {
    [mainEl, footEl].forEach(function (el) {
      if (!el) return;
      if (on) { el.setAttribute('inert', ''); } else { el.removeAttribute('inert'); }
    });
  }

  function openMenu() {
    document.body.classList.add('menu-open');
    if (toggle) toggle.setAttribute('aria-expanded', 'true');
    setInert(true);
    /* The overlay animates from visibility:hidden; focus() is a no-op until it
       is actually visible, so wait for the transition before moving focus. */
    var first = overlay && overlay.querySelector('a');
    if (!first) return;
    var done = false;
    function grab() {
      if (done) return;
      done = true;
      first.focus();
    }
    overlay.addEventListener('transitionend', grab, { once: true });
    setTimeout(grab, 450); /* fallback if transitionend never fires */
  }

  function closeMenu(returnFocus) {
    if (!document.body.classList.contains('menu-open')) return;
    document.body.classList.remove('menu-open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    setInert(false);
    if (returnFocus && toggle) toggle.focus();
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      if (document.body.classList.contains('menu-open')) { closeMenu(true); }
      else { openMenu(); }
    });
  }
  if (overlay) {
    overlay.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { closeMenu(false); });
    });
    /* Trap Tab inside the overlay while it is open */
    overlay.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var items = overlay.querySelectorAll('a');
      if (!items.length) return;
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu(true);
  });

  /* ---- Marquee pause control (WCAG 2.2.2) ------------------------------- */
  var mqBtn = document.querySelector('.marquee-pause');
  if (mqBtn) {
    mqBtn.addEventListener('click', function () {
      var paused = document.body.classList.toggle('marquee-paused');
      mqBtn.textContent = paused ? 'Play' : 'Pause';
      mqBtn.setAttribute('aria-label', paused ? 'Resume scrolling text' : 'Pause scrolling text');
    });
  }

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
        delay += brPause;
      } else if (node.nodeType === 1 && node.classList && node.classList.contains('word-survive')) {
        // Tell CSS when to reveal this word, then advance delay past it
        node.style.setProperty('--ws-delay', delay + 'ms');
        delay += Array.from(node.textContent).length * charMs;
      }
      // other elements left untouched
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
