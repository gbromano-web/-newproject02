# RND Athlete — Website Blueprint

Last updated: 20 Oct 2026

## Brand system

The palette comes straight from the RND Athlete logo: pure black, pure white, and black-and-white photography, with no brand accent colour. Hierarchy comes from contrast, inversion (white on black, black on white) and type weight rather than hue.

| Token | Hex | Use |
| --- | --- | --- |
| `ink` (Logo Black) | #000000 | Page background, hero, footer |
| `carbon` | #111111 | Cards, nav bar, raised surfaces |
| `graphite` | #262626 | Borders, dividers |
| `steel` | #5C5C5C | Disabled and inactive states |
| `smoke` | #A3A3A3 | Secondary text, captions, spec labels, eyebrows |
| `chalk` | #E6E6E6 | Hover state on white buttons and white surfaces |
| `white` (Logo White) | #FFFFFF | Headlines, primary buttons, badges, key stats |
| `signal` (functional only) | #FF3B30 | Form errors and low-stock alerts; never decorative |

**Type**

- Display: Archivo, 900 weight, italic, uppercase. It's the closest free match to the wide, heavy italic RND ATHLETE wordmark. Used for H1–H3, buttons and big stats.
- Body: Inter, 400/500/600. Body copy 16–18px, line height 1.6.
- Data: JetBrains Mono, 500. Used for specs, weights, drop numbers and timers.

**Logo use**

- Primary mark: the circular RND emblem, white on black. Used in the header (40px), favicon and footer.
- Wordmark: RND ATHLETE in white, used in the footer sign-off and on packaging-style banners.
- Clear space equals the height of the emblem's "R" on all sides. Never recolour, outline or place the mark on a busy photo without a dark scrim.
- Request the logo as SVG from the designer; the banner file is too low-resolution for production.

**Imagery** (taken from the logo banner)

- Black-and-white photography only, high contrast, crushed blacks, visible grain.
- Real training across disciplines: road running, trail and mountain, strength work, and HYROX-style hybrid racing.
- Athletes wear the RND mark visibly. Panels are split by diagonal cuts, as in the banner.

**Rules**

- Primary action = solid white button with black text. Secondary = 2px white outline, which fills white on hover. One primary per viewport.
- Proof elements (badges, stats, ratings) use white type or inverted white tags, never a colour.
- Colour photography never appears on brand surfaces; product colourways on PDPs are the only exception.
- Contrast: white on `ink` and `ink` on white both pass WCAG AAA. `smoke` on `ink` passes AA for body text.
- Motion: 200ms ease-out on hovers, 600ms reveal on scroll, a 4–8px forward nudge on CTA arrows. Respect `prefers-reduced-motion`.
- Corners: 2px radius on buttons and cards.
- Signature graphic: the banner's diagonal panel cut (about 12°), used on dividers, badge edges and image masks.

## Section 1: Hero and above the fold

The hero sells one idea in under three seconds: RND gear is engineered, tested, and built to make you faster. Recommended H1 is option A; B and C are A/B test challengers.

**Hero headline (H1) options**

1. **A — ENGINEERED FOR THE LAST MILE.** (Recommended. Speaks to endurance athletes, where gear fails late in a race.)
2. **B — EVERY SECOND IS RESEARCHED.** (Leans into the R&D name; strongest for the "Explore the Lab" story.)
3. **C — RUN FASTER. RECOVER SOONER. REPEAT.** (Direct-response, benefit-stacked; best for paid traffic landing pages.)

**Eyebrow (above H1)**: `RND LAB // SERIES 01 — NOW LIVE` in JetBrains Mono, smoke grey, 12px, tracked +0.2em.

**Subheadline**

Performance running gear developed in the lab and proven on the road. Lighter fabrics, sharper fit, faster drying, and every piece tested over thousands of real training kilometres before it reaches you.

**CTAs**

- Primary: **Shop Running Gear →** (solid white fill, black italic Archivo text, 56px tall, arrow nudges 6px on hover). Links to `/shop/running`.
- Secondary: **Explore the Lab** (2px white outline, transparent fill, fills white with black text on hover). Links to `/lab`.
- Microcopy under buttons (smoke, 13px): Free shipping over $100 · 60-day test run returns · Ships in 24h.

