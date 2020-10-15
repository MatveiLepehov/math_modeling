import numpy as np
from lab3_phizick_constant import yskorenie_svobodnogo_padenia as g
from lab3_phizick_constant import postoyanaia_bolsmana as k
from lab3_phizick_constant import chislo_elera as e
from lab3_phizick_constant import postoyanaia_planka as hp
h=100
a=np.pi/3
b=np.pi/6
t=200
o=300
v=np.sqrt((g*h*(np.tan(b))**2)/(2*(np.cos(a))**2*(1-np.tan(b)*np.tan(a))))
print(v)
n=2/np.sqrt(np.pi)*(hp/(k*t)**(1.5))*(e**((-o)/k*t)*(o**(t/2)))
print(n)