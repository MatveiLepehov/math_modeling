from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
#Пределы изменения переменной величины
#В данной задаче переменной величиной является время
t=np.arange(1,10**6,100)
#запись диф.уравнения в виде функции
def radio_function (m, t):
    dmdt=-k*m
    return dmdt
#определить начальные условий и параметров
m_0=10
k=1.61*10**(-6) # постоянная распада для Вмсмута 210
# решение дифференсальногог уравнения командой odeint
solve_Bi=odeint(radio_function, m_0,t)
#построение решения в виде графика функции 
plt.plot(t,solve_Bi[:,0],label='распад Висмута 210')
plt.show()

