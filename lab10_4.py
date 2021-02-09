from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.01)
def obdolbosfunc(v,x):
    y, omega=v
    dy_dt=omega
    domega=(-5*y-omega)/4
    return dy_dt, domega
y0=3
omega0=-1
v0=y0,omega0
sol=odeint(obdolbosfunc,v0,x)
plt.plot(x,sol[:,1],'r',label='y(t)')
plt.plot(x,sol[:,0],'b',label='omega(t)')
plt.show()