**Proof strip (bottom of hero)**: three stats in Archivo Black Italic with large white numbers: **142 g** lightest race singlet · **2.1M km** athlete-tested · **4.9/5** from 12,000+ runners. Replace the figures with your real numbers before launch.

**Visual and UI directives**

- Background: black-and-white, matching the logo banner. A 6–10 second seamless video loop, shot at 120fps and played at 50% speed. A single runner, side profile, crosses frame left to right at dawn on wet black asphalt. Rim light from behind picks out sweat and fabric texture; the RND mark on the singlet catches the light.
- Grade: full monochrome with crushed blacks, hard contrast and visible grain, like the banner photography. Alternate cuts can show trail, strength and HYROX training.
- Overlay: left-to-right gradient from `ink` at 90% to transparent at 60% width, so the headline sits on near-solid black. A faint 4% film grain and thin horizontal speed lines drift right slowly.
- Layout: copy left-aligned in the left 55% on desktop; stacked on mobile with the video cropped to the runner's torso and legs.
- Fallback: a still poster frame (WebP, under 200KB) loads first; the video (MP4/WebM, under 3MB) lazy-loads and is replaced by the still when `prefers-reduced-motion` is on or on save-data connections.
- Height: 100svh on mobile, 90vh on desktop, so the proof strip and the top of the category grid peek above the fold.
- Signature detail: a slanted 12° white hairline (50% opacity) sweeps across the bottom edge, separating hero from the next section.

## Section 2: Homepage layout and copy

Below the hero, the page runs in five bands that move a visitor from browsing (categories), to belief (tech), to buying (bestsellers), to trust (proof), to loyalty (mission). Bands alternate `ink` and `carbon` backgrounds, split by the 12° slant.

### 2.1 Category showcase grid

**Section header**: CHOOSE YOUR TERRAIN. Sub: Four lines of gear, one standard: tested until it stops failing.

**Layout**: desktop is a 2×2 asymmetric bento (Road Running spans two rows on the left); tablet 2×2 even; mobile is a horizontal snap-scroll of 85%-width cards. Each card is a full-bleed photo with a bottom gradient, title in Archivo Black Italic 36px, one-line hook, and an underlined white "Shop →" link. Hover: image scales 1.04, card lifts, arrow nudges.

| Card | Hook copy | Link |
| --- | --- | --- |
| ROAD RUNNING | Built for tempo days, long runs and race-day PRs. | /shop/road |
| TRAIL GEAR | Grip, protection and pockets for when the path ends. | /shop/trail |
| ELITE APPAREL | Race-cut singlets, split shorts and second-skin layers. | /shop/elite |
| RECOVERY & ACCESSORIES | Compression, socks, hydration — the work after the work. | /shop/recovery |

### 2.2 Innovation section: "Inside the Lab"

**Header**: BUILT IN THE LAB. BROKEN IN ON THE ROAD. Sub: Every RND product starts as a problem a runner told us about, and ships only when the data says it's solved.

**Layout**: sticky left column holds a large rotating product render (garment exploded into layers on scroll). Right column scrolls through four tech blocks, each with a mono-font label, a headline, 2 lines of copy and one large white stat.

| Tech | Headline | Copy | Stat |
| --- | --- | --- | --- |
| `AERO-KNIT™` | Weighs almost nothing. | A micro-perforated knit that cuts weight without cutting durability. | 38% lighter than standard poly |
| `HYDRO-SHIFT™` | Dry before the next mile. | Dual-layer fabric pulls sweat outward and spreads it to evaporate fast. | Dries 2× faster |
| `KINETIC FIT` | Moves the way you move. | Panels mapped from 3D stride scans, so seams sit where nothing rubs. | 0 seams on high-friction zones |
| `RE-FORM` foam | Return on every stride. | A nitrogen-infused midsole compound tuned for energy return and long-run comfort. | 82% energy return |

Trademark names and stats are placeholders; confirm with product before launch. Closing CTA: **Explore the Lab →** (underlined white text link).

### 2.3 Featured bestsellers carousel

**Header**: PROVEN BY THE PACK. Sub: The gear our runners re-order most. Right side: "View all bestsellers →".

**Layout**: 4 cards visible on desktop, 2.2 on tablet, 1.3 on mobile (peek signals scroll). Arrow buttons on desktop, swipe plus a thin white progress bar on touch.

