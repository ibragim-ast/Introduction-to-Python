print('Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов')
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
lst2 = []
lst3 = []
for i in range(len(lst)):
    if lst[i] % 1 != 0:
        lst2.append(lst[i])
    for i in range(len(lst2)):
        lst3.append = round(lst2[i] % 1, 2)

    # lst3 = [round(lst2[i] % 1, 2) for i in range(len(lst2))]
print(f'{lst3} => {max(lst3) - min(lst3)}')