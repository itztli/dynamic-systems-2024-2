#!/usr/bin/env python3

# By vdelaluz@enesmorelia.unam.mx
# GNU/GPL License
# Figure 1, Ergodic Dynamics https://doi-org.pbidi.unam.mx:2443/10.1007/978-3-030-59242-4

# F(x,y) = (x + t, y +alpha t) (mod 1)

import matplotlib.pyplot as plt
import math

alpha = 1.0/math.sqrt(2.0)
x0, y0 = 0.0, 0.1
t0 = 0.01
N = 1000

x = x0
y = y0
t = t0
X = []
Y = []
for i in range(N):
    x = (x + t) % 1
    X.append(x)
    y = (y + alpha*t) % 1
    Y.append(y)

plt.scatter(X,Y)
plt.show()

    
