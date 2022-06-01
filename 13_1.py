import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.close('all')
def f(y,x):
 return (2*x**2)/(1+x**2) - y*(2*x)/(1+x**2)
x = np.linspace(0,4,29)
y0 = 2/3
y = odeint(f, y0, x)
y = np.array(y).flatten() 
plt.plot(x, y,'-sb',linewidth=3)
i0 = np.where(y==y0)
plt.scatter(i0, y0, s=100,color='r')