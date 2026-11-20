# Heli video 2: chasing a yacht low over the water (story.py config). Target 60s+ (TikTok pays from 1 min).
W = "/home/claude/work/heli"
OUT = W + "/v2.mp4"
CARD = "card_v2.png"
DARK = "curves=all='0/0 0.10/0.28 0.40/0.68 1/1',eq=saturation=1.22:contrast=1.06"
SEG = [
    ("h05", 15.0, 3.6, 440, DARK, 0),   # 0 teaser: side by side with the boat
    ("h04", 19.0, 11.0, 440, DARK, 0),  # 1 hover over the yacht, it speeds off ~9.5
    ("h05", 0.0, 27.5, 430, DARK, 0),   # 2 the chase
    ("h06", 0.0, 13.0, 420, DARK, 0),   # 3 chase continues (h06 starts at h05 27.5)
    ("h06", 13.0, 11.5, 420, DARK, 0),  # 4 banks away into the sunset
]
CAP = [
    (0, 0, 3.6, "CHASE MODE", "Low and fast 🚁", "42 ft above the water"),
    (1, 0, 5.5, "THE TARGET", "Found a yacht 🛥️", "Let's say hi"),
    (1, 5.5, 9.3, "THE TARGET", "Hovering right on top 😈", None),
    (1, 9.3, 11.0, "THE TARGET", "They're running 👀", None),
    (2, 0, 8.0, "THE CHASE", "Don't let them escape 🏃", None),
    (2, 8.0, 16.0, "THE CHASE", "Wing to wing 😤", "Side by side at 42 ft"),
    (2, 16.0, 27.5, "THE CHASE", "They can't shake me 😂", None),
    (3, 0, 7.0, "THE CHASE", "Still on their tail 👀", None),
    (3, 7.0, 13.0, "THE CHASE", "Wait… where are they going? 🤔", None),
    (4, 0, 11.5, "THE ENDING", "Fine. Keep your yacht 🌅", "☁️ Next: how high can it go?"),
]
HUD_SRC = None
HUD_SEG = None
