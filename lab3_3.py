import numpy as np
from lab3_phizick_constant import yskorenie_svobodnogo_padenia as g
t=np.arange(0,5.1,0.1)
x0=2
v0x=10
y0=2
x=x0+v0x*t
y=y0+v0x-((g*t**2)/2)
trag=np.ndarray(shape=(len(t),3))
for i in range(len(t)):
    trag[i,0]=t[i]
    trag[i,1]=x[i]
    trag[i,2]=y[i]
print(trag)