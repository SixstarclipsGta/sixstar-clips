# Heli video 3: how high can a helicopter go (story.py config). Altitude readout enlarged under the video. 60s+.
W = "/home/claude/work/heli"
OUT = W + "/v3.mp4"
CARD = "card_v3.png"
DARK = "curves=all='0/0 0.10/0.28 0.40/0.68 1/1',eq=saturation=1.22:contrast=1.06"
SEG = [
    ("h09", 4.0, 3.2, 250, DARK, 0),    # 0 teaser: breaking out above the clouds
    ("h07", 10.0, 6.0, 420, DARK, 0),   # 1 start of the climb (293 -> 490 ft)
    ("h08", 0.0, 29.4, 420, DARK, 0),   # 2 climb into the storm clouds (490 -> 1702 ft)
    ("h09", 0.0, 3.2, 40, DARK, 0),     # 3 fiery streak in the cloud, peak ~1975 ft
    ("h09", 3.2, 21.8, 380, DARK, 0),   # 4 above the clouds, levels around 1760 ft
]
SEG_HUD = {"segs": [1, 2, 3, 4], "crop": "84:26:34:1020", "scale": 4.5}
CAP = [
    (0, 0, 3.2, "THE QUESTION", "How high can it go? ⏱️", "Watch the altitude 👇"),
    (1, 0, 6.0, "THE CLIMB", "Full throttle. Straight up 🚁", "HUD"),
    (2, 0, 9.0, "THE CLIMB", "Above the islands 🌅", "HUD"),
    (2, 9.0, 15.0, "THE CLIMB", "Into the storm clouds ⛈️", "HUD"),
    (2, 15.0, 29.4, "THE CLIMB", "Can't see a thing 😰", "HUD"),
    (3, 0, 3.2, "THE CLIMB", "Wait… what was that?? 🔥", "HUD"),
    (4, 0, 6.0, "THE TOP", "Above the clouds 😳", "HUD"),
    (4, 6.0, 21.8, "THE TOP", "Is 1,975 ft the max? 🤔", "HUD"),
]
HUD_SRC = None
HUD_SEG = None
