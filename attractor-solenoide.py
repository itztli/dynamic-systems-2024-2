#!/usr/bin/env python3
import numpy as np
#import matplotlib.pyplot as plt

def F(t,x,y):
    return (2.0*t) % 1, 0.25*(x + 2.0*np.cos(2.0*np.pi*t)), 0.25*(y+ 2.0*np.sin(2.0*np.pi*t))

iterations=10
N = 100


dt = 1.0/N
# T^1
T = np.arange(0.0,1.0,dt)
#print(T)

X = np.arange(0.0,1.0+dt,dt)
Y = np.arange(0.0,1.0+dt,dt)

# D^2
D_x = []
D_y = []

for x in X:
    for y in Y:
        if (x**2 + y**2) <= 1:
            # I
            D_x.append(x)
            D_y.append(y)
            # II
            D_x.append(-x)
            D_y.append(y)
            # III
            D_x.append(-x)
            D_y.append(-y)
            # IV
            D_x.append(x)
            D_y.append(-y)

            
#print(D_x)
#print(D_y)

A=[]
B=[]
C=[]
index=0
for x,y in zip(D_x,D_y):
    for t in T:
        A.append(t)
        B.append(x)
        C.append(y)
        print(index,t,x,y)
#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')  
#ax.scatter(A,B,C)
#plt.savefig("results/attractor-"+str(index)+".png")

for i in range(iterations):
    A2=[]
    B2=[]
    C2=[]
    index = index+1
    # x = F(x)
    total = float(len(A)*len(B)*len(C))
    j=0
    k=0
    for t,x,y in zip(A,B,C):
        j=j+1
        k=k+1
        if (j % 100) == 0:
            print((float(k)/total)*100.0)
            j=0
        #t0,x0,y0 = F(t,x,y)
        t0 = (2.0*t) % 1.0
        x0 = 0.25*(x + 2.0*np.cos(2.0*np.pi*t))
        y0 = 0.25*(y+ 2.0*np.sin(2.0*np.pi*t))
        A2.append(t0)
        B2.append(x0)
        C2.append(y0)
        print(index,t0,x0,y0)
    #print(index, len(A2), len(B2), len(C2))
    A = A2
    B = B2
    C = C2
    #fig = plt.figure()
    #ax = fig.add_subplot(projection='3d')  
#    ax.cla() 
#    ax.scatter(A,B,C)
#    ax.axes.set_xlim3d(left=0.0, right=1.0) 
#    ax.axes.set_ylim3d(bottom=-1.0, top=1.0) 
#    ax.axes.set_zlim3d(bottom=-1.0, top=1.0) 
#    plt.savefig("results/attractor-"+str(index)+".png")


#plt.show()
