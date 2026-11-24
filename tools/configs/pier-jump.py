# Sheriff pickup stunt jump (24 Nov raws 15, 16; 16 t = 15 t - 3.02). Hook first: the truck in the air over
# the gap (cinematic slow-mo, landing not shown). Then in order: drives down the track to the broken wooden
# bridge, rolls onto it and stops at the gap, reverses for a run-up, floors it, jumps, lands on the far side,
# and the game prints "Stunt Jump failed" in red (16 from 28.0 s, top right at about x 1628-1890, y 415-440).
# SEG_HUD enlarges that message under the video on the last segment (game's own pixels).
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/pier-game.mp4"
STYLE = "simple"
TITLE = "Made the jump. STILL failed 😤"
CRF = 25
BASE = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.08"
SEG = [
    ("16", 24.7, 2.0, 420, BASE, 0),            # HOOK: truck in the air over the water
    ("15", 0.4, 7.2, 420, BASE, 0, 1.3),        # sheriff pickup down the track to the bridge
    ("15", 8.0, 8.4, 420, BASE, 0, 1.25),       # onto the broken bridge, stops at the gap
    ("15", 17.6, 4.6, 420, BASE, 0),            # reverses back up the track
    ("15", 21.85, 7.65, 420, BASE, 0),          # run-up, onto the bridge, take-off
    ("16", 26.13, 2.0, 420, BASE, 0),           # in the air, lands on the far side
    ("16", 27.78, 1.8, 420, BASE, 1.6),         # "Stunt Jump failed"
]
SEG_HUD = {"segs": [6], "crop": "280:44:1620:406", "scale": 3.4, "border": "e0344a", "delay": 0.1}
CAP = []
HUD_SRC = None
HUD_SEG = None
