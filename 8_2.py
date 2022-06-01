import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.close('all')
A = np.array([3, 3, -1])
B = np.array([1, 5, -2])
C = np.array([4, 1, 1])
AB=B-A
AC=C-A
D = A + (AB + AC)
print('Координати точки D:\t%8.2f %8.2f %8.2f' % (D[0],D[1],D[2]))
nrm = np.cross(AB,AC)
S = np.linalg.norm(nrm)
print('Площа паралелограма \tS=%8.5f' % S)
fig = plt.figure()
ax = Axes3D(fig)
X,Y,Z = zip(A,B,D,C,A)
ax.plot(X,Y,Z,linewidth=4,c='k')
ax.scatter(X,Y,Z,s=100,c='r')
t = np.linspace(0,1,9)
p,q = np.meshgrid(t,t)
X = A[0]+p*AB[0]+q*AC[0]
Y = A[1]+p*AB[1]+q*AC[1]
Z = A[2]+p*AB[2]+q*AC[2]
ax.plot_surface(X,Y,Z,rstride=1,cstride=2,color='c',alpha=0.3)
ne = nrm/np.linalg.norm(nrm)
E = A+AB+AC/2
ax.quiver(*E,*ne,linewidth=2,color='b',arrow_length_ratio=0.25)
xE,yE,zE = zip(A,E)
ax.plot(xE,yE,zE,linewidth=2,c='g')
ax.scatter([E[0]],[E[1]],[E[2]],s=100,c='r')