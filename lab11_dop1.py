from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,15,0.01)
def func(z,t):
    a, b, c= z
    dg_dt=-k1*a
    dp_dt=k1*a-k2*b
    dr_dt=k2*b-k3*c
    return dg_dt, dp_dt, dr_dt
k1=0.5
k2=0.3
k3=0.1
a0=15
b0=0
c0=0
z0=a0,b0,c0
sol=odeint(func,z0,t)
plt.plot(t,sol[:,1],'r',label='dx_dt')
plt.plot(t,sol[:,0],'b',label='dy_dt')
plt.plot(t,sol[:,2],'g',label='dr_dt')
plt.show()

