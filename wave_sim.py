import argparse, math

def simulate(n=80, steps=200, c=1.0, dt=0.01, dx=0.1):
    u = [0.0] * n
    u_prev = [0.0] * n
    # Initial Gaussian pulse
    for i in range(n):
        x = (i - n//3) * dx
        u[i] = math.exp(-x*x * 10)
        u_prev[i] = u[i]
    frames = []
    r = (c * dt / dx) ** 2
    for step in range(steps):
        u_next = [0.0] * n
        for i in range(1, n-1):
            u_next[i] = 2*u[i] - u_prev[i] + r*(u[i+1] - 2*u[i] + u[i-1])
        u_next[0] = u_next[n-1] = 0  # Fixed boundaries
        u_prev = u[:]
        u = u_next[:]
        if step % (steps//10) == 0:
            frames.append((step, u[:]))
    return frames

def display(u, height=10):
    mn, mx = min(u), max(u)
    rng = mx - mn or 1
    grid = [[" "]*len(u) for _ in range(height)]
    for i, v in enumerate(u):
        row = int((1 - (v - mn) / rng) * (height - 1))
        row = max(0, min(height-1, row))
        grid[row][i] = "█"
    for row in grid: print("".join(row))

def main():
    p = argparse.ArgumentParser(description="1D wave simulation")
    p.add_argument("-n", "--width", type=int, default=60)
    p.add_argument("-s", "--steps", type=int, default=200)
    p.add_argument("-c", "--speed", type=float, default=1.0)
    args = p.parse_args()
    frames = simulate(args.width, args.steps, args.speed)
    for step, u in frames:
        print(f"--- t={step} ---")
        display(u)

if __name__ == "__main__":
    main()
