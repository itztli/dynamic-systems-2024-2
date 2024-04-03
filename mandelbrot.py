#!/usr/bin/env python3
# by vdelaluz@enesmorelia.unam.mx
# GNU/GPL License
# Mandelbrot Set
import matplotlib.pyplot as plt
import numpy as np

global depth   

def mandelbrot(z_0, n, z_max):
    i=0
    z_n = z_0

    while ((abs(z_n) <= z_max) and  (i < n)):
        z_n = z_n*z_n + z_0
        i = i + 1
    #print(abs(z_n))

    if i == n:
        return True
    else:
        return False

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    x = event.x, event.y
    point = ax.transData.inverted().transform(x)
    x0 = point[0]
    y0 = point[1] 
    #print(point)

    plt.clf()

    depth = depth + 1
    ndepth = 10**(-depth)
    a = [x0 - ndepth,  y0 + ndepth]
    b = [x0 + ndepth ,y0 + ndepth]
    c = [x0 - ndepth, y0 - ndepth]
    d = [x0 + ndepth, y0 - ndepth]

    bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width*fig.dpi, bbox.height*fig.dpi

    nx=width
    ny=height

    print(nx,ny)
    
    X = np.linspace(a[0], b[0], int(nx))
    Y = np.linspace(b[1], d[1], int(ny))

    mandelbrot_set = []
    n=1000
    z_max = 4.0

    for y in Y:
        for x in X:
            z_0 = complex(x,y)
            print(z_0)
            if mandelbrot(z_0,n,z_max):
                mandelbrot_set.append(z_0)
                
    # extract real part
    x = [data.real for data in mandelbrot_set]
    # extract imaginary part
    y = [data.imag for data in mandelbrot_set]
    print("plotting")
    plt.scatter(x,y,marker='o', s=(72./fig.dpi)**2)
    print("done")
    plt.xlim([x0-ndepth, x0+ndepth])
    plt.ylim([y0-ndepth, y0+ndepth])
    fig.canvas.draw()

    
depth = 0    

n=1000
z_max = 4.0
#z_0 = 1 + 1j

mandelbrot_set = []

a = [-2, 1.0]
b = [ 0.5, 1.0]
c = [-2,-1]
d = [ 0.5,-1]

#dx = 1
#dy = 1

#nx = (b[0]-a[0]) / dx
#ny = (b[1]-d[1]) / dy

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)


bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width*fig.dpi, bbox.height*fig.dpi

nx=width
ny=height
print(nx,ny)

X = np.linspace(a[0], b[0], int(nx))
Y = np.linspace(b[1], d[1], int(ny))

for y in Y:
    for x in X:
        z_0 = complex(x,y)
        #print(z_0)
        if mandelbrot(z_0,n,z_max):
            mandelbrot_set.append(z_0)

# extract real part
x = [data.real for data in mandelbrot_set]
# extract imaginary part
y = [data.imag for data in mandelbrot_set]


plt.scatter(x,y,marker='o', s=(72./fig.dpi)**2)
plt.xlim([-2, 0.5])
plt.ylim([-1, 1.0])

print(z_0)


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()


