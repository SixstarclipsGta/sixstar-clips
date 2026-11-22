# Plane crash journey v2 (22 Nov style: one title line, no card, no step captions, no ambulance).
# Raws 01-04 of the 21 Nov afternoon batch (local /home/claude/w21b/raw). ~65 s.
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/plane2-game.mp4"
STYLE = "simple"
TITLE = "I just wanted to see what that smoke was 😭"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
WOOD = "eq=contrast=1.06:saturation=1.15:gamma=1.15:brightness=0.02"
SEG = [
    ("04", 16.5, 2.5, 420, DAY, 0),          # cold open: Jason at the burning wreck
    ("01", 25.0, 4.8, 420, DAY, 0, 1.2),     # bridge, smoke column ahead
    ("02", 1.0, 8.0, 420, WOOD, 0, 1.15),    # off the road, smashing through bushes
    ("02", 11.0, 6.0, 420, WOOD, 0),         # tall grass, smoke over the trees
    ("02", 19.0, 10.8, 420, WOOD, 0),        # mud: wheels spinning, crawling, into the swamp water (the struggle)
    ("03", 0.0, 9.0, 420, WOOD, 0, 1.5),     # truck's done: wading through the swamp
    ("03", 9.5, 9.5, 420, WOOD, 0, 1.3),     # running through bushes and trees
    ("03", 19.0, 2.6, 420, DAY, 0),          # smoke much closer
    ("04", 7.0, 4.5, 420, DAY, 0),           # running at the black smoke
    ("04", 11.5, 18.0, 420, DAY, 0.6),       # the burning wreck, wing in the grass
]
CAP = []
HUD_SRC = None
HUD_SEG = None
