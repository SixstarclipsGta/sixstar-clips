# NPC flying glitch (22 Nov raws 22, 23), 23 Nov. Hook = guard flies sideways past the truck at the farm gate
# (23 at 27.8-28.3, real speed), then context (their black truck, through the yard to the gate), then the
# replay: 23z = 23 from 27.3, crop 1100x620 at 760,460 scaled to 1920x1080, slowed with a freeze mid-air.
W = "/home/claude/w21b/raw"
OUT = "/home/claude/w21b/out/npcfly-game.mp4"
STYLE = "simple"
TITLE = "13 years of waiting for this 💀"
CRF = 26
FD = 0.2
DAY = "eq=contrast=1.07:saturation=1.15"
BLUE = "curves=all='0/0 0.10/0.20 0.40/0.56 1/1',eq=saturation=1.05:contrast=1.04"
SEG = [
    ("23", 27.5, 1.3, 700, DAY, 0),            # HOOK: the guard flies past the truck
    ("22", 12.0, 6.0, 420, DAY, 0, 1.3),       # earlier: takes their black truck at the secret farm
    ("23", 3.5, 8.5, 420, DAY, 0, 1.5),        # through the yard
    ("23", 21.0, 6.5, 420, DAY, 0, 1.3),       # to the gate...
    ("23z", 0.3, 0.5, 600, DAY, 0.9, 0.35),    # replay, zoomed, slow, freeze mid-air
    ("23z", 0.8, 0.45, 600, DAY, 0, 0.5),      # lands like nothing happened
    ("23", 28.6, 1.3, 420, DAY, 0.5),          # drives off
]
CAP = []
HUD_SRC = None
HUD_SEG = None
