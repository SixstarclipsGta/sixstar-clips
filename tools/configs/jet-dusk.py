# Jet at dusk, 5 stars (24 Nov raws 17, 18, 19; 19 t = 18 t - 3.5; no overlap 17 -> 18). Very dark footage,
# lifted with curves. Hook and cover (no fade-in): the fighter jet from behind as the afterburner lights
# (18 at 24.4 s), cut before anything happens to it. Then in order: gets into the striped pickup, drives
# through the Mile Zero gate, across the apron past the hangars, jumps out, sprints to the jet while being
# shot, climbs in, afterburner, rolls with the screen going red, and the jet is blown up on the runway
# (19 at 27.6 s, black-and-white shatter). Weapon wheel (18 at 17.7 to 18.6) skipped. Ending held 3 s.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/jetdusk-game.mp4"
STYLE = "simple"
TITLE = "5 stars. One jet. Can I get it off the ground?! 👀"
CRF = 25
DUSK = "curves=all='0/0 0.10/0.24 0.40/0.62 1/1',eq=saturation=1.2:contrast=1.06"
END = "curves=all='0/0 0.10/0.20 0.40/0.55 1/1',eq=saturation=1.1:contrast=1.04"
SEG = [
    ("18", 24.42, 1.9, 680, DUSK, 0),           # HOOK and cover: jet from behind, afterburner lit
    ("17", 0.3, 4.3, 640, DUSK, 0, 1.3),        # gets into the striped pickup
    ("17", 13.6, 6.2, 420, DUSK, 0, 1.3),       # road to the base, through the Mile Zero gate
    ("18", 3.6, 7.0, 420, DUSK, 0, 1.5),        # across the apron past the hangars, stars on
    ("18", 10.6, 2.7, 420, DUSK, 0),            # jumps out next to the jets
    ("18", 12.95, 3.0, 700, DUSK, 0),           # sprints to the jet, gets shot
    ("18", 15.6, 1.85, 420, DUSK, 0),           # climbs into the cockpit
    ("18", 21.6, 2.4, 520, DUSK, 0),            # engine start
    ("18", 23.65, 2.6, 680, DUSK, 0),           # afterburner
    ("18", 25.9, 4.05, 420, DUSK, 0),           # rolling, screen going red
    ("19", 26.1, 3.85, 420, END, 3.0),          # blown up on the runway
]
SEG_HUD = {"segs": [9], "crop": "196:40:1704:24", "scale": 4.4, "border": "e0344a"}  # the 5 wanted stars, enlarged under the video while he rolls
CAP = []
HUD_SRC = None
HUD_SEG = None
