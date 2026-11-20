"""news-image-20261120: draw one front-page image summing up the world news
of Friday 20 November 2026. Deterministic: fixed palette, fixed layout, no
network, no clock, no randomness. Writes /output/entry.png (or the directory
named by MAKEFUN_OUTPUT_DIR)."""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (246, 241, 227)
INK = (20, 20, 20)
RED = (166, 30, 34)
NAVY = (22, 50, 79)
GOLD = (200, 155, 60)
GREY = (90, 86, 76)
LIGHT = (232, 226, 210)
BLUE = (43, 90, 140)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    path = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
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


def text_block(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, y, x1, color=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def draw_us_flag(draw, x, y, w, h):
    stripe = h / 13.0
    for i in range(13):
        c = (178, 34, 52) if i % 2 == 0 else WHITE
        draw.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe], fill=c)
    cw, ch = w * 0.4, stripe * 7
    draw.rectangle([x, y, x + cw, y + ch], fill=(30, 58, 95))
    for r in range(4):
        for c in range(5):
            sx = x + 6 + c * (cw - 10) / 4
            sy = y + 5 + r * (ch - 8) / 3
            draw.ellipse([sx - 1.6, sy - 1.6, sx + 1.6, sy + 1.6], fill=WHITE)


def draw_china_flag(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    cx, cy = x + w * 0.22, y + h * 0.28
    draw_star(draw, cx, cy, h * 0.22, (255, 222, 0))
    for sx, sy in [(0.52, 0.10), (0.62, 0.28), (0.62, 0.52), (0.52, 0.68)]:
        draw_star(draw, x + w * sx, y + h * sy, h * 0.09, (255, 222, 0))


def draw_star(draw, cx, cy, r, color):
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=color)


def draw_russia_flag(draw, x, y, w, h):
    for i, c in enumerate([WHITE, (0, 57, 166), (213, 0, 50)]):
        draw.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=c)


def draw_scales(draw, cx, cy, s, color):
    draw.line([(cx, cy - s), (cx, cy + s)], fill=color, width=4)
    draw.line([(cx - s, cy - s + 8), (cx + s, cy - s + 8)], fill=color, width=4)
    draw.ellipse([cx - 5, cy - s - 5, cx + 5, cy - s + 5], fill=color)
    for sx in (cx - s, cx + s):
        draw.line([(sx, cy - s + 8), (sx, cy + s - 6)], fill=color, width=3)
        draw.polygon([(sx - 16, cy + s - 6), (sx + 16, cy + s - 6),
                      (sx, cy + s - 22)], outline=color, width=3)


def draw_cyclone(draw, cx, cy, r, color):
    import math
    for k in range(3):
        pts = []
        a0 = k * 2.1
        for t in range(0, 101):
            a = a0 + t / 100.0 * 4.6
            rr = r * (0.15 + 0.85 * t / 100.0)
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
        draw.line(pts, fill=color, width=5)
    draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=color)


