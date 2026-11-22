#!/usr/bin/env python3
"""Draw the Sunday 22 November 2026 world-news front page (Pillow, shapes+text).

No photos, no network. Deterministic 1024x1024 PNG written beside this file.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (251, 247, 238)
INK = (26, 26, 30)
RED = (178, 30, 30)
BLUE = (28, 68, 138)
TEAL = (18, 110, 110)
GOLD = (170, 120, 18)
GREY = (105, 105, 110)
DARK = (38, 42, 56)
SKY = (205, 226, 242)
CREAM = (255, 255, 255)
GREEN = (34, 120, 62)
ORANGE = (214, 110, 24)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrap(x, y, text, font, maxw, fill=INK, leading=5):
    for ln in wrap_lines(text, font, maxw):
        d.text((x, y), ln, font=font, fill=fill)
        y += font.size + leading
    return y


def center(cx, y, text, font, fill=INK):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill)
    return y + font.size


# ---------------- Masthead ----------------
d.rectangle([0, 0, W, 146], fill=DARK)
center(W // 2, 12, "THE WORLD TODAY", F(SERIF_B, 60), fill=(255, 255, 255))
center(W // 2, 84, "Sunday 22 November 2026  •  World News in One Picture", F(SANS_B, 24), fill=(242, 222, 158))
d.rectangle([0, 146, W, 154], fill=RED)

# ---------------- Lead headline ----------------
d.rectangle([24, 168, 1000, 174], fill=INK)
center(W // 2, 182, "CLIMATE TALKS STALL, AI STOCKS FALL", F(SERIF_B, 38), fill=RED)
y = draw_wrap(60, 230,
              "COP31 runs into Sunday overtime in Antalya as the AI boom's record IPO week ends in a global sell-off",
              F(SANS_B, 24), 904)
# two lead panels
# LEFT: COP31
d.rectangle([36, 312, 500, 540], outline=INK, width=3, fill=SKY)
d.rectangle([36, 312, 500, 346], fill=TEAL)
center(268, 318, "COP31 • ANTALYA, TÜRKIYE", F(SANS_B, 20), fill=(255, 255, 255))
# globe
d.ellipse([120, 366, 240, 486], fill=(90, 170, 230), outline=INK, width=3)
d.ellipse([148, 392, 190, 428], fill=GREEN)
d.ellipse([182, 430, 222, 462], fill=GREEN)
d.arc([120, 366, 240, 486], 20, 160, fill=INK, width=2)
d.line([120, 426, 240, 426], fill=INK, width=2)
# thermometer
d.rectangle([300, 366, 330, 470], fill=(255, 255, 255), outline=INK, width=3)
d.rectangle([306, 386, 324, 464], fill=RED)
d.ellipse([292, 462, 338, 498], fill=RED, outline=INK, width=3)
center(315, 352, "1.5°C", F(SANS_B, 18), fill=RED)
# oil barrel with slash
d.rectangle([386, 386, 446, 486], fill=(60, 60, 60), outline=INK, width=3)
d.rectangle([386, 410, 446, 424], fill=(255, 200, 60))
d.rectangle([386, 446, 446, 460], fill=(255, 200, 60))
d.line([382, 382, 450, 490], fill=RED, width=7)
center(416, 352, "OIL", F(SANS_B, 16), fill=INK)
d.rectangle([36, 498, 500, 540], fill=CREAM)
draw_wrap(50, 503, "~200 nations deadlocked; fossil-fuel words dropped; EU: 'good deal or no deal'", F(SANS, 15), 436)
# RIGHT: markets
d.rectangle([524, 312, 988, 540], outline=INK, width=3, fill=(52, 48, 66))
d.rectangle([524, 312, 988, 346], fill=RED)
center(756, 318, "AI BUBBLE POPS • MARKETS", F(SANS_B, 20), fill=(255, 255, 255))
# axes + falling line
d.line([570, 380, 570, 470], fill=(255, 255, 255), width=3)
d.line([570, 470, 950, 470], fill=(255, 255, 255), width=3)
pts = [(580, 388), (650, 378), (720, 392), (790, 420), (860, 448), (940, 462)]
d.line(pts, fill=(255, 120, 80), width=7)
for px, py in pts:
    d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=(255, 220, 120), outline=INK, width=2)
d.polygon([(940, 462), (916, 454), (924, 480)], fill=(255, 120, 80))
center(660, 356, "NASDAQ −5.3%", F(SANS_B, 22), fill=(255, 220, 120))
center(850, 356, "S&P −3.7%", F(SANS_B, 22), fill=(255, 255, 255))
d.rectangle([524, 498, 988, 540], fill=CREAM)
draw_wrap(538, 503, "Anthropic $2tn IPO falls 8.5%; Nvidia −14%; 2026 gains wiped out", F(SANS, 15), 436)


# ---------------- Lower grid ----------------
d.rectangle([24, 552, 1000, 558], fill=INK)
boxes = [(36, 572, 500, 786), (524, 572, 988, 786), (36, 800, 500, 978), (524, 800, 988, 978)]


def story_box(box, header, header_col, title, body, icon=None):
    x0, y0, x1, y1 = box
    d.rectangle([x0, y0, x1, y1], outline=INK, width=3, fill=CREAM)
    d.rectangle([x0, y0, x1, y0 + 34], fill=header_col)
    center((x0 + x1) // 2, y0 + 6, header, F(SANS_B, 19), fill=(255, 255, 255))
    yy = draw_wrap(x0 + 16, y0 + 44, title, F(SERIF_B, 22), x1 - x0 - 32, fill=INK, leading=3)
    yy = draw_wrap(x0 + 16, yy + 4, body, F(SANS, 17), x1 - x0 - 32, fill=INK, leading=4)
    return yy


# 1 Israel
yy = story_box(boxes[0], "ISRAEL • COALITION TALKS", BLUE,
               "Eisenkot invites Netanyahu's party to talks",
               "President Herzog gave ex-army chief Gadi Eisenkot first mandate (67 vs 46). "
               "Netanyahu stays caretaker; no bloc has 61 of 120 seats.")
# mini seat bars
x0, y0, x1, y1 = boxes[0]
d.rectangle([x0 + 16, y1 - 44, x0 + 16 + 250, y1 - 28], fill=BLUE)
d.rectangle([x0 + 16, y1 - 24, x0 + 16 + 180, y1 - 10], fill=RED)
d.text((x0 + 276, y1 - 46), "67", font=F(SANS_B, 16), fill=BLUE)
d.text((x0 + 206, y1 - 26), "46", font=F(SANS_B, 16), fill=RED)

# 2 Mexico
story_box(boxes[1], "MEXICO • CARTEL BOSS TAKEN", (120, 40, 40),
          "'El Chapo Isidro' captured in Sinaloa",
          "FBI top-10 fugitive ($5m reward) seized in Guasave. Firefight kills 11; "
          "helicopters, burning trucks; US intel helped.")
x0, y0, x1, y1 = boxes[1]
# helicopter silhouette
hx, hy = x1 - 150, y1 - 52
d.ellipse([hx, hy, hx + 70, hy + 30], fill=INK)
d.rectangle([hx + 66, hy + 10, hx + 110, hy + 18], fill=INK)
d.line([hx - 14, hy - 8, hx + 84, hy - 8], fill=INK, width=4)
d.line([hx + 35, hy - 8, hx + 35, hy + 2], fill=INK, width=4)
d.rectangle([hx + 14, hy + 8, hx + 40, hy + 24], fill=(180, 220, 255))

# 3 Space
story_box(boxes[2], "SPACE • MERCURY ARRIVAL", (70, 60, 130),
          "BepiColombo reaches Mercury after 8 years",
          "ESA/JAXA MPO + Mio captured. Science Apr 2027. Voyager 1: 1 light-day.")
x0, y0, x1, y1 = boxes[2]
# mercury + orbit (kept clear of the body text)
mx, my = x1 - 96, y1 - 62
d.ellipse([mx, my, mx + 44, my + 44], fill=(170, 150, 130), outline=INK, width=2)
d.ellipse([mx + 8, my + 10, mx + 18, my + 20], fill=(130, 115, 100))
d.ellipse([mx + 24, my + 24, mx + 35, my + 35], fill=(130, 115, 100))
d.arc([mx - 16, my - 12, mx + 60, my + 56], 300, 120, fill=GOLD, width=3)
d.rectangle([mx + 48, my - 8, mx + 62, my + 2], fill=GOLD, outline=INK, width=1)

# 4 Cricket
story_box(boxes[3], "CRICKET • RECORD 720/9", GREEN,
          "India pile up 720/9 in Wellington",
          "Rahul 136, Pant 128 — highest Test total in NZ. NZ trail by 352, Day 4.")
x0, y0, x1, y1 = boxes[3]
# bat + ball
bx, by = x1 - 110, y1 - 64
d.polygon([(bx, by + 50), (bx + 14, by + 50), (bx + 44, by), (bx + 32, by - 6)], fill=(210, 170, 110), outline=INK)
d.rectangle([bx + 38, by - 22, bx + 46, by - 2], fill=(120, 80, 40), outline=INK, width=1)
d.ellipse([bx + 56, by + 28, bx + 84, by + 56], fill=RED, outline=INK, width=2)
d.arc([bx + 60, by + 30, bx + 80, by + 54], 90, 270, fill=(255, 255, 255), width=2)

# ---------------- Footer ----------------
d.rectangle([0, 990, W, 1024], fill=DARK)
center(W // 2, 999, "ALSO TODAY: ATP Finals — Alcaraz v Zverev • France — 4th protest weekend • India — 10m HPV doses", F(SANS_B, 16), fill=(255, 255, 255))

img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} {img.size} {os.path.getsize(OUT)} bytes")
