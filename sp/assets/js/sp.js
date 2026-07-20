/* Surviving Pretrial — sp.survivingthefeds.com
   Budget: this file stays under ~3KB. No dependencies. */
(function () {
  'use strict';

  /* Scroll reveals (skipped for reduced motion — CSS shows content immediately).
     The .js gate means content stays visible for crawlers / no-JS readers. */
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revealed = document.querySelectorAll('[data-reveal]');
  if (!reduced && 'IntersectionObserver' in window && revealed.length) {
    document.documentElement.classList.add('js');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    revealed.forEach(function (el) { io.observe(el); });
  } else {
    revealed.forEach(function (el) { el.classList.add('in'); });
  }

  /* Sticky buy bar: appears after the hero scrolls out, hides near the footer */
  var bar = document.getElementById('buybar');
  var hero = document.querySelector('.hero, .page-hero');
  var foot = document.querySelector('.sp-footer');
  if (bar && hero && 'IntersectionObserver' in window) {
    var pastHero = false, atFoot = false;
    var update = function () { bar.classList.toggle('on', pastHero && !atFoot); };
    new IntersectionObserver(function (en) {
      pastHero = !en[0].isIntersecting && en[0].boundingClientRect.top < 0; update();
    }).observe(hero);
    if (foot) {
      new IntersectionObserver(function (en) { atFoot = en[0].isIntersecting; update(); }).observe(foot);
    }
  }

  /* Kindle Instant Preview facade: iframe loads only on click */
  var facade = document.getElementById('reader-facade');
  if (facade) {
    facade.addEventListener('click', function () {
      var box = facade.parentNode;
      var frame = document.createElement('iframe');
      frame.src = 'https://read.amazon.com/kp/card?asin=B0BTCDLWN8&preview=inline&hideBuy=false';
      frame.title = 'Surviving Pretrial — free Kindle preview';
      frame.setAttribute('allowfullscreen', '');
      box.appendChild(frame);
      facade.remove();
    });
  }

  /* Outbound Amazon CTA tracking: one delegated listener.
     Fires a custom event to whichever analytics is installed (see README). */
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[data-cta]');
    if (!a) return;
    var label = a.getAttribute('data-cta');
    if (window.goatcounter && window.goatcounter.count) {
      window.goatcounter.count({ path: 'cta/' + label, title: label, event: true });
    }
    if (window.plausible) { window.plausible('Amazon Click', { props: { cta: label } }); }
  });
}());
