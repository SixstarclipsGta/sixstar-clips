# Heli video 4: trying to land on a busy road (story.py config). Pause menu (h12 11.0-15.4) cut out. 60s+.
W = "/home/claude/work/heli"
OUT = W + "/v4.mp4"
CARD = "card_v4.png"
DARK = "curves=all='0/0 0.10/0.28 0.40/0.68 1/1',eq=saturation=1.2:contrast=1.06"
SEG = [
    ("h11", 4.0, 8.0, 640, DARK, 0),        # 0 over the lit town, traffic on the right
    ("h11", 12.0, 12.0, 420, DARK, 0),      # 1 lining up over the busy road
    ("h12", 0.0, 10.6, 400, DARK, 0),       # 2 descending into traffic, hits at ~10.3
    ("h12", 8.6, 2.0, 400, DARK, 0, 0.5),   # 3 slow-mo replay of the touchdown
    ("h12", 15.5, 5.5, 420, DARK, 0),       # 4 wreck on its side by the truck, crawling out
    ("h12", 21.0, 8.5, 480, DARK, 0),       # 5 walks away along the road
    ("h13", 0.0, 16.0, 420, DARK, 0),       # 6 walks home past the houses and RVs
]
CAP = [
    (0, 0, 8.0, "THE PLAN", "Rush hour traffic 🚗", "Perfect place to land, right?"),
    (1, 0, 6.0, "THE PLAN", "Picking my parking spot 👀", None),
    (1, 6.0, 12.0, "THE PLAN", "Nice and slow… 🤞", None),
    (2, 0, 6.0, "THE LANDING", "Right… here 👇", None),
    (2, 6.0, 10.6, "THE LANDING", "Mind the truck 😬", None),
    (3, 0, 4.0, "REPLAY", "Let's see that again 🎥", "Half speed"),
    (4, 0, 5.5, "THE DAMAGE", "Parked it. Kind of 😭", "Is this a landing or a crash?"),
    (5, 0, 8.5, "THE AFTERMATH", "Nothing to see here 🚶", None),
    (6, 0, 16.0, "GOING HOME", "Long way home tonight 🏠", "Whose fault was it, me or the truck?"),
]
HUD_SRC = None
HUD_SEG = None
