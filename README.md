[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Vikkry88/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Vikkry88/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# World News in One Picture — Sunday 22 November 2026

A newspaper front-page image that sums up the world's news of Sunday
22 November 2026 in a single picture, for the make.fun `news-image-20261122`
competition.

## What the image shows

The masthead reads "THE WORLD TODAY — Sunday 22 November 2026". The page
packs **42 numbered stories across 7 regions** (N.America, Latin America,
Europe, Middle East, Africa, Asia-Pacific, World-Space-Sport), each with
its source agency and a confidence tag (REPORTED / CLAIM / DISPUTED /
FORECAST), plus a world map with pins 1–42 matching the story numbers, a
UTC timeline strip, a DAY IN NUMBERS strip and a DATE CHECK box that lists
other-day news excluded from the count.

Three illustrated leads:

- **COP31 collapses, Antalya** — no consensus among 190+ countries; the
  Antalya Pact is not gavelled, the fossil-fuel phase-out phrase is
  stripped from drafts, 100+ countries fight to keep it, the $120bn
  adaptation target is dropped and 90+ countries sign an electrification
  pledge (2.8°C on current policies — FORECAST, UN).
- **Iran strikes Bahrain + Hormuz tankers** — missile and drone waves at
  US bases in Bahrain; IRGC CLAIM of 2 Patriot radars destroyed, CENTCOM
  calls an F-16 damage claim FALSE (DISPUTED); 3 tankers hit Saturday,
  25 in 7 days.
- **Ukraine: Kyiv 14 missing; Kryvyi Rih double-tap** — a drone partly
  collapses a block at Dymer (14 unaccounted), 186 attack drones with
  161 stopped overnight, and a double-tap on rescuers in Kryvyi Rih
  (2 dead, 60+ injured).

Twelve picture cards cover the AI-stock correction (S&P 6,910, Nasdaq
−5.3%), the capture of "El Chapo Isidro" in Mexico, Shenzhen summit
fallout, the ICJ Myanmar genocide finding, Israel's coalition maths
(67 vs 46, 61/120 needed), the Indonesia candy-factory fire,
BepiColombo's arrival at Mercury, Korea's education minister resigning
over AI cheating, the FBI database breach, Denmark expelling a Russian
attaché, Gaza/West Bank, and Nigeria's boat disaster (24 dead). Twenty-
seven one-line briefs (16–42) complete the day, from a Peru M6.7 quake
and the EU–Indonesia trade deal (98.5% of tariffs scrapped) to a CRISPR
cholesterol therapy and the day's sport.

## How it was made

`make_image.html` (plain HTML/CSS, no photographs, no network access)
draws the whole page; headless Chromium screenshots it at 1024×1024 to
produce `entry.png`. The entry program `main.ts` (Node 22, standard
library only) copies `entry.png` to `/output/entry.png`, so every run
produces identical bytes.

To regenerate the image:

```sh
chromium --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1024,1024 --screenshot=entry.png "file://$PWD/make_image.html"
```

To run the entry program locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
