#!/usr/bin/env python3
"""1D wave equation simulation with ASCII display."""
import sys, math, time
def simulate(n=80, steps=100, speed=0.5, damping=0.999):
    u=[0.0]*n; v=[0.0]*n
    u[n//4]=1.0; u[3*n//4]=-1.0
    for step in range(steps):
        new_u=u[:]
        for i in range(1,n-1):
            new_u[i]=u[i]+v[i]; v[i]=(v[i]+speed*(u[i-1]-2*u[i]+u[i+1]))*damping
        u=new_u
        h=10; mn,mx=-1.5,1.5
        print(f"\033[2J\033[HStep {step}:")
        for row in range(h,-h-1,-1):
            threshold=row/(h+1)*(mx-mn)/2
            line=""
            for x in range(n): line+="█" if u[x]>=threshold else " "
            print(line)
        time.sleep(0.05)
def cli():
    steps=int(sys.argv[1]) if len(sys.argv)>1 else 60
    simulate(steps=steps)
if __name__=="__main__": cli()
