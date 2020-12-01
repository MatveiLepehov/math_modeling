import matplotlib.pyplot as plt
import numpy as np
def spiral(b=0.1):
    f=np.arange(0,8*np.pi,0.1)
    r=np.e**(b*f)
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.show
spiral()

def spiral(b=0.1,k=0.1):
    f=np.arange(0,8*np.pi,0.1)
    r=k*f
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.show
spiral()

def spiral(k=0.1):
    f=np.arange(0.1,8*np.pi,0.1)
    r=k/(0.5*f)
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.show
spiral()

def spiral(k=0.1):
    f=np.arange(0,8*np.pi,0.1)
    r=np.sin(k*f)
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.show
spiral()