**Product card anatomy (top to bottom)**

1. Image area, 4:5 ratio, `carbon` background, product shot on a neutral surface; a second on-body image swaps in on hover.
2. Badge top-left (one per card max): slanted white tag, black text, mono font.
3. Wishlist heart top-right (outline white, fills white when saved).
4. Quick-add bar slides up on hover with size chips (desktop); mobile shows a "+" button that opens a size sheet.
5. Product name (Inter 600, 16px, white), then category line (smoke, 13px).
6. Colour swatches (max 4 dots + "+2").
7. Price in JetBrains Mono: `$000` white; on sale, the old price struck through in smoke and the new price in white beside a black-on-white SALE tag.
8. Rating: 5 small stars + review count (e.g. ★ 4.8 · 1,204).

**Badge set**: LAB TESTED · MARATHON APPROVED · NEW DROP · ATHLETE PICK · ULTRA-LIGHT. Low stock uses the `signal` red tag: ONLY 6 LEFT.

**Placeholder products**

| Product | Category | Price | Badge |
| --- | --- | --- | --- |
| VELOCITY RACE SINGLET | Elite Apparel | $65 | ULTRA-LIGHT |
| APEX 5" SPLIT SHORT | Road Running | $70 | MARATHON APPROVED |
| RIDGELINE TRAIL TEE | Trail Gear | $55 | LAB TESTED |
| PACE-1 RUNNING SHOE | Road Running | $180 | NEW DROP |
| COMPRESS PRO CALF SLEEVES | Recovery | $40 | ATHLETE PICK |

### 2.4 Social proof and athlete testimonials

**Header**: THE NUMBERS DON'T LIE. NEITHER DO OUR RUNNERS.

**Metrics band** (four counters that tick up on scroll, white Archivo numbers, smoke labels): **2.1M** km logged in RND gear · **48,000** Run Club members · **312** podium finishes this season · **4.9★** average rating. Replace with real data at launch.

**Review cards** (3-up on desktop, swipe on mobile). Each card: runner photo (circle, 48px), name, a verified-runner tick, their discipline and PR in mono, star rating, the product reviewed (linked), and a 2–3 line quote.

- "Ran Berlin in the Velocity Singlet. Zero chafe at 42K and it was still dry at the finish." — Maya R., Marathon · PR 2:58:41
- "The Ridgeline tee survived 100 miles of mud and still looks new. That's the review." — Jonas K., Ultra Trail · 100-mile finisher
- "Finally, split shorts with pockets that actually hold gels without bouncing." — Dev P., Half Marathon · PR 1:21:07

Testimonials are illustrative; replace with real, consented reviews before launch. Below the cards: a strip of 5 partner race or club logos in white at 40% opacity, and a link "Read 12,000+ reviews →".

### 2.5 Brand story: "The RND Mission"

**Layout**: full-width band. Left: a black-and-white image of a runner on a treadmill wired with sensors, thin white data overlays. Right: copy, a signature line, and a CTA.

**Header**: R&D IS IN OUR NAME. RUNNING IS IN OUR BLOOD.

**Copy**:

RND started with a simple frustration: gear that looked fast but failed at kilometre thirty. So we built a lab. We put runners on force plates and in heat chambers, logged their sweat, scanned their stride, and listened to every complaint.

Every RND piece is designed with athletes, tested by athletes, and revised until it disappears on the run. No hype, no shortcuts. Just gear that lets you think about the finish line instead of your kit.

**Signature line** (mono, white): RESEARCH. DEVELOP. RUN.

**CTA**: **Read Our Story →** (secondary outline button) linking to `/about`.

## Section 3: Product detail page (PDP) blueprint

The example PDP is the PACE-1 road shoe. The page answers the buyer's three questions in order: will it make me faster, will it fit, and can I trust it.

**Layout**

- Desktop: 60/40 split. Left is a sticky gallery (vertical thumbnails plus a large image, 7–9 shots including sole, heel, on-foot in motion, and a 360° spin). Right is the buy box, which scrolls.
- Mobile: full-width swipe gallery with dot indicators, then the buy box. A sticky bottom bar appears once "Add to Cart" scrolls off screen, showing price, selected size and the button.
- Breadcrumb above: Home / Road Running / Shoes / PACE-1.

