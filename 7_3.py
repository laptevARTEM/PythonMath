import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
xmin=0; xmax=1
tmax=2*np.pi
nframes=100
fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)
ttl = ax.text(3.0, 0.9, '')
def u(x,t):
    return x**2 * np.sin(t)
def init():
    line.set_data([], [])
    ttl.set_text('')
    return line,ttl
def animate(i):
    x = np.linspace(xmin, xmax, 100)
    t=i*tmax/nframes
    y = u(x,t)
    ttl.set_text('t={:4.2f}'.format(t))
    line.set_data(x, y)
    return line,ttl
anim = FuncAnimation(fig, animate, init_func=init,
frames=nframes, interval=80, blit=True)
anim.save("C:\\Programming\\anim.gif",writer='pillow')