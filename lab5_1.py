from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
from sympy import Eq,solve,solveset,linsolve,nonlinsolve
from sympy import  Abs
A,a,q,r,p=symbols('A,e,a,q,r,p')
ch=(exp(a)-exp(-a))/2
sh=(exp**a-exp**-a)/2
x=(A*sh.subs(a,p))/(ch.subs(a,p)-cos(a,q))
y=(A*sin.subs(a,p))/(ch.subs(a,p)-cos.subs(a,q))

p1=int(input('p='))
a1=int(input('a='))
q1=int(input('q='))
r1=int(input('r='))
print(x)