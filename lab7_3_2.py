import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
fig,ax=plt.subplots()
ball,=plt.plot([],[],'-',color='r')
xdata,ydata=[],[]
edge=20
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(t):
    t=np.arange(0,2*np.pi,0.1)
    xdata.append(16*(np.sin(t)**3))
    ydata.append(13*(np.cos(t)**3)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))
    ball.set_data(xdata,ydata)
    return ball
ani=FuncAnimation(fig,animate,frames=np.arange(1,3,0.1),interval=100)
ani.save('lec7_2.gif')