from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0.1,3,0.01)
def obdolbosfunc(v,x):
    y, omega=v
    dy_dx=omega
    domega_dx=(((omega**2)/y)-((3*(y**3))/x**0.5))
    return dy_dx, domega_dx
y0=0.1
omega0=1
v0=y0,omega0
sol=odeint(obdolbosfunc,v0,x)
plt.plot(x,sol[:,1],'r',label='y(t)')
plt.plot(x,sol[:,0],'b',label='omega(t)')
plt.show()