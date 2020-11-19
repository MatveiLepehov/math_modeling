from sympy import symbols
from sympy import sqrt
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
i,j,x,z,y=symbols('x y z i j')
q1=1
q2=-0.5
E1=((q1*x)/sqrt((x**2+y**2+z**2)**3))*i+((q1*y)/sqrt((x**2+y**2+z**2)**3))*j+((q1*z)/sqrt((x**2+y**2+z**2)**3))
print(E1)