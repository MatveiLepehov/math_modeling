import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation		
frames = 365	
seconds_in_year = 365 * 24 * 60 * 60	
years = 1
t = np.linspace(0, years*seconds_in_year, frames)
def move_func(s, t):
    x, v_x, y, v_y, x2, v_x2, y2, v_y2, x3, v_x3, y3, v_y3, x4, v_x4, y4, v_y4 = s
    dxdt = v_x
    dv_xdt = - G * m * x / (x**2 + y**2)**1.5
    dydt = v_y
    dv_ydt = - G * m * y / (x**2 + y**2)**1.5
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * m * y2 / (x2**2 + y2**2)**1.5
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m * x3 / (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = - G * m * y3 / (x3**2 + y3**2)**1.5
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m * x4 / (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = - G * m * y4 / (x4**2 + y4**2)**1.5
    
    return dxdt, dv_xdt, dydt, dv_ydt, dxdt2, dv_xdt2, dydt2, dv_ydt2, dxdt3, dv_xdt3, dydt3, dv_ydt3, dxdt4, dv_xdt4, dydt4, dv_ydt4
G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x0 = 149 * 10**9
v_x0 = 0
y0 = 0
v_y0 = 30000

x20 = 58 * 10**9
v_x20 = 0
y20 = 0
v_y20 = 36000

x30 = 133 * 10**9
v_x30 = 0
y30 = 0
v_y30 = -36000

x40 = 144 * 10**9
v_x40 = 0
y40 = 0
v_y40 = 5000
s0 = (x0, v_x0, y0, v_y0, x20, v_x20, y20, v_y20, x30, v_x30, y30, v_y30, x40, v_x40, y40, v_y40)
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        x2= sol[i,4]
        y2=sol[i,6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 8]
        y4 = sol[i, 10]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        x2= sol[:i, 4]
        y2= sol[:i,6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
    return ((x, y), (x2,y2),(x3,y3),(x4,y4))

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')
ball2, = plt.plot([], [], 'o', color='g')
ball_line2, = plt.plot([], [], '-', color='g')
ball3, = plt.plot([], [], 'o', color='k')
ball_line3, = plt.plot([], [], '-', color='k')
ball4, = plt.plot([], [], 'o', color='r')
ball_line4, = plt.plot([], [], '-', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])
    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])
    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])
    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])

plt.plot([0], [0], 'o', color='y', ms=20)

ani = FuncAnimation(fig,animate,frames=frames,interval=30)
plt.axis('equal')
edge = 2*x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.show()