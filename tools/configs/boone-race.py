# Boone Speedway oval elimination race, 21 Nov 2026 (raws 08, 09, 10 of raw/2026-11-21). ~32 s.
# Entry $450 (game's rent screen), prize $1,500 (Zubair). 09 -> 10 overlap: 10 starts at 09's 26.53.
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/race/race.mp4"
CARD = "racecard.png"
CRF = 27
DAY = "eq=contrast=1.06:saturation=1.15"
SEG = [
    ("08", 27.9, 1.86, 420, DAY, 0),    # 0 GO!
    ("09", 0.0, 9.0, 420, DAY, 0),      # 1 lap 1, passing people, 4th -> 2nd
    ("09", 9.0, 6.0, 420, DAY, 0),      # 2 holding 2nd
    ("10", 14.0, 15.98, 420, DAY, 0.7), # 3 lap 3: monster trucks, elimination imminent, crash, ELIMINATED
]
CAP = [
    (0, 0, 1.86, "ENTRY $450", "1st place wins $1,500 💰", None),
    (1, 0, 9.0, "LAP 1", "Passing everyone 😤", None),
    (2, 0, 6.0, "LAP 1", "Up to 2nd place… 🤞", None),
    (3, 0, 6.5, "LAP 3", "Almost there… 👀", None),
    (3, 6.5, 9.0, "LAP 3", "Wait… MONSTER TRUCKS?! 😳", None),
    (3, 9.0, 12.3, "LAP 3", "Dropping fast 😰", None),
    (3, 12.3, 16.68, "RESULT", "$450 gone 💀", "Race again or never? 👇"),
]
SEG_HUD = {"segs": [1, 2], "crop": "190:190:1715:855", "scale": 0.95}
HUD_SRC = None
HUD_SEG = None
