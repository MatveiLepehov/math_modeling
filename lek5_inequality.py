from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
from sympy import Eq,solve,solveset,linsolve,nonlinsolve
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import  Abs

x,y,z=symbols('x y z')
sol=reduce_abs_inequality(Abs(x-5)-3,'<',x)
print(sol)

sol=reduce_rational_inequalities([[y+2>0]],y)
print(sol)

sol=reduce_rational_inequalities([[y+2<=0]],y)
print(sol)

sol=reduce_rational_inequalities([[y+2<0]],y)
print(sol)