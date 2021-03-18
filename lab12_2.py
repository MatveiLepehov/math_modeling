import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation		
frames = 1000	
t = np.linspace(0, 100, frames)
def move_func(s, t):
    x, v_x, y, v_y, x2, v_x2, y2, v_y2, x3, v_x3, y3, v_y3, x4, v_x4, y4, v_y4, x5, v_x5, y5, v_y5 = s
    dxdt = v_x
    dv_xdt = (k*q1*q)/(m*(x**2+y**2)**1.5)
    dydt = v_y
    dv_ydt = (k*q1*q)/(m*(x**2+y**2)**1.5)
    
    dxdt2 = v_x2
    dv_xdt2 = (k*q2*q)/(m*(x2**2+y2**2)**1.5)
    dydt2 = v_y2
    dv_ydt2 = (k*q2*q)/(m*(x2**2+y2**2)**1.5)
    
    dxdt3 = v_x3
    dv_xdt3 = (k*q3*q)/(m*(x3**2+y3**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (k*q3*q)/(m*(x3**2+y3**2)**1.5)
    
    dxdt4 = v_x4
    dv_xdt4 = (k*q4*q)/(m*(x4**2+y4**2)**1.5)
    dydt4 = v_y4
    dv_ydt4 = (k*q4*q)/(m*(x4**2+y4**2)**1.5)
    
    dxdt5= v_x5
    dv_xdt5 = (k*q5*q)/(m*(x5**2+y5**2)**1.5)
    dydt5 = v_y5
    dv_ydt5 = (k*q5*q)/(m*(x5**2+y5**2)**1.5)
    return dxdt, dv_xdt, dydt, dv_ydt, dxdt2, dv_xdt2, dydt2, dv_ydt2, dxdt3, dv_xdt3, dydt3, dv_ydt3, dxdt4, dv_xdt4, dydt4, dv_ydt4, dxdt5, dv_xdt5, dydt5, dv_ydt5
k = 9*10**9
m = 1*10**9
q=100
q1=-1
q2=-1
q3=1
q4=1
q5=1
x0 = -30
v_x0 = 1
y0 = 20
v_y0 = 0

x20 = -30
v_x20 = 1
y20 = -20
v_y20 = 0

x30 = -30
v_x30 = 1
y30 = -40
v_y30 = 0

x40 = -30
v_x40 =1 
y40 = 40
v_y40 = 0

x50 = -30
v_x50 = 1
y50 = 0
v_y50 = 0
s0 = (x0, v_x0, y0, v_y0, x20, v_x20, y20, v_y20, x30, v_x30, y30, v_y30, x40, v_x40, y40, v_y40, x50, v_x50, y50, v_y50)
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        x2= sol[i,4]
        y2=sol[i,6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 12]
        y4 = sol[i, 14]
        x5 = sol[i, 16]
        y5 = sol[i, 18]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        x2= sol[:i, 4]
        y2= sol[:i,6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
        x5 = sol[:i, 16]
        y5 = sol[:i, 18]
    return ((x, y), (x2,y2),(x3,y3),(x4,y4),(x5,y5))

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='g')
ball_line, = plt.plot([], [], '-', color='g')
ball2, = plt.plot([], [], 'o', color='g')
ball_line2, = plt.plot([], [], '-', color='g')
ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')
ball4, = plt.plot([], [], 'o', color='r')
ball_line4, = plt.plot([], [], '-', color='r')
ball5, = plt.plot([], [], 'o', color='r')
ball_line5, = plt.plot([], [], '-', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])
    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])
    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])
    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])
    ball5.set_data(solve_func(i, 'point')[4])
    ball_line5.set_data(solve_func(i, 'line')[4])

plt.plot([0], [0], 'o', color='b', ms=20)

ani = FuncAnimation(fig,animate,frames=frames,interval=30)
plt.axis('equal')
edge = 50*2
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab12_2.gif')

