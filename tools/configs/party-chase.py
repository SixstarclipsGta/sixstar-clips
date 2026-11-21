# Beach party police chase, 21 Nov 2026 (raws in raw/2026-11-21/, here numbered 04..07). ~30 s.
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/chase/chase.mp4"
CARD = "chasecard.png"
DAY = "eq=contrast=1.06:saturation=1.15"
CRF = 26
SEG = [
    ("03", 9.0, 2.6, 420, DAY, 0),    # 0 the fist fight
    ("04", 0.0, 2.8, 420, DAY, 0),    # 0 gun at the party, everyone runs
    ("04", 25.0, 3.0, 360, DAY, 0),   # 1 runs at the man by the boat, tackle
    ("05", 3.5, 4.5, 560, DAY, 0),    # 2 boat escape, 3 stars, police boat, shots
    ("05", 27.0, 2.6, 250, DAY, 0),   # 3 police RIB right next to him
    ("06", 14.5, 8.0, 420, DAY, 0),   # 4 sheriff car: cop, crash, smashed front, pole
    ("06", 26.5, 3.16, 150, DAY, 0),  # 5 Patrol Unit rams him into the fence
    ("07", 20.0, 6.0, 420, DAY, 0),   # 6 hides the car at Boone Speedway among people
]
CAP = [
    (0, 0, 2.6, "THE PARTY", "They wouldn't let me in 😤", None),
    (1, 0, 2.8, "THE PARTY", "So I came back… 😬", None),
    (2, 0, 3.0, "WANTED", "Excuse me, I need a boat 🏃", None),
    (3, 0, 4.5, "3 STARS", "Cops on the water 🚨", None),
    (4, 0, 2.6, "3 STARS", "Way too close 😰", None),
    (5, 0, 3.5, "PLAN B", "Grab a sheriff car 🚓", None),
    (5, 3.5, 8.0, "PLAN B", "Nobody stops a cop… right? 😬", None),
    (6, 0, 3.16, "PLAN B", "Wrong. Other cops rammed me 😤", None),
    (7, 0, 6.0, "HIDING", "Blend in at the speedway 👀", "Next: I joined their race 🏁"),
]
HUD_SRC = None
HUD_SEG = None
