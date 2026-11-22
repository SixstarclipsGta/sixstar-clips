# Secret farm, daytime: WASTED on try 1, came back and drove out in their truck (raws 13-23 + 12 map, 21 Nov afternoon batch). ~72 s.
# 12m.mp4 = map from 12 at 25.6-29.8 + 2.6 s hold, teal ring + "North Mariana County" label (ring.png) on the farm icon at (1093, 447).
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/farm-day-game.mp4"
STYLE = "simple"
TITLE = "Got WASTED. Came back for their truck 😤"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
DARK = "curves=all='0/0 0.10/0.26 0.40/0.66 1/1',eq=saturation=1.15:contrast=1.05"
BLUE = "curves=all='0/0 0.10/0.20 0.40/0.56 1/1',eq=saturation=1.05:contrast=1.04"
SEG = [
    ("21", 18.3, 2.6, 420, DAY, 0),           # cold open: WASTED by the truck
    ("13", 1.0, 5.0, 420, DAY, 0),            # try 1: along the fence
    ("14", 2.0, 4.0, 420, DAY, 0),            # a guard goes down
    ("15", 23.5, 4.0, 420, DAY, 0, 1.3),      # up the stairs
    ("16", 4.0, 4.5, 420, DAY, 0, 1.3),       # to the door
    ("16", 14.0, 5.5, 420, DARK, 0),          # inside, picks up the launcher
    ("19", 7.0, 4.6, 420, BLUE, 0),           # shooting, the flash (cut before the long white-out)
    ("19", 18.0, 6.0, 420, DAY, 0),           # the office
    ("21", 13.0, 7.7, 420, DAY, 0),           # out the back... WASTED
    ("21", 27.8, 2.1, 420, DAY, 0),           # the fields of plants
    ("22", 9.0, 4.0, 420, BLUE, 0),           # try 2: the grow hall
    ("22", 12.5, 9.5, 420, DAY, 0, 1.4),      # their black truck
    ("23", 4.0, 8.0, 420, DAY, 0, 1.4),       # through the yard
    ("23", 23.5, 6.3, 420, DAY, 0),           # out of the gate
    ("12m", 0.0, 6.8, 553, DAY, 0),           # map: where it is
]
CAP = []
HUD_SRC = None
HUD_SEG = None
