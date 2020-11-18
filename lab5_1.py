from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs

a, q, p, A = symbols("a q p A")

ch = (exp(a) + exp(-a))/2
sh = (exp(a)-exp(-a))/2

x = (A*sh.subs(a, p))/(ch.subs(a, p)-cos(q))

y = (A*sin(p))/((ch.subs(a, p))-(cos(q)))

p1 = int(input("p= "))
a1 = int(input("a= "))
q1 = int(input("q= "))
A1 = int(input("A= "))

x = x.subs(p, p1)
x = x.subs(q, q1)
x = x.subs(A, A1)
x = x.subs(a, a1)

print(x)