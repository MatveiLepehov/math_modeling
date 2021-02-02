from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,2*np.pi,0.1)
def radio_function (w,t):
    dmdt=(l*np.pi*r**2)/(4*np.pi*q*v)
    return dmdt
r=6400000
v=30400
q=147*10**9  
l=3.827*10**26
solve_Bi=odeint(radio_function, l,t)
plt.plot(t,solve_Bi[:,0])
plt.show()