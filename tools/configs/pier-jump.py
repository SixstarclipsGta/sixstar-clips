# Sheriff pickup stunt jump (24 Nov raws 15, 16; 16 t = 15 t - 3.02). Hook first: the truck in the air over
# the gap (cinematic slow-mo, landing not shown). Then in order: drives down the track to the broken wooden
# bridge, rolls onto it and stops at the gap, reverses for a run-up, floors it, jumps, lands on the far side,
# and the game prints "Stunt Jump failed" in red (16 from 28.0 s, top right at about x 1628-1890, y 415-440).
# SEG_HUD enlarges that message under the video on the last segment (game's own pixels).
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/pier-game.mp4"
STYLE = "simple"
TITLE = "Can a sheriff truck jump THIS in GTA 6?! 👀"
CRF = 25
BASE = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.08"
CINE = BASE + ",crop=1708:960:106:60,scale=1920:1080:flags=lanczos"  # cinematic cam: zoom out its black bars
SEG = [
    ("16", 25.53, 1.45, 420, CINE, 0, 0.8),     # HOOK and cover (Zubair picked "B"): frame 0 = whole truck in the air over the water, side view; no fade-in
    ("15", 0.4, 7.2, 420, BASE, 0, 1.3),        # sheriff pickup down the track to the bridge
    ("15", 8.0, 8.4, 420, BASE, 0, 1.25),       # onto the broken bridge, stops at the gap
    ("15", 17.6, 4.6, 420, BASE, 0),            # reverses back up the track
    ("15", 21.85, 5.9, 420, BASE, 0),           # run-up, onto the bridge (game camera cut at 15 t = 27.77)
    ("16", 24.4, 3.03, 420, CINE, 0),           # slow-mo in the air, lands on the far side
    ("16", 27.08, 2.5, 420, BASE, 1.6),         # slides to a stop, "Stunt Jump failed" from 28.0
]
SEG_HUD = {"segs": [6], "crop": "280:44:1620:406", "scale": 3.4, "border": "e0344a", "delay": 0.8}
CAP = []
HUD_SRC = None
HUD_SEG = None
