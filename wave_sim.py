#!/usr/bin/env python3
"""1D wave equation simulation."""
import math
def simulate(n=200,c=1.0,dt=0.01,dx=0.05,steps=500):
    r=(c*dt/dx)**2;u=[[0.0]*n for _ in range(3)]
    for i in range(n): u[0][i]=math.exp(-((i-n//4)*dx)**2/0.1)
    for i in range(1,n-1): u[1][i]=u[0][i]+0.5*r*(u[0][i+1]-2*u[0][i]+u[0][i-1])
    history=[list(u[0]),list(u[1])]
    for _ in range(steps):
        for i in range(1,n-1): u[2][i]=2*u[1][i]-u[0][i]+r*(u[1][i+1]-2*u[1][i]+u[1][i-1])
        u[0],u[1],u[2]=u[1],u[2],u[0];history.append(list(u[1]))
    return history
if __name__=="__main__":
    h=simulate()
    energy=sum(x*x for x in h[-1])
    print(f"Wave sim: {len(h)} frames, final energy={energy:.4f}")
    print("Wave equation OK")
