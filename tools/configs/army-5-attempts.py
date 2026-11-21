# Army base supercut v2: 5 attempts, all at the base, finale = full Black Hawk attempt (story.py config).
W = "/home/claude/work/army"
OUT = W + "/army2.mp4"
CARD = "card5.png"
DUSK = "curves=all='0/0 0.10/0.22 0.40/0.60 1/1',eq=saturation=1.2:contrast=1.06"
DAY = "eq=contrast=1.06:saturation=1.15"
SEG = [
    ("a2", 21.0, 2.6, 380, DAY, 0),      # 0 cold open: jeep mid-roll
    ("a2", 17.5, 9.5, 380, DAY, 0),      # 1 attempt 1: jeep through the gate, roll
    ("a4", 1.0, 4.0, 420, DUSK, 0),      # 2 attempt 2: tank through the gate
    ("a5", 13.5, 6.0, 420, DUSK, 0),     # 3 shoots the heli down
    ("a5", 27.0, 2.6, 420, DUSK, 0),     # 4 WASTED
    ("a6", 15.5, 10.1, 420, DAY, 0),     # 5 attempt 3: pickup on rims to the jet, WASTED
    ("a7", 14.5, 3.5, 200, DAY, 0),      # 6 attempt 4: climbs the jet
    ("a7", 24.0, 4.5, 420, DAY, 0),      # 7 shot in the cockpit, WASTED
    ("b1", 3.5, 4.0, 420, DAY, 0),       # 8 attempt 5: sheriff car through the gate
    ("b2", 21.0, 4.5, 420, DAY, 0),      # 9 car shot up next to the Black Hawk
    ("b2", 25.5, 3.5, 300, DAY, 0),      # 10 runs to the door
    ("b3", 3.0, 4.5, 420, DAY, 0),       # 11 takeoff, engine damaged
    ("b4", 20.0, 6.0, 420, DAY, 0),      # 12 Apache chase, tracers
    ("a8", 8.0, 8.5, 420, DAY, 0),       # 13 fuel empty, into the sea
    ("a9", 21.0, 4.6, 420, DAY, 0),      # 14 shot while swimming, WASTED
]
CAP = [
    (0, 0, 2.6, "5 ATTEMPTS", "One jet. Zero luck 💀", "Count the WASTEDs"),
    (1, 0, 9.5, "ATTEMPT 1", "Drive in like I belong 🚙", "💀 x0"),
    (2, 0, 4.0, "ATTEMPT 2", "Fine. Bring a tank 🪖", "💀 x0"),
    (3, 0, 6.0, "ATTEMPT 2", "Took down their heli 🔥", "💀 x0"),
    (4, 0, 2.6, "ATTEMPT 2", "…and still died 😭", "💀 x1"),
    (5, 0, 8.5, "ATTEMPT 3", "Pickup on bare rims 😂", "💀 x1"),
    (5, 8.5, 10.1, "ATTEMPT 3", "Nope 💀", "💀 x2"),
    (6, 0, 3.5, "ATTEMPT 4", "Made it to the F-16 😳", "💀 x2"),
    (7, 0, 4.5, "ATTEMPT 4", "Shot in the cockpit 😭", "💀 x3"),
    (8, 0, 4.0, "ATTEMPT 5", "Cop car = VIP pass 🚓", "💀 x3"),
    (9, 0, 4.5, "ATTEMPT 5", "They saw through it 😬", "💀 x3"),
    (10, 0, 3.5, "ATTEMPT 5", "Forget the jet. Take the Black Hawk 🚁", "💀 x3"),
    (11, 0, 4.5, "ATTEMPT 5", "Engine damaged… whatever 😤", "💀 x3"),
    (12, 0, 6.0, "ATTEMPT 5", "Two Apaches on me 😰", "💀 x3"),
    (13, 0, 8.5, "ATTEMPT 5", "Fuel empty?! ⛽", "💀 x3"),
    (14, 0, 4.6, "ATTEMPT 5", "Swim for it… 💀", "💀 x4 · Which try was closest?"),
]
HUD_SRC = None
HUD_SEG = None
