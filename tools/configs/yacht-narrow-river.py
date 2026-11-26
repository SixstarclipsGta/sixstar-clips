# Yacht through the narrow mangrove channel (24 Nov raw 01, one continuous 30 s take). Zubair's idea 1 of
# 26 Nov: "passing a big ship through a small path", pure what-happens-next excitement, nothing given away.
# Hook and cover (no fade-in) = 01 at 9.0: high camera, the whole yacht with its wake and the tight channel
# ahead. Then the whole clip from the start at normal speed; it comes out into the open lake at ~22 s.
# Line and caption picked by Zubair (4b): "Testing GTA 6: big ship, tiny river. What happens? 🤔" /
# "wait for the narrow part 👀". "Ship" is his word and stays as the correction-bait slip.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/yacht-game.mp4"
STYLE = "simple"
TITLE = "Testing GTA 6: big ship, tiny river. What happens? 🤔"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
DAY = "eq=brightness=0.02:contrast=1.07:saturation=1.18"
SEG = [
    ("01", 9.0, 1.6, 420, DAY, 0),              # HOOK and cover: yacht in the tight channel
    ("01", 0.3, 29.5, 420, DAY, 2.0),           # the whole run, out into the lake, held
]
SEG_HUD = None
CAP = []
HUD_SRC = None
HUD_SEG = None
