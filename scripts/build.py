#!/usr/bin/env python3
"""Build RND Athletes content pages from markdown.

Usage:  python3 scripts/build.py   (then: npm run build)

- content/journal/<category>/<slug>.md  ->  journal/<category>/<slug>/index.html
- content/pages/<slug>.md               ->  <slug>/index.html
- Also writes journal/index.html, sitemap.xml and robots.txt.

Front matter (between --- lines): title, description, date or updated, category.
Requires: pip install markdown
"""
import datetime
import html
import json
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://rndathletes.com"
BRAND = "RND Athletes"
ADSENSE_PUB = "ca-pub-6723626743879731"
AUTHOR = "RND Athletes Team"

# Pages that already exist as hand-built HTML (included in the sitemap).
STATIC_PAGES = ["/", "/shop/running/", "/lab/"]


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    return meta, body


def md_to_html(body):
    out = markdown.markdown(body, extensions=["tables", "attr_list", "sane_lists"])
    # Wide tables scroll sideways on phones instead of widening the page.
    out = out.replace("<table>", '<div class="-mx-4 overflow-x-auto px-4 sm:mx-0 sm:px-0"><table class="min-w-[32rem]">')
    return out.replace("</table>", "</table></div>")


def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def header(active=""):
    def link(href, label, key):
        cls = "text-white" if key == active else "text-smoke transition hover:text-white"
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}" class="{cls}"{cur}>{label}</a>'

    return f"""  <header class="border-b border-graphite">
    <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <a href="/" class="flex items-center gap-3" aria-label="{BRAND} home">
        <img src="/assets/brand/rnd-emblem-lowres.png" alt="" width="36" height="36" class="h-9 w-9 rounded-full" />
        <span class="hidden font-display text-lg font-black uppercase italic tracking-tight sm:inline">RND Athletes</span>
      </a>
      <nav class="flex items-center gap-5 whitespace-nowrap font-display text-sm font-extrabold uppercase italic tracking-wide sm:gap-6">
        {link('/journal/', 'Journal', 'journal')}
        {link('/about/', 'About', 'about')}
      </nav>
    </div>
  </header>"""


FOOTER = f"""  <footer class="border-t border-graphite">
    <div class="mx-auto flex max-w-7xl flex-col gap-4 px-4 py-8 text-xs text-smoke sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
      <p>&copy; {datetime.date.today().year} {BRAND}. All rights reserved.</p>
      <nav class="flex flex-wrap gap-x-5 gap-y-2" aria-label="Footer">
        <a href="/journal/" class="hover:text-white">Journal</a>
        <a href="/shop/running/" class="hover:text-white">Shop</a>
        <a href="/lab/" class="hover:text-white">The Lab</a>
        <a href="/about/" class="hover:text-white">About</a>
        <a href="/contact/" class="hover:text-white">Contact</a>
        <a href="/privacy/" class="hover:text-white">Privacy Policy</a>
        <a href="/terms/" class="hover:text-white">Terms of Use</a>
      </nav>
    </div>
  </footer>"""

PROSE = (
    "prose prose-invert prose-lg max-w-none "
    "prose-headings:font-display prose-headings:font-black prose-headings:uppercase prose-headings:italic "
    "prose-headings:tracking-tight prose-h2:mt-14 prose-h2:text-3xl prose-h3:text-xl "
    "prose-a:text-white prose-a:underline-offset-4 hover:prose-a:text-chalk "
    "prose-strong:text-white prose-blockquote:not-italic prose-blockquote:border-l-white "
    "prose-blockquote:bg-carbon prose-blockquote:px-6 prose-blockquote:py-1 prose-blockquote:font-normal "
    "prose-th:text-left prose-th:font-sans prose-th:font-semibold prose-th:normal-case prose-th:not-italic prose-th:tracking-normal "
    "prose-td:align-top prose-table:text-base"
)


