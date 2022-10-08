print('Даны два файла, в каждом из которых находится запись многочлена')
print('Задача - сформировать файл, содержащий сумму многочленов') 
# 2*x² + 4*x + 5
# 3*x² + 10*x + 6 
# Вывод: 5*x² + 14*x + 11
import sympy

x = sympy.Symbol('x')

with open('Seminar4Data001.txt', 'r') as data1:
    a = data1.read()
print(a)
with open('Seminar4Data002.txt', 'r') as data2:
    b = data2.read()  
print(b)

c = sympy.simplify(a+'+'+b)
with open("Seminar4Data003.txt", 'w') as f:
    f.write(str(c))
print(c)