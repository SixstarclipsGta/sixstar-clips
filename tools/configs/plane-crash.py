# Plane crash journey, 21 Nov 2026 batch 2 (raws 01-04 on the way, 08 quad + attacker, 10 ambulance crash). ~65 s.
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/plane-game.mp4"
CARD = "planecard.png"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
WOOD = "eq=contrast=1.06:saturation=1.15:gamma=1.15:brightness=0.02"
SEG = [
    ("04", 16.5, 2.5, 420, DAY, 0),          # 0 cold open: Jason at the burning wreck
    ("01", 25.0, 4.8, 420, DAY, 0, 1.2),     # 1 bridge, smoke column ahead
    ("02", 1.0, 8.0, 420, WOOD, 0, 1.3),     # 2 off the road, through the bushes
    ("02", 11.0, 3.5, 420, WOOD, 0),         # 3 smoke over the trees
    ("02", 20.5, 9.2, 420, WOOD, 0, 1.3),    # 4 mud, into the swamp water
    ("03", 0.0, 9.0, 420, WOOD, 0, 1.5),     # 5 wading through the swamp
    ("03", 9.5, 9.5, 420, WOOD, 0, 1.3),     # 6 running through bushes and trees
    ("03", 19.0, 2.6, 420, DAY, 0),          # 7 smoke much closer
    ("04", 7.0, 4.5, 420, DAY, 0),           # 8 running at the black smoke
    ("04", 11.5, 11.0, 420, DAY, 0),         # 9 the burning wreck, wing in the grass
    ("08", 0.0, 4.8, 420, DAY, 0),           # 10 back with a quad: a man attacks him
    ("10", 19.0, 6.5, 420, DAY, 0.7),        # 11 drives into the ambulance
]
CAP = [
    (0, 0, 2.5, "PLANE DOWN", "Wait for how I got here 👀", None),
    (1, 0, 4.0, "ON THE BRIDGE", "What's that smoke? 👀", None),
    (2, 0, 6.15, "OFF ROAD", "Shortcut. Trust me 😤", None),
    (3, 0, 3.5, "OFF ROAD", "It's getting bigger… 😳", None),
    (4, 0, 7.08, "THE SWAMP", "Uh oh… 😬", None),
    (5, 0, 6.0, "ON FOOT", "Truck's done. Walking it 🌊", None),
    (6, 0, 7.31, "ON FOOT", "Through the bushes… 🌿", None),
    (7, 0, 2.6, "CLOSER", "Almost there… 🤞", None),
    (8, 0, 4.5, "CLOSER", "There it is… 🔥", None),
    (9, 0, 11.0, "PLANE CRASH", "Still burning 🔥", None),
    (10, 0, 4.8, "BACK WITH A QUAD", "Who is THIS guy?! 😳", None),
    (11, 0, 7.2, "AMBULANCE", "Called an ambulance… kind of 🚑", "Something was watching me on the way 👀"),
]
HUD_SRC = None
HUD_SEG = None
