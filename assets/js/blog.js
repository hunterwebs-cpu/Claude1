/* ============================================================================
   SURVIVING THE FEDS — Blog engine (client-side, buildless)
   Reads /content/posts.json (list of slugs), loads each Markdown file,
   parses its YAML-ish frontmatter, and renders cards.
   Used by:  blog.html  (full list, #post-list)
             index.html (latest 3, #home-posts)
   ========================================================================== */
(function () {
  'use strict';

  var CONTENT_BASE = '/content/blog/';
  var AUTO_INDEX = '/content/posts.php';   // preferred: lists posts automatically (needs PHP)
  var MANIFEST = '/content/posts.json';    // fallback: static manifest (works anywhere)

  /* Minimal frontmatter parser: ---\n key: "value" \n--- \n body */
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

  function cardHTML(post) {
    var thumb = post.cover
      ? '<img src="' + esc(post.cover) + '" alt="" loading="lazy" />'
      : '<span class="ph-mark" aria-hidden="true">§</span>';
    return '' +
      '<a class="post-card" href="/post.html?slug=' + encodeURIComponent(post.slug) + '">' +
        '<div class="post-thumb">' + thumb + '</div>' +
        '<div class="post-body">' +
          '<span class="post-cat">' + esc(post.category || 'Article') + '</span>' +
          '<h3>' + esc(post.title) + '</h3>' +
          '<p>' + esc(post.excerpt || '') + '</p>' +
          '<span class="post-date">' + fmtDate(post.date) + '</span>' +
        '</div>' +
      '</a>';
  }

  // Try the PHP auto-index first; if it isn't available, fall back to the
  // static JSON manifest. Either way we end up with an array of slugs.
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

  // Auto-wire whichever container is present on the page.
  render('post-list', 0);
  render('home-posts', 3);
})();
