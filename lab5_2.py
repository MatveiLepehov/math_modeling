from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
x,y,z,a=symbols('x y z a')
simp_expr=simplify((x*y**2-2*x*y*z+x*z**2+y**2-2*y*z+z**2)/(x**2-1))
print(simp_expr)
sim_expr=simplify((1+sin(a)/1-sin(a))**0.5)+((1-sin(a))/(1+sin(a))**0.5)
print(sim_expr)