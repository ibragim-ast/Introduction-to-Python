print('4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры')

n = int(input('Введите число: '))
pos1 = int(input('Введите индекс первого множителя: '))
pos2 = int(input('Введите индекс второго множителя: '))
lst = []

for i in range(-n, n + 1):
    lst.append(i)
  
if pos1 == n or pos2 == n or n == 0:
    print('Error! Один из множителей равен нулю! Попробуйте снова!')
else:
    print(lst)
    print(f'Произведение элементов на указанных позициях: {lst[pos1] * lst[pos2]}')



