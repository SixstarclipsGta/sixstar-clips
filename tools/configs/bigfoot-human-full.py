# "Bigfoot turned HUMAN", v3 = EXACTLY as Zubair asked (26 Nov, after rejecting v1 and v2):
# "Don't crop these. Just make them as it is, combined. Especially from the start."
# All three raws (24 Nov 08, 09, 10) in order, from the first frame of 08 to the last frame of 10, nothing cut,
# nothing zoomed, the whole 16:9 frame shown (FULL). Only the duplicate is removed: 09 repeats the end of 08
# (09 t = 08 t - 21.03), so 09 joins at 8.42 with the 0.35 s dissolve over identical frames (invisible).
# No hook in front: he wants it from the start. He will say frame by frame if anything should go.
# His story: weird voices and a smell, he sees Bigfoot (the far figure by the mangroves that Jason aims at in
# 09 at ~21 to 26 s, right side of the frame: v1/v2 cropped it OUT), follows him, he keeps vanishing, in 10 he
# is "human again", then the fight.
# Line and caption (2d): "Bigfoot turned HUMAN in GTA 6?! 😳" / "is this a secret character? 👀". Game sound only.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/bigfoot-full-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "Bigfoot turned HUMAN in GTA 6?! 😳"
CRF = 25
ENC_EXTRA = ["-maxrate", "3.5M", "-bufsize", "7M"]
DAY = "eq=brightness=0.03:contrast=1.06:saturation=1.14:gamma=1.06"
SEG = [
    ("08", 0.0, 29.8, 0, DAY, 0),               # whole clip 08: the drive, into the mangroves, gets out
    ("09", 8.42, 21.05, 0, DAY, 0),             # rest of 09: holds his head, runs, pistol, aims, runs on
    ("10", 0.0, 29.95, 0, DAY, 3.0),            # whole clip 10: the crouched man, chase, fight, carried
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
