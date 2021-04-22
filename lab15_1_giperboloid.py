import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
fig= plt.figure()
ax=p3.Axes3D(fig)
f=np.linspace(0,2*np.pi,100)
o= np.linspace(0,2*np.pi,100)

x=2*np.outer(np.cos(f),np.sinh(o))
y=3*np.outer(np.sin(f),np.sinh(o))
z=np.outer(4,(np.sinh(o)))
ax.plot_surface(x,y,z,color='b')
plt.show()