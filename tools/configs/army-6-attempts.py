# Army base supercut: 6 attempts to steal a jet, WASTED counter (story.py config). Action every second, 60s+.
W = "/home/claude/work/army"
OUT = W + "/army.mp4"
NIGHT = "curves=all='0/0 0.10/0.28 0.40/0.68 1/1',eq=saturation=1.2:contrast=1.06"
DUSK = "curves=all='0/0 0.10/0.22 0.40/0.60 1/1',eq=saturation=1.2:contrast=1.06"
DAY = "eq=contrast=1.06:saturation=1.15"
SEG = [
    ("a2", 21.0, 2.6, 380, DAY, 0),      # 0 cold open: jeep mid-roll
    ("a1", 13.5, 3.5, 420, NIGHT, 0),    # 1 attempt 1: vault the wall at night
    ("a1", 24.0, 5.6, 420, NIGHT, 0),    # 2 shot, WASTED
    ("a2", 17.5, 10.1, 380, DAY, 0),     # 3 attempt 2: jeep through the gate, roll
    ("a4", 1.0, 4.0, 420, DUSK, 0),      # 4 attempt 3: tank through the gate
    ("a5", 13.5, 6.0, 420, DUSK, 0),     # 5 shoots the heli down, explosions
    ("a5", 27.0, 2.6, 420, DUSK, 0),     # 6 WASTED
    ("a6", 15.0, 10.6, 420, DAY, 0),     # 7 attempt 4: pickup on rims to the jet, WASTED
    ("a7", 14.5, 3.5, 200, DAY, 0),      # 8 attempt 5: climbs the jet
    ("a7", 24.0, 4.5, 420, DAY, 0),      # 9 shot in the cockpit, WASTED
    ("a8", 7.5, 9.5, 420, DAY, 0),       # 10 attempt 6: Black Hawk out of fuel, crash
    ("a9", 21.0, 4.6, 420, DAY, 0),      # 11 shot while swimming, WASTED
]
CAP = [
    (0, 0, 2.6, "6 ATTEMPTS", "One jet. Zero luck 💀", "Count the WASTEDs"),
    (1, 0, 3.5, "ATTEMPT 1", "Sneak in at night 🌙", "💀 x0"),
    (2, 0, 5.6, "ATTEMPT 1", "One guard. Done 😭", "💀 x1"),
    (3, 0, 10.1, "ATTEMPT 2", "Drive in like I belong 🚙", "💀 x1"),
    (4, 0, 4.0, "ATTEMPT 3", "Fine. Bring a tank 🪖", "💀 x1"),
    (5, 0, 6.0, "ATTEMPT 3", "Took down their heli 🔥", "💀 x1"),
    (6, 0, 2.6, "ATTEMPT 3", "…and still died 😭", "💀 x2"),
    (7, 0, 9.0, "ATTEMPT 4", "Pickup on bare rims 😂", "💀 x2"),
    (7, 9.0, 10.6, "ATTEMPT 4", "Nope 💀", "💀 x3"),
    (8, 0, 3.5, "ATTEMPT 5", "Made it to the F-16 😳", "💀 x3"),
    (9, 0, 4.5, "ATTEMPT 5", "Shot in the cockpit 😭", "💀 x4"),
    (10, 0, 9.5, "ATTEMPT 6", "Stole a Black Hawk… no fuel ⛽", "💀 x4"),
    (11, 0, 4.6, "ATTEMPT 6", "Swim for it? 💀", "💀 x5 · Which try was closest?"),
]
HUD_SRC = None
HUD_SEG = None
