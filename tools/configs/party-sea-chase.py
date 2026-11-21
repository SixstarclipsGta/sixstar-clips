# Beach party -> escape from the cops by sea, 21 Nov 2026 (raws 03, 04, 05 of raw/2026-11-21). ~31 s. Sea only, no car.
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/chase/sea.mp4"
CARD = "seacard.png"
CRF = 26
DAY = "eq=contrast=1.06:saturation=1.15"
SEG = [
    ("03", 9.0, 2.6, 420, DAY, 0),          # 0 fist fight at the party
    ("04", 0.0, 3.0, 420, DAY, 0),          # 1 gun out, everyone runs
    ("04", 15.8, 3.0, 420, DAY, 0),         # 2 cops called, runs into the sea
    ("04", 24.8, 3.1, 360, DAY, 0),         # 3 tackles a man by a boat
    ("05", 0.0, 14.0, 560, DAY, 0, 1.15),   # 4 boat escape, 3 stars, sirens, police boat
    ("05", 15.0, 7.0, 420, DAY, 0, 1.15),   # 5 under the bridge
    ("05", 26.5, 3.1, 250, DAY, 0),         # 6 a boat pulls up right next to him
]
CAP = [
    (0, 0, 2.6, "THE PARTY", "They wouldn't let me in 😤", None),
    (1, 0, 3.0, "THE PARTY", "So I came back… 😬", None),
    (2, 0, 3.0, "WANTED", "Someone called the cops 🚨", None),
    (3, 0, 3.1, "WANTED", "Excuse me, I need your boat 🏃", None),
    (4, 0, 6.0, "3 STARS", "Cops on the water 🚨", None),
    (4, 6.0, 12.17, "3 STARS", "Full throttle. Don't look back 😰", None),
    (5, 0, 6.09, "3 STARS", "Under the bridge… 👀", None),
    (6, 0, 3.1, "3 STARS", "Who is THAT? 😳", "Part 2: did I lose them? 👀"),
]
SEG_HUD = {"segs": [4, 5], "crop": "150:100:1760:12", "scale": 1.8}
HUD_SRC = None
HUD_SEG = None
