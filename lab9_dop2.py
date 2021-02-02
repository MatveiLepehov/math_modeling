from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(6,18,0.1)
def radio_function (s0,t):
    dsdt=E0*s*np.cos((np.pi/12)*(t-12))*k*((s/np.pi)**0.5)
    return dsdt
k=300*10**(-8)
E0=1367
s0=1600
solve_Bi=odeint(radio_function, s0,t)
plt.plot(t,solve_Bi[:,0])
plt.show()