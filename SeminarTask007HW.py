print('Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным')
num = int(input('Введите число от 1 до 7'))
if num > 5 and num < 8:
    print('Выходной!')
if num < 6 and num > 0:
    print('Солнце еще высоко!')
if num < 1 or num > 7:
    print('Некорректный ввод! Введите число от 1 до 7 (включительно)')