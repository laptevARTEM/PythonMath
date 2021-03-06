import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,simplify,lambdify,sin,integrate,pprint
plt.close('all')
a=2; b=3
x=symbols('x')
fx=(2-4*x)*sin(2*x)
ix=simplify(integrate(fx, x))
print('Первісна =');pprint(ix)
s=integrate(fx, (x,a,b))
print('Площа \u2248 %6.4f'% s.evalf())
xx=np.linspace(-2,3,101)
f=lambdify(x,fx,'numpy')
yf=f(xx)
p=lambdify(x,ix,'numpy')
yp=p(xx)
fig, ax = plt.subplots(1, 1)
ax.plot(xx,yf,'b',lw=3,label='f(x)')
ax.plot(xx,yp,'g',lw=3,label='\u222Bf(x)dx')
ax.legend(fontsize=12,loc='lower right' )
ax.axhline(color='black')
ax.axvline(color='black') 
xs = np.linspace(a, b, num=21)
ys=f(xs)
y0=np.zeros(len(ys))
ax.fill_between(xs, ys, y0, color='c') 