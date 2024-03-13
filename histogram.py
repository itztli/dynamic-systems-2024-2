#!/usr/bin/env python3

# Victor De la Luz
# vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

import matplotlib.pyplot as plt

with open("chaos.dat") as f:
    data = f.readlines()

X=[]
Y=[]
for line in data:
    if "#" not in line[0]:
        x,y = line.split("\t")
        X.append(float(x))
        Y.append(float(y))

plt.hist(Y,bins=10,density=True,stacked=True)
plt.show()
