print('Задача 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве')
import math
Xa = float(input('Введите координаты Xa: '))
Ya = float(input('Введите координаты Ya: '))
Xb = float(input('Введите координаты Xb: '))
Yb = float(input('Введите координаты Yb: '))

print(float(math.sqrt(math.pow((Xb - Xa), 2) + math.pow((Yb - Ya), 2))))




