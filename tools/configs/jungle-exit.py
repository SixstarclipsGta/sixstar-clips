# "I need to get out of this jungle" (24 Nov raws 11, 12, 13). Zubair's idea 4 of 26 Nov: "GTA 6 jungle is wild,
# everything here wants me dead, I want exit. And then whole 3 videos frame by frame."
# Built like bigfoot-human-full.py (his rule of 26 Nov): the three raws whole and in order, nothing cut, nothing
# zoomed, the whole 16:9 frame (FULL), no hook in front. Only the duplicate is removed: 13 repeats the end of 12
# (13 t = 12 t - 23.03), so 13 joins at 6.22 with the dissolve over identical frames. 11 and 12 do not overlap.
# Content: 11 deer knocks him down, 12 wading and the screen goes red, 13 injured, alligator, WASTED (held 3 s).
# Line and caption picked by Zubair (6, d+e): "I need to get out of this jungle without dying ☠️" /
# "count how many things attack me 👀 I just want the exit 😤". Game sound only, natural level.
# Repeat footage: 11 to 13 were already in the swamp trip (24 Nov). He knows and wants it anyway.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/jungle-exit-game.mp4"
STYLE = "simple"
FULL = True
TITLE = "I need to get out of this jungle without dying ☠️"
CRF = 25
ENC_EXTRA = ["-maxrate", "3.5M", "-bufsize", "7M"]
DAY = "eq=brightness=0.03:contrast=1.06:saturation=1.14:gamma=1.06"
SEG = [
    ("11", 0.0, 29.85, 0, DAY, 0),              # whole clip 11: the deer
    ("12", 0.0, 29.6, 0, DAY, 0),               # whole clip 12: wading, the screen goes red
    ("13", 6.22, 23.5, 0, DAY, 3.0),            # rest of 13: injured, the alligator, WASTED
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
