import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz
plt.close('all')
def f(x):
 return (3*x-2)*np.cos(5*x)
x = np.linspace(-3, 3, num=121)
y=f(x)
С=0
yint = cumtrapz(y, x, initial=None)+С
fig = plt.figure()
plt.plot(x[1:], yint, 'k-',linewidth=3,label='\u222Bf(x)dx' )
plt.plot(x,y,'r',linewidth=3,label='f(x)' )
plt.legend(fontsize=12,loc='upper left' )
plt.grid(True)
x0 = 1.5
i0 = np.where(x==x0)[0][0]
k1=(yint[i0+1]-yint[i0])/(x[i0+1]-x[i0])
xd1 = np.linspace(-1, 1, 20)
yd1 = yint[i0]+k1*(xd1-x[i0])
plt.plot(xd1,yd1,linestyle='--',color='b')