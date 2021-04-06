import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation	
seconds_in_year = 365 * 24 * 60 * 60	
frames= 1000
years = 1
t = np.linspace(0, years*seconds_in_year, frames)
def move_func(s,t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3)=s
    dxdt1=v_x1
    dv_xdt1=(+ k *q1*q2/m1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
             + k *q1*q3/m1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5)
    dydt1=v_y1
    dv_ydt1=(+ k *q1*q2/m1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
             + k *q1*q3/m1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5)
    
    dxdt2=v_x2
    dv_xdt2=(+ k *q2*q1/m2*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
             + k *q2*q3/m2*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5)
    dydt2=v_y2
    dv_ydt2=(+ k *q2*q1/m2*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
             + k *q2*q3/m2*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    dxdt3=v_x3
    dv_xdt3=(+ k *q3*q1/m3*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
             + k *q3*q2/m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5)
    dydt3=v_y3
    dv_ydt3=(+ k *q3*q1/m3*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
             + k *q3*q2/m3*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5)
    
    return (dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3,)
x10=149*10**9
v_x10=-10000
y10=0
v_y10=0
    
x20=-149*10**9
v_x20=10000
y20=0
v_y20=0
    
x30=0
v_x30=0
y30=149*10**9
v_y30=0
    
s0=(x10,v_x10,y10,v_y10,
    x20,v_x20,y20,v_y20,
    x30,v_x30,y30,v_y30)

m1=1
q1=2*10**5

m2=1
q2=2*10**5

m3=1
q3=-2*10**5

k=8.98755*10**9

def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        x2= sol[i,4]
        y2=sol[i,6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        x2= sol[:i, 4]
        y2= sol[:i,6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
    return ((x, y), (x2,y2),(x3,y3))

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')
ball2, = plt.plot([], [], 'o', color='g')
ball_line2, = plt.plot([], [], '-', color='g')
ball3, = plt.plot([], [], 'o', color='k')
ball_line3, = plt.plot([], [], '-', color='k')
def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])
    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])
    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

ani = FuncAnimation(fig,animate,frames=frames, interval=30)
plt.axis('equal')
edge = 2*x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab13_2.htm')