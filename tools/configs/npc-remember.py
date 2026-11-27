# "NPCs in GTA 6 REMEMBER what you did 😳" + caption "do NPCs remember you in your game too? 👀" (Zubair's pick 1e).
# 27 Nov raws 02 + 03 WHOLE and in order (his story: "2nd and 3rd video combine"), FULL frame, no hook.
# Only the repeat is removed: 03 t = 02 t - 20.528 (03 frame 0 = 02 at 20.528, mse 0.24).
# Content: Jason walks through the store and out at dusk; men stop him: "Hey!" / "You messed up our motel pretty bad." /
# "We gotta return the favor!" (02 at 13.0 to 17.6); fist fight, weapon wheel (03 at 2), "Where you going, boy? Get over
# here and take it like a man!" (03 at 17.5 to 20.4); he runs to a car (03 at 21 to 29.6). End held 3 s.
# The game's own subtitles are enlarged under the video while they show (segments split on the SAME frames: each next
# segment starts FD before the previous one ends, so the dissolve blends identical frames and nothing is cut).
W = "/home/claude/work/r1127"
OUT = "/home/claude/work/out/npc-remember-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "NPCs in GTA 6 REMEMBER what you did 😳"
CRF = 25
ENC_EXTRA = ["-maxrate", "3.5M", "-bufsize", "7M"]
G = "curves=all='0/0 0.10/0.25 0.40/0.64 1/1',eq=saturation=1.12:contrast=1.06"
SEG = [
    ("02", 0.0, 12.9, 0, G, 0),        # store, walks out, men in the parking lot
    ("02", 12.55, 5.3, 0, G, 0),       # "Hey!" / "You messed up our motel pretty bad." / "We gotta return the favor!"
    ("02", 17.5, 3.378, 0, G, 0),      # fight starts (to 02 at 20.878 = 03 at 0.35)
    ("03", 0.0, 17.3, 0, G, 0),        # fight, weapon wheel
    ("03", 16.95, 3.65, 0, G, 0),      # "Where you going, boy? Get over here and take it like a man!"
    ("03", 20.25, 9.36, 0, G, 3.0),    # to the end of 03, held 3 s
]
SEG_HUD = {"segs": [1, 4], "crop": "720:50:600:952", "scale": 1.45, "border": "2de2d0", "delay": 0.3}
CAP = []
HUD_SRC = None
HUD_SEG = None
