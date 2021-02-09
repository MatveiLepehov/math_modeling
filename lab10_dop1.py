from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-1,1,0.01)
def obdolbosfunc(v,x):
    y,t,z=v
    dx_dt=3*x-y+z
    dy_dt=x+y+z
    dz_dt=4*x-y+4*z
    return dx_dt, dy_dt, dz_dt
y0=1
z0=-3
x0=-71
omega0=0
v0=y0,x0,z0
sol=odeint(obdolbosfunc,v0,x)
plt.plot(x,sol[:,1],'r')
plt.plot(x,sol[:,0],'b')
plt.plot(x,sol[:,2],'g')
plt.show()