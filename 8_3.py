import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.close('all')
A=np.array([0, 0, 0])
B=np.array([2, 1, 0])
C=np.array([1, 2, 0])
D=np.array([1.3, 1.1, 2])
X,Y,Z=zip(A,B,C,A,D,B,C,D)
fig = plt.figure()
ax=Axes3D(fig)
ax.plot(X,Y,Z,linewidth=4,c='k')
AB=B-A
AC=C-A
AD=D-A
mp=np.array([AB,AC,AD])
V=np.abs(np.linalg.det(mp))/6
print("Об’єм тетраедра \tV=%8.5f" % V)
Nrm=np.cross(AB,AC)
S=np.linalg.norm(Nrm)/2
print('Площа трикутника ABC\tS=%8.5f' % S)
h=3*V/S
print('Висота тетраедра \th=%8.5f' % h)
Nrm=-Nrm
n=Nrm/np.linalg.norm(Nrm)
E=(1/3)*(A+B+C)
xED,yED,zED=zip(D,E)
print(xED[1],yED[1],zED[1])
ax.plot(xED,yED,zED,linewidth=4,c='g')
ax.scatter(*E,s=100,c='r')
xAE,yAE,zAE=zip(A,E)
ax.plot(xAE,yAE,zAE,linewidth=4,c='b')