# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
test = open('Seminar4HWResult.txt','w')

k = int(input('Введите натуральную степень k: '))

list = [random.randint(0, 5) for i in range(k+1)]

n = ''

for i in range(k+1):
    if list[i] == 0:
        continue
    elif i < k:
        n += str(list[i]) + ' * x^' + str(k-i) + ' + ' 
    else:
        n += str(list[i]) + ' = 0'

print(n)

test.write(n)
test.close()
        




