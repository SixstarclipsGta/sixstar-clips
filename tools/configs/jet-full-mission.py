# Jet, the full mission (24 Nov raws 24, 26, 27; 26 t = 24 t - 26.5, so 24 -> 26 is one continuous take;
# gap before 27). Zubair's idea 2 (25 Nov): a 1 to 2 min video at normal speed: trying to get a plane,
# grabbing one, take-off, then enjoying the flight. Ends in the air (no missile, no jump: that is the
# flyover video, `jet-flyover.py`). Hook and cover (no fade-in): the jet side-on over the sea with the
# afterburner lit (26 at 25.0). Wanted stars enlarged under the video from the cockpit to the climb-out.
# Line and caption picked by Zubair: "Trying to steal a fighter jet in GTA 6 (full mission) 👀" /
# "full mission, no cuts 🤯".
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/mission-game.mp4"
STYLE = "simple"
TITLE = "Trying to steal a fighter jet in GTA 6 (full mission) 👀"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
DAY = "eq=contrast=1.06:saturation=1.15"
AIR = "eq=brightness=0.04:contrast=1.07:saturation=1.16:gamma=1.07"
HOOK = "eq=brightness=0.08:contrast=1.08:saturation=1.2:gamma=1.15,crop=1477:831:318:180,scale=1920:1080:flags=lanczos"
SEG = [
    ("26", 25.5, 1.1, 315, HOOK, 0, 0.6),       # HOOK and cover: jet side-on over the sea, afterburner lit, zoomed and brightened
    ("24", 0.3, 15.6, 420, DAY, 0),             # sheriff pickup along the fence, onto the apron, stars on
    ("24", 15.55, 2.3, 340, DAY, 0),            # pulls up at the fighters, jumps out
    ("24", 17.5, 12.1, 420, DAY, 0),            # runs along the line of jets, picks one, ladder, cockpit
    ("26", 2.75, 27.2, 420, AIR, 0),            # afterburner, taxi, runway, take-off, out over the sea
    ("27", 0.5, 6.5, 420, AIR, 2.0),            # enjoying it: rolls above the clouds
]
SEG_HUD = {"segs": [4], "crop": "196:40:1704:24", "scale": 4.4, "border": "e0344a"}
CAP = []
HUD_SRC = None
HUD_SEG = None
