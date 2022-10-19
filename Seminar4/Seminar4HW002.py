print('Задача: Задайте натуральное число N. Напишите программу, которая составит список простых')
print('множителей числа N')

num = int(input('Введите число: '))
list = []
a = 2
while num > 1:
    if num % a == 0:
        list.append(a)
        num = num/a
    else:
        a += 1
print(f'Ответ: {list}')