**Buy box, top to bottom**

1. Badge row: NEW DROP · LAB TESTED.
2. **Product title (H1)**: PACE-1
3. **Subtitle**: Daily trainer to race-day rocket. Engineered for tempo, built for 42K.
4. Rating: ★ 4.8 (1,204 reviews) — links to the reviews section.
5. Price: **$180** in JetBrains Mono. Below it: or 4 payments of $45 (BNPL widget).
6. Colourway selector: image swatches with name on hover (Black / White, White / Black, Triple Black).
7. Size selector (rules below).
8. Primary CTA: **Add to Cart** (full-width white with black text, 56px). Secondary: heart icon "Save".
9. Delivery line with truck icon: Order in the next 3h 12m for delivery by Thu, Oct 23.
10. Service row: Free shipping over $100 · 60-day test run returns · 2-year warranty.

**Hook copy (under buy box)**

The PACE-1 is built for runners who want one shoe for everything. A RE-FORM midsole returns 82% of your energy, and a carbon-infused plate keeps you rolling forward when your legs start to fade. It weighs 218g in a men's US 9.

### Tech specs and material breakdown

Shown as an accordion (open by default on desktop) with a spec table and a layered exploded diagram of the shoe.

| Spec | Value |
| --- | --- |
| Weight | 218 g (men's US 9) / 186 g (women's US 7) |
| Heel-to-toe drop | 8 mm |
| Stack height | 38 mm heel / 30 mm forefoot |
| Midsole | RE-FORM nitrogen-infused foam, 82% energy return |
| Plate | Carbon-infused nylon propulsion plate |
| Upper | AERO-KNIT™ engineered mesh, 38% lighter than standard |
| Outsole | Hi-Grip rubber on forefoot and heel strike zones |
| Best for | Tempo runs, long runs, 10K to marathon racing |
| Expected life | 650–800 km |

All figures are placeholders until product signs off.

**Feature bullets (icon + bold lead + one line)**

- **Energy return**: RE-FORM foam gives back more of every stride so late-race kilometres feel like early ones.
- **Forward roll**: the propulsion plate guides your foot through toe-off for a smoother, faster transition.
- **Breathable lock-down**: AERO-KNIT™ wraps the midfoot without hot spots, even at 30°C.
- **Grip in the wet**: rubber placed only where you strike, keeping weight down without losing traction.
- **Reflective detailing**: 360° reflective hits for dawn and dusk runs.

### Fit and sizing guide interface rules

1. Size chips in a 5-column grid, 48×48px minimum touch target. States: available (white outline), selected (white fill, black text), low stock (red signal dot plus "2 left" on hover), sold out (struck through, `graphite` text, still tappable to open "Notify me").
2. A men's/women's toggle and a US/UK/EU unit toggle sit above the grid. The chosen unit is remembered per visitor.
3. A **Fit indicator** sits above the chips: a 5-point slider showing "Runs small · True to size · Runs large", with the marker set from review data (e.g. 78% say true to size).
4. Fit note line: Snug, race-ready fit. If you're between sizes or have wide feet, go up half a size.
5. **Find My Size** link opens a side drawer (bottom sheet on mobile) with three tabs:
    - Size chart: foot length in cm and in, mapped to US/UK/EU.
    - Fit finder quiz: current shoe brand and size, foot width, preferred fit; returns a recommended size with a confidence score.
    - How to measure: a 3-step illustration (heel to wall, mark longest toe, measure).
6. Clicking Add to Cart without a size shakes the size grid, outlines it in signal red, and scrolls it into view. No modal.
7. Apparel PDPs swap the shoe chart for a body chart (chest, waist, hip, inseam) and add a "Model is 183 cm and wears M" line under the gallery.

### "Tested in the Elements" trust badges

A horizontal strip of six badges directly under the spec accordion. Each badge is a monochrome line icon in a slanted white frame with a mono label and a one-line test result on hover or tap.

| Badge | Test result (placeholder) |
| --- | --- |
| HEAT TESTED | 2 hours at 35°C and 60% humidity in the climate chamber. |
| RAIN READY | Outsole grip held on wet asphalt and painted crossings. |
| 1,000 KM TESTED | Athlete panel logged 1,000 km per pair before sign-off. |
| COLD PROOF | Midsole stays responsive down to −5°C. |
| NIGHT VISIBLE | Reflective hits visible from 150 m in headlights. |
| ATHLETE APPROVED | Rated 4.7/5 or higher by 40 test runners before launch. |

