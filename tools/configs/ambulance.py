# Plane crash follow-up (22 Nov raws 08, 10): back at the burning wreck on the quad, a survivor attacks him,
# he drives off past the walking survivors, finds the ambulance... and crashes the quad into it (game crash cam),
# paramedics just stand there. 22 Nov style.
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/ambulance-game.mp4"
STYLE = "simple"
TITLE = "The ambulance finally came… and I hit it 💀"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
SEG = [
    ("08", 0.8, 6.5, 420, DAY, 0),             # at the wreck, a survivor jumps him, he gets away
    ("08", 14.0, 6.0, 420, DAY, 0, 1.4),       # past the survivors walking off
    ("10", 8.0, 9.0, 420, DAY, 0, 1.5),        # across the field, something blue on the road
    ("10", 17.0, 2.5, 420, DAY, 0),            # through the bushes... ambulance
    ("10", 19.5, 4.2, 420, DAY, 0),            # crash cam: into the ambulance
    ("10", 23.7, 2.9, 420, DAY, 0),            # door off, paramedic with the stretcher
    ("10", 26.6, 3.2, 420, DAY, 0.5),          # they just stare
]
CAP = []
HUD_SRC = None
HUD_SEG = None
