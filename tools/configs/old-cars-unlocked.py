# Two old cars, both start (24 Nov raw 06, one continuous take). Zubair's idea 2 of 26 Nov: "look, I learned how
# to unlock 🔓 😂". Callback to his best TikTok ("Broke the window. STILL can't drive it", 60K).
# Hook and cover (no fade-in) = 06 at 3.75: elbow through the window of the white '81 Walton, the blue Rancher
# already in the background. Then the whole clip in order: walks up, smashes the window, hotwires, drives a few
# metres, gets out, walks to the blue '86 Rancher (unlocked), hotwires, drives off. The game's vehicle name card
# ("DECLASSE '81 WALTON", "'86 RANCHER") is enlarged under the video while it is on screen.
# Line and caption picked by Zubair (2b): "Remember when I couldn't steal ONE car in GTA 6? 😂" / "no clone key needed 🔓".
# AUDIO: the car radio plays in the source at 11.3 to 16.4 s and from 27.65 s (video 10.65 to 15.75 and from 27.0):
# mute the game sound there; own light music (tools/sneaky.py) runs under everything.
W = "/home/claude/work/raw1124"
OUT = "/home/claude/work/out/oldcars-game.mp4"
STYLE = "simple"
TITLE = "Remember when I couldn't steal ONE car in GTA 6? 😂"
CRF = 26
ENC_EXTRA = ["-maxrate", "4M", "-bufsize", "8M"]
DAY = "eq=brightness=0.02:contrast=1.07:saturation=1.16"
SEG = [
    ("06", 3.75, 0.9, 340, DAY, 0),             # HOOK and cover: elbow through the window
    ("06", 1.2, 7.1, 340, DAY, 0),              # walks up, smashes the window, gets in
    ("06", 7.95, 4.85, 340, DAY, 0),            # hotwire, '81 Walton card on screen
    ("06", 12.45, 13.35, 340, DAY, 0),          # drives, gets out, walks to the blue Rancher, gets in
    ("06", 25.45, 4.15, 340, DAY, 2.5),         # hotwire, '86 Rancher card, engine on, held
]
SEG_HUD = {"segs": [2, 4], "crop": "304:114:32:694", "crops": {4: "304:114:32:764"}, "scale": 2.2, "border": "2de2d0"}
CAP = []
HUD_SRC = None
HUD_SEG = None
