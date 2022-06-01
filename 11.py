import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import quad
plt.close('all')
f2=lambda x: 3*x**2-6*x-5
f1=lambda x: 6*x**2+3*x-5
x = np.linspace(-4, 3, 151)
y1=f1(x)
y2=f2(x)
fig = plt.figure(facecolor='white')
plt.plot(x,y1,'k-',x,y2,'b-',linewidth=4)
f =lambda x: f2(x)-f1(x)
x1=fsolve(f,-3)[0]
x2=fsolve(f,0.0)[0]
print('Точки перетину: {:6.3f} {:6.3f}'.format(x1,x2))
xf = np.linspace(x1, x2, 41)
yu=f2(xf)
yd=f1(xf)
plt.fill_between(xf, yu, yd, color='c')
s=quad(f, x1, x2)[0]
print('Площа між кривими={:6.4f}'.format(s))
