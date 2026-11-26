# "Bigfoot turned HUMAN" (24 Nov raws 09 and 10). Zubair's idea 3 of 26 Nov. There is NO Bigfoot creature in the
# raws: the story is the shirtless long-haired swamp man, sold as "Bigfoot's human form" (question form).
# Hook and cover (no fade-in) = 10 at 15.25, zoomed 1.33x: the man charging at Jason. Then in his order:
# truck off the track into the mangroves (short), gets out and holds his head, pulls the pistol and aims at
# the bushes, finds the man crouched in the grass, the man runs, chase with the man vanishing ahead, he turns
# and charges, fight, knocked out, Jason carries him; end held 3 s.
# Line and caption picked by Zubair (2d): "Bigfoot turned HUMAN in GTA 6?! 😳" / "is this a secret character? 👀".
# SOUND: game sound only, natural level, no music (his rule of 26 Nov). No radio found in 09 0 to 10 s.
# Skipped: 09 12 to 20.9 (running, weapon wheel), 10 4.6 to 7.2 (camera points at the sky).
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/bigfoot-human-game.mp4"
STYLE = "simple"
TITLE = "Bigfoot turned HUMAN in GTA 6?! 😳"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
DAY = "eq=brightness=0.03:contrast=1.07:saturation=1.16:gamma=1.05"
# Jason stands far left in 09, where the minimap and a top-left HUD bar sit: zoom 1.33x on the upper-left
# 1440x810 instead (delogo left coloured streaks, don't use it).
ZL = ",crop=1440:810:0:50,scale=1920:1080:flags=lanczos"
DARK = "eq=brightness=0.05:contrast=1.06:saturation=1.16:gamma=1.14" + ZL
HOOK = "eq=brightness=0.05:contrast=1.08:saturation=1.18:gamma=1.12,crop=1440:810:150:250,scale=1920:1080:flags=lanczos"
SEG = [
    ("10", 15.25, 1.0, 410, HOOK, 0),           # HOOK and cover: the man charges
    ("09", 1.5, 3.7, 420, DAY, 0),              # truck off the track into the mangroves
    ("09", 7.6, 4.6, 260, DARK, 0),             # gets out, holds his head, starts running
    ("09", 20.9, 4.4, 120, DAY + ",crop=1386:780:0:90,scale=1920:1080:flags=lanczos", 0),        # pistol out, aims at the bushes
    ("10", 0.0, 4.6, 420, DAY, 0),              # finds the man crouched in the grass
    ("10", 7.2, 0.95, 700, DAY, 0),             # the man runs
    ("10", 7.8, 22.1, 340, DAY, 3.0),           # chase, he vanishes, turns, fight, knocked out, carried
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
