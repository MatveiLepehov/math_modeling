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

import matplotlib.pyplot as plt
import numpy as np
def circlea_plotter (r=1,a=19.5,b=18,title='circle plotter'):
    x=np.arange(-22.0,22.0,0.1)
    y=np.arange(-22.0,22.0,0.1)
    X,Y = np.meshgrid(x,y)
    fxy=(X**2/a**2)+(Y**2/b**2)
    plt.contour(X,Y,fxy,levels=[1])
    plt.axis('equal')
    plt.show()
circlea_plotter()
