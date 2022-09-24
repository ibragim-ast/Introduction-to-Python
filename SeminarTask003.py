print('Задача 3. Напишите программу, которая на вход принимает 5 чисел и находит минимальное из них')

# c1 = int(input('Введите первое число: '))
# c2 = int(input('Введите второе число: '))
# c3 = int(input('Введите третье число: '))
# c4 = int(input('Введите четвертое число: '))
# c5 = int(input('Введите пятое число: '))

# max = c1
# if c2 > max:
#     max = c2
# if c3 > max:
#     max = c3
# if c4 > max:
#     max = c4
# if c5 > max:
#     max = c5

print(f'Максимальное число = {max}')

####

c1 = int(input('Введите число: '))
max = c1
for i in range(4):
    c1 = int(input('Введите число: '))
    if c1 > max:
        max = c1

print(f'Максимальное число = {max}')