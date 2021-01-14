import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='b',lw=2)
balltwo,=plt.plot([],[],'o',color='r',lw=2)
def circle_move(R):
    alpha=np.arange(0,2*np.pi,0.1)
    x=R*np.cos(alpha)
    y=R*np.sin(alpha)
    return x,y
def obeme(R):
    alpha=np.arange(0,2*np.pi,0.3)
    x=R*np.cos(alpha)
    y=R*np.sin(alpha)
    return x,y
edge=10
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(i):
    balltwo.set_data(obeme(R=i))
    ball.set_data(circle_move(R=i))
ani=FuncAnimation(fig,animate,frames=np.arange(0,10,0.1),interval=100)
