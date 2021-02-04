from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.01)
def ezfunc(v,x):
    y,z=v
    dy_dx=(y**2)*z
    dz_dx=z/x-y*z**2
    return dy_dx, dz_dx
y0=1
z0=-3
v0=y0,z0
sol=odeint(ezfunc,v0,x)
plt.plot(x,sol[:,1],'r',label='dy_dx')
plt.plot(x,sol[:,0],'b',label='dz_dx')
plt.show()