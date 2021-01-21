from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,8,0.1)
def radio_function (n,t):
    dmdt=k*-n*t
    return dmdt
n=1000
k=0.08
solve_Bi=odeint(radio_function, n,t)
plt.plot(t,solve_Bi[:,0])
plt.show()
