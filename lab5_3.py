from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs
 
x,E=symbols('x E')

expr=(((x**2)+x+(1/x)+(1/x**2))-4)
solveset_expr=solveset(expr,x)
print(solveset_expr)

e=0.8
m=9
pat=E-e*sin(E)-m
solveset_expr=solveset(pat,E)
print(solveset_expr)
