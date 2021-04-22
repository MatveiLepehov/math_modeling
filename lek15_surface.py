import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
fig= plt.figure()
ax=p3.Axes3D(fig)
phi=np.linspace(0,2*np.pi,100)
theta= np.linspace(0,np.pi,100)

x=10*np.outer(np.cos(phi),np.sin(theta))
y=10*np.outer(np.sin(phi),np.sin(theta))
z=10*np.outer(np.ones(np.size(phi)),np.cos(theta))
ax.plot_surface(x,y,z,color='b')
plt.show()