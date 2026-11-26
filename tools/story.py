"""Build the gas-station money guide: segments joined with short dissolves,
brand card on top, step captions under the video, enlarged money HUD, map at the end."""
import subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont
from card2 import emoji_img, ANTON

W = "/home/claude/work/gas"
OUT = W + "/story.mp4"
FD = 0.35  # dissolve length
GENTLE = "curves=all='0/0 0.10/0.24 0.40/0.62 1/1',eq=saturation=1.2:contrast=1.06"
BASE = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.08"
BRIGHT = "eq=contrast=1.06:saturation=1.15"

# (file, start, dur, crop_x, grade, hold)
SEG = [
    ("g4", 2.5, 3.3, 360, GENTLE, 0),
    ("g1", 0.0, 20.5, 460, BASE, 0),
    ("g1", 26.3, 3.6, 460, BRIGHT, 0),
    ("g4", 11.0, 8.5, 380, GENTLE, 0),
    ("g2", 0.0, 3.5, 460, GENTLE, 0),
    ("g2", 9.5, 14.2, 460, GENTLE, 0),
    ("g3", 3.0, 5.0, 400, BASE, 0),
    ("g5", 7.9, 1.2, 300, BRIGHT, 3.2),
]
# captions: (segment, rel_start, rel_end, label, text)
CAP = [
    (0, 0, 3.3, "STEP 1", "Find this gas station", "📍 location at the end"),
    (1, 0, 6.5, "STEP 2", "Take care of the staff 😤", None),
    (1, 6.5, 14, "STEP 2", "Grab what you can 🛒", None),
    (1, 14, 20.5, "STEP 2", "The clerk fights back 😂", None),
    (2, 0, 3.6, "STEP 3", "Head to the back 🚪", None),
    (3, 0, 4.5, "STEP 3", "This door? 🤔", None),
    (3, 4.5, 8.5, "STEP 3", "Nope… keep going 👀", None),
    (4, 0, 3.5, "STEP 4", "Find the wooden crate 📦", None),
    (5, 0, 8.0, "STEP 4", "Force it open 💪", None),
    (5, 8.0, 14.2, "STEP 4", "Grab everything inside 💰", "HUD"),
    (6, 0, 5.0, "STEP 5", "Leave through the back 🏃", None),
    (7, 0, 5.2, "📍 LOCATION", "Southwind, next to Mile Zero Air Station", None),
]
HUD_SRC = ("g2", 17.8, 5.0)
HUD_SEG = 5  # money counter $0 -> $600 at 18.0-21.0 in g2

CARD = "card.png"  # brand card file inside W
# Per-segment HUD (e.g. the altitude readout): {"segs": [1, 2], "crop": "w:h:x:y", "scale": 3.6}
SEG_HUD = None

# 22 Nov style: STYLE = "simple" -> no brand card, no step captions; one TITLE line on top,
# square video at VY, blurred zoomed copy of the same video behind. Configs set STYLE, TITLE.
STYLE, TITLE, VY = "card", "", 560
TITLE_FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"

# Encoder (21 Nov: smaller files rule). Configs may override.
CRF, PRESET, ABR = 24, "slow", "128k"
ENC_EXTRA = []  # e.g. ["-maxrate", "4M", "-bufsize", "8M"] for 60 s+ videos

# Optional: python3 story.py CONFIG.py  (a file that sets W, OUT, SEG, CAP, HUD_SRC, HUD_SEG)
if len(sys.argv) > 1:
    exec(open(sys.argv[1]).read())


