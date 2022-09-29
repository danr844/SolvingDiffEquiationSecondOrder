from ast import Eq
import sympy
from IPython.display import display

#Authors
# Daniel Alejandro Angel Fuertes
# Jairo Adolfo Cespedes Plata
# Juanpablo Barriga Alvares
# Jessica 

# redefino las incognitas
t = sympy.Symbol('t')
y = sympy.Function('y')
# definiendo la ecuación
m=float(input("Ingrese la masa del objeto atada al resorte \n"))
yi=float(input("Ingrese el valor de la resistencia del medio\n"))
k=float(input("Ingrese el valor de la constante de Hooke\n"))
print(sympy.diff(y(t)).diff(y(t)))
eq = m * sympy.diff(y(t),t,2) + yi*sympy.diff(y(t)) + k * y(t)
print(eq)
# Condición inicial
a=float(input("Ingrese el valor de la función y(t) en la condición inicial t = 0\n"))
b=float(input("Ingrese el valor de la función y'(t) en la condición inicial t = 0\n"))


# Resolviendo la ecuación
edo_sol = sympy.dsolve(eq).rhs
display(sympy.Eq(y(t), edo_sol))
cnd0 = sympy.Eq(edo_sol.subs(t, 0), a)
# Initial conditions:
cnd0 = sympy.Eq(edo_sol.subs(t, 0), a)  # y(0) = a
cnd1 = sympy.Eq(edo_sol.diff(t).subs(t, 0), b)  # y'(0) = b
C1, C2 = sympy.symbols("C1, C2")  # generic constants
#  Solve for C1, C2:
C1C2_sl = sympy.solve([cnd0, cnd1], (C1, C2))

print("La solución general de la ED es: ",edo_sol, "\n")
# Substitute back into solution:
y_sl1 = sympy.simplify(edo_sol.subs(C1C2_sl))
print("Solution with initial conditions:")
display(sympy.Eq(y(t), y_sl1))
