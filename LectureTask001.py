# print('Hello world')

# value = None # None ипользуется для создания пустой переменной
# value = 12345
# print(type(value)) #type выводит тип переменной

# w = 'hello \nworld' #/n - перевод на новую строку
# print(s)
# print(w)

# a = 123
# b = 1.23
# s = "'hello world'"  # для обрамления текста подходят как одинарые, так и двойные кавычки
# print(a, '-', b, '-', s) # в выводе можно использовать строки
# print('{} - {} - {}'.format(a, b, s)) # форматирование вывода
# print(f'{a} - {b} - {s}') # третий вариант вывода
# print('{1} - {2} - {0}'.format(a, b, s)) # можно задавать порядок вывода, задавая индексы переменных

# f = True
# print(f)

# list = [1, 2, 3, 'hello']  # создание списка
# print(list)

# print() ## отвечает за вывод данных
# input() ## отвечает за ввод данных

# print('Введите А')
# a = int(input()) #если нужно вещественное число, используем float вместо int, по умолчанию идут строки
# print('Введите B')
# b = int(input())
# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# ==--- арифметические операции ---==
# a = 1.3
# b = 3
# c = a + b
# c = a - b
# c = round(a * b, 3) # round - округляет число, 3 - количество знаков в округлении
# c = a / b  # по умолчанию деление происходит как для вещественных чисел
# c = a // b  # деление в целых числах
# c = a % b # остаток от деления
# с = a ** b # возведение а в степень b

# ==--- логические операции ---==
# >, >=, <, <=, ==, !=
# not, and, or
# print(1 > 3)
# print(1 < 3)
# print(1 < 4 and 5 > 2)
# print(1 == 2)
# print(1 != 2)
# print(1 < 3 < 5)

# print(1 > 2 or 4 < 6)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)  # покажет есть 2 в списке f
# print(not 2 in f)  # отрицание того, что 2 есть в списке

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(f'максимальное число {a}')
# else:
#     print(f'максимальное число {b}')

# username = input('Введите имя ')
# if username == 'Aisha':
#     print('Super Aisha')
# elif username == 'Safiya':
#     print('Good girl, Safiya')
# elif username == 'Khadija':
#     print('My girl, Khadija')
# else:
#     print('Welcome, ', username)

# ==--- WHILE ---==
# original = int(input('Введите число - '))
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(f'ответ = {inverted}')

# ==--- WHILE & ELSE ---==
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# ==--- FOR ---==
# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# for i in range(1, 10 , 2): # 1 - стартовая позиция, 10 - конечная позиция, 2 - шаг
#     print(i)

# ==--- НЕМНОГО О СТРОКАХ ---==
# text = 'съешь еще этих мягких французских булок'
# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще','ЕЩЕ'))

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])   # c
# print(text[1])   # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])   # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...