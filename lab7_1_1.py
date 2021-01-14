import matplotlib.pyplot as plt
from math import sqrt, cos, sin
import numpy as np
def cikloida(r):
    t = np.linspace(-2*np.pi, 6*np.pi, 100)
    x = (r*(t - np.sin(t)))
    y = (r*(1 - np.cos(t)))
    plt.plot(x,y)
    plt.axis("equal")
    plt.show
cikloida(10)