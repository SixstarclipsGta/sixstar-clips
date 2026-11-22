# Stolen sheriff car (21 Nov raws 06, 07), 22 Nov style. In order: swerving, hits the pole and a hydrant,
# hydrant again, another county's police car rams him, limps the wreck to Boone Speedway and parks by the crowd.
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/sh/sheriff-game.mp4"
STYLE = "simple"
TITLE = "Just borrowed it for 5 minutes 💔"
CRF = 26
DAY = "eq=contrast=1.07:saturation=1.15"
SEG = [
    ("06", 14.3, 3.5, 420, DAY, 0),            # swerving, something goes flying
    ("06", 17.8, 3.2, 420, DAY, 0),            # into the pole, hydrant bursts
    ("06", 21.0, 2.3, 420, DAY, 0, 1.3),       # keeps going
    ("06", 23.2, 2.6, 420, DAY, 0),            # hydrant number two
    ("06", 25.8, 3.8, 420, DAY, 0),            # rammed by the other county's police
    ("07", 0.0, 3.0, 420, DAY, 0),             # out of the bushes, wrecked
    ("07", 3.0, 13.0, 420, DAY, 0, 1.7),       # limping it across town
    ("07", 16.0, 6.0, 420, DAY, 0, 1.2),       # Boone Speedway
    ("07", 22.0, 7.5, 420, DAY, 0),            # parks it right by the crowd
]
CAP = []
HUD_SRC = None
HUD_SEG = None
