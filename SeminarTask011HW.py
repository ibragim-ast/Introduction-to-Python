print('Задача 11. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')


x = int(input())
y = int(input())
z = int(input())


if (not(x and y and z)) == (not(x) or not(y) or not(z)):
    print('ok')
else:
    print('no')