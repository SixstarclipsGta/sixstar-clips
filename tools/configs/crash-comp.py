# Crash compilation (23 Nov): every crash from 19 to 22 Nov, short lead-in then the hit, no slow-mo, quick
# 0.15 s dissolves, escalating to the jeep roll-over. Sources are symlinks in /home/claude/crash/raw:
# race = 21 Nov 10, sport/sportcc/rail = 22 Nov 11/11cc/12, sher = 21 Nov 06, pole/hum/gate/heli/heli2/flip = 19 Nov
# 27/10/07/22/09/12.
W = "/home/claude/crash/raw"
OUT = "/home/claude/crash/crash-game.mp4"
STYLE = "simple"
TITLE = "GTA 6 physics are actually insane 😭"
CRF = 26
FD = 0.15
DAY = "eq=contrast=1.07:saturation=1.15"
DUSK = "curves=all='0/0 0.10/0.18 0.45/0.58 1/1',eq=saturation=1.12:contrast=1.05"
SEG = [
    ("race", 24.5, 5.4, 420, DAY, 0),          # monster truck flattens him: ELIMINATED
    ("sport", 21.0, 2.25, 420, DAY, 0),        # sports car tries to pass...
    ("sportcc", 0.0, 2.5, 420, DAY, 0),        # crash cam, both cars
    ("sport", 25.75, 2.0, 420, DAY, 0),        # aftermath
    ("pole", 24.6, 5.0, 420, DAY, 0),          # sheriff car into a pole, crash cam
    ("sher", 17.8, 3.2, 420, DAY, 0),          # pole + hydrant
    ("sher", 23.2, 2.6, 420, DAY, 0),          # hydrant again
    ("sher", 25.8, 3.8, 420, DAY, 0),          # rammed by the other county
    ("rail", 4.0, 3.2, 420, DAY, 0),           # off the road onto the railway
    ("rail", 12.6, 2.0, 420, DAY, 0),          # launches back onto the road
    ("hum", 21.3, 4.0, 420, DAY, 0),           # straight into an army Humvee
    ("gate", 1.5, 4.0, 420, DUSK, 0),          # tank through the airbase gate
    ("gate", 8.4, 2.0, 420, DUSK, 0),          # truck goes up
    ("heli2", 13.2, 6.6, 420, DUSK, 0),        # helicopter shot down, crashes on the runway
    ("heli", 12.5, 5.0, 420, DAY, 0),          # out of fuel, into the sea
    ("flip", 13.3, 2.4, 420, DAY, 0),          # jeep clips the pole...
    ("flip", 20.8, 7.2, 420, DAY, 0),          # ...and rolls over and over
    ("flip", 28.0, 1.8, 420, DAY, 0.6),        # upside down
]
CAP = []
HUD_SRC = None
HUD_SEG = None
