import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=1,b=1,c=0,xa=-10,xb=10,dx=0.1,title='Parabola plotter'):
    x=np.arange(xa,xb,dx)
    y=a*x**2+b*x+c
    plt.plot(x,y,label='my parabola')
    plt.xlabel('Coord x')
    plt.ylabel('Coord y')
    plt.legend()
    plt.show()
parabola_plotter()

import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(k=2,x=3,xa=-10,xb=10,dx=1,title='Parabola plotter'):
    x=np.arange(xa,xb,dx)
    y=k/x
    plt.plot(x,y,label='my giperbpla')
    plt.xlabel('Coord x')
    plt.ylabel('Coord y')
    plt.legend()
    plt.show()
parabola_plotter()