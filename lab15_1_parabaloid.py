import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
fig= plt.figure()
ax=p3.Axes3D(fig)
f=np.linspace(0,2*np.pi,100)
o= np.linspace(0,2*np.pi,100)

x=np.outer(f,np.cos(o))
y=np.outer(f,np.sin(o))
z=np.outer(f**2,np.ones(np.size(f)))
ax.plot_surface(x,y,z,color='b')
plt.show()