**Below the badges, in order**: "Complete the kit" cross-sell row (singlet, shorts, socks); reviews with fit and comfort sub-scores, filterable by distance and foot type; a Q&A block; and "Recently viewed".

## Section 4: RND Run Club and Strava integration

The Run Club band trades membership perks for an email, then deepens engagement through Strava. It sits on the homepage between Social Proof and the Mission band, and as a full page at `/run-club`.

**Layout**

- Desktop: two columns on an `ink` background with a faint topographic route line in white at 8% opacity, over a dimmed black-and-white group-run photo. Left: copy, perks and the form. Right: a live "club leaderboard" card showing this week's top 5 members by distance, pulled from the Strava club.
- Mobile: copy, then form, then a collapsed leaderboard with "See this week's leaders".

**Copy**

- Eyebrow (mono, smoke): RND RUN CLUB // 48,000 MEMBERS
- Headline: RUN WITH THE PACK.
- Sub: Join free and turn every kilometre into progress: training plans from our athletes, early access to lab drops, and monthly challenges with real prizes.

**Perks (4 icon bullets)**

- **Early access**: shop new drops 48 hours before everyone else.
- **Free training plans**: 5K to marathon plans written by RND athletes and coaches.
- **Monthly challenges**: hit the target distance, earn badges, win kit.
- **10% off your first order**, sent the moment you join.

**Email capture form**

1. Fields inline on desktop, stacked on mobile: First name · Email · "My main distance" select (5K / 10K / Half / Marathon / Ultra / Trail). The distance tag personalises the welcome email flow.
2. Button: **Join the Club →** (white fill, black text).
3. Consent line (smoke, 12px): By joining you agree to receive RND emails. Unsubscribe anytime. See our Privacy Policy. Use an unticked marketing checkbox where local law requires it (GDPR, UAE PDPL).
4. Success state replaces the form: YOU'RE IN, [NAME]. Check your inbox for your 10% code. Then a second step appears: Connect Strava to join this month's challenge.
5. Errors appear inline under the field in signal red, never as a pop-up.

**Strava integration**

- **Connect with Strava** button using Strava's official orange button asset and "Powered by Strava" attribution, as their brand guidelines require.
- OAuth flow requesting `read` and `activity:read` scopes only. Explain on the button's tooltip: We only read your runs, never post on your behalf.
- Once connected, members are added to the public RND Strava Club and auto-entered into the current challenge.
- **Challenge card** on the page: OCTOBER: RUN 100K. A progress ring fills white as their kilometres sync, with "62.4 / 100 km — 9 days left" in mono.
- **Leaderboard card**: rank, avatar, first name and last initial, weekly km, and a small RND emblem for Club members wearing a registered RND product.
- **Account dashboard** (`/account/run-club`): lifetime km, badges earned, challenge history, and shoe mileage tracking that prompts a replacement at 650 km (a natural re-purchase trigger).

**Events strip (below the band)**: three cards for upcoming group runs: city, date, distance, pace groups, and an "RSVP" button. Example: DUBAI · SAT 6:00 AM · 10K · Kite Beach · Pace groups 4:30–6:30 /km.

**Measurement**: track form-view to submit rate (target 8–12%), Strava connect rate after signup (target 25%+), and 90-day repeat-purchase rate of Club members against non-members.

## Section 5: Navigation and footer architecture

The header carries six top-level items so the whole menu reads in one glance; depth lives in mega-menus. The footer is the site's index, with legal and trust detail at the bottom.

### Header

**Announcement bar** (32px, white fill, black text, rotates every 5s): FREE SHIPPING OVER $100 · JOIN RUN CLUB, GET 10% OFF · PACE-1 NOW LIVE →

**Main bar** (72px desktop, 60px mobile; `ink` at 80% with backdrop blur once scrolled; hides on scroll down and returns on scroll up):

- Left: the circular RND emblem (40px, white), linking home.
- Centre: the six menu items below.
- Right: Search (opens a full-width overlay with trending searches), Account, Wishlist, Cart with a white count bubble (black number).

