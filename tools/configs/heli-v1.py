# Heli video 1: how to get a helicopter without the army (story.py config)
W = "/home/claude/work/heli"
OUT = W + "/v1.mp4"
DARK = "curves=all='0/0 0.10/0.26 0.40/0.64 1/1',eq=saturation=1.22:contrast=1.06"
MAPG = "eq=contrast=1.04:saturation=1.1"
SEG = [
    ("h04", 7.5, 3.6, 420, DARK, 0),    # 0 teaser: flying over the Keys
    ("h01", 13.0, 6.0, 420, DARK, 0),   # 1 sheriff car drive
    ("h01", 22.5, 6.7, 360, DARK, 0),   # 2 arrive at the dock gate
    ("h02", 0.0, 8.5, 520, DARK, 0),    # 3 out of the car, through the gate
    ("h02", 16.7, 5.9, 400, DARK, 0),   # 4 walk to the helipad
    ("h02", 22.6, 7.1, 420, DARK, 0),   # 5 get in, take off
    ("h03", 13.5, 5.5, 420, DARK, 0),   # 6 flight
    ("h04", 0.0, 6.0, 420, DARK, 0),    # 7 flight (continues from h03 19.0)
    ("h02", 11.6, 3.2, 400, MAPG, 3.0), # 8 map, held
]
CAP = [
    (0, 0, 3.6, "SUNSET RIDE", "Free helicopter 🚁", "📍 location at the end"),
    (1, 0, 6.0, "STEP 1", "Grab any car 🚓", "Mine was a sheriff car lol"),
    (2, 0, 6.7, "STEP 2", "Drive to the docks 🌴", "Right next to the army airport"),
    (3, 0, 4.5, "STEP 3", "Walk through the gate 🚧", None),
    (3, 4.5, 8.5, "STEP 3", "Restricted area? Never heard of it 🤷", None),
    (4, 0, 5.9, "STEP 4", "There she is 😍", "Buckingham Maverick on the helipad"),
    (5, 0, 7.1, "STEP 5", "Jump in and lift off ✈️", "2 stars and the army never came"),
    (6, 0, 5.5, "STEP 6", "Enjoy the view 😎", None),
    (7, 0, 6.0, "STEP 6", "No jets. No tanks. Just vibes 🌅", None),
    (8, 0, 6.2, "📍 LOCATION", "Helipad at the Southwind docks", "Next to Mile Zero Air Station"),
]
HUD_SRC = None
HUD_SEG = None
