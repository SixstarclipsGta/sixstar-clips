# Farm security fails (22 Nov raws 22, 23), 23 Nov, Zubair's picks: guard runs away instead of shooting (23 ~1.1),
# guard falls onto the road (23 ~17.2, the hook), gate guard runs instead of fighting (23 ~26.0), then the
# flying gate guard (23 ~27.8). Zooms are 2.67x crops (720x405) scaled to 1920x1080:
# 23z1 = 23 from 0.5 at (0,120); 23z2 = 23 from 17.0 at (900,330); 23z3 = 23 from 25.9 at (480,380);
# 23z = 23 from 27.3, crop 1100x620 at (760,460).
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/cowards-game.mp4"
STYLE = "simple"
TITLE = "13 years for this AI 💀"
CRF = 26
FD = 0.2
DAY = "eq=contrast=1.07:saturation=1.15"
SEG = [
    ("23z2", 0.3, 0.9, 150, DAY, 0.3, 0.6),    # HOOK: guard falls flat onto the road
    ("22", 12.0, 6.0, 420, DAY, 0, 1.3),       # how it started: I take their black truck
    ("23", 0.0, 1.4, 420, DAY, 0),             # pull out...
    ("23z1", 0.1, 0.8, 100, DAY, 0.3, 0.6),    # their guard runs away instead of shooting
    ("23", 3.5, 6.5, 420, DAY, 0, 1.5),        # through the yard
    ("23", 16.5, 1.8, 600, DAY, 0),            # the fall, wide
    ("23", 21.0, 4.9, 420, DAY, 0, 1.3),       # to the gate
    ("23z3", 0.1, 0.9, 250, DAY, 0.2, 0.6),    # gate guard runs instead of fighting
    ("23", 26.9, 1.7, 700, DAY, 0),            # and this one... flies
    ("23z", 0.3, 0.5, 600, DAY, 0.9, 0.35),    # replay, freeze mid-air
    ("23z", 0.8, 0.45, 600, DAY, 0, 0.5),      # lands
    ("23", 28.6, 1.3, 420, DAY, 0.5),          # drive off
]
CAP = []
HUD_SRC = None
HUD_SEG = None
