from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp

x,y,z=symbols('x y z')

simp_expr=simplify(sin(x)**2+cos(x)**2)
print(simp_expr)

simp_expr=simplify((x**3+x**2-x-1)/(x**2+2*x+1))
print(simp_expr)

simp_expr=expand((x+1)**2)
print(simp_expr)

simp_expr=expand((x+4)**3)
print(simp_expr)

simp_expr=expand((x+2)*(x-3))
print(simp_expr)

simp_expr=expand((x+1)*(x-2)-(x-1)*x)
print(simp_expr)

simp_expr=factor(x**3-x**2+x-1)
print(simp_expr)

simp_expr=expand((cos(x)+sin(x))**2)
print(simp_expr)
simp_expr=factor(simp_expr)
print(simp_expr)

simp_expr=trigsimp(sin(x)**4-2*cos(x)**2*sin(x)**2+cos(x)**4)
print(simp_expr)
