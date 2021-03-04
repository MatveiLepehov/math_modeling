import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 100
G = 9.8
t = np.linspace(0, 5, frames)
l0=2.5
q = 0.45

def move_1(variable, t):
    L, x= variable
    dx_dt = x
    d2x_dt2 = G*(x/L)-q*((L-x)/L)
    return  dx_dt, d2x_dt2
m = 0.5
x0 = 0.5

variable = l0, x0

def solve_func(i):
    sol = odeint(move_1, variable, t)
    z = l0-sol[i, 0]-x0
    z=-z
    if z > l0:
        z = l0
    x = [z, l0]
    y = [0, 0]
    return x, y
def solve_func_palk(i):
    sol = odeint(move_1, variable, t)
    x = [l0,l0]
    z = l0 - sol[i, 0]-x0
    z = -z
    if z > l0:
        z = l0
    y = [0,-z]

    return x, y

fig, ax = plt.subplots()

edge = 6
plt.axis("equal")
ax.set_xlim(0, edge)
ax.set_ylim(-edge-3, edge)

ball, = plt.plot([], [], 'o', color='r')
palk, = plt.plot([], [], '-', color='b')
palk1, = plt.plot([], [], '-', color='b')
def animate(i):
    palk.set_data(solve_func(i))
    palk1.set_data(solve_func_palk(i))
ani = FuncAnimation(fig,animate,frames=frames,interval=30)
plt.show()