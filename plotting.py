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
    x0, mat = ((data[0])[1:]).split(",")
    for line in data:
        if "#" not in line[0]:
            i, x = line.split("\t")
            I.append(float(i))
            X.append(float(x))

            #print(I)
            #print(X)

    ax.plot(I,X,label=x0)

#fig = plt.figure()

fig, ax = plt.subplots()

#dynamicPlot(ax,"data4.dat")
dynamicPlot(ax,"data5.dat")

plt.xlabel("i")
plt.ylabel("x_i")
plt.legend()
plt.show()
        
