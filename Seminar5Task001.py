# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполялось условие A[i] - 1 = A[i-1]. Найдите это число
# Пример: 
# Ввод: 1 2 4 5 -> 3


with open('Seminar5Task001File.txt', 'r') as n:
    list = n.read()
print(list)
list = list.split()
for i in range(len(list)-1):
    if int(list[i]) + 1 != int(list[i+1]):
        print(int(list[i])+1)





