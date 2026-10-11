<?php
/* ============================================================================
   SURVIVING THE FEDS — Shared SEO helpers
   One place for <title>/meta/canonical/Open Graph/Twitter tags and for the
   JSON-LD entity graph, so pages can't drift apart. Include it at the top of a
   page (before <head>) and call stf_meta() inside <head>, before _head.php.

   The Organization / Person / WebSite nodes below are the site's single source
   of truth. Every page that mentions them uses the same @id values.
   ========================================================================== */

if (!defined('STF_SITE')) {
    define('STF_SITE', 'https://survivingthefeds.com');
    define('STF_ORG_ID', STF_SITE . '/#org');
    define('STF_PERSON_ID', STF_SITE . '/#bilal');
    define('STF_WEBSITE_ID', STF_SITE . '/#website');
    define('STF_DEFAULT_IMAGE', 'assets/img/og-home.jpg');   // 1200x630
}

/** Escape for HTML text and attribute values. */
function h($s)
{
    return htmlspecialchars((string) $s, ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML5, 'UTF-8');
}

/** Absolute URL for a site-relative path ('' = homepage). */
function stf_url($path = '')
{
    if (preg_match('#^https?://#i', $path)) return $path;
    return STF_SITE . '/' . ltrim($path, '/');
}

/**
 * Print <title>, meta description, canonical, robots, Open Graph and Twitter tags.
 *   title        full <title> text (required)
 *   description  meta description (required)
 *   path         canonical path, e.g. 'about.php' or 'post.php?slug=x' ('' = home)
 *   og_title / og_description   social overrides (default: title / description)
 *   type         og:type (default 'website')
 *   image, image_alt   social image, site-relative (default og-home.jpg);
 *                      width/height are read from the file when it exists
 *   noindex      true → robots noindex and no canonical
 *   extra_og     array of [property, content] pairs (e.g. article:published_time)
 */
function stf_meta(array $m)
{
    $title = $m['title'];
    $desc  = $m['description'];
    $ogT   = isset($m['og_title']) ? $m['og_title'] : $title;
    $ogD   = isset($m['og_description']) ? $m['og_description'] : $desc;
    $imgPath = ltrim(!empty($m['image']) ? $m['image'] : STF_DEFAULT_IMAGE, '/');
    $img   = stf_url($imgPath);
    $imgWH = is_file(__DIR__ . '/' . $imgPath) ? @getimagesize(__DIR__ . '/' . $imgPath) : false;
    $alt   = isset($m['image_alt']) ? $m['image_alt'] : $ogT;
    $noindex = !empty($m['noindex']);
    $url   = stf_url(isset($m['path']) ? $m['path'] : '');

    $o = array();
    $o[] = '<title>' . h($title) . '</title>';
    $o[] = '<meta name="description" content="' . h($desc) . '" />';
    if ($noindex) {
        $o[] = '<meta name="robots" content="noindex, follow" />';
    } else {
        $o[] = '<link rel="canonical" href="' . h($url) . '" />';
    }
    $o[] = '<meta property="og:type" content="' . h(isset($m['type']) ? $m['type'] : 'website') . '" />';
    $o[] = '<meta property="og:site_name" content="Surviving the Feds" />';
    $o[] = '<meta property="og:locale" content="en_US" />';
    if (!$noindex) $o[] = '<meta property="og:url" content="' . h($url) . '" />';
    $o[] = '<meta property="og:title" content="' . h($ogT) . '" />';
    $o[] = '<meta property="og:description" content="' . h($ogD) . '" />';
    $o[] = '<meta property="og:image" content="' . h($img) . '" />';
    if ($imgWH) {
        $o[] = '<meta property="og:image:width" content="' . (int) $imgWH[0] . '" />';
        $o[] = '<meta property="og:image:height" content="' . (int) $imgWH[1] . '" />';
    }
    $o[] = '<meta property="og:image:alt" content="' . h($alt) . '" />';
    if (!empty($m['extra_og'])) {
        foreach ($m['extra_og'] as $pair) {
            $o[] = '<meta property="' . h($pair[0]) . '" content="' . h($pair[1]) . '" />';
        }
    }
    // Large card only when the image is big enough to fill it (Twitter/X: ≥ 600px wide)
    $card = (!$imgWH || $imgWH[0] >= 600) ? 'summary_large_image' : 'summary';
    $o[] = '<meta name="twitter:card" content="' . $card . '" />';
    $o[] = '<meta name="twitter:title" content="' . h($ogT) . '" />';
    $o[] = '<meta name="twitter:description" content="' . h($ogD) . '" />';
    $o[] = '<meta name="twitter:image" content="' . h($img) . '" />';
    echo '  ' . implode("\n  ", $o) . "\n";
}

/* ---- JSON-LD entity graph ------------------------------------------------ */

function stf_website_node()
{
    return array(
        '@type'      => 'WebSite',
        '@id'        => STF_WEBSITE_ID,
        'url'        => STF_SITE . '/',
        'name'       => 'Surviving the Feds',
        'inLanguage' => 'en-US',
        'publisher'  => array('@id' => STF_ORG_ID),
    );
}

function stf_org_node()
{
    return array(
        '@type'       => 'Organization',
        '@id'         => STF_ORG_ID,
        'name'        => 'Surviving the Feds',
        'url'         => STF_SITE . '/',
        'slogan'      => 'Knowledge + Strength = Freedom',
        'description' => 'Real-world knowledge about the federal criminal system, from someone who served 20 years in federal prison. Free guides, books, and resources for federal defendants and their families.',
        'logo'        => array(
            '@type'  => 'ImageObject',
            'url'    => STF_SITE . '/assets/img/logo-silver.png',
            'width'  => 228,
            'height' => 228,
        ),
        'founder'     => array('@id' => STF_PERSON_ID),
    );
}

function stf_person_node()
{
    return array(
        '@type'       => 'Person',
        '@id'         => STF_PERSON_ID,
        'name'        => 'Bilal Khan',
        'url'         => STF_SITE . '/about.php',
        'image'       => STF_SITE . '/assets/img/bilal-khan.jpg',
        'description' => 'Author and federal system educator who served 20 years in federal prison. Writes on pretrial procedure, sentencing, and post-conviction relief for defendants and their families.',
        'knowsAbout'  => array(
            'Federal sentencing guidelines',
            '28 U.S.C. § 2255 post-conviction relief',
            'First Step Act time credits',
            'Federal Bureau of Prisons designation',
            'Federal pretrial detention',
        ),
        'sameAs'      => array(
            'https://www.amazon.com/stores/author/B0BT42HHBS',
        ),
    );
}

/** BreadcrumbList from [[name, path], ...]; the last item is the current page. */
function stf_breadcrumbs(array $items)
{
    $list = array();
    foreach (array_values($items) as $i => $it) {
        $list[] = array(
            '@type'    => 'ListItem',
            'position' => $i + 1,
            'name'     => $it[0],
            'item'     => stf_url($it[1]),
        );
    }
    return array('@type' => 'BreadcrumbList', 'itemListElement' => $list);
}

/** Print one JSON-LD <script> holding an @graph. JSON_HEX_TAG keeps "</script>" out. */
function stf_jsonld(array $graph)
{
    $json = json_encode(
        array('@context' => 'https://schema.org', '@graph' => array_values($graph)),
        JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_HEX_TAG | JSON_HEX_AMP
    );
    echo "  <script type=\"application/ld+json\">\n" . $json . "\n  </script>\n";
}
