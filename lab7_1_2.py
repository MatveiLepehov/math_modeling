import matplotlib.pyplot as plt
from math import sqrt, cos, sin
import numpy as np
def astroida(r):
    t = np.linspace(-2*np.pi, 6*np.pi, 100)
    x = (r*np.sin(t)**3)
    y = (r*np.cos(t)**3)
    plt.axis("equal")
    plt.plot(x,y)
    plt.show
astroida(3)