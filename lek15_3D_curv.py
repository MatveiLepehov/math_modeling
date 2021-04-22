import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import axes3D

fig=plt.figure()
ax=fig.gca(projection='3d')
t=np.arange(0.01,4*np.pi,0.01)
r=1

x=r*np.cos(t)
y=r*t**0.5
z=r*np.log10(t)
ax.plot(x,y,z)
ax.legend()
arrow_x0=0
arrow_y0=0
arrow_z0=0

arrow_x1=1
arrow_y1=1
arrow_z1=1
ax.quiver(arrow_x0=0,arrow_y0=0,arrow_z0=0,arrow_x1=1,arrow_y1=1,arrow_z1=1,length=1,normalize=True,color='r')
plt.show()

