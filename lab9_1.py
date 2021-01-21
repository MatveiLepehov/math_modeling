from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,3000,0.1)
def radio_function (n,t):
    dmdt=k*n
    return dmdt
n=10
k=1/1200
solve_Bi=odeint(radio_function, n,t)
plt.plot(t,n*10*np.ones(len(t))) 
plt.plot(t,solve_Bi[:,0])
plt.show()