| Menu item | Mega-menu columns | Featured tile |
| --- | --- | --- |
| NEW & FEATURED | New Drops · Bestsellers · Lab Exclusives · Gift Guide | Latest drop image |
| MEN | Shoes · Tops · Shorts & Tights · Jackets · Accessories | Men's race kit |
| WOMEN | Shoes · Sports Bras · Tops · Shorts & Tights · Jackets · Accessories | Women's race kit |
| SHOP BY RUN | Road · Trail · Race Day · Track · Recovery | Trail collection |
| THE LAB | Our Tech · Testing Process · Materials · Sustainability · Journal | Lab video still |
| RUN CLUB | Join · Challenges · Events · Training Plans · Ambassadors | Current challenge |

**Mobile**: hamburger on the left opens a full-height drawer. Top-level items are accordion rows, followed by Account and Help links, and a Run Club card at the bottom. Cart stays visible in the bar.

### Footer

**Top band**: newsletter repeat in one line: GET LAB DROPS FIRST. Email field plus Join button.

**Link columns** (4 on desktop, accordions on mobile)

| Shop | Help | The Lab | Company |
| --- | --- | --- | --- |
| Men | Order Status | Our Technology | About RND |
| Women | Shipping & Delivery | Testing Process | Athletes & Ambassadors |
| Road Running | Returns & 60-Day Test Run | Materials | Careers |
| Trail Gear | Size Guide | Sustainability | Press |
| Recovery & Accessories | Warranty | Journal | Store Locator |
| Gift Cards | Contact Us / FAQ | Training Plans | Affiliates & Partners |

**Social icons** (white line icons at 24px, inverting to a white circle on hover, each labelled for screen readers): Instagram · TikTok · Strava · YouTube · X · Facebook.

**Trust row**: payment icons (Visa, Mastercard, Amex, Apple Pay, Google Pay, PayPal, Tabby/Klarna), a secure-checkout lock, and a country/currency selector (e.g. UAE · AED).

**Legal bar** (smoke, 12px)

- © 2026 RND Athlete. All rights reserved.
- Privacy Policy · Terms of Service · Cookie Settings · Accessibility Statement · Sitemap
- Registered company name, trade licence number and address, as local law requires (a placeholder until legal supplies it).

**Sign-off**: the RND ATHLETE wordmark in oversized Archivo Black Italic at 8% white opacity, spanning the full footer width.

## Section 6: HTML + Tailwind hero component

The hero is implemented in this repository: `index.html` is the production version (compiled Tailwind in `dist/styles.css`, self-hosted fonts in `assets/fonts/`), and `prototype/hero-cdn.html` is the single-file version that runs from the Tailwind CDN with no build step.

- Brand tokens live in `tailwind.config.js` (`ink`, `carbon`, `graphite`, `steel`, `smoke`, `chalk`, `signal`; white is Tailwind's built-in `#FFFFFF`).
- Fonts and the hero effects (film grain, reduced-motion handling) live in `src/input.css`.
- Screenshots of the hero at desktop, tablet and mobile sizes are in `docs/screenshots/`.

**Button patterns** (reuse site-wide):

```html
<!-- Primary -->
<a href="/shop/running"
   class="group inline-flex h-14 items-center gap-3 rounded-sm bg-white px-8
          font-display text-base font-extrabold uppercase italic tracking-wide text-ink
          transition hover:bg-chalk focus-visible:ring-2 focus-visible:ring-white
          focus-visible:ring-offset-4 focus-visible:ring-offset-ink">
  Shop Running Gear
  <svg class="h-5 w-5 transition-transform group-hover:translate-x-1.5" viewBox="0 0 24 24"
       fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
</a>

<!-- Secondary -->
<a href="/lab"
   class="inline-flex h-14 items-center rounded-sm border-2 border-white px-8
          font-display text-base font-extrabold uppercase italic tracking-wide text-white
          transition hover:bg-white hover:text-ink">
  Explore the Lab
</a>
```

**Before production**

- [ ] Get the logo as SVG (emblem and wordmark); the banner file is too low-resolution for the header.
- [ ] Swap `assets/img/hero-poster.jpg` (a low-res crop of the banner) for a full-resolution black-and-white hero still, and add the video loop to `assets/video/`.
- [ ] Replace the proof-strip numbers, product specs and testimonials with verified, real content.
