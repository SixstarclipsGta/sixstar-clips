# Secret farm raid, part 1 (21 Nov 2026, raws 11, 12, 15, 17, 18, 19 of raw/2026-11-21). ~33 s. Night: curves lift.
# Call it "secret farm" in posts (the game's map card says "Industrial Weed Grow"). Payout clips come later.
# 11z.mp4 = zoomed map card: ffmpeg -ss 5.0 -t 4.4 -i 11.mp4 -vf "crop=760:760:880:170,scale=1080:1080:flags=lanczos,pad=1920:1080:0:0" -crf 16 11z.mp4
W = "/home/claude/w21/raw"
OUT = "/home/claude/w21/farm/farm1.mp4"
CARD = "farmcard.png"
CRF = 26
NIGHT = "curves=all='0/0 0.10/0.30 0.40/0.72 1/1',eq=saturation=1.2:contrast=1.06"
BLUE = "curves=all='0/0 0.10/0.24 0.40/0.62 1/1',eq=saturation=1.1:contrast=1.05"
MAP = "eq=contrast=1.04"
SEG = [
    ("15", 19.0, 2.5, 420, NIGHT, 0),   # 0 cold open: gunfight at the container
    ("11z", 1.3, 3.0, 0, MAP, 0),      # 1 map card: security high, take $5,800-6,000
    ("12", 1.6, 3.4, 480, NIGHT, 0),    # 2 fence gunfight, sparks
    ("15", 22.4, 3.2, 520, NIGHT, 0),   # 3 flashlight, kill cam by the bulldozers
    ("17", 0.0, 4.5, 420, BLUE, 0),     # 4 sneaks into the container building
    ("18", 20.0, 5.6, 480, BLUE, 0),    # 5 catwalk fight, close range
    ("19", 1.5, 3.5, 300, BLUE, 0),     # 6 picks up the launcher
    ("19", 17.0, 6.5, 300, BLUE, 0.6),  # 7 aims it over the grow hall
]
CAP = [
    (0, 0, 2.5, "SECRET FARM", "Heavily armed 😳", None),
    (1, 0, 3.0, "ON THE MAP", "Worth up to $6,000 💰", None),
    (2, 0, 3.4, "THE FENCE", "Guards everywhere 😬", None),
    (3, 0, 3.2, "THE YARD", "Clearing a way in 😤", None),
    (4, 0, 4.5, "INSIDE", "Quiet… 🤫", None),
    (5, 0, 5.6, "INSIDE", "They're in here too 😰", None),
    (6, 0, 3.5, "INSIDE", "Wait… is that a launcher? 👀", None),
    (7, 0, 7.1, "THE GROW HALL", "Take the $6,000… or blow it up? 💥", "Part 2 on my profile 👀"),
]
HUD_SRC = None
HUD_SEG = None
