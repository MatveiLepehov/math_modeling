from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames=200
t=np.linspace (0,15,frames)
def func(z,t):
    y,v=z
    dy_dt=v
    dv_dt=g-(k/m)*y-0.8*m*v+5*np.cos(omega*t)
    return dy_dt,dv_dt
k=12.5
g=10
v0=0.5
l=0.08
omega=10
m=0.5
F0=1
y0=0.2
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
edge=2
ax.set_xlim(0,edge)
ax.set_ylim(0,1)
ani.save('lab11_3c.gif')