import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.close('all')
A=np.array([1, 2, 2])
B=np.array([1, 5, -2])
C=np.array([4, 5, 1])
X,Y,Z=zip(A,B,C,A)
fig = plt.figure()
ax=Axes3D(fig)
ax.plot(X,Y,Z,linewidth=4,c='k')
AB=B-A
AC=C-A
BC=C-B
LAB,LAC,LBC=map(np.linalg.norm,[AB,AC,BC])
sL='Довжини сторін: AB={:.4f}\tAC={:.4f}\tBC={:.4f}'.format(LAB,LAC,LBC)
print(sL)
def anglegrad(a,b):
 sp=np.dot(a,b)
 la=np.linalg.norm(a)
 lb=np.linalg.norm(b)
 alph=np.arccos(sp/la/lb)*180/np.pi

 return alph
aA,aB,aC=map(anglegrad,[AB,-AB,AC],[AC,BC,BC])
sA='Кути трикутника:\tA={:.2f} \tB={:.2f} \tC={:.2f}'.format(aA, aB, aC)
print(sA)
S=np.linalg.norm(np.cross(AB,AC))/2
print('Площа трикутника \tS=%6.5f' % S)
BA = A-B
x = -1*np.dot(BA,AC)/(LAC**2)
D = BA+x*AC
D = D+B
tmp = D.tolist()
tmp = [int(i) for i in tmp]
D = np.array(tmp)
print(BA,D)
xBD,yBD,zBD=zip(B,D)
ax.plot(xBD,yBD,zBD,linewidth=4,c='r')
ax.scatter([D[0]],[D[1]],[D[2]],s=100,c='r')