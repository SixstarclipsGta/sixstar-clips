"""Synthesize an original suspense/action music bed (no samples, no copyright).

python3 suspense.py OUT.wav DURATION --attempts 2.25,11.4,... --hits 22.7,31.45,... [--bpm 108 --bpm-end 132]
  attempts: times where a new beat starts (riser before, accent on it)
  hits:     big impact booms (e.g. WASTED moments)
"""
import argparse
import numpy as np
import wave

SR = 48000


def env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    e = np.minimum(1.0, t / max(a, 1e-4)) * np.exp(-t / max(r, 1e-4))
    return e


def lowpass(x, cutoff):
    # one-pole low-pass, vectorised enough for our lengths
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def saw(f, n, phase=0.0):
    t = np.arange(n) / SR
    return 2 * ((t * f + phase) % 1.0) - 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("dur", type=float)
    ap.add_argument("--attempts", default="")
    ap.add_argument("--hits", default="")
    ap.add_argument("--bpm", type=float, default=108)
    ap.add_argument("--bpm-end", type=float, default=132)
    a = ap.parse_args()
    attempts = [float(x) for x in a.attempts.split(",") if x]
    hits = [float(x) for x in a.hits.split(",") if x]
    N = int(a.dur * SR)
    L = np.zeros(N)
    R = np.zeros(N)
    rng = np.random.default_rng(7)

    # 1. drone: A1 + E2 detuned saws, low-passed, slow swell
    t = np.arange(N) / SR
    drone = 0.5 * saw(55.0, N) + 0.5 * saw(55.3, N, 0.3) + 0.35 * saw(82.41, N, 0.6)
    drone = lowpass(drone, 260.0)
    swell = 0.6 + 0.4 * np.sin(2 * np.pi * t / 8.0) ** 2
    drone *= 0.22 * swell
    L += drone
    R += drone * 0.95

    # 2. beat grid with accelerating tempo
    beats = []
    x = attempts[0] if attempts else 0.0
    while x < a.dur - 0.3:
        frac = x / a.dur
        bpm = a.bpm + (a.bpm_end - a.bpm) * frac
        beats.append((x, 60.0 / bpm))
        x += 60.0 / bpm / 2  # eighth notes

    kick_len = int(0.35 * SR)
    kt = np.arange(kick_len) / SR
    kick = np.sin(2 * np.pi * (45 + 90 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
    hat_len = int(0.05 * SR)
    hat = rng.standard_normal(hat_len) * env(hat_len, 0.001, 0.012)
    hat = hat - lowpass(hat, 6000)
    pluck_len = int(0.18 * SR)
    notes = [110.0, 110.0, 130.81, 110.0, 164.81, 110.0, 146.83, 130.81]  # A minor ostinato

    for i, (bt, beat) in enumerate(beats):
        s = int(bt * SR)
        if i % 2 == 0:  # quarter notes: heartbeat kick (double on every 4th)
            e = min(N, s + kick_len)
            L[s:e] += 0.55 * kick[: e - s]
            R[s:e] += 0.55 * kick[: e - s]
        e = min(N, s + hat_len)
        L[s:e] += 0.10 * hat[: e - s]
        R[s:e] += 0.13 * hat[: e - s]
        f = notes[i % len(notes)]
        e = min(N, s + pluck_len)
        p = saw(f, e - s) * env(e - s, 0.002, 0.07)
        L[s:e] += 0.07 * p
        R[s:e] += 0.08 * p

    # 3. risers (noise sweep 1.5 s) into each attempt + accent boom on it
    boom_len = int(1.6 * SR)
    bt_ = np.arange(boom_len) / SR
    boom = np.sin(2 * np.pi * (38 + 60 * np.exp(-bt_ * 6)) * bt_) * np.exp(-bt_ * 2.2)
    noise_tail = rng.standard_normal(boom_len) * np.exp(-bt_ * 5)
    boom = boom + 0.25 * lowpass(noise_tail, 900)
    for at in attempts[1:]:
        rl = int(1.5 * SR)
        s = max(0, int(at * SR) - rl)
        n = int(at * SR) - s
        if n > 0:
            ns = rng.standard_normal(n)
            ns = ns - lowpass(ns, 1500)
            ramp = np.linspace(0, 1, n) ** 2
            L[s:s + n] += 0.18 * ns * ramp
            R[s:s + n] += 0.18 * ns * ramp
        s = int(at * SR)
        e = min(N, s + boom_len)
        L[s:e] += 0.45 * boom[: e - s]
        R[s:e] += 0.45 * boom[: e - s]
    for h in hits + attempts[:1]:
        s = int(h * SR)
        e = min(N, s + boom_len)
        L[s:e] += 0.9 * boom[: e - s]
        R[s:e] += 0.9 * boom[: e - s]

    # fades and normalise
    fi, fo = int(0.05 * SR), int(1.5 * SR)
    for ch in (L, R):
        ch[:fi] *= np.linspace(0, 1, fi)
        ch[-fo:] *= np.linspace(1, 0, fo)
    peak = max(np.abs(L).max(), np.abs(R).max())
    L, R = L / peak * 0.89, R / peak * 0.89
    data = (np.stack([L, R], axis=1) * 32767).astype(np.int16)
    with wave.open(a.out, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


if __name__ == "__main__":
    main()
