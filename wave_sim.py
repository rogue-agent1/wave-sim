#!/usr/bin/env python3
"""wave_sim - 1D wave equation simulation."""
import argparse, math

def simulate(n=100, steps=200, c=1.0, dx=1.0, dt=0.5):
    u_prev = [0.0]*n; u_curr = [0.0]*n
    # Initial pulse
    for i in range(n):
        x = (i - n//4) / (n/20)
        u_curr[i] = math.exp(-x*x)
    r = (c*dt/dx)**2
    history = [u_curr[:]]
    for _ in range(steps):
        u_next = [0.0]*n
        for i in range(1, n-1):
            u_next[i] = 2*u_curr[i] - u_prev[i] + r*(u_curr[i+1]-2*u_curr[i]+u_curr[i-1])
        u_prev, u_curr = u_curr, u_next
        history.append(u_curr[:])
    return history

def main():
    p = argparse.ArgumentParser(description="1D wave simulation")
    p.add_argument("-n", "--points", type=int, default=80)
    p.add_argument("-s", "--steps", type=int, default=200)
    p.add_argument("--frames", type=int, default=10)
    args = p.parse_args()
    history = simulate(args.points, args.steps)
    ticks = " ▁▂▃▄▅▆▇█"
    step_size = max(1, len(history) // args.frames)
    for i in range(0, len(history), step_size):
        row = history[i]
        mn, mx = min(row), max(row)
        rng = mx - mn or 1
        line = "".join(ticks[min(int((v-mn)/rng*8), 8)] for v in row)
        print(f"t={i:3d} {line}")

if __name__ == "__main__":
    main()
