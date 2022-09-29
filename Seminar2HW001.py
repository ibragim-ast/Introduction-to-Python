
print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр')
# - 6782 -> 23
# - 0,56 -> 11

a = input('Введите вещественное число: ')
a = list(a)

answer = 0
for i in a:
    if '.' in a:
        a.remove('.')
    elif i == 0:
        a.remove(i)
for i in a:
    answer = answer + int(i)

print(f'Cумма цифр в числе: {answer}')


