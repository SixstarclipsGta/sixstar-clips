# "Whose dog is THIS in GTA 6?!" (24 Nov raw 14, whole). Zubair's idea 5 of 26 Nov: "dogs can kill you in GTA 6".
# Built by his rule of 26 Nov: the raw whole, nothing cut, nothing zoomed, the whole 16:9 frame (FULL), no hook.
# Content: quad arrives at men by a couch, fist fight, the screen goes red, he runs and hides behind a low wall
# (weapon wheel at 20), a spotted dog comes at him (24 to 29). End held 3 s.
# Line and caption picked by Zubair (5a): "Whose dog is THIS in GTA 6?! 😳" / "wait for the dog 👀". Game sound only.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/dog-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "Whose dog is THIS in GTA 6?! 😳"
CRF = 25
ENC_EXTRA = ["-maxrate", "3.5M", "-bufsize", "7M"]
DAY = "eq=brightness=0.03:contrast=1.06:saturation=1.14:gamma=1.06"
SEG = [
    ("14", 0.0, 29.5, 0, DAY, 3.0),             # whole clip 14
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
