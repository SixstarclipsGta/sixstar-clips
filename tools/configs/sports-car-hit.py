# Grey SUV vs black sports car on the highway, then off-road escape (raws 11, 12 of the 21 Nov afternoon batch). ~29 s.
# 11zr = 2x zoom of 11 from 21.4 s: ffmpeg -ss 21.4 -t 2.4 -i 11.mp4 -vf "crop=1080:608:620:380,scale=1920:1080" 11zr.mp4
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/sportscar-game.mp4"
STYLE = "simple"
TITLE = "He really thought he could pass me 💀"
CRF = 25
DAY = "eq=contrast=1.07:saturation=1.15"
SEG = [
    ("11", 0.3, 4.2, 420, DAY, 0),          # chaos on the highway, take off past the truck
    ("11", 18.0, 3.5, 420, DAY, 0),         # traffic, building up
    ("11", 21.0, 1.0, 420, DAY, 0),         # the black sports car tries to pass
    ("11", 22.0, 1.25, 420, DAY, 0, 0.5),   # the hit, half speed
    ("11", 23.25, 2.5, 380, DAY, 0),        # game crash cam
    ("11", 25.75, 3.45, 420, DAY, 0),       # pushing him sideways down the road
    ("11zr", 0.5, 1.6, 420, DAY, 0, 0.5),     # replay, 2x zoom, half speed
    ("12", 4.3, 2.2, 420, DAY, 0),          # off the road
    ("12", 6.0, 4.5, 420, DAY, 0, 1.3),     # rough ground, under the bridge
    ("12", 10.5, 3.5, 420, DAY, 0),         # climbing the embankment
    ("12", 13.3, 1.7, 420, DAY, 0.5),       # lands on the road
]
CAP = []
HUD_SRC = None
HUD_SEG = None
