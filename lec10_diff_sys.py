from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
#определяем переменную величину
t=np.arange(0,10,0.01)
#определяем функцию для системы диф уравнений
def diff_func(z,t):#z-изменяемая величина
    theta,omega=z# указание изменяемых функций,через z
    #первое уравнение системы
    dtheta_dt=omega
    #второе уравнение системы
    domega_dt=-k*omega-c*np.sin(theta)
    return dtheta_dt, domega_dt
theta0=np.pi-0.1
omega0=0
z0=theta0,omega0
k=0.25
c=5
sol=odeint(diff_func,z0,t)
plt.plot(t,sol[:,1],'r',label='theta(t)')
plt.show()