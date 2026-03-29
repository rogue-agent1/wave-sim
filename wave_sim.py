#!/usr/bin/env python3
"""1D wave equation simulator using finite differences."""
import math

class WaveSim:
    def __init__(self, n=100, c=1.0, dx=0.1, dt=0.05):
        self.n = n; self.c = c; self.dx = dx; self.dt = dt
        self.u = [0.0] * n      # current
        self.u_prev = [0.0] * n  # previous
        self.r = (c * dt / dx) ** 2

    def init_gaussian(self, center=None, width=5):
        if center is None: center = self.n // 2
        for i in range(self.n):
            self.u[i] = math.exp(-((i - center) / width) ** 2)
            self.u_prev[i] = self.u[i]

    def init_sine(self, frequency=1):
        for i in range(self.n):
            self.u[i] = math.sin(2 * math.pi * frequency * i / self.n)
            self.u_prev[i] = self.u[i]

    def step(self):
        u_next = [0.0] * self.n
        for i in range(1, self.n - 1):
            u_next[i] = (2 * self.u[i] - self.u_prev[i] +
                        self.r * (self.u[i+1] - 2*self.u[i] + self.u[i-1]))
        # Fixed boundary conditions
        u_next[0] = 0; u_next[-1] = 0
        self.u_prev = self.u
        self.u = u_next

    def energy(self):
        ke = sum((self.u[i] - self.u_prev[i])**2 for i in range(self.n)) / (2 * self.dt**2)
        pe = sum((self.u[i+1] - self.u[i])**2 for i in range(self.n-1)) * self.c**2 / (2 * self.dx**2)
        return ke + pe

    def max_amplitude(self):
        return max(abs(x) for x in self.u)

if __name__ == "__main__":
    w = WaveSim(n=50)
    w.init_gaussian(width=3)
    for _ in range(100):
        w.step()
    print(f"Max amplitude: {w.max_amplitude():.4f}")

def test():
    w = WaveSim(n=50, c=1.0, dx=0.1, dt=0.05)
    w.init_gaussian(width=3)
    assert w.max_amplitude() > 0
    e0 = w.energy()
    for _ in range(100):
        w.step()
    # Wave should propagate (max amplitude decreases from spreading)
    assert w.max_amplitude() < 1.0
    # Boundary conditions
    assert w.u[0] == 0 and w.u[-1] == 0
    # Sine init
    w2 = WaveSim(n=100)
    w2.init_sine(frequency=2)
    assert w2.max_amplitude() > 0
    print("  wave_sim: ALL TESTS PASSED")
