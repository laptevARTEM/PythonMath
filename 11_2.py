import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import sin,cos,symbols,simplify,lambdify,exp,sqrt
plt.close('all')
x0=0; x1=4*np.pi
x=symbols('x')
f1=(x**2-2)*sin(x)+2*x*cos(x)
f2=(2-x**2)*cos(x)+2*x*sin(x)
fx1=simplify(f1.diff(x))
fx2=simplify(f2.diff(x))
fl=sqrt(fx1**2 + fx2**2)
Fl=lambdify(x, fl, 'numpy')
L=quad(Fl, x0, x1)[0]
print('Довжина = {:6.4f}'.format(L))
F=lambdify(x, f1, "numpy")
xc = np.linspace(-5, 13, 201)
yc=F(xc)
fig = plt.figure()
plt.plot(xc, yc, 'k-',linewidth=3 )
xsect = np.linspace(0, 4*np.pi, 101)
ysect=F(xsect)
plt.plot(xsect, ysect, 'r-',linewidth=6 )
plt.grid(True)