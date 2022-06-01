import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
nframes=100
def X(t):
 return (t**2 - 2)*np.sin(t) + 2*t*np.cos(t)
def Y(t):
 return (2 - t**2)*np.cos(t) + 2*t*np.sin(t)
tmin=0; tmax=np.pi/3
t=np.linspace(tmin, tmax, 100)
x=X(t)
y=Y(t)
xmin=np.floor(min(x))
xmax=np.floor(max(x))+1
ymin=np.floor(min(y))
ymax=np.floor(max(y))+1
fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
ax.plot(x,y, lw=3,color='black')
ttl = ax.text(xmin+(xmax-xmin)/2, 0.9*ymax, '')
def animate(i):
 tp=tmin+i*(tmax-tmin)/nframes
 xp=X(tp)
 yp=Y(tp)
 ttl.set_text('t={:4.2f}'.format(tp))
 pt=ax.scatter([xp],[yp],linewidth=10,color='red')
 return pt,ttl
anim = FuncAnimation(fig, animate, frames=nframes,
interval=10, blit=True)