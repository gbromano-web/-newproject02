# RND Athlete — Website

Official website for **RND Athlete**: research-driven performance gear for runners and hybrid athletes.

This repository holds the brand's website blueprint and the first production component, the homepage hero, built with HTML and Tailwind CSS in the black-and-white palette of the RND Athlete logo.

## What's inside

| Path | What it is |
| --- | --- |
| `index.html` | Homepage hero, production version (uses compiled CSS and self-hosted fonts) |
| `dist/styles.css` | Compiled, minified Tailwind CSS. Committed so the site runs without a build |
| `src/input.css` | Tailwind source: font faces, Tailwind layers, hero effects |
| `tailwind.config.js` | Brand tokens: colours, fonts, animations |
| `assets/brand/` | Logo banner and emblem (low resolution, see "Before launch") |
| `assets/fonts/` | Archivo, Inter and JetBrains Mono (SIL Open Font License) |
| `content/` | Markdown source for Journal articles and About/Contact/Privacy/Terms |
| `scripts/build.py` | Generates pages, `sitemap.xml`, `robots.txt`, `ads.txt` and `404.html` from `content/` |
| `.nojekyll` | Stops GitHub Pages turning source markdown into duplicate public pages |
| `assets/img/hero-poster.jpg` | Placeholder hero still cropped from the brand banner |

## Brand tokens

| Token | Hex | Use |
| --- | --- | --- |
| `ink` | `#000000` | Background (logo black) |
| `carbon` | `#111111` | Cards, nav |
| `graphite` | `#262626` | Borders |
| `steel` | `#5C5C5C` | Disabled |
| `smoke` | `#A3A3A3` | Secondary text |
| `chalk` | `#E6E6E6` | White-button hover |
| `white` | `#FFFFFF` | Headlines, primary actions (logo white) |
| `signal` | `#FF3B30` | Errors and low stock only |

Display type is **Archivo Black Italic** (closest free match to the wordmark), body is **Inter**, data is **JetBrains Mono**.

## Run it locally

Open `index.html` in a browser. No build is needed, because `dist/styles.css` is committed.

To change styles:

```bash
npm install
npm run dev      # rebuilds dist/styles.css on every save
npm run build    # minified production build
npm run serve    # local server at http://localhost:3000
```

Run `npm run build` and commit `dist/styles.css` after any change to classes, `src/input.css` or `tailwind.config.js`.

## Adding a Journal article

1. Write a markdown file in `content/journal/<category>/<slug>.md` with front matter:

   ```
   ---
   title: Article title
   description: One-sentence summary for Google (under 160 characters)
   date: 2026-10-21
   category: Marathon Training
   ---
   ```

2. Run `python3 scripts/build.py` (needs `pip install markdown`), then `npm run build`.
3. Commit everything. The article, Journal index and `sitemap.xml` update automatically.

About, Contact, Privacy and Terms live in `content/pages/` and build the same way.

## Upload to GitHub

1. Create an empty repository on GitHub (no README, licence or .gitignore), for example `rnd-athlete-website`.
2. From this folder, run:

   ```bash
   git remote add origin https://github.com/<your-username>/rnd-athlete-website.git
   git branch -M main
   git push -u origin main
   ```

3. The site is published by GitHub Pages from the `main` branch (root) at https://rndathletes.com. Every push to `main` goes live within a few minutes.

## Before launch

- [ ] Replace `assets/brand/` files with the logo as SVG (emblem and wordmark).
- [ ] Replace `assets/img/hero-poster.jpg` with a full-resolution black-and-white hero still, and add `assets/video/hero-loop.webm` and `.mp4` (6–10 s, under 3 MB).
- [ ] Replace placeholder stats, product specs, prices and testimonials with real, verified content.
- [ ] Build the remaining store sections from the website blueprint doc: category grid, bestsellers, social proof, Run Club.

## Licence

© 2026 RND Athlete. All rights reserved. Brand assets and photography may not be reused without permission. Bundled fonts are under the SIL Open Font License.
