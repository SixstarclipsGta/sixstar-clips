# Farm guards fail, explainer v2 (24 Nov): the whole escape clip (22 Nov raw 23) as it is, frozen at each
# guard's reaction with a ring + zoom + caption. Hook = the guard who falls onto the road.
SRC = "/home/claude/w21b/raw/23.mp4"
OUT = "/home/claude/w21b/out/guards-explainer.mp4"
TITLE = "13 years for this AI 😂"
END = 29.9
CROP = (200, 1440)
MUSIC = "/home/claude/w21b/out/guards.wav"
HOOK = "fall"
FREEZES = {
    "run":  dict(t=1.20, cx=282, cy=418, rx=55, ry=70, z=2.5, cap="He had a gun… and ran away 🏃"),
    "fall": dict(t=17.60, cx=1275, cy=505, rx=70, ry=55, z=2.5, cap="Then he just… fell onto the road 😂",
                 hookcap="Watch this guard 👀"),
    "gate": dict(t=26.20, cx=735, cy=540, rx=50, ry=70, z=2.5, cap="Gate guard didn't even try 😅"),
    "fly":  dict(t=28.12, cx=1400, cy=760, rx=170, ry=95, z=2.0, cap="…and this one learned to fly 🕊️"),
}
ORDER = ["run", "fall", "gate", "fly"]
EXTRA_CAPS = [("He screams pretty real though 😅", 26.8, 30.3)]
