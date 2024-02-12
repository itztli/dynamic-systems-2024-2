#!/usr/bin/env python3

# Author: Victor De la Luz
# email: vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

import sys

x0 = float(sys.argv[1]) # 1) Initial Condition
#x0 = 1.5   # 1) Initial Condition
print("#x0="+str(x0)+",x = x + 1")
print("#i\tx_i")
x = x0      
print(str(0)+'\t'+str(x))
for i in range(100-1):  # 3) Iterate
    x = x + 1.0   # 2) Matematical expression (recursive).
    print(str(i+1)+'\t'+str(x))
