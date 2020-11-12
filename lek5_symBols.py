import math
print(math.sqrt(3))

import sympy
print(sympy.sqrt(3))
print(2*sympy.sqrt(3))

from sympy import symbols
x,y=symbols('x y')
expt=x+2*y
print(expt)
print(expt+1)
print(expt+x)
print(expt*x)

from sympy import sin,cos,pi,exp
print (sin(x**2)-exp(-2*x)+cos(pi/x))