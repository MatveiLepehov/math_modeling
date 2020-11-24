import matplotlib.pyplot as plt
import numpy as np
def circlea_plotter (r=1,title='circle plotter'):
    x=np.arange(-2.0,2.0,0.1)
    y=np.arange(-2.0,2.0,0.1)
    X,Y = np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[r**2])
    plt.axis('equal')
    plt.show()
circlea_plotter(1)