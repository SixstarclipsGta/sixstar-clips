# Secret farm, daytime v2 (22 Nov): told in order, no spoiler at the start.
# Fence fight -> guards down -> sneak -> stairs -> inside -> stairwell fight + flashbang -> office (money)
# -> escape -> shot at their truck, WASTED -> respawn -> 2nd try: grow hall -> their truck -> out the gate -> map.
# Launcher pickup left out on purpose (he never fires it in these clips; it goes in the launcher reel).
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/farm-day2-game.mp4"
STYLE = "simple"
TITLE = "Got WASTED. Came back for their truck 😤"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
DARK = "curves=all='0/0 0.10/0.26 0.40/0.66 1/1',eq=saturation=1.15:contrast=1.05"
BLUE = "curves=all='0/0 0.10/0.20 0.40/0.56 1/1',eq=saturation=1.05:contrast=1.04"
SEG = [
    ("13", 17.0, 5.2, 300, DAY, 0),            # open on action: shooting the guards from the fence
    ("14", 0.3, 4.5, 420, DAY, 0),             # guard down behind the wall
    ("14", 13.0, 5.2, 300, DAY, 0),            # finishes the last guard, moves in
    ("15", 10.0, 7.0, 420, DAY, 0, 1.4),       # sneaks along the building in the shadow
    ("15", 21.5, 8.0, 420, DAY, 0, 1.5),       # past the trucks to the stairs
    ("16", 0.5, 8.0, 420, DAY, 0, 1.5),        # up the stairs, through the door
    ("16", 9.0, 4.5, 420, DARK, 0, 1.3),       # dark inside
    ("19", 5.0, 6.3, 420, BLUE, 0),            # stairwell fight... flashbang
    ("19", 14.8, 4.0, 420, DAY, 0, 1.2),       # still blinded, finds the door
    ("19", 19.0, 5.0, 420, DAY, 0, 1.2),       # the office
    ("20", 2.5, 3.0, 420, DAY, 0),             # money
    ("21", 1.0, 10.0, 420, DARK, 0, 1.3),      # escape: down the stairs, firefight, corridor
    ("21", 11.0, 7.5, 420, DAY, 0),            # out the door, jumps down to their truck... shot
    ("21", 18.5, 2.5, 420, DAY, 0),            # WASTED
    ("21", 27.8, 1.8, 420, DAY, 0),            # back in
    ("22", 1.0, 10.5, 420, BLUE, 0, 1.5),      # 2nd try: through the grow hall
    ("22", 12.0, 11.5, 420, DAY, 0, 1.4),      # their black truck, in, go
    ("23", 3.5, 8.5, 420, DAY, 0, 1.4),        # through the yard
    ("23", 23.5, 6.1, 420, DAY, 0),            # out of the gate
    ("12m", 0.0, 6.8, 553, DAY, 0),            # map: where it is
]
CAP = []
HUD_SRC = None
HUD_SEG = None
