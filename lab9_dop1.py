from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
r0=6378100
h0=5*r0
r=np.arange(h0,r0,-100)
def radio_function (v,r):
    dvdr=-((G*M)/(r**2*v))
    return dvdr
M=5.97*10**24
G=6.67*10**(-11)
v0=0.01
solve_Bi=odeint(radio_function,v0,r)
plt.plot(r,solve_Bi[:,0])
plt.show()
