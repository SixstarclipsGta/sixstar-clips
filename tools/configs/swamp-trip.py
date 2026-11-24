# Swamp trip (24 Nov raws 07, 09, 10, 11, 12, 13; 13 t = 12 t - 23.05), 22 Nov style, in the order it happened:
# gets out of the Rancher next to two alligators and walks over them, kicks the second one, drives into the
# mangroves and gets out, finds a shirtless man crouched in the grass, fist fight, knocks him out and carries
# him, a deer rams him flat, wades into the water and the screen goes red (attacker never visible),
# walks on injured, an alligator takes him. WASTED.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/swamp-game.mp4"
STYLE = "simple"
TITLE = "Everything in this swamp wants me dead 💀"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
BASE = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.08"
HURT = "eq=contrast=1.05:saturation=1.08:gamma=1.05"
KILL = "eq=contrast=1.04:saturation=1.05"
SEG = [
    ("07", 2.6, 2.6, 330, BASE, 0),             # HOOK: out of the truck, two alligators right there
    ("07", 4.85, 6.75, 420, BASE, 0),           # walks onto the first one, stands on it
    ("07", 11.25, 4.95, 440, BASE, 0),          # kicks the second one
    ("09", 1.5, 3.5, 420, BASE, 0, 1.2),        # Rancher into the mangroves
    ("09", 7.2, 2.3, 200, BASE, 0),             # gets out
    ("10", 0.0, 4.6, 420, BASE, 0),             # a man crouched in the grass
    ("10", 13.6, 6.2, 420, BASE, 0),            # fist fight
    ("10", 19.45, 3.55, 380, BASE, 0, 1.3),     # he's out
    ("10", 24.2, 5.4, 380, BASE, 0, 1.2),       # carries him off
    ("11", 4.0, 8.0, 380, BASE, 0),             # deer rams him flat
    ("12", 10.6, 5.9, 330, BASE, 0),            # wades in, screen goes red
    ("13", 15.5, 5.7, 400, HURT, 0, 1.3),       # limping through the marsh
    ("13", 20.85, 2.55, 400, HURT, 0),          # alligator lunges
    ("13", 23.05, 2.55, 260, HURT, 0),          # it has him
    ("13", 25.25, 4.5, 420, KILL, 0.8),         # kill cam, WASTED
]
CAP = []
HUD_SRC = None
HUD_SEG = None
