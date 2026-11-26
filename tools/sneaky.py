#!/usr/bin/env python3
"""Light "sneaky" comedy bed: pizzicato bass walk, soft shaker, finger snaps. Own music, no samples.
Usage: sneaky.py OUT.wav DUR [--bpm 104] [--stings t1,t2]   (stings = short high pluck chord at those times)
Made 26 Nov 2026 because the suspense track is wrong for calm or funny clips (Zubair: "your music was off")."""
import argparse, wave
import numpy as np

SR = 44100

def pluck(freq, dur, damp=0.996, bright=0.5, seed=0):
    """Karplus-Strong plucked string."""
    n = int(SR * dur)
    period = max(2, int(SR / freq))
    rng = np.random.default_rng(seed)
    buf = rng.uniform(-1, 1, period)
    # soften the excitation so it sounds like a finger, not a pick
    buf = bright * buf + (1 - bright) * np.convolve(buf, np.ones(5) / 5, mode="same")
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % period]
        buf[i % period] = damp * 0.5 * (buf[i % period] + buf[(i + 1) % period])
    env = np.minimum(1, np.arange(n) / (0.003 * SR)) * np.exp(-np.arange(n) / (0.35 * dur * SR))
    return out * env

def noise_hit(dur, lo, hi, decay, seed=0):
    n = int(SR * dur)
    rng = np.random.default_rng(seed)
    x = rng.normal(0, 1, n)
    spec = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    spec[(f < lo) | (f > hi)] = 0
    x = np.fft.irfft(spec, n)
    return x / (np.abs(x).max() + 1e-9) * np.exp(-np.arange(n) / (decay * SR))

def add(mix, sig, t, gain):
    i = int(t * SR)
    if i >= len(mix):
        return
    j = min(len(mix), i + len(sig))
    mix[i:j] += gain * sig[: j - i]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("dur", type=float)
    ap.add_argument("--bpm", type=float, default=104)
    ap.add_argument("--stings", default="")
    a = ap.parse_args()
    mix = np.zeros(int(SR * (a.dur + 1)))
    e = 60 / a.bpm / 2                      # one eighth note
    A = 110.0
    semi = lambda k: A * 2 ** (k / 12)
    # two-bar walking figure in A minor, eighth notes; None = rest (the gaps make it sound like tiptoeing)
    bars = [
        [0, None, 3, None, 7, None, 3, 5],
        [0, None, 3, None, 6, 7, None, None],
        [-2, None, 2, None, 5, None, 2, 3],
        [-5, None, -1, None, 2, 4, None, None],
    ]
    cache = {}
    t, bar = 0.0, 0
    snap = noise_hit(0.09, 1500, 5000, 0.018, 3)
    shaker = noise_hit(0.05, 5000, 11000, 0.012, 5)
    while t < a.dur:
        pat = bars[bar % len(bars)]
        for k, note in enumerate(pat):
            tt = t + k * e
            if tt >= a.dur:
                break
            if note is not None:
                if note not in cache:
                    cache[note] = pluck(semi(note), 0.45, seed=note + 20)
                add(mix, cache[note], tt, 0.9)
                if k in (4, 5) and bar % 2 == 1:      # little answer an octave up at the end of every second bar
                    hi = (note + 12, "hi")
                    if hi not in cache:
                        cache[hi] = pluck(semi(note + 12), 0.3, bright=0.7, seed=note + 60)
                    add(mix, cache[hi], tt + e / 2, 0.35)
            add(mix, shaker, tt, 0.10 if k % 2 else 0.16)
            if k in (2, 6):
                add(mix, snap, tt, 0.30)
        t += 8 * e
        bar += 1
    for s in [float(x) for x in a.stings.split(",") if x]:
        for j, k in enumerate((12, 16, 19, 24)):
            add(mix, pluck(semi(k), 0.9, bright=0.8, seed=100 + k), s + 0.045 * j, 0.5)
    mix = mix[: int(SR * a.dur)]
    fade = int(0.8 * SR)
    mix[-fade:] *= np.linspace(1, 0, fade)
    mix = np.tanh(1.4 * mix / (np.abs(mix).max() + 1e-9)) * 0.85
    st = np.stack([mix, mix], axis=1)
    with wave.open(a.out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype("<i2").tobytes())

if __name__ == "__main__":
    main()
