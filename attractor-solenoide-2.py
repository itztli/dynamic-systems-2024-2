#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import random

X=[]
Y=[]
T=[]

N = 400
dx = 1.0/float(N/2)
dy = 1.0/float(N/2)
dt = 1.0/float(2*N)

A = np.arange(0,1+dx,dx)
B = np.arange(0,1+dy,dy)
C = np.arange(0,1,dt)

# x0
for x in A:
    for y in B:
        for t in C:
            if (x*x+y*y) <= 1.0:
                X.append(x)
                Y.append(y)
                T.append(t)

                X.append(-x)
                Y.append(y)
                T.append(t)

                X.append(-x)
                Y.append(-y)
                T.append(t)

                X.append(x)
                Y.append(-y)
                T.append(t)

print(len(X))

X1 = []
Y1 = []
T1 = []

# x1 sub x
for x,y,t in zip(X,Y,T):
    dado = random.randint(0, 100000)
    if dado == 1:
        X1.append(x)
        Y1.append(y)
        T1.append(t)

print(len(X1))

X2 = np.array(X1)
Y2 = np.array(Y1)
T2 = np.array(T1)

# x1 = f(x1)
for i in range(3):
    print("Itera:",i)
    X2 = 0.25*(X2+2.0*np.cos(2.0*np.pi*T2))
    Y2 = 0.25*(Y2+2.0*np.sin(2.0*np.pi*T2))
    T2 = 2.0*T2 % 1.0
    #T2 = T3
    #X2 = X3
    #Y2 = Y3

XT = []
YT = []
ZT = []

# Transformacion lineal para visualizar
for x,y,t in zip(X2,Y2,T2):    
    XT.append((10.0+x)*np.cos(t*2.0*np.pi))
    YT.append((10.0+x)*np.sin(t*2.0*np.pi))
    ZT.append(y)

#print(len(X1))
   
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#ax = fig.add_subplot()  
ax.axes.set_xlim3d(left=-11.0, right=11.0) 
ax.axes.set_ylim3d(bottom=-11.0, top=11.0) 
ax.axes.set_zlim3d(bottom=-11.0, top=11.0) 
ax.scatter(XT,YT,ZT)
plt.show()
