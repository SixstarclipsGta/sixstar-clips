# Bigfoot encounter on the quad, 21 Nov 2026 batch 2 (raw 06 = continuation of 05, overlap: 06 t = 05 t - 18.0).
# 06z15 / 06z2 = 1.5x / 2x zooms of 06 from 6.0 s (so z-time = 06 time - 6.0):
#   ffmpeg -ss 6 -t 6 -i 06.mp4 -vf "crop=720:720:570:140,scale=1080:1080,pad=1920:1080:0:0" 06z15.mp4
#   06z3: crop=360:360:750:290,scale=1080:1080,unsharp=5:5:0.8
#   ffmpeg -ss 6 -t 6 -i 06.mp4 -vf "crop=540:540:660:230,scale=1080:1080,pad=1920:1080:0:0" 06z2.mp4
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/bigfoot-game.mp4"
CARD = "bfcard.png"
CRF = 25
DAY = "eq=contrast=1.07:saturation=1.15:brightness=0.03"
SEG = [
    ("06z2", 0.8, 1.2, 0, DAY, 0),          # 0 something crouched on the path (2x)
    ("06z3", 2.0, 0.9, 0, DAY, 0, 0.5),     # 1 it gets up (3x, half speed)
    ("06z3", 2.45, 0.25, 0, DAY, 1.6),      # 2 freeze: bigfoot?
    ("06z15", 3.0, 2.3, 0, DAY, 0, 0.75),   # 3 shots, it runs past the body
    ("06", 11.3, 3.2, 420, DAY, 0),         # 4 gone into the bushes, body left on the path
    ("06z3", 2.6, 1.4, 0, DAY, 0, 0.4),     # 5 replay, 3x at 0.4 speed
    ("06", 14.5, 3.0, 420, DAY, 0.8),       # 6 riding into the swamp after it
]
CAP = [
    (0, 0, 1.2, "SHORTCUT", "Something's on the path… 👀", None),
    (1, 0, 1.8, "WAIT", "Oh sh*t… the f*ck?! 😳", None),
    (2, 0, 1.85, "WAIT", "Is that… BIGFOOT?? 🦶", None),
    (3, 0, 3.07, "IT RAN", "It was over a body 🩸", None),
    (4, 0, 3.2, "GONE", "Where did it go?? 😰", None),
    (5, 0, 3.5, "REPLAY", "Look at it… 👀", None),
    (6, 0, 3.8, "THE SWAMP", "Going after it… 👀", "Part 2 on my profile 👀"),
]
HUD_SRC = None
HUD_SEG = None
