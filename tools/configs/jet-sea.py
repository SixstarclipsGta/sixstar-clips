# Jet attempt #3: into the sea (24 Nov raws 29, 30, 31, 32, 33; 31 t = 30 t - 24.52, 33 t = 32 t - 26.02;
# no overlap 29 -> 30 or 31 -> 32). Hook first (Zubair likes the best moment up front and again in place):
# the jet hits the water. Then in order: steals sheriff car 446 at The Chow Mart, through the base fence with
# stars on, across the apron, runs to a jet, taxi, take-off, low over the sea, into the water, the jet sinks,
# he swims out and floats up while a big sea animal passes overhead (33 at 27 s). No WASTED in the files.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/jetsea-game.mp4"
STYLE = "simple"
TITLE = "At least nobody will find it 😂"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
DAY = "eq=contrast=1.06:saturation=1.15"
MID = "eq=brightness=0.03:contrast=1.06:saturation=1.15:gamma=1.05"
SEA = "eq=brightness=0.06:contrast=1.08:saturation=1.2:gamma=1.15"
SEG = [
    ("32", 18.0, 3.6, 420, SEA, 0),             # HOOK: the jet goes into the water
    ("29", 12.3, 7.2, 700, MID, 0, 1.3),        # walks up to sheriff car 446, gets in
    ("29", 24.5, 3.5, 420, MID, 0),             # drives off
    ("30", 9.5, 4.5, 420, MID, 0),              # base road, straight through the fence
    ("30", 22.3, 3.2, 420, MID, 0),             # across the apron to the jets
    ("31", 0.63, 9.97, 340, DAY, 0, 1.3),       # out, sprint, up the ladder
    ("31", 11.5, 4.5, 420, DAY, 0),             # rolling out between the fighters
    ("31", 24.0, 5.9, 420, DAY, 0),             # runway, take-off
    ("32", 0.0, 7.5, 420, SEA, 0, 1.5),         # over the sea
    ("32", 13.5, 8.85, 420, SEA, 0),            # lower, lower, into the water
    ("32", 22.0, 7.4, 420, SEA, 0, 1.5),        # the jet sinks
    ("33", 8.3, 6.5, 340, SEA, 0),              # climbs out, swims clear
    ("33", 23.0, 6.75, 420, SEA, 0.6),          # floats up, something big passes overhead
]
CAP = []
HUD_SRC = None
HUD_SEG = None
