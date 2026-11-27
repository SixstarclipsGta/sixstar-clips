# "Rockstar, please check this rock 😂" (YouTube live stream 7FnC9V2n-As, part 2 as downloaded by Zubair,
# "GTA 6-2.mp4", 1280x720 30 fps; first 102 s archived as raw/2026-11-27/01-stream2-rock-on-road.mp4).
# Zubair, 27 Nov: hook = the best moment first (black sedan hits the rock and flies, 74.6 s), then the story
# in order with the boring waiting parts trimmed. Picked line 5 + caption e. Game sound only (no voice, no radio seen
# in the spectrogram; engine from 92 s, horn at 97 s).
# Content: rock in the road (0.9-7.5; stream glitch from 7.7), a pickup jumps and a black car spins (15-23),
# skip 23-69.5 (waiting), white sedan bounces, black sedan hits the rock and flies, crashed pickup off the road,
# police SUV jumps (69.5-80.2), skip 80.2-85 (walking), walks to the crashed pickup by the sea and drives off (85-99.8).
W = "/home/claude/work/rock"
OUT = "/home/claude/work/out/rock-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "Rockstar, please check this rock 😂"
CRF = 25
ENC_EXTRA = ["-maxrate", "3.5M", "-bufsize", "7M"]
G = "curves=all='0/0 0.10/0.24 0.40/0.62 1/1',eq=saturation=1.2:contrast=1.06"
SEG = [
    ("s2", 74.55, 1.25, 0, G, 0, 0.7),   # HOOK and cover: black sedan in the air over the rock (frame 0), slow-mo
    ("s2", 0.9, 6.6, 0, G, 0),           # the rock in the road
    ("s2", 15.0, 8.0, 0, G, 0),          # pickup jumps, black car spins by the trailer
    ("s2", 69.5, 10.7, 0, G, 0),         # white sedan bounces, black sedan flies, pickup off the road, police SUV jumps
    ("s2", 85.0, 14.8, 0, G, 1.5),       # walks to the crashed pickup by the sea, gets in, drives off at sunset
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
