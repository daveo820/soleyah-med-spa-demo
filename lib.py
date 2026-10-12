# Shared static page helpers for LuminArch concept demos (copied into each repo). Each build.py sets CFG then calls page().
import json, os, re
CFG = {}
def img(src, alt, sizes='100vw', eager=False, w=None, h=None, cls=''):
    small = src.replace('.webp', '-800.webp')
    srcset = f' srcset="img/{small} 800w, img/{src} 1600w" sizes="{sizes}"' if os.path.exists('img/' + small) else ''
    if w is None and os.path.exists('img/' + src):
        from PIL import Image
        w, h = Image.open('img/' + src).size
    dims = f' width="{w}" height="{h}"' if w else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="img/{src}"{srcset} alt="{alt}"{dims}{load}' + (f' class="{cls}"' if cls else '') + '>'
def bc(*n):
    B = CFG['base']
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": a, "item": B + b} for i, (a, b) in enumerate(n)]}
def page(fn, t, d, body, ld=None, extra_ld=()):
    assert 50 <= len(t) <= 62, (fn, len(t), t)
    assert 130 <= len(d) <= 165, (fn, len(d), d)
    for txt in (t, d):
        assert not re.search(r'[\u2013\u2014]| - ', txt), ('dash', txt)
    B = CFG['base']
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in CFG['nav'])
    url = B + ('' if fn == 'index.html' else fn)
    lds = [ld or CFG['org']] + list(extra_ld)
    ldhtml = ''.join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in lds)
    head = f'''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{CFG['name']} (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{B}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{B}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="{CFG['theme']}">
{CFG['fonthead']}
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="{CFG['icon']}">
<script>document.documentElement.classList.replace('no-js','js-ready')</script>{ldhtml}</head><body class="pg-{fn[:-5]}">
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. {CFG['bar']}</div>
<header class="top"><div class="wrap nav">{CFG['mark']}
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul>{CFG['cta']}</div></header><main id="main">'''
    open(fn, 'w').write(head + body + '</main>' + CFG['foot'] + '<script src="js/main.js" defer></script></body></html>')
def finish(pages):
    B = CFG['base']
    open('robots.txt', 'w').write('User-agent: *\nDisallow: /\n# Concept demo by LuminArch. Not for indexing.\n')
    open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{B}{"" if p=="index.html" else p}</loc></url>\n' for p in pages) + '</urlset>\n')
    open('vercel.json', 'w').write(json.dumps({"cleanUrls": False, "headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}, {"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]}, indent=1))
    open('.nojekyll', 'w').write('')
