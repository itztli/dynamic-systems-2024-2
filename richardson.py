#!/usr/bin/env python3

# Author: Victor De la Luz
# email: vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

import sys
r = float(sys.argv[1])
x0 = float(sys.argv[2]) # 1) Initial Condition
N = int(sys.argv[3]) # iterations
#x0 = 1.5   # 1) Initial Condition
print("#r="+str(r)+",x0="+str(x0)+",x = rx(1-x)") #print initial conditions and equation
print("#i\tx_i")  # print header
x = x0      
print(str(0)+'\t'+str(x))
for i in range(N-1):  # 3) Iterate
    x = r*x*(1.0 - x)   # 2) Mathematical expression (recursive).
    print(str(i+1)+'\t'+str(x))
