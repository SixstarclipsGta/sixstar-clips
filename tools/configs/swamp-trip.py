# v2 (Zubair, 24 Nov): deer first as the hook, then the swamp man, then the alligators (shorter), same ending.
# Swamp trip (24 Nov raws 07, 09, 10, 11, 12, 13; 13 t = 12 t - 23.05), 22 Nov style, in the order it happened:
# gets out of the Rancher next to two alligators and walks over them, kicks the second one, drives into the
# mangroves and gets out, finds a shirtless man crouched in the grass, fist fight, knocks him out and carries
# him, a deer rams him flat, wades into the water and the screen goes red (attacker never visible),
# walks on injured, an alligator takes him. WASTED.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/swamp-game.mp4"
STYLE = "simple"
TITLE = "I just wanted a peaceful walk in GTA 6 💔"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
BASE = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.08"
HURT = "eq=contrast=1.05:saturation=1.08:gamma=1.05"
KILL = "eq=contrast=1.04:saturation=1.05"
SEG = [
    ("11", 5.9, 6.1, 380, BASE, 0),             # HOOK: deer rams him flat in the first second
    ("09", 1.5, 3.5, 420, BASE, 0, 1.2),        # Rancher into the mangroves
    ("09", 7.2, 2.3, 200, BASE, 0),             # gets out
    ("10", 0.0, 4.6, 420, BASE, 0),             # a man crouched in the grass
    ("10", 12.4, 7.4, 420, BASE, 0),            # he comes over, fist fight
    ("10", 19.45, 3.55, 380, BASE, 0),          # he's out
    ("10", 24.2, 5.4, 380, BASE, 0),            # carries him off
    ("07", 2.6, 2.6, 330, BASE, 0),             # out of the truck, two alligators right there
    ("07", 4.85, 4.75, 420, BASE, 0),           # walks onto the first one
    ("07", 11.9, 3.5, 440, BASE, 0),            # kicks the second one
    ("12", 9.6, 6.9, 330, BASE, 0),             # wades in, screen goes red
    ("13", 15.5, 5.7, 400, HURT, 0),            # limping through the marsh
    ("13", 20.85, 2.55, 400, HURT, 0),          # alligator lunges
    ("13", 23.05, 2.55, 260, HURT, 0),          # it has him
    ("13", 25.25, 4.5, 420, KILL, 0.8),         # kill cam, WASTED
]
CAP = []
HUD_SRC = None
HUD_SEG = None
