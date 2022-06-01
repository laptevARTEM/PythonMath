import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,lambdify,solve,limit,oo
import warnings
plt.close('all')
x,y=symbols('x y')
f=((x**2)-6*x+4)/(3*x-2)
a= limit(f/x,x,oo)
b= limit(f-a*x,x,oo)
fasm=a*x+b
print('Рівняння асимптоти: y=',fasm)
sols=solve(3*x-2,x)
print('Корені знаменника:',sols)
print('Границя =',limit(f,x,sols[0]))
F=lambdify(x, f, "numpy")
X=np.linspace(-5,5,101)
warnings.filterwarnings('ignore')
Y=F(X)
plt.plot(X,Y,'b',linewidth=3)
Fasm=lambdify(x, fasm, "numpy")
Yasm=Fasm(X)
plt.plot(X,Yasm,linestyle='--',color='r')
kl=np.where(Y==np.inf)
print(kl)
plt.vlines(2/3,-6,6,linestyle='--',color='r')
plt.axhline(color='k')
plt.axvline(color='k')
plt.grid(True)
