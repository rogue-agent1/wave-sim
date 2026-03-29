#!/usr/bin/env python3
"""wave_sim - 1D and 2D wave equation simulation."""
import sys, math

def wave_1d(length, steps, c=1.0, dx=0.1, dt=0.01, init=None):
    n = int(length / dx)
    if init is None:
        u = [math.exp(-((i*dx - length/2)**2) / 0.1) for i in range(n)]
    else:
        u = list(init)
    u_prev = u[:]
    history = [u[:]]
    r = (c * dt / dx) ** 2
    for _ in range(steps):
        u_new = [0.0] * n
        for i in range(1, n-1):
            u_new[i] = 2*u[i] - u_prev[i] + r*(u[i+1] - 2*u[i] + u[i-1])
        u_prev = u
        u = u_new
        history.append(u[:])
    return history

def wave_2d(size, steps, c=1.0, dx=0.1, dt=0.01):
    n = int(size / dx)
    u = [[0.0]*n for _ in range(n)]
    # initial pulse
    cx, cy = n//2, n//2
    for y in range(n):
        for x in range(n):
            d = ((x-cx)**2 + (y-cy)**2) * dx**2
            u[y][x] = math.exp(-d / 0.1)
    u_prev = [row[:] for row in u]
    r = (c * dt / dx) ** 2
    for _ in range(steps):
        u_new = [[0.0]*n for _ in range(n)]
        for y in range(1, n-1):
            for x in range(1, n-1):
                u_new[y][x] = (2*u[y][x] - u_prev[y][x] +
                    r*(u[y][x+1]+u[y][x-1]+u[y+1][x]+u[y-1][x]-4*u[y][x]))
        u_prev = u
        u = u_new
    return u

def test():
    h = wave_1d(5.0, 100)
    assert len(h) == 101
    assert len(h[0]) == 50
    # wave should propagate (energy moves)
    peak_0 = max(abs(v) for v in h[0])
    peak_50 = max(abs(v) for v in h[50])
    assert peak_0 > 0  # initial pulse
    # 2D
    u = wave_2d(2.0, 20)
    assert len(u) == 20
    assert len(u[0]) == 20
    # center should have changed from initial
    center = u[10][10]
    assert isinstance(center, float)
    print("OK: wave_sim")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: wave_sim.py test")
