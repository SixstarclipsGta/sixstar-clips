#!/usr/bin/env python3
"""Explainer renderer (24 Nov): one whole raw clip, played as it is, that freezes at chosen moments,
zooms in on an NPC with a ring around it, and shows a caption under the video. Optional hook freeze first.

Usage: python3 tools/explainer.py tools/configs/<config>.py
Config: SRC, OUT, TITLE, END (clip end, s), HOOK (key into FREEZES or None),
FREEZES = {key: dict(t=, cx=, cy=, rx=, ry=, z=, cap=)}  (coords in the 1920x1080 source)
ORDER = [keys in play order]. Optional: DUR (freeze length, default 2.2), LINGER (caption after, default 1.3).
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
from card2 import emoji_img

FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
FPS, VW = 30, 1080
DUR, LINGER = 2.2, 1.3
cfg = {}
exec(open(sys.argv[1]).read(), cfg)
SRC, OUT, TITLE, END = cfg["SRC"], cfg["OUT"], cfg["TITLE"], cfg["END"]
FR, ORDER, HOOK = cfg["FREEZES"], cfg["ORDER"], cfg.get("HOOK")
DUR, LINGER = cfg.get("DUR", DUR), cfg.get("LINGER", LINGER)
CX, CW = cfg.get("CROP", (0, 1920))          # source crop (x, width), full height; 1440 wide = 4:3, bigger on screen
VH = int(round(1080 * VW / CW / 2) * 2)
VY = cfg.get("VY", (1920 - VH) // 2 - 40)
WD = os.path.splitext(OUT)[0] + "_parts"
os.makedirs(WD, exist_ok=True)


def run(cmd):
    subprocess.run(cmd, check=True)


def text_png(path, text, size, y_top=None, y_bottom=None, stroke=0, shadow=True):
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    emo, words = "", text.split(" ")
    if words and not words[-1].isascii():
        emo, words = words[-1], words[:-1]
    f = ImageFont.truetype(FONT, size)
    ew = emoji_img(emo, int(size * 0.95)).width + 12 if emo else 0
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > 960 and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    if d.textlength(lines[-1], font=f) + ew > 980:
        lines.append("")
    lh = int(size * 1.22)
    y = y_top if y_top is not None else y_bottom - lh * len(lines)
    for i, l in enumerate(lines):
        last = i == len(lines) - 1
        lw = d.textlength(l, font=f) + (ew if last else 0)
        x = (1080 - lw) / 2
        if shadow:
            for dx, dy in ((0, 3), (2, 2), (-2, 2)):
                d.text((x + dx, y + dy), l, font=f, fill=(0, 0, 0, 150))
        d.text((x, y), l, font=f, fill=(255, 255, 255, 255), stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
        if last and emo:
            e = emoji_img(emo, int(size * 0.95))
            im.paste(e, (int(x + d.textlength(l, font=f) + (12 if l else 0)), y + int(size * 0.08)), e)
        y += lh
    im.save(path)


def play(i, a, b):
    out = f"{WD}/p{i}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", SRC,
         "-vf", f"crop={CW}:1080:{CX}:0,scale={VW}:{VH},fps={FPS},format=yuv420p", "-af", "aresample=48000",
         "-ac", "2", "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "aac", "-b:a", "192k", out])
    return out, b - a


def freeze(i, k):
    F = FR[k]
    png = f"{WD}/f{i}.png"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{F['t']:.3f}", "-i", SRC, "-frames:v", "1", png])
    im = Image.open(png).convert("RGB").crop((CX, 0, CX + CW, 1080))
    d = ImageDraw.Draw(im)
    cx, cy, rx, ry = F["cx"] - CX, F["cy"], F["rx"], F.get("ry", F["rx"])
    d.ellipse((cx - rx - 2, cy - ry - 2, cx + rx + 2, cy + ry + 2), outline=(0, 0, 0), width=8)
    d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), outline=(255, 214, 0), width=5)
    im.save(png)
    Z, n = F.get("z", 2.5), int(DUR * FPS)
    zin, zout = 14, 9
    z = (f"if(lt(in,{zin}),1+({Z}-1)*in/{zin},if(gt(in,{n - zout}),max(1,{Z}-({Z}-1)*(in-{n - zout})/{zout}),{Z}))")
    vf = (f"scale={CW}:1080,zoompan=z='{z}':x='max(0,min(iw-iw/zoom,{cx}-iw/zoom/2))':"
          f"y='max(0,min(ih-ih/zoom,{cy}-ih/zoom/2))':d=1:s={VW}x{VH}:fps={FPS},format=yuv420p")
    out = f"{WD}/f{i}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{DUR}", "-i", png,
         "-f", "lavfi", "-t", f"{DUR}", "-i", "anullsrc=r=48000:cl=stereo",
         "-vf", vf, "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "aac", "-b:a", "192k",
         "-shortest", out])
    return out, DUR


parts, caps, t, prev, i = [], [], 0.0, 0.0, 0
if HOOK:
    p, d = freeze(i, HOOK); parts.append(p)
    caps.append((FR[HOOK].get("hookcap", FR[HOOK]["cap"]), t, t + d)); t += d; i += 1
for k in ORDER:
    p, d = play(i, prev, FR[k]["t"]); parts.append(p); t += d; i += 1
    p, d = freeze(i, k); parts.append(p)
    caps.append((FR[k]["cap"], t, t + d + LINGER)); t += d; i += 1
    prev = FR[k]["t"]
p, d = play(i, prev, END); parts.append(p); t += d
total = t
# keep captions from overlapping the next one
caps = [(c, a, min(b, caps[j + 1][1]) if j + 1 < len(caps) else b) for j, (c, a, b) in enumerate(caps)]

body = f"{WD}/body.mp4"
lst = f"{WD}/list.txt"
open(lst, "w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", body])

title = f"{WD}/title.png"
text_png(title, TITLE, 74, y_bottom=VY - 60)
inputs = ["-i", body, "-i", title]
fc = [f"[0:v]split[fg][b];[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.28:saturation=0.9[bg];"
      f"[bg][fg]overlay=0:{VY}[v0];[v0][1:v]overlay=0:0[v1]"]
last = "v1"
for j, (c, a, b) in enumerate(caps):
    cp = f"{WD}/cap{j}.png"
    text_png(cp, c, 58, y_top=VY + VH + 50, stroke=4, shadow=False)
    inputs += ["-i", cp]
    fc.append(f"[{last}][{j + 2}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[c{j}]")
    last = f"c{j}"
music = cfg.get("MUSIC")
amap = "0:a"
if music:
    inputs += ["-i", music]
    fc.append(f"[{len(caps) + 2}:a]volume={cfg.get('MUSIC_VOL', 0.45)}[m];[0:a][m]amix=inputs=2:normalize=0:duration=first,"
              f"alimiter=limit=0.95[a]")
    amap = "[a]"
run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", f"[{last}]", "-map", amap,
     "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-maxrate", "4M", "-bufsize", "8M", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT])
print(f"total {total:.2f}", [(c, round(a, 2), round(b, 2)) for c, a, b in caps])
