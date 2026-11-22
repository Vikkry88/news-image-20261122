[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Vikkry88/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Vikkry88/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# World News in One Picture — Sunday 22 November 2026

A newspaper front-page image that sums up the world's news of Sunday
22 November 2026 in a single picture, for the make.fun `news-image-20261122`
competition.

## What the image shows

The masthead reads "THE WORLD TODAY — Sunday 22 November 2026". The lead
story, "Climate Talks Stall, AI Stocks Fall", pairs two panels:

- **COP31, Antalya** — nearly 200 nations remain deadlocked into Sunday
  overtime over fossil-fuel language and climate finance; the draft drops
  explicit fossil-fuel wording and a $120bn adaptation target, and the EU
  warns it is "a good deal or no deal" while the text admits the 1.5°C
  limit will be overshot.
- **AI Bubble Pops** — Anthropic's record IPO (briefly above $2 trillion)
  tumbles 8.5% as the Nasdaq falls 5.3% (wiping out its 2026 gains), the
  S&P 500 drops 3.7% into correction territory and Nvidia falls 14%, with
  Asian markets plunging in the global sell-off.

Four further stories fill the page:

- **Israel / Coalition Talks** — Gadi Eisenkot, tasked by President Herzog
  to form the next government (67 recommendations vs 46 for Netanyahu),
  invites Netanyahu's party to coalition talks; Netanyahu remains caretaker
  prime minister and no bloc holds 61 of 120 Knesset seats.
- **Mexico / Cartel Boss Taken** — "El Chapo Isidro" (Fausto Isidro Meza
  Flores), one of the FBI's ten most wanted with a $5 million reward, is
  captured in Guasave, Sinaloa; the firefight kills 11 people amid
  helicopters and burning trucks, with US intelligence credited.
- **Space / Mercury Arrival** — the ESA/JAXA BepiColombo mission reaches
  Mercury after an eight-year journey, its twin orbiters MPO and Mio
  captured by the planet ahead of science operations from April 2027;
  NASA's Voyager 1 is now one light-day from Earth.
- **Cricket / Record 720/9** — India declare at 720/9 in Wellington against
  New Zealand, the highest Test total in New Zealand, built on centuries
  from KL Rahul (136) and Rishabh Pant (128); New Zealand trail by 352 on
  Day 4.

A footer line adds three more of the day's stories: the ATP Finals title
decider between Carlos Alcaraz and Alexander Zverev, France's fourth
weekend of cost-of-living protests, and India passing ten million HPV
vaccine doses.

## How it was made

`make_image.py` (Python 3 + Pillow) draws the whole page from shapes and
text only — no photographs and no network access — and writes `entry.png`
(1024×1024 PNG). The entry program `main.ts` (Node 22, standard library
only) copies `entry.png` to `/output/entry.png`, so every run produces
identical bytes.

To regenerate the image:

```sh
python3 make_image.py
```

To run the entry program locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
