# Free rocket launcher at the secret farm (22 Nov): in order, fight in -> stairs -> door -> the table -> pickup
# -> aim over the grow hall -> scope -> map with the farm ringed. ~33 s. He never fires it in these clips, so the
# story is "they left it on the table", not an explosion.
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/launcher-game.mp4"
STYLE = "simple"
TITLE = "They really left this on the table 💀"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
DARK = "curves=all='0/0 0.10/0.26 0.40/0.66 1/1',eq=saturation=1.15:contrast=1.05"
BLUE = "curves=all='0/0 0.08/0.24 0.40/0.66 1/1',eq=saturation=1.05:contrast=1.04"
SEG = [
    ("13", 17.0, 3.6, 300, DAY, 0),            # open on action: shooting from the fence
    ("15", 22.0, 7.0, 420, DAY, 0, 1.6),       # past the trucks, up the stairs
    ("16", 5.5, 3.2, 420, DAY, 0),             # the door
    ("16", 9.0, 4.5, 420, DARK, 0, 1.3),       # dark inside
    ("16", 13.3, 6.3, 420, DARK, 0),           # the table... picks it up
    ("16", 20.0, 4.0, 420, BLUE, 0),           # aims over the grow hall
    ("18", 1.5, 2.6, 420, BLUE, 0),            # scope (static, keep short)
    ("12m", 0.0, 6.8, 553, DAY, 0),            # where: the farm, North Mariana County
]
CAP = []
HUD_SRC = None
HUD_SEG = None
