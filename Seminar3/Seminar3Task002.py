# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

# list = ['ffff','3rfhg','4']
# a = input('Введите число: ')
# if list.count(a) > 0:
#     print('Yes')
# else:
#     print('')

list = ['ffff','3rfhg', '4']
flag = False
for i in list:
    if i.isdigit():
        flag = True
print(flag)