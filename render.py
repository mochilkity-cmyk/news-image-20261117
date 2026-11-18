"""Render the news-image-20261117 entry: a 1024x1024 infographic of
Tuesday 17 November 2026 world news. Drawn with PIL (stdlib-adjacent
build tool only; the entry program itself is a plain copy in main.ts).
Run: python3 render.py  -> writes entry.png next to this file."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (15, 42, 68)
INK = (18, 35, 58)
GREY = (61, 74, 92)
BG = (244, 246, 248)
CARD = (255, 255, 255)
BORDER = (216, 222, 230)
SUBBLUE = (159, 184, 208)
FOOTGREY = (110, 122, 138)

# (kicker, accent colour, headline, detail)
STORIES = [
    ("MIDDLE EAST", (192, 57, 43),
     "US strikes Iran as Hormuz war grows",
     "US warplanes hit a missile site on Qeshm Island; a fourth tanker "
     "was mined in the Strait of Hormuz."),
    ("EUROPE", (31, 111, 235),
     "Ukraine strikes Crimean Bridge",
     "Kyiv struck the Crimean Bridge; Russian strikes hit Kyiv bridges "
     "and Zaporizhzhia, killing 40."),
    ("MIDDLE EAST", (14, 124, 107),
     "Four nations demand Gaza aid access",
     "UK, Australia, Canada and Italy urged Israel to open crossings "
     "as winter rains flood shelters."),
    ("ASIA-PACIFIC", (108, 74, 182),
     "Trump, Xi, Putin to meet in Shenzhen",
     "The three leaders will hold a first-ever trilateral summit on "
     "Thursday, on the APEC sidelines."),
    ("TECHNOLOGY", (217, 115, 13),
     "US tightens AI chip export ban on China",
     "New rules close loopholes that let Chinese firms reach advanced "
     "AI chips via overseas data centres."),
    ("HEALTH", (46, 125, 50),
     "US loses measles elimination status",
     "PAHO: the US lost the status after a year of uninterrupted "
     "measles transmission."),
]


def wrap(draw, text, font, max_w):
    """Wrap text to fit max_w pixels; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- header band ----
    d.rectangle([0, 0, W, 150], fill=NAVY)
    f_date = ImageFont.truetype(BOLD, 56)
    f_sub = ImageFont.truetype(BOLD, 24)
    d.text((32, 22), "TUESDAY 17 NOVEMBER 2026", font=f_date, fill=(255, 255, 255))
    d.text((34, 96), "WORLD NEWS  ·  THE DAY IN SIX STORIES",
           font=f_sub, fill=SUBBLUE)

    # ---- story cards: 2 cols x 3 rows ----
    cw, ch, gap, m = 488, 256, 16, 16
    f_kick = ImageFont.truetype(BOLD, 19)
    f_head = ImageFont.truetype(BOLD, 30)
    f_det = ImageFont.truetype(REG, 22)
    for i, (kicker, accent, head, detail) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = m + col * (cw + gap)
        y = 166 + row * (ch + gap)
        # card
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14,
                            fill=CARD, outline=BORDER, width=2)
        # accent bar
        d.rounded_rectangle([x + 2, y + 16, x + 12, y + ch - 16], radius=5,
                            fill=accent)
        tx = x + 30
        tw = cw - 30 - 22  # text width
        d.text((tx, y + 20), kicker, font=f_kick, fill=accent)
        head_lines = wrap(d, head, f_head, tw)
        assert len(head_lines) <= 2, f"headline too long: {head!r} -> {head_lines}"
        hy = y + 54
        for ln in head_lines:
            d.text((tx, hy), ln, font=f_head, fill=INK)
            hy += 37
        det_lines = wrap(d, detail, f_det, tw)
        assert len(det_lines) <= 3, f"detail too long: {detail!r} -> {det_lines}"
        dy = y + 54 + 2 * 37 + 8
        for ln in det_lines:
            d.text((tx, dy), ln, font=f_det, fill=GREY)
            dy += 28

    # ---- footer ----
    f_foot = ImageFont.truetype(REG, 19)
    foot = "Sources: Reuters · AFP · AP · PAHO · Le Monde  —  events of 17 Nov 2026"
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, 982), foot, font=f_foot, fill=FOOTGREY)

    img.save("entry.png", "PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
