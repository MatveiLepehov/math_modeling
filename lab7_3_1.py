import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
fig,ax=plt.subplots()
ball,=plt.plot([],[],'-',color='r')
xdata,ydata=[],[]
edge=5
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(t):
    xdata.append(np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    ydata.append(np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    ball.set_data(xdata,ydata)
    return ball
ani=FuncAnimation(fig,animate,frames=np.arange(1,3,0.1),interval=100)
ani.save('lec7_2.gif') 