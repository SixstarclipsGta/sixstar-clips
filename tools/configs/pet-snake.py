# "My pet python in GTA 6 looks REAL 😳" (27 Nov raw 01, Zubair's pick 4 + caption c "is this a python? 🐍").
# Correction bait: it is a corn snake, not a python. Single clip, not a story: hook = the close-up snake as it
# coils (frame 0 = cover), then the clip from the first frame: Jason at the terrarium, puts a blue bowl in,
# inspect close-up of the snake sliding and coiling (9.2 to 26); the walk-away (26 to 29.7) is left out.
# FULL frame (the close-up fills the width). Game sound only (no radio or music in the spectrogram).
W = "/home/claude/work/r1127"
OUT = "/home/claude/work/out/pet-snake-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "My pet python in GTA 6 looks REAL 😳"
CRF = 24
BASE = "eq=brightness=0.04:contrast=1.07:saturation=1.15:gamma=1.06"
SEG = [
    ("01", 13.3, 2.0, 0, BASE, 0, 0.8),   # HOOK and cover: the snake on the log, coils up
    ("01", 0.0, 9.03, 0, BASE, 0),        # from the first frame: Jason at the terrarium, closes the lid
    ("01", 9.22, 16.78, 0, BASE, 2.0),    # inspect close-up (game's 0.2 s dark dip at 9.03 skipped), snake slides and coils
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
