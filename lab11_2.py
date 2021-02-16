from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.01)
def func(z,t):
    x, y=z
    dx_dt=k1*(a0-x-y)
    dy_dt=k2*(a0-x-y)
    return dx_dt, dy_dt
a0=15
k1=0.5
k2=0.3
x0=0
y0=0
z0=x0,y0
sol=odeint(func,z0,t)
plt.plot(t,sol[:,1],'r',label='dx_dt')
plt.plot(t,sol[:,0],'b',label='dy_dt')
plt.show()