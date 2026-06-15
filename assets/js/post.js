/* ============================================================================
   SURVIVING THE FEDS — Single article renderer
   Reads ?slug= from the URL, loads the Markdown file, parses frontmatter,
   and renders the body. Uses marked.js (loaded via CDN in post.html).
   ========================================================================== */
(function () {
  'use strict';

  var CONTENT_BASE = 'content/blog/';

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

  function getParam(name) {
    return new URLSearchParams(window.location.search).get(name);
  }

  function fail(msg) {
    var host = document.getElementById('article-root');
    if (host) {
      host.innerHTML = '<div class="article-header"><span class="eyebrow center">The Journal</span>' +
        '<h1>Article not found</h1><p class="lead center">' + msg +
        '</p><div class="center" style="margin-top:28px;"><a class="btn btn--primary" href="blog.html">Back to the Journal</a></div></div>';
    }
  }

  var slug = getParam('slug');
  if (!slug || !/^[a-z0-9\-]+$/i.test(slug)) {
    fail('We couldn\'t find that article.');
    return;
  }

  fetch(CONTENT_BASE + slug + '.md')
    .then(function (r) { if (!r.ok) throw new Error('404'); return r.text(); })
    .then(function (raw) {
      var meta = parseFrontmatter(raw);
      document.title = (meta.title || 'Article') + ' — Surviving the Feds';

      var metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc && meta.excerpt) metaDesc.setAttribute('content', meta.excerpt);

      var cat = document.getElementById('a-cat');
      var title = document.getElementById('a-title');
      var byline = document.getElementById('a-meta');
      var prose = document.getElementById('a-body');

      if (cat) cat.textContent = meta.category || 'Article';
      if (title) title.textContent = meta.title || '';
      if (byline) {
        byline.textContent = [meta.author, fmtDate(meta.date)].filter(Boolean).join('  ·  ');
      }
      if (prose) {
        prose.innerHTML = (window.marked ? window.marked.parse(meta.body) : meta.body);
      }
    })
    .catch(function () {
      fail('We couldn\'t load that article. It may have moved, or you may be viewing this file locally instead of on a web host.');
    });
})();
