print('Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)')
quarter = int(input('Введите координату X: '))

if quarter < 1 or quarter > 4:
    print('ERROR! Неверное значение четверти')
if quarter == 1:
    print('x > 0:y > 0')
if quarter == 2: 
    print('x < 0:y > 0')
if quarter == 3:
    print('x < 0:y < 0')
if quarter == 4:
    print('x > 0:y < 0')