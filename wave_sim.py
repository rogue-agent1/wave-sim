#!/usr/bin/env python3
"""Wave Simulator - 1D and 2D wave propagation with reflection."""
import sys, math

def wave_1d(length=80, steps=60, speed=1.0, damping=0.99):
    u = [0.0]*length; u_prev = [0.0]*length
    mid = length // 2
    for i in range(length):
        u[i] = math.exp(-((i-mid)/3)**2)
    u_prev = u[:]
    frames = []
    for _ in range(steps):
        u_next = [0.0]*length
        for i in range(1, length-1):
            u_next[i] = 2*u[i] - u_prev[i] + speed**2*(u[i+1]-2*u[i]+u[i-1])
            u_next[i] *= damping
        frames.append(u[:])
        u_prev = u[:]; u = u_next[:]
    return frames

def render_1d(frame, height=10):
    mn, mx = min(frame), max(frame); rng = mx - mn or 1
    grid = [[" "]*len(frame) for _ in range(height)]
    for x, v in enumerate(frame):
        row = int((1 - (v - mn) / rng) * (height - 1))
        row = max(0, min(height - 1, row))
        grid[row][x] = "█"
    return ["".join(r) for r in grid]

def main():
    frames = wave_1d(70, 40)
    print("=== Wave Simulator ===\n")
    for i in [0, 5, 10, 15, 20, 30]:
        if i < len(frames):
            print(f"t={i}:")
            for line in render_1d(frames[i], 8): print(f"  {line}")
            print()

if __name__ == "__main__":
    main()
