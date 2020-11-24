import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=1,b=1,c=0,title='Parabola plotter'):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y,label='my parabola')
    plt.xlabel('Coord x')
    plt.ylebel('Coord y')
    plt.snow()
    plt.legend()
parabola_plotter()