import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.close('all')
A=np.array([0, -3, 1])
B=np.array([-4, 1, 2])
C=np.array([2, -7, 5])

fig = plt.figure()
ax=Axes3D(fig)
X,Y,Z=zip(A,B,C)
ax.scatter(X,Y,Z,s=100,c='r')
X,Y,Z=zip(A,B,C,A)
ax.plot(X,Y,Z,linewidth=4,c='k')
d=np.array([B-A,C-A])
detx=np.linalg.det(d[:,1:])
dety=np.linalg.det(d[:,[0,2]])
detz=np.linalg.det(d[:,0:-1])
x= np.linspace(-8,4,61)
y= np.linspace(-8,4,81)
X,Y=np.meshgrid(x,y)
Z=A[2]+1/detz*((Y-A[1])*dety-(X-A[0])*detx)
ax.plot_surface(X,Y,Z,rstride=5, cstride=5,color='c',alpha=0.5)