/* ============================================================================
   SURVIVING THE FEDS — Journal enhancements (progressive, not required)

   Articles and the article list are rendered on the server (blog.php), so this
   file is only an enhancement: on the split-pane Journal it lets a click swap
   the article into the reader without a full page load. If anything here fails
   the click falls back to a normal navigation to /journal/<slug>, which is a
   complete page on its own.
   ========================================================================== */
(function () {
  'use strict';

  var reader = document.getElementById('journal-reader');
  if (!reader) return;

  var ARTICLE_PATH = /^\/journal\/([a-z0-9]+(?:-[a-z0-9]+)*)\/?$/;

  function slugFromPath(path) {
    var m = (path || window.location.pathname).match(ARTICLE_PATH);
    return m ? m[1] : null;
  }

  /* Simple string hash — seeds image layout variation per article */
  function hashCode(str) {
    var h = 0;
    for (var i = 0; i < str.length; i++) {
      h = (Math.imul(31, h) + str.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  }

  /* Apply alternating float classes to prose images after render */
  function enhanceImages(container, slug) {
    var imgs = container.querySelectorAll('img');
    if (!imgs.length) return;
    var sides = ['left', 'right'];
    var start = hashCode(slug || '') % 2;
    var count = 0;
    imgs.forEach(function (img) {
      img.classList.add('prose-img');
      var para = img.parentElement;
      if (para) para.classList.add('prose-img-para');
      /* Every 3rd image goes full-width to break up the rhythm */
      if (count % 3 === 2) {
        img.classList.add('prose-img--full');
      } else {
        img.classList.add('prose-img--' + sides[(start + count) % 2]);
      }
      count++;
    });
  }

  function setReaderState(showArticle) {
    var welcome = document.getElementById('journal-welcome');
    var article = document.getElementById('journal-article');
    if (showArticle) {
      if (article) {
        article.hidden = false;
        article.classList.add('fade-enter');
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            article.classList.remove('fade-enter');
          });
        });
      }
      if (welcome) welcome.classList.add('is-hidden');
    } else {
      if (welcome) welcome.classList.remove('is-hidden');
      if (article) {
        article.hidden = true;
        article.classList.remove('fade-enter');
      }
    }
  }

  function markActive(slug) {
    document.querySelectorAll('.journal-item').forEach(function (a) {
      var on = a.getAttribute('data-slug') === slug;
      a.classList.toggle('journal-item--active', on);
      if (on) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
  }

  /* Swap an article into the reader by fetching its server-rendered page. */
  function loadArticleInReader(slug, skipHistory) {
    var url = '/journal/' + slug;
    return fetch(url, { headers: { 'X-Requested-With': 'fetch' }, credentials: 'same-origin' })
      .then(function (r) {
        if (!r.ok) throw new Error('status ' + r.status);
        return r.text();
      })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var body = doc.getElementById('jr-body');
        var title = doc.getElementById('jr-title');
        if (!body || !title) throw new Error('unexpected page');

        ['jr-cat', 'jr-title', 'jr-meta'].forEach(function (id) {
          var from = doc.getElementById(id), to = document.getElementById(id);
          if (from && to) to.textContent = from.textContent;
        });
        var bodyEl = document.getElementById('jr-body');
        bodyEl.innerHTML = body.innerHTML;
        enhanceImages(bodyEl, slug);

        /* Keep title, description and canonical honest for the new URL */
        document.title = doc.title;
        var d = document.querySelector('meta[name="description"]');
        var nd = doc.querySelector('meta[name="description"]');
        if (d && nd) d.setAttribute('content', nd.getAttribute('content'));
        var c = document.querySelector('link[rel="canonical"]');
        var nc = doc.querySelector('link[rel="canonical"]');
        if (c && nc) c.setAttribute('href', nc.getAttribute('href'));

        if (!skipHistory) history.pushState({ slug: slug }, '', url);
        markActive(slug);
        setReaderState(true);
        document.body.classList.add('journal-reading');
        reader.scrollTop = 0;
      });
  }

  function showWelcome() {
    setReaderState(false);
    document.body.classList.remove('journal-reading');
    document.title = 'Federal Case Guides: Plain-English Answers | Surviving the Feds';
    markActive(null);
  }

  /* Article images on a directly-loaded page */
  var initialBody = document.getElementById('jr-body');
  var initialSlug = slugFromPath();
  if (initialBody && initialSlug) enhanceImages(initialBody, initialSlug);

  /* Intercept in-page article links; anything that fails just navigates. */
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest('a[href^="/journal/"]');
    if (!a) return;
    var slug = slugFromPath(a.getAttribute('href'));
    if (!slug) return;
    e.preventDefault();
    loadArticleInReader(slug).catch(function () {
      window.location.href = a.getAttribute('href');
    });
  });

  /* Mobile: back to the article list */
  var backBtn = document.getElementById('journal-back');
  if (backBtn) {
    backBtn.addEventListener('click', function () {
      history.pushState(null, '', '/journal');
      showWelcome();
    });
  }

  /* Browser back / forward */
  window.addEventListener('popstate', function () {
    var slug = slugFromPath();
    if (slug) {
      loadArticleInReader(slug, true).catch(function () { window.location.reload(); });
    } else {
      showWelcome();
    }
  });
})();