def page(title, description, canonical, body, active="", jsonld=None, ads=True, robots=""):
    ld = ""
    if jsonld:
        ld = "\n".join(
            f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in jsonld
        )
    adcode = (f'  <meta name="google-adsense-account" content="{ADSENSE_PUB}" />\n'
              f'  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUB}" crossorigin="anonymous"></script>\n') if ads else ""
    robots_tag = f'  <meta name="robots" content="{robots}" />\n' if robots else ""
    return f"""<!doctype html>
<html lang="en" class="bg-ink">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <link rel="canonical" href="{SITE}{canonical}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:url" content="{SITE}{canonical}" />
  <meta property="og:site_name" content="{BRAND}" />
  <link rel="icon" type="image/png" href="/assets/brand/rnd-emblem-lowres.png" />
  <link rel="stylesheet" href="/dist/styles.css" />
{adcode}{robots_tag}{ld}
</head>
<body class="bg-ink font-sans text-white antialiased">
{header(active)}
{body}
{FOOTER}
</body>
</html>
"""


def write(rel, content):
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")


def build():
    sitemap = [(p, None) for p in STATIC_PAGES]
    articles = []

    # Journal articles
    for md in sorted((ROOT / "content/journal").rglob("*.md")):
        meta, body = parse(md)
        cat_slug = md.parent.name
        slug = md.stem
        url = f"/journal/{cat_slug}/{slug}/"
        date = meta.get("date", datetime.date.today().isoformat())
        category = meta.get("category", cat_slug.replace("-", " ").title())
        title = meta["title"]
        words = len(re.findall(r"\w+", body))
        articles.append(dict(url=url, title=title, description=meta.get("description", ""),
                             date=date, category=category, minutes=max(1, round(words / 230))))
        jsonld = [
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": title,
                "description": meta.get("description", ""),
                "datePublished": date,
                "dateModified": meta.get("updated", date),
                "author": {"@type": "Organization", "name": AUTHOR, "url": f"{SITE}/about/"},
                "publisher": {"@type": "Organization", "name": BRAND, "url": SITE,
                              "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/brand/rnd-emblem-lowres.png"}},
                "mainEntityOfPage": f"{SITE}{url}",
            },
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Journal", "item": f"{SITE}/journal/"},
                    {"@type": "ListItem", "position": 3, "name": title, "item": f"{SITE}{url}"},
                ],
            },
        ]
        content = f"""  <main class="mx-auto max-w-3xl px-4 py-12 sm:px-6 md:py-16">
    <nav class="font-mono text-xs uppercase tracking-[0.18em] text-smoke" aria-label="Breadcrumb">
      <a href="/" class="hover:text-white">Home</a> / <a href="/journal/" class="hover:text-white">Journal</a> / <span>{html.escape(category)}</span>
    </nav>
    <h1 class="mt-5 font-display text-4xl font-black uppercase italic leading-[0.95] tracking-[-0.01em] sm:text-5xl">{html.escape(title)}</h1>
    <p class="mt-5 text-sm text-smoke">By <a href="/about/" class="text-white underline underline-offset-4">{AUTHOR}</a> &middot; Updated <time datetime="{meta.get('updated', date)}">{nice_date(meta.get('updated', date))}</time> &middot; {articles[-1]['minutes']} min read</p>
    <article class="{PROSE} mt-10">
{md_to_html(body)}
    </article>
  </main>"""
        write(f"journal/{cat_slug}/{slug}/index.html",
              page(f"{title} | {BRAND}", meta.get("description", ""), url, content, "journal", jsonld))
        sitemap.append((url, meta.get("updated", date)))

    # Journal index
    articles.sort(key=lambda a: a["date"], reverse=True)
    cards = "\n".join(
        f"""      <li class="border-t border-graphite py-8">
        <p class="font-mono text-xs uppercase tracking-[0.18em] text-smoke">{html.escape(a['category'])} &middot; {a['minutes']} min read</p>
        <h2 class="mt-3 font-display text-2xl font-black uppercase italic leading-tight sm:text-3xl"><a href="{a['url']}" class="hover:text-chalk">{html.escape(a['title'])}</a></h2>
        <p class="mt-3 max-w-2xl text-white/75">{html.escape(a['description'])}</p>
        <a href="{a['url']}" class="mt-4 inline-block font-display text-sm font-extrabold uppercase italic tracking-wide underline underline-offset-4">Read the guide &rarr;</a>
      </li>"""
        for a in articles
    )
    index = f"""  <main class="mx-auto max-w-4xl px-4 py-14 sm:px-6 md:py-20">
    <p class="font-mono text-xs uppercase tracking-[0.22em] text-smoke"><span class="mr-2 inline-block h-1.5 w-1.5 -translate-y-px rounded-full bg-white align-middle"></span>The RND Journal</p>
    <h1 class="mt-4 font-display text-5xl font-black uppercase italic leading-[0.92] tracking-[-0.01em] sm:text-6xl">Train smarter.<br />Race faster.</h1>
    <p class="mt-6 max-w-2xl text-lg leading-relaxed text-white/80">Free training plans, pace charts and race-preparation guides for half marathon and marathon runners.</p>
    <ul class="mt-12">
{cards}
    </ul>
  </main>"""
    write("journal/index.html",
          page(f"The Journal: Marathon Training Guides | {BRAND}",
               "Free marathon and half marathon training plans, pace charts and race-preparation guides from RND Athletes.",
               "/journal/", index, "journal"))
    sitemap.append(("/journal/", articles[0]["date"] if articles else None))

    # Static content pages
    for md in sorted((ROOT / "content/pages").glob("*.md")):
        meta, body = parse(md)
        url = f"/{md.stem}/"
        updated = meta.get("updated")
        upd = f'<p class="mt-4 text-sm text-smoke">Last updated {nice_date(updated)}</p>' if updated else ""
        content = f"""  <main class="mx-auto max-w-3xl px-4 py-12 sm:px-6 md:py-16">
    <h1 class="font-display text-4xl font-black uppercase italic leading-[0.95] sm:text-5xl">{html.escape(meta['title'])}</h1>
    {upd}
    <div class="{PROSE} mt-10">
{md_to_html(body)}
    </div>
  </main>"""
        write(f"{md.stem}/index.html", page(f"{meta['title']} | {BRAND}", meta.get("description", ""), url, content, "about" if md.stem == "about" else ""))
        sitemap.append((url, updated))

    # sitemap.xml + robots.txt
    urls = "\n".join(
        f"  <url><loc>{SITE}{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>" for u, d in sitemap
    )
    write("sitemap.xml",
          f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    write("ads.txt", "google.com, " + ADSENSE_PUB.replace("ca-", "") + ", DIRECT, f08c47fec0942fa0\n")
    write("robots.txt",
          "User-agent: *\nAllow: /\n"
          "Disallow: /content/\nDisallow: /scripts/\nDisallow: /src/\nDisallow: /docs/\n"
          "Disallow: /README.md\nDisallow: /package.json\nDisallow: /package-lock.json\nDisallow: /tailwind.config.js\n"
          f"\nSitemap: {SITE}/sitemap.xml\n")
    # 404 page: no ads (not allowed on error pages), not indexed
    nf = """  <main class="mx-auto max-w-3xl px-4 py-20 sm:px-6 md:py-28">
    <p class="font-mono text-xs uppercase tracking-[0.22em] text-smoke">Error 404</p>
    <h1 class="mt-4 font-display text-5xl font-black uppercase italic leading-[0.92] sm:text-6xl">Wrong turn.</h1>
    <p class="mt-6 text-lg text-white/80">This page doesn't exist or has moved. Try the Journal for training plans, pace charts and race guides.</p>
    <div class="mt-8 flex flex-col gap-3 sm:flex-row">
      <a href="/journal/" class="inline-flex h-14 items-center justify-center rounded-sm bg-white px-8 font-display text-base font-extrabold uppercase italic tracking-wide text-ink transition hover:bg-chalk">Go to the Journal</a>
      <a href="/" class="inline-flex h-14 items-center justify-center rounded-sm border-2 border-white px-8 font-display text-base font-extrabold uppercase italic tracking-wide transition hover:bg-white hover:text-ink">Back to home</a>
    </div>
  </main>"""
    write("404.html", page(f"Page not found | {BRAND}", "Page not found.", "/404.html", nf, ads=False, robots="noindex"))
    print(f"Built {len(articles)} articles, {len(sitemap)} sitemap URLs")


if __name__ == "__main__":
    build()
