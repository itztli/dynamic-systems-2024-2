#!/usr/bin/env python3
# 20/04/2023
# by vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

import numpy as np
import matplotlib.pyplot as plt

def f(X,x0,y0,m):
    return m*(X-x0) + y0

def triangle(x0,y0,L,theta):
    R = [[np.cos(theta), -np.sin(theta)],
         [np.sin(theta), np.cos(theta)]]
    X = [-(L/2.0), (L/2.0), 0,-(L/2.0)]
    Y = [0,0,(np.sqrt(3)/2.0)*L,0]
    #plt.plot(X,Y)
    [X1,Y1] = np.dot(R,[X,Y])
    X1 = X1 +x0
    Y1 = Y1 +y0
    plt.plot(X1,Y1)

def fractal(depth, x0,y0,L,beta):
    if depth > 0:    
        #u1 = [x0,y0]
        #u2 = [x0 - (L/4), y0 + (np.sqrt(3)/2.0)*(L/2.0)]
        #u3 = [x0 + (L/4), y0 + (np.sqrt(3)/2.0)*(L/2.0)]
        x1, y1 = [-L/6.0,0.0]
        x2, y2 = [0, L/(2.0*np.sqrt(3))]
        x3, y3 = [L/6.0,0.0]
        U = [x1, x2, x3]
        V = [y1, y2, y3]
        #rotate 60 degrees == pi/6
        theta = np.pi/3.0
        R = [[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]]
        [U1,V1] = np.dot(R,[U,V])
        theta = -np.pi/3.0
        R = [[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]]
        [U2,V2] = np.dot(R,[U,V])
        theta = np.pi    
        R = [[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]]    
        [U3,V3] = np.dot(R,[U,V])
        # Trasladarlos U3,V3 se queda igual
        U1 = U1 - (L/4.0)
        V1 = V1 + np.sqrt(3.0)*L/4.0
        
        U2 = U2 + (L/4.0)
        V2 = V2 + np.sqrt(3.0)*L/4.0
        
        theta = beta
        
        R = [[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]]
        
        [U11,V11] = np.dot(R,[U1,V1])
        [U12,V12] = np.dot(R,[U2,V2])
        [U13,V13] = np.dot(R,[U3,V3])
        
        U11 = U11 + x0
        U12 = U12 + x0
        U13 = U13 + x0
        
        V11 = V11 + y0
        V12 = V12 + y0
        V13 = V13 + y0
        
        plt.plot(U11,V11)
        plt.plot(U12,V12)
        plt.plot(U13,V13)

        a = (U11[0] + U11[2]) /2.0
        b = (V11[0] + V11[2]) / 2.0
        theta = beta + np.pi /3.0
        fractal(depth-1, a,b,L/3.0,theta) 

        a = (U12[0] + U12[2]) /2.0
        b = (V12[0] + V12[2]) / 2.0
        theta = beta-np.pi/3.0

        fractal(depth-1, a,b,L/3.0,theta)

        a = x0
        b = y0
        theta = beta +np.pi
        fractal(depth-1, a,b,L/3.0,theta)
        
        ##U = [x0, x0 - (L/4), x0 + (L/4)]
    	##V = [y0, y0 + (np.sqrt(3)/2.0)*(L/2.0), y0 + (np.sqrt(3)/2.0)*(L/2.0)]
    	##
    	##
    	##[U1,V1] = np.dot(R,[U,V])
    	##
    	##triangle(U1[0], V1[0], L/3.0,np.pi/3.0,L/3,L/3)
    	##triangle(U1[1], V1[1], L/3.0, np.pi,L/3,L/3)
    	##triangle(U1[2], V1[2], L/3.0, -np.pi/3.0,L/3,L/3)
    	
    	#p1 = [x0-(L/2.0),y0]
    	#p2 = [x0+(L/2.0),y0]
    	#p3 = [x0, y0+ (np.sqrt(3)/2.0)*L]
    	
    	#dx = 0.001
    	#X0 = np.arange(x0 - L/2, x0 +dx, dx)
    	#X1 = np.arange(x0, x0 + L/2 +dx, dx)
    	#X2 = np.arange(x0-(L/2.0), x0 + (L/2.0) +dx, dx)
    	#m0 = np.sqrt(L*L - L*L/4.0) / (L/2.0) + m
    	#m1 = -m0
    	#plt.scatter(X2,f(X2,x0,y0,m))
    	#plt.scatter(X0,f(X0,x0-(L/2.0),y0,m0))
    	#plt.scatter(X1,f(X1,x0+(L/2.0),y0,m1))    

#X = np.arange(0,10,0.1)

#x0, y0 = 0.0, 0.0
#m=np.pi/4.0
#Y = f(X,x0,y0,m)

fig = plt.figure()
ax = fig.add_subplot(111)
depth = 9


triangle(0.0,0.0,1.0,0.0)
fractal(depth, 0.0,0.0,1.0,0.0) 
ax.set_aspect('equal','box')
#ax.set_xlim([-1, 1])
#ax.set_ylim([-1, 1])


plt.show()
