#!/usr/bin/env python3
"""Generate the Opacity Index social/OG card (assets/opacity-og.png).

Reproducible press artifact: the headline % is computed from data/opacity.json so the card
never drifts from the data. Run after opacity.json changes. Pure PIL — no external services.
"""

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OPACITY = ROOT / "data" / "opacity.json"
OUT = ROOT / "assets" / "opacity-og.png"

W, H = 1200, 630
BG = (10, 14, 26)
CARD = (17, 24, 39)
GREEN = (16, 185, 129)
RED = (239, 68, 68)
AMBER = (245, 158, 11)
TEXT = (249, 250, 251)
MUTED = (156, 163, 175)
BORDER = (30, 41, 59)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def headline_pct() -> int:
    d = json.loads(OPACITY.read_text())
    cats = d["categories"]
    tot = sum(c["tps"] for c in cats)
    op60 = sum(c["tps"] for c in cats if c["opacity"] >= 60)
    return round(100 * op60 / tot)


def main():
    pct = headline_pct()
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    f_kicker = font("DejaVuSans-Bold.ttf", 26)
    f_big = font("DejaVuSans-Bold.ttf", 150)
    f_h = font("DejaVuSans-Bold.ttf", 44)
    f_body = font("DejaVuSans.ttf", 30)
    f_mono = font("DejaVuSansMono.ttf", 24)
    f_foot = font("DejaVuSans.ttf", 24)

    # kicker
    d.text((60, 54), "THE OPACITY INDEX", font=f_kicker, fill=GREEN)
    d.text((60, 90), "Universe of Finance", font=f_body, fill=MUTED)

    # big stat
    d.text((56, 150), f"{pct}%", font=f_big, fill=RED)
    # headline text (wrapped)
    lines = [
        "of the world's transaction throughput",
        "flows through systems too opaque",
        "to independently verify.",
    ]
    y = 340
    for ln in lines:
        d.text((60, y), ln, font=f_h, fill=TEXT)
        y += 52

    # measured vs estimated contrast chips (bottom)
    chip_y = 520
    # measured chip
    d.rounded_rectangle([60, chip_y, 590, chip_y + 60], radius=12, fill=CARD, outline=GREEN, width=2)
    d.ellipse([80, chip_y + 24, 96, chip_y + 40], fill=GREEN)
    d.text((110, chip_y + 16), "Open ledgers: seconds ago", font=f_mono, fill=TEXT)
    # estimated chip
    d.rounded_rectangle([610, chip_y, 1140, chip_y + 60], radius=12, fill=CARD, outline=RED, width=2)
    d.ellipse([630, chip_y + 24, 646, chip_y + 40], fill=RED)
    d.text((660, chip_y + 16), "TradFi estimates: as of 2024", font=f_mono, fill=TEXT)

    # right rail: opacity scale ticks
    d.text((760, 60), "opacity 0 → 100", font=f_foot, fill=MUTED)
    for i, (lab, col) in enumerate([("Pix 24", GREEN), ("UPI 30", GREEN), ("Cards 60", AMBER), ("China 88", RED)]):
        yy = 110 + i * 46
        d.rounded_rectangle([760, yy, 1140, yy + 34], radius=8, fill=CARD, outline=BORDER, width=1)
        # bar fill proportional to score
        score = int(lab.split()[-1])
        d.rounded_rectangle([760, yy, 760 + int(380 * score / 100), yy + 34], radius=8, fill=col)
        d.text((774, yy + 5), lab, font=f_foot, fill=TEXT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG")
    print(f"wrote {OUT} ({W}x{H}) headline {pct}%")


if __name__ == "__main__":
    main()
