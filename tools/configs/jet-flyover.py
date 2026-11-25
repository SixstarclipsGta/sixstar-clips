# Jet flyover and the jump (24 Nov raws 27, 28; 28 t = 27 t - 10.5). Zubair's idea 1 (25 Nov): play the WHOLE
# flight, not a fast cut. Hook and cover (no fade-in) = the frame he screenshotted: the jet over Mile Zero
# Air Station with 5 stars (27 at 18.0). Then the clip from the start at normal speed: rolls over the sea,
# back to the island, over the base, hit, canopy off, eject, free fall with the parachute prompt on screen,
# tarmac, WASTED, held 3 s. Only the weapon wheel (27 at 16.0 to 17.5) is skipped.
# Line and caption picked by Zubair: "I stole their jet and flew back to say hi 😂" / "wait for the jump 👀".
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/flyover-game.mp4"
STYLE = "simple"
TITLE = "I stole their jet and flew back to say hi 😂"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
AIR = "eq=brightness=0.04:contrast=1.07:saturation=1.16:gamma=1.07"
SEG = [
    ("27", 18.0, 1.9, 420, AIR, 0),             # HOOK and cover: jet over the base, 5 stars
    ("27", 0.5, 15.45, 420, AIR, 0),            # the whole flight: rolls over the sea, back to the island
    ("27", 17.55, 7.35, 420, AIR, 0),           # over the base, hit, canopy off
    ("27", 24.55, 1.5, 250, AIR, 0),            # ejects, thrown clear
    ("27", 25.7, 4.2, 420, AIR, 0),             # free fall
    ("28", 19.05, 10.9, 420, AIR, 3.0),         # still falling, tarmac, WASTED
]
SEG_HUD = {"segs": [0, 2], "crop": "196:40:1704:24", "scale": 4.4, "border": "e0344a"}
CAP = []
HUD_SRC = None
HUD_SEG = None
