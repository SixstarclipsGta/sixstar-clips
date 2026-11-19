"""SixStar Clips card, big-hook version (added 19 Nov 2026, after the SpectreX study).
Same layout as card.py (dark background, white card above a square video window at
y=460..1540), but the hook is set large in Anton capitals on up to two centred lines,
with the emoji at the end of the last line.

Usage: python3 card2.py out.png "Trying to pet a crocodile" "👀"
Run it in a folder that contains logo.png."""
import sys
from PIL import Image, ImageDraw, ImageFont

FD = "/usr/share/fonts/truetype/google-fonts/"
ANTON = FD + "ofl/anton/Anton-Regular.ttf"
BOLD, MED = FD + "Poppins-Bold.ttf", FD + "Poppins-Medium.ttf"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
W, H = 1080, 1920
BG = (10, 11, 16, 255)
CARD_Y0, CARD_Y1 = 110, 460
VID_Y0, VID_Y1 = 460, 1540
INK = (15, 15, 20, 255)
MAXW = W - 80


def emoji_img(ch, size):
    f = ImageFont.truetype(EMOJI, 109)
    im = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
    box = im.getbbox()
    im = im.crop(box) if box else im
    r = size / im.height
    return im.resize((max(1, int(im.width * r)), size), Image.LANCZOS)


def split_two(words, d, f):
    """Best two-line split: the one whose longer line is shortest."""
    if len(words) == 1:
        return [words[0]]
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        w = max(d.textlength(a, font=f), d.textlength(b, font=f))
        if best is None or w < best[0]:
            best = (w, [a, b])
    return best[1]


def build(out, hook, emojis):
    im = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, VID_Y0, W, VID_Y1), fill=(0, 0, 0, 0))
    d.rectangle((0, CARD_Y0, W, CARD_Y1), fill=(255, 255, 255, 255))
    # small header row: logo, name, tagline
    s = 84
    logo = Image.open("logo.png").convert("RGBA").resize((s, s), Image.LANCZOS)
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, s - 1, s - 1), fill=255)
    im.paste(logo, (40, CARD_Y0 + 22), mask)
    d.text((140, CARD_Y0 + 26), "SixStar Clips | GTA", font=ImageFont.truetype(BOLD, 34), fill=INK)
    d.text((140, CARD_Y0 + 70), "Daily GTA 6 clips", font=ImageFont.truetype(MED, 26), fill=(120, 125, 135, 255))
    # big hook, up to two lines, shrunk until both lines fit
    words = hook.upper().split()
    size = 104
    while True:
        f = ImageFont.truetype(ANTON, size)
        lines = split_two(words, d, f)
        ew = sum(emoji_img(c, int(size * 0.8)).width + 10 for c in emojis)
        widths = [d.textlength(l, font=f) for l in lines]
        widths[-1] += (ew + 14) if emojis else 0
        if max(widths) <= MAXW or size <= 60:
            break
        size -= 4
    top, bottom = CARD_Y0 + 122, CARD_Y1 - 22
    lh = int(size * 1.08)
    y = top + ((bottom - top) - lh * len(lines)) // 2
    for i, l in enumerate(lines):
        x = (W - widths[i]) // 2
        d.text((x, y - int(size * 0.12)), l, font=f, fill=INK)
        if i == len(lines) - 1 and emojis:
            ex = x + d.textlength(l, font=f) + 14
            for c in emojis:
                e = emoji_img(c, int(size * 0.8))
                im.paste(e, (int(ex), y + int(size * 0.12)), e)
                ex += e.width + 10
        y += lh
    im.save(out)
    print(out, "hook size", size, "lines", lines)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
