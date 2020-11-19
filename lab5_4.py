from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
x=symbols('x')
gagen=reduce_abs_inequality((abs((x**2)+2*x-3))+(3*(x+1)),'<',x)
print(gagen)
gaben=reduce_abs_inequality((((x-1)*(x+2))/((x-3)*(x+4))),"<=",x)
print(gaben)