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

# max = int(input('Введите число: '))
# for i in range(4):
#     a = int(input('Введите число: '))
#     if a > max:
#         max = a

# print(f'Максимальное число = {max}')

#######

# a = list(map(int,input().split()))

# maximum = max(a)

# print(f'Максимальное число = {maximum}')

########

print(max(list(map(int,input().split()))))