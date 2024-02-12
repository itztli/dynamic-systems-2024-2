#!/usr/bin/env python3

# Author: Victor De la Luz
# email: vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

import matplotlib.pyplot as plt

def dynamicPlot(ax, filename):
    with open(filename) as f:
        data = f.readlines()
    I = []
    X = []
    r,x0, mat = ((data[0])[1:]).split(",")
    for line in data:
        if "#" not in line[0]:
            i, x = line.split("\t")
            I.append(float(i))
            X.append(float(x))
            #print(I)
            #print(X)

    ax.plot(I,X,label=r+x0)
    ax.scatter(I,X,marker='o')
#fig = plt.figure()

fig, ax = plt.subplots()

#dynamicPlot(ax,"data4.dat")
dynamicPlot(ax,"richardson.dat")

plt.xlabel("i")
plt.ylabel("x_i")
plt.legend()
plt.show()
        
