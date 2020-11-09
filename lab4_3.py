import numpy as np
from lab3_phizick_constant import yskorenie_svobodnogo_padenia as g
def mult_func(m=1,h=1,v=1):
    E=(m*v**2)/2+m*g*h
    return(E)
tmp=mult_func(2,5,2)
print(tmp)