def text_png(path, label, text, sub, hud_space):
    im = Image.new("RGBA", (1080, 380), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    lf = ImageFont.truetype(ANTON, 44)
    y = 18
    if "📍" in label:
        e = emoji_img("📍", 44)
        lw = d.textlength(label.replace("📍 ", ""), font=lf)
        x = (1080 - (e.width + 10 + lw)) // 2
        im.paste(e, (int(x), y + 6), e)
        d.text((x + e.width + 10, y), label.replace("📍 ", ""), font=lf, fill=(45, 226, 208, 255))
    else:
        lw = d.textlength(label, font=lf)
        d.text(((1080 - lw) // 2, y), label, font=lf, fill=(45, 226, 208, 255))
    y += 64
    # main text, emoji split off the end
    emo = ""
    words = text.split(" ")
    if words and not words[-1].isascii():
        emo = words[-1]
        text = " ".join(words[:-1])
    size = 76
    while True:
        f = ImageFont.truetype(ANTON, size)
        tw = d.textlength(text.upper(), font=f)
        ew = (emoji_img(emo, int(size * 0.85)).width + 14) if emo else 0
        if tw + ew <= 1000 or size <= 44:
            break
        size -= 4
    lines = [text.upper()]
    if tw + ew > 1000:  # two lines
        ws = text.upper().split()
        best = None
        for i in range(1, len(ws)):
            a, b = " ".join(ws[:i]), " ".join(ws[i:])
            m = max(d.textlength(a, font=f), d.textlength(b, font=f) + ew)
            if best is None or m < best[0]:
                best = (m, [a, b])
        lines = best[1]
    for i, l in enumerate(lines):
        lw = d.textlength(l, font=f) + (ew if i == len(lines) - 1 else 0)
        x = (1080 - lw) // 2
        # soft shadow
        d.text((x + 3, y + 3), l, font=f, fill=(0, 0, 0, 200))
        d.text((x, y), l, font=f, fill=(255, 255, 255, 255))
        if i == len(lines) - 1 and emo:
            e = emoji_img(emo, int(size * 0.85))
            im.paste(e, (int(x + d.textlength(l, font=f) + 14), y + int(size * 0.12)), e)
        y += int(size * 1.12)
    if sub:
        sf = ImageFont.truetype(ANTON, 40)
        first = sub.split(" ")[0]
        if first.isascii():
            e, s = None, sub.upper()
        else:
            e, s = emoji_img(first, 38), sub[len(first):].strip().upper()
        sw = (e.width + 10 if e else 0) + d.textlength(s, font=sf)
        x = (1080 - sw) // 2
        if e:
            im.paste(e, (int(x), y + 10), e)
            x += e.width + 10
        d.text((x, y + 4), s, font=sf, fill=(200, 205, 215, 255))
    im.save(path)


def title_png(path, text):
    """One plain white line (wraps to 2-3), TikTok-style, emoji kept at the end, centred above the video."""
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    emo = ""
    words = text.split(" ")
    if words and not words[-1].isascii():
        emo, words = words[-1], words[:-1]
    size = 74
    for sz in (74, 70, 66, 62):  # a line that almost fits gets a slightly smaller font, so the emoji never sits alone
        fz = ImageFont.truetype(TITLE_FONT, sz)
        if d.textlength(" ".join(words), font=fz) + (int(sz * 0.95) + 12 if emo else 0) <= 1000:
            size = sz
            break
    f = ImageFont.truetype(TITLE_FONT, size)
    ew = emoji_img(emo, int(size * 0.95)).width + 12 if emo else 0
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > 960 and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    if d.textlength(lines[-1], font=f) + ew > 1000:
        lw_ = lines[-1].split(" ")
        if len(lw_) > 1:  # take the last word down with the emoji
            lines[-1] = " ".join(lw_[:-1]); lines.append(lw_[-1])
        else:
            lines.append("")
    lh = int(size * 1.22)
    y = VY - 70 - lh * len(lines)
    for i, l in enumerate(lines):
        last = i == len(lines) - 1
        lw = d.textlength(l, font=f) + (ew if last else 0)
        x = (1080 - lw) / 2
        for dx, dy in ((0, 3), (2, 2), (-2, 2)):
            d.text((x + dx, y + dy), l, font=f, fill=(0, 0, 0, 150))
        d.text((x, y), l, font=f, fill=(255, 255, 255, 255))
        if last and emo:
            e = emoji_img(emo, int(size * 0.95))
            im.paste(e, (int(x + d.textlength(l, font=f) + (12 if l else 0)), y + int(size * 0.08)), e)
        y += lh
    im.save(path)


def main():
    starts, t = [], 0.0
    def eff(s):
        return s[2] / (s[6] if len(s) > 6 else 1.0) + s[5]
    for i, s in enumerate(SEG):
        starts.append(t)
        t += eff(s) - FD
    total = t + FD
    inputs, fc = [], []
    for i, sg in enumerate(SEG):
        f, ss, du, x, gr, hold = sg[:6]
        sp = sg[6] if len(sg) > 6 else 1.0
        inputs += ["-ss", str(ss), "-t", str(du), "-i", f"{W}/{f}.mp4"]
        src = f"[{i}:v]setpts=(PTS-STARTPTS)/{sp},fps=60000/1001"
        if SEG_HUD and i in SEG_HUD["segs"]:
            hcrop = SEG_HUD.get("crops", {}).get(i, SEG_HUD.get("crop"))  # per-segment crop when the card moves
            cw, ch_, _, _ = [int(v) for v in hcrop.split(":")]
            sw, sh = int(cw * SEG_HUD["scale"]) // 2 * 2, int(ch_ * SEG_HUD["scale"]) // 2 * 2
            fc.append(src + f",split[s{i}][h{i}]")
            hpad = f",tpad=stop_mode=clone:stop_duration={hold}" if hold else ""  # the message stays up through the end hold
            fc.append(f"[h{i}]crop={hcrop},scale={sw}:{sh}:flags=lanczos,pad={sw+8}:{sh+8}:4:4:color=0x{SEG_HUD.get('border', '2de2d0')}{hpad},format=rgba,setpts=PTS+{starts[i]:.3f}/TB[sh{i}]")
            src = f"[s{i}]null"
        elif HUD_SEG is not None and i == HUD_SEG:
            fc.append(src + f",split[s{i}][h{i}]")
            fc.append(f"[h{i}]crop=190:86:1720:20,scale=380:172:flags=lanczos,pad=388:180:4:4:color=0x2de2d0,format=rgba,setpts=PTS+{starts[i]:.3f}/TB[hud]")
            src = f"[s{i}]null"
        v = src + f",{gr},crop=1080:1080:{x}:0,unsharp=5:5:0.6,format=yuv420p,setsar=1,settb=AVTB"
        a = f"[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo" + (("," + ",".join(["atempo=0.5"] * (1 if sp < 0.5 else 0) + [f"atempo={sp * 2 if sp < 0.5 else sp}"])) if sp != 1.0 else "")
        if hold:
            v += f",tpad=stop_mode=clone:stop_duration={hold}"
            a += f",apad=pad_dur={hold}"
        fc.append(v + f"[v{i}]")
        fc.append(a + f",atrim=0:{du / sp + hold}[a{i}]")
    prev_v, prev_a = "v0", "a0"
    for i in range(1, len(SEG)):
        off = starts[i]
        fc.append(f"[{prev_v}][v{i}]xfade=transition=fade:duration={FD}:offset={off:.3f}[x{i}]")
        fc.append(f"[{prev_a}][a{i}]acrossfade=d={FD}[y{i}]")
        prev_v, prev_a = f"x{i}", f"y{i}"
    n = len(SEG)
    if STYLE == "simple":
        tp = f"{W}/{os.path.basename(OUT)[:-4]}_title.png"
        title_png(tp, TITLE)
        inputs += ["-i", tp]
        fc.append(f"[{prev_v}]split[fg][bgs];[bgs]scale=1920:1920,crop=1080:1920:420:0,boxblur=30:3,eq=brightness=-0.16:saturation=0.95[bg];"
                  f"[bg][fg]overlay=0:{VY}[p0];[p0][{n}:v]overlay=0:0[c0]")
    else:
        inputs += ["-i", f"{W}/{CARD}"]
        fc.append(f"[{prev_v}]pad=1080:1920:0:460:color=0x0a0b10[p0];[p0][{n}:v]overlay=0:0[c0]")
    cur = "c0"
    k = n + 1
    for j, (seg, a0, a1, label, text, sub) in enumerate(CAP):
        png = f"{W}/{os.path.basename(OUT)[:-4]}_cap{j}.png"
        text_png(png, label, text, None if sub == "HUD" else sub, sub == "HUD")
        ta = starts[seg] + a0 + (FD / 2 if a0 == 0 and seg > 0 else 0)
        tb = starts[seg] + a1 - (FD / 2 if seg < n - 1 and a1 >= eff(SEG[seg]) - SEG[seg][5] - 0.01 else 0)
        if seg == n - 1 and a1 >= eff(SEG[seg]) - SEG[seg][5] - 0.01:
            tb = total
        inputs += ["-loop", "1", "-t", f"{total:.2f}", "-i", png]
        fc.append(f"[{cur}][{k}:v]overlay=0:1545:enable='between(t,{ta:.3f},{tb:.3f})'[c{j+1}]")
        cur = f"c{j+1}"
        k += 1
        if sub == "HUD" and HUD_SEG is not None:
            t_hud = starts[seg] + (HUD_SRC[1] - SEG[seg][1])
            fc.append(f"[{cur}][hud]overlay=(W-w)/2:1722:eof_action=pass:enable='between(t,{t_hud+0.3:.3f},{tb:.3f})'[ch]")
            cur = "ch"
    if SEG_HUD:
        for i in SEG_HUD["segs"]:
            a, b = starts[i] + FD / 2, starts[i] + eff(SEG[i]) - SEG[i][5] - FD / 2
            if i == n - 1:
                b = total
            a += SEG_HUD.get("delay", 0)
            fc.append(f"[{cur}][sh{i}]overlay=(W-w)/2:1722:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[sh_o{i}]")
            cur = f"sh_o{i}"
    # No fade-in (Zubair, 25 Nov): a black first frame makes viewers skip and becomes the default cover.
    # Frame 0 must be the bright, most attractive frame of the hook.
    fc.append(f"[{cur}]fade=t=out:st={total-0.4:.2f}:d=0.4,format=yuv420p[out]")
    fc.append(f"[{prev_a}]afade=t=in:st=0:d=0.04,afade=t=out:st={total-0.5:.2f}:d=0.5[aout]")
    cmd = ["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", ";".join(fc), "-map", "[out]", "-map", "[aout]",
           "-t", f"{total:.2f}", "-c:v", "libx264", "-preset", PRESET, "-crf", str(CRF), *ENC_EXTRA, "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", ABR, "-movflags", "+faststart", OUT]
    print("total", round(total, 2), "starts", [round(s, 2) for s in starts])
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
