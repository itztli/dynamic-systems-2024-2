#!/usr/bin/env python3

# Author: Victor De la Luz
# email: vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

x0 = 3   # 1) Initial Condition
print("#i\tx_i")
x = x0      
print(str(0)+'\t'+str(x))
for i in range(100-1):  # 3) Iterate
    x = x + 1   # 2) Matematical expression (recursive).
    print(str(i+1)+'\t'+str(x))