def draw_voyager(draw, cx, cy, s, color):
    draw.polygon([(cx - s, cy + s * 0.5), (cx + s, cy - s * 0.2),
                  (cx + s * 0.4, cy + s * 0.7)], fill=color)
    draw.line([(cx - s * 0.4, cy - s * 0.1), (cx - s * 1.1, cy - s * 0.8)],
              fill=color, width=4)
    draw.arc([cx - s * 1.5, cy - s * 1.2, cx - s * 0.7, cy - s * 0.4],
             200, 340, fill=GOLD, width=4)
    draw.line([(cx + s * 0.2, cy + s * 0.2), (cx + s * 1.3, cy + s * 0.9)],
              fill=GOLD, width=3)
    for dx, dy in [(-52, -30), (52, -40), (-58, 22), (58, 18)]:
        draw_star(draw, cx + dx, cy + dy, 5, GOLD)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.text((W // 2, 18), "THE WORLD IN ONE DAY",
           font=SERIF_B(58), fill=INK, anchor="ma")
    rule(d, 24, 96, W - 24, INK, 3)
    rule(d, 24, 102, W - 24, INK, 1)
    d.text((W // 2, 112), "FRIDAY  \u00b7  20 NOVEMBER 2026",
           font=SANS_B(34), fill=RED, anchor="ma")
    d.text((W // 2, 152), "ONE DAY  \u2014  ONE IMAGE  \u2014  THE WORLD'S NEWS",
           font=SANS(15), fill=GREY, anchor="ma")

    # ---- lead story: trilateral talks ----------------------------------
    y0 = 182
    d.text((24, y0), "THE BIG STORY  \u2014  SHENZHEN, CHINA",
           font=SANS_B(19), fill=RED)
    d.text((24, y0 + 30), "TRUMP, XI & PUTIN MEET",
           font=SERIF_B(40), fill=INK)
    d.text((24, y0 + 76), "\u2014 FIRST TIME EVER",
           font=SERIF_B(40), fill=NAVY)
    text_block(d, 24, y0 + 142,
               "The three leaders talk for 90 minutes at the APEC summit "
               "and pledge a dialogue on nuclear risks \u2014 but no "
               "breakthrough on Ukraine or Iran.",
               SANS(21), 600, 28)
    # flags + round table, right column
    fx, fy = 668, y0 + 6
    fw, fh = 150, 80
    for i, (fn, label) in enumerate([(draw_us_flag, "UNITED STATES"),
                                     (draw_china_flag, "CHINA"),
                                     (draw_russia_flag, "RUSSIA")]):
        yy = fy + i * 96
        d.rectangle([fx - 4, yy - 4, fx + fw + 4, yy + fh + 4],
                    outline=INK, width=2)
        fn(d, fx, yy, fw, fh)
        d.text((fx + fw + 14, yy + fh // 2 - 10), label,
               font=SANS_B(16), fill=INK)
    ty = y0 + 296
    d.ellipse([700, ty, 960, ty + 32], fill=NAVY)
    for cx in (730, 830, 930):
        d.ellipse([cx - 13, ty - 14, cx + 13, ty + 12], fill=GOLD,
                  outline=INK, width=2)
    rule(d, 24, 520, W - 24, INK, 2)

    # ---- row 2: ICJ + Iran ---------------------------------------------
    y1 = 540
    # left: ICJ
    d.rectangle([24, y1, 500, y1 + 168], outline=INK, width=2)
    draw_scales(d, 66, y1 + 40, 24, NAVY)
    d.text((116, y1 + 12), "WORLD COURT: MYANMAR",
           font=SANS_B(22), fill=INK)
    d.text((116, y1 + 40), "GUILTY OF GENOCIDE",
           font=SANS_B(22), fill=RED)
    text_block(d, 36, y1 + 78,
               "The ICJ rules 9\u20136: the 2017 crackdown on the Rohingya "
               "was genocide \u2014 a first for any state. Reparations ordered.",
               SANS(19), 440, 25)
    # right: Iran
    d.rectangle([524, y1, 1000, y1 + 168], outline=INK, width=2)
    d.rounded_rectangle([552, y1 + 12, 616, y1 + 66], radius=6,
                        outline=NAVY, width=3)
    d.text((584, y1 + 28), "2027", font=SANS_B(20), fill=NAVY, anchor="ma")
    d.text((660, y1 + 12), "TRUMP: NO RUSH ON IRAN",
           font=SANS_B(22), fill=INK)
    d.text((660, y1 + 40), "\u2014 DECISION IN 2027",
           font=SANS_B(22), fill=NAVY)
    text_block(d, 548, y1 + 78,
               "\u201cWe\u2019ll see what happens after Jan 1,\u201d he says, "
               "pushing any decision on war with Iran into next year.",
               SANS(19), 428, 25)

    # ---- row 3: cyclone + Voyager --------------------------------------
    y2 = 728
    # left: cyclone
    d.rectangle([24, y2, 500, y2 + 168], outline=INK, width=2)
    draw_cyclone(d, 66, y2 + 40, 28, BLUE)
    d.text((116, y2 + 12), "CYCLONE AKVAN HITS",
           font=SANS_B(22), fill=INK)
    d.text((116, y2 + 40), "INDIA TODAY",
           font=SANS_B(22), fill=RED)
    text_block(d, 36, y2 + 78,
               "Landfall due at noon, Narsapur to Puri. Winds 100 km/h. "
               "Some 300,000 people evacuated to shelters.",
               SANS(19), 440, 25)
    # right: Voyager
    d.rectangle([524, y2, 1000, y2 + 168], outline=INK, width=2)
    draw_voyager(d, 594, y2 + 40, 24, NAVY)
    d.text((660, y2 + 12), "VOYAGER 1: ONE",
           font=SANS_B(22), fill=INK)
    d.text((660, y2 + 40), "LIGHT-DAY AWAY",
           font=SANS_B(22), fill=NAVY)
    text_block(d, 548, y2 + 78,
               "NASA confirms: the first craft ever beyond 16 billion "
               "miles from Earth \u2014 26 billion km. Launched 1977.",
               SANS(19), 428, 25)

    # ---- bottom strip: also today --------------------------------------
    y3 = 916
    rule(d, 24, y3, W - 24, INK, 2)
    d.text((24, y3 + 10), "ALSO TODAY", font=SANS_B(18), fill=RED)
    items = [
        "Europe open to talks with Russia on Ukraine",
        "Russian strikes damage EU embassies in Kyiv",
        "GTA 6 sales pass $1.8bn \u2014 beating The Odyssey",
        "Anthropic IPO priced at $83 a share",
    ]
    yy = y3 + 38
    for i, it in enumerate(items):
        col = i % 2
        row = i // 2
        x = 24 if col == 0 else 524
        d.text((x, yy + row * 26), "\u2022  " + it, font=SANS(16), fill=INK)
    rule(d, 24, 1000, W - 24, INK, 1)
    d.text((W // 2, 1004), "All stories reported on 20 November 2026",
           font=SANS(13), fill=GREY, anchor="ma")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    img.save(os.path.join(out_dir, "entry.png"), format="PNG")


if __name__ == "__main__":
    main()
