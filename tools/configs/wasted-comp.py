# WASTED compilation (23 Nov): every death from 18 to 22 Nov, each = short lead-up + the WASTED card.
# Hook = crocodile drags him in. Ends on the heli fight: shoots the helicopter down, dies anyway.
# Sources are symlinks in /home/claude/wasted/raw: croc/fight/vault = 18 Nov 17/12/28, heli/runway/swim/jet =
# 19 Nov 09/13/23/31, farm = 22 Nov 21.
W = "/home/claude/wasted/raw"
OUT = "/home/claude/wasted/wasted-game.mp4"
STYLE = "simple"
TITLE = "Every way GTA 6 killed me so far 💀"
CRF = 26
FD = 0.15
DAY = "eq=contrast=1.07:saturation=1.15"
DARK = "curves=all='0/0 0.10/0.26 0.40/0.66 1/1',eq=saturation=1.15:contrast=1.05"
DUSK = "curves=all='0/0 0.10/0.18 0.45/0.58 1/1',eq=saturation=1.12:contrast=1.05"
SEG = [
    ("croc", 9.4, 6.1, 420, DAY, 0),           # HOOK: crocodile lunges, drags him into the water
    ("croc", 26.6, 2.9, 420, DAY, 0),          # WASTED
    ("fight", 19.5, 9.5, 420, DAY, 0, 1.3),    # 1 vs 3 at the stairs, goes down, WASTED
    ("swim", 12.0, 13.2, 420, DAY, 0, 1.5),    # bullets in the water, dives, shot underwater, WASTED
    ("farm", 14.5, 5.8, 420, DAY, 0),          # jumps down to their truck, shot, WASTED
    ("vault", 24.4, 5.35, 500, DARK, 0),       # back over the wall, guard fires, WASTED
    ("runway", 14.5, 10.8, 420, DAY, 0, 1.4),  # runs under the army jet, shot, WASTED
    ("jet", 15.0, 13.2, 420, DAY, 0, 1.5),     # climbs into the fighter jet, shot in the cockpit, WASTED
    ("heli", 13.0, 3.2, 420, DUSK, 0),         # shoots the helicopter down...
    ("heli", 22.5, 7.4, 420, DUSK, 0.5),       # ...and still gets WASTED
]
CAP = []
HUD_SRC = None
HUD_SEG = None
