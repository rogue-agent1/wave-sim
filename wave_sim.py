#!/usr/bin/env python3
"""1D and 2D wave equation with finite differences."""
import sys, math

def wave_1d(n=100, steps=200, c=1.0, dt=0.01, dx=0.1):
    u = [0.0]*n; u_prev = [0.0]*n; u_next = [0.0]*n
    for i in range(n): u[i] = math.exp(-((i-n//4)**2)/20)  # Gaussian pulse
    u_prev = u[:]
    r = (c*dt/dx)**2; frames = [u[:]]
    for _ in range(steps):
        for i in range(1, n-1):
            u_next[i] = 2*u[i]-u_prev[i]+r*(u[i+1]-2*u[i]+u[i-1])
        u_next[0] = u_next[n-1] = 0
        u_prev, u, u_next = u, u_next, u_prev
        frames.append(u[:])
    return frames

def main():
    frames = wave_1d(60, 100)
    chars = " ·░▒▓█"
    print("1D Wave propagation:")
    for i in range(0, len(frames), 10):
        row = ""
        for v in frames[i]:
            level = int(min(abs(v)*5, 5))
            row += chars[level]
        print(f"t={i:3d}: {row}")

if __name__ == "__main__": main()
