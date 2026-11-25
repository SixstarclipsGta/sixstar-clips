# Police SUV into the military base (24 Nov raws 22, 23; 23 t = 22 t - 23.02). No real ending in the files:
# it ends inside the base as the first wanted star starts blinking (23 from 25.6 s, top right).
# Hook and cover (no fade-in): the Key Lento Police SUV rolling up under the MILE ZERO AIR STATION sign,
# slow-mo, cut before it passes. Then in order: walks up to the Vapid Police Montagne at the store, gets in,
# pulls out, drives, the "Military area: entry is not allowed" sign with an alligator lying next to it
# (23 at 14.2 s), the gate road, through the gate past the guard, inside, star. Ending held ~3 s (his note).
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/suv-game.mp4"
STYLE = "simple"
TITLE = "Will the army stop a police car in GTA 6?! 👀"
CRF = 25
BASE = "eq=brightness=0.06:contrast=1.08:saturation=1.18:gamma=1.12"
ZOOM = BASE + ",crop=1600:900:320:120,scale=1920:1080:flags=lanczos"
SEG = [
    ("23", 23.45, 0.5, 480, ZOOM, 0, 0.4),      # HOOK and cover: SUV under the gate sign, slow-mo
    ("22", 8.5, 6.7, 420, BASE, 0, 1.3),        # walks across the lot to the police SUV
    ("22", 14.85, 4.05, 340, BASE, 0),          # opens the door, gets in
    ("22", 25.6, 4.0, 420, BASE, 0),            # backs out, onto the road
    ("23", 6.25, 7.05, 420, BASE, 0, 1.5),      # drives toward the base
    ("23", 12.95, 3.25, 560, BASE, 0),          # "Military area: entry is not allowed" + alligator
    ("23", 15.85, 6.55, 420, BASE, 0, 1.3),     # the road to the gate, radar dome
    ("23", 22.05, 3.45, 520, BASE, 0),          # under the sign, through the gate, past the guard
    ("23", 25.15, 4.5, 420, BASE, 3.0),         # inside the base, first star blinks (ends with the star lit)
]
SEG_HUD = {"segs": [8], "crop": "100:64:1814:10", "scale": 3.4, "border": "e0344a", "delay": 0.35}
CAP = []
HUD_SRC = None
HUD_SEG = None
