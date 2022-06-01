import matplotlib.pyplot as plt
from sympy import symbols,integrate,And,solve,plot_implicit
plt.close('all')
x,y=symbols('x y')
Fun=x**2/4 + y**2
plot_implicit(And(Fun<=1,x>=0,y>=0), depth=2)
fig=plt.gcf()
ax=fig.gca()
ax.axis('equal')
ax.set_xlim(-1,2)
ax.set_ylim(-1,2)
x0=0; x1=2
y0=0
sols=solve(Fun-1,y)
print(sols)
y1=sols[1]
mu=30 * x**3 * y**7
m=integrate(mu,(y,y0,y1),(x,x0,x1))
print('Маса платівки=',m)