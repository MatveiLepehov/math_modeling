from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames=200
t=np.linspace (0,5,frames)
def func(z,t):
    y, v=z
    dy_dt=v
    dv_dt=-g-M*v
    return dy_dt, dv_dt
M=0.2
g=9.8
v0=20
y0=1
z0=y0,v0
def solve_func (i,key):
    sol=odeint(func,z0,t)
    if key =='point':
        x=np.ones(len(t))
        y=sol[i,0]
    return x,y
fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r')
def animate(i):
    ball.set_data(solve_func(i,'point'))
ani=FuncAnimation(fig,animate,frames=frames,interval=30)
edge=20
ax.set_xlim(0,edge)
ax.set_ylim(0,edge)
ani.save('lab11_1.gif')