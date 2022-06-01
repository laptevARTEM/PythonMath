import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad,nquad
from sympy import symbols,sqrt,integrate
plt.close('all')
f=lambda y,x: 12*x*y + 9*x**2 * y**2
g=lambda x: np.sqrt(x)
h=lambda x: -x**2
I1=dblquad(f, 0, 1, h, g)
print("I1 ={:5.3}".format(I1[0]))
xbnd=lambda : [0, 1]
ybnd=lambda x:[h(x),g(x)]
I2=nquad(f, [ybnd,xbnd])
print("I2 ={:5.3}".format(I2[0]))
xh = np.linspace(-1, 2, num=61)
xg = np.linspace(0, 2, num=41)
yg=g(xg)
yh=h(xh)
fig = plt.figure(facecolor='white')
plt.plot(xg, yg, 'k-', xh, yh,'b-',linewidth=4 )
xr = np.linspace(0, 1, num=21)
yrg=g(xr)
yrh=h(xr)
plt.fill_between(xr, yrg, yrh, color='c')
plt.grid(True)
x,y=symbols('x y')
fx= 12*x*y + 9*x**2 * y**2
I3 = integrate(fx,(y, -x**2, sqrt(x)), (x, 0, 1))
print("I3=",I3)