# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

import math
import sympy
x = sympy.Symbol('x')
f = input()
print(sympy.solve(f,x)) 



# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
 
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
 
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")



# x1 = (-B-((B**2 - 4*A*C)**0.5))/(2*A)
# x2 = (-B+((B**2 - 4*A*C)**0.5))/(2*A)