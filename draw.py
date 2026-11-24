#!/usr/bin/env python3
"""Draw the front page for Tuesday 24 November 2026.

Run: python3 draw.py  -> writes entry.png (1024x1024) next to this file.
Pure Pillow drawing, no network, no external assets.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (23, 48, 84)
STEEL = (70, 90, 110)
LIGHT = (226, 220, 205)
SEA = (38, 78, 110)
SKY = (196, 214, 228)
SMOKE = (120, 120, 118)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap, returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, max_w, fill=INK, leading=None):
    x, y = xy
    leading = leading or int(fnt.size * 1.22)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_lead_scene(draw, x0, y0, x1, y1):
    """Stylised sea scene: sky, sun, sea, warship, drone, smoke plume."""
    draw.rectangle([x0, y0, x1, y1], fill=SKY, outline=INK, width=2)
    horizon = y0 + int((y1 - y0) * 0.52)
    draw.rectangle([x0, horizon, x1, y1], fill=SEA)
    # sun
    draw.ellipse([x1 - 78, y0 + 14, x1 - 34, y0 + 58], fill=(240, 196, 90))
    # distant coastline
    draw.polygon([(x0, horizon), (x0 + 90, horizon - 26), (x0 + 190, horizon),
                  (x0 + 260, horizon - 18), (x1, horizon)], fill=(96, 110, 96))
    # smoke plume
    cx = x0 + 150
    for i, r in enumerate([46, 38, 30, 22]):
        draw.ellipse([cx - r, y0 + 26 + i * 26 - r // 2,
                      cx + r, y0 + 26 + i * 26 + r // 2], fill=SMOKE)
    # warship hull
    hy = horizon + 26
    draw.polygon([(x0 + 40, hy), (x0 + 300, hy), (x0 + 268, hy + 34),
                  (x0 + 66, hy + 34)], fill=(38, 44, 52))
    # superstructure + mast + funnel
    draw.rectangle([x0 + 120, hy - 34, x0 + 220, hy], fill=(52, 60, 70))
    draw.rectangle([x0 + 236, hy - 26, x0 + 252, hy], fill=(52, 60, 70))
    draw.line([(x0 + 168, hy - 34), (x0 + 168, hy - 58)], fill=(38, 44, 52), width=5)
    draw.line([(x0 + 150, hy - 52), (x0 + 190, hy - 52)], fill=(38, 44, 52), width=4)
    # listing tilt + waves
    for wx in range(x0 + 20, x1 - 20, 46):
        draw.arc([wx, hy + 38, wx + 40, hy + 54], 0, 180, fill=(210, 226, 238), width=3)
    # drone above
    dx, dy = x0 + 300, y0 + 46
    draw.ellipse([dx - 22, dy - 8, dx + 22, dy + 8], fill=(30, 30, 30))
    draw.line([(dx - 34, dy - 10), (dx - 14, dy - 4)], fill=(30, 30, 30), width=3)
    draw.line([(dx + 14, dy - 4), (dx + 34, dy - 10)], fill=(30, 30, 30), width=3)
    draw.line([(dx - 6, dy + 8), (dx + 6, dy + 8)], fill=(30, 30, 30), width=3)
    # caption on a dark strip at the bottom of the scene
    draw.rectangle([x0, y1 - 30, x1, y1], fill=(20, 40, 60))
    draw.text((x0 + 8, y1 - 24),
              "Ukrainian sea drones strike a Russian warship off Libya.",
              font=font(SANS, 15), fill=(240, 240, 240))


def card(draw, x0, y0, w, h, kicker, headline, deck, accent=RED):
    draw.rectangle([x0, y0, x0 + w, y0 + h], outline=INK, width=2)
    draw.rectangle([x0, y0, x0 + w, y0 + 28], fill=accent)
    draw.text((x0 + 10, y0 + 5), kicker, font=font(SANS_B, 15), fill=(255, 255, 255))
    y = para(draw, (x0 + 10, y0 + 36), headline, font(SANS_B, 19), w - 20,
             leading=22)
    para(draw, (x0 + 10, y + 4), deck, font(SANS, 14), w - 20, leading=17)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36  # margin

    # ---- top dateline ----
    d.text((M, 18), "TUESDAY 24 NOVEMBER 2026  |  ONE DAY, ONE PAGE",
           font=font(SANS_B, 17), fill=RED)
    d.text((W - M - 240, 18), "THE WORLD IN ONE DAY",
           font=font(SANS_B, 17), fill=INK)
    rule(d, M, 46, W - M, 3)

    # ---- masthead ----
    d.text((M, 56), "THE WORLD IN ONE DAY", font=font(SERIF, 62), fill=INK)
    d.text((M, 128), "TUESDAY 24 NOVEMBER 2026",
           font=font(SANS_B, 24), fill=NAVY)
    d.text((W - M - 300, 130), "WORLD  •  POLITICS  •  MARKETS",
           font=font(SANS, 15), fill=STEEL)
    rule(d, M, 164, W - M, 2)

    # ---- lead story ----
    lead_y = 176
    lead_h = 224
    d.text((M, lead_y), "LEAD STORY", font=font(SANS_B, 16), fill=RED)
    y = para(d, (M, lead_y + 26),
             "KYIV SINKS RUSSIAN WARSHIP OFF LIBYA",
             font(SERIF, 36), 470, leading=43)
    para(d, (M, y + 8),
         "Ukraine says its sea drones sank a Russian naval corvette "
         "in Benghazi harbour — the war's reach now stretches far "
         "beyond Europe.",
         font(SANS, 18), 470, leading=22)
    draw_lead_scene(d, M + 500, lead_y, W - M, lead_y + lead_h)
    rule(d, M, lead_y + lead_h + 12, W - M, 2)

    # ---- inside today ----
    gy = lead_y + lead_h + 26
    d.text((M, gy), "INSIDE TODAY", font=font(SANS_B, 18), fill=NAVY)
    d.text((W - M - 330, gy), "REPORTED 24 NOVEMBER 2026",
           font=font(SANS, 15), fill=STEEL)
    gy += 28

    cw = (W - 2 * M - 24) // 2
    ch = 120
    gap = 8
    stories = [
        ("NATO  •  EUROPE", "NATO sends early-warning jets to Poland",
         "AWACS aircraft deploy after three Russian missiles landed on "
         "NATO's eastern flank, Warsaw says.", NAVY),
        ("SECURITY  •  ASIA", "Russian jet enters South Korean airspace",
         "Seoul briefly issues an evacuation warning for Ulleung island "
         "after the incursion on Tuesday.", NAVY),
        ("ECONOMY  •  ASIA", "Singapore lifts 2026 growth forecast",
         "The city-state raises its outlook to about 6% after third-quarter "
         "growth of 6.1% beat expectations.", STEEL),
        ("USA  •  WASHINGTON", "FBI deputy director to retire in December",
         "Christopher Raia plans to step down, the Washington Post "
         "reports — the latest exit at the bureau.", STEEL),
        ("TECH  •  SILICON VALLEY", "Trump backs Nvidia chief's return",
         "The president says he secured a deal to reinstate Jensen Huang "
         "as CEO after his ouster on 12 November.", STEEL),
        ("USA  •  SANCTIONS", "US hits Iran's shadow banking networks",
         "Treasury sanctions dozens of people and entities in a new "
         "push to isolate Tehran from global finance.", RED),
        ("CLIMATE  •  COP31", "Climate summit ends with no deal",
         "COP31 in Turkiye collapses over fossil fuels and finance, "
         "the biggest breakdown since 2009.", RED),
        ("AUSTRALIA  •  VOTE", "Victoria vote tests Pauline Hanson",
         "Saturday's state election will show if the One Nation surge "
         "turns into real power in Australia.", NAVY),
    ]
    for i, (kick, head, deck, acc) in enumerate(stories):
        r, c = divmod(i, 2)
        x0 = M + c * (cw + 24)
        y0 = gy + r * (ch + gap)
        card(d, x0, y0, cw, ch, kick, head, deck, acc)

    fy = gy + 4 * (ch + gap) + 6
    rule(d, M, fy, W - M, 3)
    d.text((M, fy + 10),
           "Sources: Reuters, AP, AFP, RFE/RL, Washington Post — first reported 23–24 November 2026.",
           font=font(SANS, 15), fill=INK)
    d.text((M, fy + 32),
           "One day. One page. The world in one image.",
           font=font(SERIF_R, 17), fill=STEEL)
    d.text((W - M - 150, fy + 32), "24 NOV 2026", font=font(SANS_B, 16), fill=RED)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
