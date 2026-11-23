# Night farm stealth (21 Nov raws 13, 14, 16), 23 Nov. Crouch-run along the fence, takes the guard's rifle,
# across the lit yard, into the shadows, peeks past the container, creeps past the truck, up the stairs,
# then the farm on the map (11z).
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/sh/stealth-game.mp4"
STYLE = "simple"
TITLE = "They never even saw me 🤫"
CRF = 26
NIGHT = "curves=all='0/0 0.10/0.26 0.40/0.66 1/1',eq=saturation=1.12:contrast=1.05"
MAP = "eq=contrast=1.04:saturation=1.05"
SEG = [
    ("13", 20.6, 3.6, 420, NIGHT, 0),          # crouch-run along the fence
    ("14", 1.0, 5.5, 420, NIGHT, 0),           # takes the guard's rifle
    ("14", 9.5, 7.5, 420, NIGHT, 0, 1.4),      # across the lit yard
    ("14", 17.0, 5.0, 420, NIGHT, 0, 1.3),     # into the shadow along the wall
    ("14", 26.5, 3.0, 420, NIGHT, 0),          # peeks
    ("16", 1.0, 5.0, 420, NIGHT, 0),           # behind the container
    ("16", 14.8, 5.0, 420, NIGHT, 0),          # creeps past the truck
    ("16", 20.0, 9.9, 420, NIGHT, 0, 1.4),     # up the stairs
    ("12m", 0.0, 6.8, 553, MAP, 0),            # where: farm ringed on the map, North Mariana County (no "weed" text)
]
CAP = []
HUD_SRC = None
HUD_SEG = None
