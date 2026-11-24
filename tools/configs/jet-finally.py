# Jet attempt #2: he finally flies (24 Nov raws 24, 26, 27, 28; 26 t = 24 t - 26.5, 28 t = 27 t - 10.5;
# 26 -> 27 has a gap). In order: sheriff pickup pulls up at the fighters with stars on, runs to a P-996 Lazer,
# climbs in, afterburner, taxi, take-off over the sea, turns back over Mile Zero, takes a missile over the
# base (27 at 20.5), ejects, never opens the parachute (prompt on screen), hits the tarmac, WASTED.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/jet2-game.mp4"
STYLE = "simple"
TITLE = "I finally got to fly the jet 😤"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
DAY = "eq=contrast=1.06:saturation=1.15"
AIR = "eq=brightness=0.03:contrast=1.06:saturation=1.15:gamma=1.05"
SEG = [
    ("24", 15.0, 2.3, 330, DAY, 0),             # HOOK: sheriff pickup pulls up at the fighter jets
    ("24", 16.95, 6.65, 230, DAY, 0, 1.15),     # out, sprint across the apron
    ("24", 23.25, 3.6, 230, DAY, 0),            # up the ladder, in the cockpit
    ("26", 4.6, 4.9, 420, DAY, 0),              # afterburner, rolling
    ("26", 9.15, 6.85, 420, DAY, 0, 1.7),       # taxi onto the runway
    ("26", 15.65, 8.35, 420, AIR, 0),           # take-off, over the sea
    ("26", 23.65, 5.95, 420, AIR, 0, 1.3),      # banking
    ("27", 3.0, 10.0, 420, AIR, 0, 1.4),        # rolls, back toward the island
    ("27", 12.65, 3.35, 420, AIR, 0),           # over Mile Zero
    ("27", 17.4, 3.6, 400, AIR, 0),             # (weapon wheel skipped) low over the base, missile hit
    ("27", 20.65, 3.95, 420, AIR, 0),           # spinning, canopy off, eject
    ("28", 13.75, 1.85, 250, AIR, 0),           # thrown clear, jet falls away
    ("28", 15.25, 10.75, 420, AIR, 0, 1.4),     # free fall over the hangars, parachute never opens
    ("28", 25.65, 4.1, 420, DAY, 1.0),          # tarmac, WASTED
]
CAP = []
HUD_SRC = None
HUD_SEG = None
