from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
def radio_function (v,t):
    dmdt=(-G/m)*v**2+a0
    return dmdt
v0=0
m=5
a0=1
G=0.5
solve_Bi=odeint(radio_function, v0,t)
plt.plot(t,solve_Bi[:,0])
plt.show()
