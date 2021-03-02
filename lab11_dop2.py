import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation
	
frames = 200
	
t = np.linspace(0, 5, frames)

def move_func(z, t):
	
    x, v_x, y, v_y = z
	
    dxdt = v_x
	
    dv_xdt = -k*v**2
	
    dydt = v_y
	
    dv_ydt = - g
	
    return dxdt, dv_xdt, dydt, dv_ydt
g = 9.8
k=0.1
v = 15
alpha = 65 * np.pi / 180
x0 = 10
v_x0 =v * np.cos(alpha)
y0 = 0
v_y0 = v * np.sin(alpha)

z0 = x0, v_x0, y0, v_y0
def solve_func(i, key):
    sol = odeint(move_func, z0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='g')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,animate,frames=frames,interval=30)
edge = 20
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
ani.save('lab11_dop2.gif')
