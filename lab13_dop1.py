import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation	
t = np.arange(10**(-7),1.5*10**(-7),1*10**(-10))
def move_func(s,t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4)=s
    dxdt1=v_x1
    dv_xdt1=(-G*m2*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
             - G *m3*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5
             - G *m4*(x1-x4)/((x1-x4)**2+(y1-y4)**2)**1.5
             + k *q1*q2/m1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
             + k *q1*q3/m1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5
             + k *q1*q4/m1*(x1-x4)/((x1-x4)**2+(y1-y4)**2)**1.5)
    dydt1=v_y1
    dv_ydt1=(-G*m2*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
             - G *m3*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5
             - G *m4*(y1-y4)/((x1-x4)**2+(y1-y4)**2)**1.5
             + k *q1*q2/m1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
             + k *q1*q3/m1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5
             + k *q1*q4/m1*(y1-y4)/((x1-x4)**2+(y1-y4)**2)**1.5)
    
    dxdt2=v_x2
    dv_xdt2=(-G*m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
             - G *m3*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5
             - G *m4*(x2-x4)/((x2-x4)**2+(y2-y4)**2)**1.5
             + k *q2*q1/m2*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
             + k *q2*q3/m2*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5
             + k *q2*q4/m2*(x2-x4)/((x2-x4)**2+(y2-y4)**2)**1.5)
    dydt2=v_y2
    dv_ydt2=(-G*m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
             - G *m3*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5
             - G *m4*(y2-y4)/((x2-x4)**2+(y2-y4)**2)**1.5
             + k *q2*q1/m2*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
             + k *q2*q3/m2*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5
             + k *q2*q4/m2*(y2-y4)/((x2-x4)**2+(y2-y4)**2)**1.5)
    
    dxdt3=v_x3
    dv_xdt3=(-G*m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
             - G *m2*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5
             - G *m4*(x3-x4)/((x3-x4)**2+(y3-y4)**2)**1.5
             + k *q3*q1/m3*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
             + k *q3*q2/m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5
             + k *q3*q4/m3*(x3-x4)/((x3-x4)**2+(y3-y4)**2)**1.5)
    dydt3=v_y3
    dv_ydt3=(-G*m1*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
             - G *m2*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5
             - G *m4*(y4-y3)/((x4-x3)**2+(y4-y3)**2)**1.5
             + k *q4*q1/m3*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
             + k *q4*q2/m3*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5
             + k *q4*q3/m3*(y4-y3)/((x4-x3)**2+(y4-y3)**2)**1.5)
    
    dxdt4=v_x4
    dv_xdt4=(-G*m1*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5
             - G *m2*(x4-x2)/((x4-x2)**2+(y4-y2)**2)**1.5
             - G *m3*(x4-x3)/((x4-x3)**2+(y4-y3)**2)**1.5
             + k *q4*q1/m4*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5
             + k *q4*q2/m4*(x4-x2)/((x4-x2)**2+(y4-y2)**2)**1.5
             + k *q4*q3/m4*(x4-x3)/((x4-x3)**2+(y4-y3)**2)**1.5)
    dydt4=v_y4
    dv_ydt4=(-G*m1*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
             - G *m2*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5
             - G *m3*(y4-y3)/((x4-x3)**2+(y4-y3)**2)**1.5
             + k *q4*q1/m4*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
             + k *q4*q2/m4*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5
             + k *q4*q3/m4*(y4-y3)/((x4-x3)**2+(y4-y3)**2)**1.5)
    return (dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3,
            dxdt4,dv_xdt4,dydt4,dv_ydt4)
a=0.008

x10=a
v_x10=-1*10**6*np.cos(np.pi/4)
y10=a
v_y10=1*10**6*np.sin(np.pi/4)
    
x20=-a
v_x20=-1*10**6*np.sin(np.pi/4)
y20=a
v_y20=-1*10**6*np.cos(np.pi/4)
    
x30=-a
v_x30=1*10**6*np.cos(np.pi/4)
y30=-a
v_y30=-1*10**6*np.sin(np.pi/4)
    
x40=a
v_x40=1*10**6*np.sin(np.pi/4)
y40=-a
v_y40=1*10**6*np.cos(np.pi/4)

s0=(x10,v_x10,y10,v_y10,
    x20,v_x20,y20,v_y20,
    x30,v_x30,y30,v_y30,
    x40,v_x40,y40,v_y40)

m1=1.1*10**(-27)
q1=-1.1*10**(-13)

m2=1.1*10**(-27)
q2=1.1*10**(-13)

m3=1.1*10**(-27)
q3=-1.1*10**(-13)

m4=1.1*10**(-27)
q4=1.1*10**(-13)

G=6.67*10**(-11)
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
        x4 = sol[i, 12]
        y4 = sol[i, 14]
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

ani = FuncAnimation(fig,animate,frames=30, interval=10)
plt.show()