from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-1,1,0.01)
def ggfunc(v,t):
    x,y=v
    dx_dt=3*x-2*y+(np.exp(3*t))/(np.exp(t)+1)
    dy_dt=x-(np.exp(3*t))/(np.exp(t)+1)
    return dx_dt, dy_dt
x0=5
y0=-7
v0=x0,y0
sol=odeint(ggfunc,v0,t)
plt.plot(t,sol[:,1],'r',label='dx_dt')
plt.plot(t,sol[:,0],'b',label='dy_dt')
plt.show()