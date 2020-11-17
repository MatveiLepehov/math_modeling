from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
from sympy import Eq,solve,solveset,linsolve,nonlinsolve
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import  Abs
from sympy.vector import CoordSys3D
N=CoordSys3D('N')
a,b,c=symbols('a b c')
v=N.i-2*N.j
print(v/3)
print(v*4/3)
v1=2*N.i+3*N.j-N.k
v2=N.i-4*N.j-N.k
print(v1)
print(v2)
sol=v1.dot(v2)
v=*(a*b+a*c+b**2+b+b*c0)*N.i+N,j
v=(sin(a)**2)+cos(a)**2*N.i-(2*cos(b)**2-1)*N.k
sol=trigsimp(v)
print(slo)