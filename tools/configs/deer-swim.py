# Deer swim (21 Nov raws 01, 02), 22 Nov style. Dirt bike out of the bushes onto the beach, wades in, swims out,
# something swims ahead... a deer, then side by side (02z = 2x zoom of 02 from 22 s: crop 960x540 at 420,380).
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/sh/deer-game.mp4"
STYLE = "simple"
TITLE = "Not the swim partner I expected 😭"
CRF = 26
DAY = "eq=contrast=1.06:saturation=1.12"
SEG = [
    ("01", 12.0, 3.5, 420, DAY, 0),            # bike bursts out onto the beach
    ("01", 17.5, 3.5, 420, DAY, 0),            # off the bike, into the sea
    ("02", 6.5, 4.0, 420, DAY, 0, 1.3),        # wades in, dives
    ("02", 15.5, 5.0, 420, DAY, 0),            # swimming out... something ahead
    ("02", 20.5, 3.5, 420, DAY, 0),            # it's a deer
    ("02z", 1.5, 5.5, 420, DAY, 0),            # close: the deer right next to him
    ("02", 27.5, 2.3, 420, DAY, 0.4),          # side by side
]
CAP = []
HUD_SRC = None
HUD_SEG = None
