"""Builds the SixStar Clips branded frame: dark brand background, a white header card
with the logo, channel name, tagline and a one-line hook. The video sits in a square
window below the card (y=460..1540), which is left transparent here."""
import sys
from PIL import Image, ImageDraw, ImageFont

FD = "/usr/share/fonts/truetype/google-fonts/"
BOLD, MED = FD + "Poppins-Bold.ttf", FD + "Poppins-Medium.ttf"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
W, H = 1080, 1920
BG = (10, 11, 16, 255)          # logo background colour
CARD_Y0, CARD_Y1 = 150, 460     # header card
VID_Y0, VID_Y1 = 460, 1540      # square video window


def emoji_img(ch, size):
    f = ImageFont.truetype(EMOJI, 109)
    im = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
    box = im.getbbox()
    im = im.crop(box) if box else im
    r = size / im.height
    return im.resize((max(1, int(im.width * r)), size), Image.LANCZOS)


def build(out, hook, emojis):
    im = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(im)
    # transparent window for the video
    d.rectangle((0, VID_Y0, W, VID_Y1), fill=(0, 0, 0, 0))
    # white card
    d.rectangle((0, CARD_Y0, W, CARD_Y1), fill=(255, 255, 255, 255))
    # round logo
    logo = Image.open("logo.png").convert("RGBA").resize((132, 132), Image.LANCZOS)
    mask = Image.new("L", (132, 132), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 131, 131), fill=255)
    im.paste(logo, (48, CARD_Y0 + 30), mask)
    # name and tagline
    d.text((204, CARD_Y0 + 38), "SixStar Clips | GTA", font=ImageFont.truetype(BOLD, 46), fill=(15, 15, 20, 255))
    d.text((204, CARD_Y0 + 100), "Daily GTA 6 clips", font=ImageFont.truetype(MED, 36), fill=(120, 125, 135, 255))
    # hook line, shrunk until it fits
    size = 58
    while True:
        f = ImageFont.truetype(BOLD, size)
        tw = d.textlength(hook, font=f)
        ew = sum(emoji_img(c, size).width + 8 for c in emojis)
        if tw + ew + 16 <= W - 96 or size <= 40:
            break
        size -= 2
    y = CARD_Y0 + 200
    d.text((48, y), hook, font=f, fill=(15, 15, 20, 255))
    x = 48 + tw + 16
    for c in emojis:
        e = emoji_img(c, int(size * 1.0))
        im.paste(e, (int(x), y + int(size * 0.22)), e)
        x += e.width + 8
    im.save(out)
    print(out, "hook size", size)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
