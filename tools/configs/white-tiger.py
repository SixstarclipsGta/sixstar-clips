# White tiger (24 Nov raws 03, 04; 04 t = 03 t - 12.52), 22 Nov style. In order: a white tiger walks out from
# behind the crates right behind him, he runs, climbs the tank and the container onto the roofs, the tiger
# follows below, he comes down onto the tank, it waits beside him, he steps off, it kills him. WASTED.
# Crop changes inside continuous footage start FD early, so the dissolve reads as a soft slide.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/tiger-game.mp4"
STYLE = "simple"
TITLE = "POV: you meet a white tiger in GTA 6 👀"
CRF = 26
SHADE = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.08"
KILL = "eq=contrast=1.04:saturation=1.05"
SEG = [
    ("03", 2.9, 3.3, 340, SHADE, 0),            # HOOK: tiger comes out from behind the crates
    ("03", 5.85, 1.55, 190, SHADE, 0),          # right behind him, he runs
    ("03", 7.05, 5.55, 400, SHADE, 0),          # tank, container, onto the roof
    ("03", 12.25, 5.35, 380, SHADE, 0, 1.6),    # across the roofs
    ("03", 17.25, 5.35, 380, SHADE, 0),         # looks down, tiger below
    ("03", 22.25, 1.65, 110, SHADE, 0),         # tiger right under the container
    ("03", 23.55, 2.05, 200, SHADE, 0),         # climbs down onto the tank
    ("04", 12.75, 7.7, 380, SHADE, 0, 1.25),    # on the tank, tiger waits beside him
    ("04", 21.7, 2.9, 380, SHADE, 0),           # (weapon wheel skipped) it sniffs at him, he steps off
    ("04", 24.25, 2.35, 250, SHADE, 0),         # attack
    ("04", 26.25, 3.38, 330, KILL, 0.9),        # kill cam, WASTED
]
CAP = []
HUD_SRC = None
HUD_SEG = None
