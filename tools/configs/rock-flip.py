# "Wtf is this, made my car crash 😤" (Zubair's own line, 27 Nov raw 07, "use as a whole 30 sec").
# Whole clip from the first frame, FULL frame, no hook, game sound only. Content: drives the black pickup from the
# gas station at sunset (0 to 12), hits a rock and the pickup flips end over end (13.0 to 16.5, best frame 13.4),
# lands on its wheels (17), he gets out (20 to 22), walks back to the rocks on the road (26 to 29.9). End held 2 s.
W = "/home/claude/work/r1127"
OUT = "/home/claude/work/out/rock-flip-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "Fixed the car for Lucia. Then GTA 6 did this 😤"  # his pick 2 (27 Nov), replaces his first line
CRF = 25
G = "curves=all='0/0 0.10/0.24 0.40/0.62 1/1',eq=saturation=1.15:contrast=1.06"
SEG = [
    ("07", 0.0, 29.97, 0, G, 2.0),   # whole clip
]
SEG_HUD = None
CAP = [  # beat captions under the video (Zubair asked for "captions when it happens")
    (0, 0.0, 5.0, "", "Car fully repaired for Lucia 🔧", None),
    (0, 5.0, 11.8, "", "Driving it to her real careful 😌", None),
    (0, 11.8, 13.0, "", "Wait… what's on the road? 👀", None),
    (0, 13.0, 16.8, "", "NOOOO 😭", None),
    (0, 16.8, 20.5, "", "It landed?! 🤯", None),
    (0, 20.5, 25.8, "", "How do I explain this to Lucia 💀", None),
    (0, 25.8, 29.97, "", "Found the problem 😤", None),
]
HUD_SRC = None
HUD_SEG = None
PRESET = "veryfast"
