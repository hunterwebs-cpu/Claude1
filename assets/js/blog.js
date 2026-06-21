/* ============================================================================
   SURVIVING THE FEDS — Blog engine (client-side, buildless)
   Reads /content/posts.json (list of slugs), loads each Markdown file,
   parses its YAML-ish frontmatter, and renders content.

   Two modes:
     JOURNAL  — split-pane command center (blog.html), detected by #journal-reader
     GRID     — card grid for homepage (#home-posts) and any other grid containers
   ========================================================================== */
(function () {
  'use strict';

  var CONTENT_BASE = 'content/blog/';
  var AUTO_INDEX   = 'content/posts.php';
  var MANIFEST     = 'content/posts.json';

  /* Minimal frontmatter parser */
  function parseFrontmatter(raw) {
    var meta = {}, body = raw;
    var m = raw.match(/^---\s*\n([\s\S]*?)\n---\s*\n?([\s\S]*)$/);
    if (m) {
      body = m[2];
      m[1].split('\n').forEach(function (line) {
        var idx = line.indexOf(':');
        if (idx === -1) return;
        var key = line.slice(0, idx).trim();
        var val = line.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
        if (key) meta[key] = val;
      });
    }
    meta.body = body;
    return meta;
  }

  function fmtDate(iso) {
    var d = new Date(iso + 'T00:00:00');
    if (isNaN(d)) return iso || '';
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  }

  function esc(s) {
    return String(s || '').replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  /* Strip print/layout markers left in Markdown source */
  function stripMarkers(md) {
    return md
      .replace(/\[LOGO:[^\]]*\]/g, '')
      .replace(/\[ORANGE RULE LINE[^\]]*\]/g, '')
      .replace(/\[HEADSHOT:[^\]]*\]/g, '')
      .replace(/\[SIGNATURE IMAGE[^\]]*\]/g, '')
      .replace(/\[TWO-BOOK FOOTER\]/g, '');
  }

  /* Fetch slug list (PHP auto-index preferred, JSON fallback) */
  function getSlugs() {
    return fetch(AUTO_INDEX)
      .then(function (r) {
        if (!r.ok) throw new Error('no php');
        return r.json();
      })
      .then(function (slugs) {
        if (Array.isArray(slugs) && slugs.length) return slugs;
        throw new Error('empty');
      })
      .catch(function () {
        return fetch(MANIFEST).then(function (r) {
          if (!r.ok) throw new Error('manifest');
          return r.json();
        });
      });
  }

  /* Load and parse all posts */
  function loadPosts() {
    return getSlugs()
      .then(function (slugs) {
        return Promise.all(slugs.map(function (slug) {
          return fetch(CONTENT_BASE + slug + '.md')
            .then(function (r) { return r.ok ? r.text() : ''; })
            .then(function (raw) {
              if (!raw) return null;
              var meta = parseFrontmatter(raw);
              meta.slug = slug;
              return meta;
            })
            .catch(function () { return null; });
        }));
      })
      .then(function (posts) {
        return posts
          .filter(Boolean)
          .sort(function (a, b) { return (b.date || '').localeCompare(a.date || ''); });
      });
  }

  /* ---- GRID MODE: card rendering (homepage) ------------------------------- */

  function cardHTML(post) {
    var thumb = post.cover
      ? '<img src="' + esc(post.cover) + '" alt="" loading="lazy" />'
      : '<span class="ph-mark" aria-hidden="true">§</span>';
    return '' +
      '<a class="post-card" href="post.html?slug=' + encodeURIComponent(post.slug) + '">' +
        '<div class="post-thumb">' + thumb + '</div>' +
        '<div class="post-body">' +
          '<span class="post-cat">' + esc(post.category || 'Article') + '</span>' +
          '<h3>' + esc(post.title) + '</h3>' +
          '<p>' + esc(post.excerpt || '') + '</p>' +
          '<span class="post-date">' + fmtDate(post.date) + '</span>' +
        '</div>' +
      '</a>';
  }

  function render(targetId, limit) {
    var el = document.getElementById(targetId);
    if (!el) return;
    loadPosts().then(function (posts) {
      var list = limit ? posts.slice(0, limit) : posts;
      if (!list.length) {
        el.innerHTML = '<p style="color:var(--muted)">No articles yet — check back soon.</p>';
        return;
      }
      el.innerHTML = list.map(cardHTML).join('');
    }).catch(function () {
      el.innerHTML = '<p style="color:var(--muted)">Articles are loading from the server. If you are viewing this file locally, run it on a web host to see posts.</p>';
    });
  }

  /* ---- JOURNAL MODE: split-pane command center ---------------------------- */

  function journalItemHTML(post) {
    return '<button class="journal-item" data-slug="' + esc(post.slug) + '" type="button">' +
      '<span class="journal-item-cat">' + esc(post.category || 'Article') + '</span>' +
      '<span class="journal-item-title">' + esc(post.title) + '</span>' +
      '<span class="journal-item-date">' + fmtDate(post.date) + '</span>' +
      '</button>';
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
      /* Fade article in: make visible but transparent, then remove fade-enter */
      if (article) {
        article.hidden = false;
        article.classList.add('fade-enter');
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            article.classList.remove('fade-enter');
          });
        });
      }
      /* Fade welcome out via class */
      if (welcome) welcome.classList.add('is-hidden');
    } else {
      /* Restore welcome, hide article */
      if (welcome) welcome.classList.remove('is-hidden');
      if (article) {
        article.hidden = true;
        article.classList.remove('fade-enter');
      }
    }
  }

  function loadArticleInReader(slug, skipHistory) {
    if (!skipHistory) {
      history.pushState({ slug: slug }, '', '?slug=' + encodeURIComponent(slug));
    }

    /* Mark active item in sidebar */
    document.querySelectorAll('.journal-item').forEach(function (btn) {
      btn.classList.toggle('journal-item--active', btn.dataset.slug === slug);
    });

    /* Show article pane with loading message */
    setReaderState(true);
    var bodyEl = document.getElementById('jr-body');
    if (bodyEl) bodyEl.innerHTML = '<p style="text-align:center;color:var(--muted);padding:56px 0;">Loading…</p>';

    /* Scroll reader back to top */
    var reader = document.getElementById('journal-reader');
    if (reader) reader.scrollTop = 0;

    /* Mobile: enter reading mode */
    document.body.classList.add('journal-reading');

    /* Update document title immediately (will be overwritten on load) */
    document.title = 'Loading… | Surviving the Feds';

    fetch(CONTENT_BASE + slug + '.md')
      .then(function (r) { if (!r.ok) throw new Error('404'); return r.text(); })
      .then(function (raw) {
        var meta = parseFrontmatter(raw);

        /* SEO: title and description */
        document.title = (meta.title || 'Article') + ' | Surviving the Feds';
        var desc = document.querySelector('meta[name="description"]');
        if (desc && meta.excerpt) desc.setAttribute('content', meta.excerpt);

        /* Populate article header */
        var catEl   = document.getElementById('jr-cat');
        var titleEl = document.getElementById('jr-title');
        var metaEl  = document.getElementById('jr-meta');
        if (catEl)   catEl.textContent   = meta.category || 'Article';
        if (titleEl) titleEl.textContent = meta.title || '';
        if (metaEl)  metaEl.textContent  = [meta.author, fmtDate(meta.date)].filter(Boolean).join('  ·  ');

        /* Render body */
        var bodyText = stripMarkers(meta.body);
        if (bodyEl) {
          bodyEl.innerHTML = window.marked
            ? window.marked.parse(bodyText)
            : '<pre style="white-space:pre-wrap">' + esc(bodyText) + '</pre>';
          enhanceImages(bodyEl, slug);
        }
      })
      .catch(function () {
        if (bodyEl) bodyEl.innerHTML = '<p style="text-align:center;color:var(--muted);padding:56px 0;">Could not load that article. Try refreshing.</p>';
        document.title = 'The Journal | Surviving the Feds';
      });
  }

  function showWelcome() {
    setReaderState(false);
    document.body.classList.remove('journal-reading');
    document.title = 'The Journal | Surviving the Feds';
    document.querySelectorAll('.journal-item').forEach(function (btn) {
      btn.classList.remove('journal-item--active');
    });
  }

  function renderJournal() {
    var listEl = document.getElementById('post-list');
    if (!listEl) return;

    loadPosts().then(function (posts) {
      if (!posts.length) {
        listEl.innerHTML = '<p style="color:var(--muted);padding:16px 24px;font-size:.9rem;">No articles yet — check back soon.</p>';
        return;
      }
      listEl.innerHTML = posts.map(journalItemHTML).join('');

      /* Wire clicks */
      listEl.querySelectorAll('.journal-item').forEach(function (btn) {
        btn.addEventListener('click', function () {
          loadArticleInReader(btn.dataset.slug);
        });
      });

      /* Auto-load from URL slug */
      var slug = new URLSearchParams(window.location.search).get('slug');
      if (slug) {
        loadArticleInReader(slug, true);
      }
    }).catch(function () {
      listEl.innerHTML = '<p style="color:var(--muted);padding:16px 24px;font-size:.9rem;">Articles loading from server.</p>';
    });

    /* Back button (mobile) */
    var backBtn = document.getElementById('journal-back');
    if (backBtn) {
      backBtn.addEventListener('click', function () {
        history.pushState(null, '', window.location.pathname);
        showWelcome();
      });
    }

    /* Browser back/forward */
    window.addEventListener('popstate', function (e) {
      var slug = e.state && e.state.slug;
      if (slug) {
        loadArticleInReader(slug, true);
      } else {
        showWelcome();
      }
    });
  }

  /* ---- Auto-wire ---------------------------------------------------------- */
  if (document.getElementById('journal-reader')) {
    renderJournal();
  } else {
    render('post-list', 0);
    render('home-posts', 3);
  }

})();
