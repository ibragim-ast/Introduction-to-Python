# Дан список. Выведите те его элементы, которые встречаются
# в списке только один раз. Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.
# [1,2,3,4,4,5,5,6] -> [1,2,3,6]

list = [1, 2, 3, 4, 4, 5, 5, 6]
list1 = []
for i in range(len(list)):
    a = list[i]
    count = 0
    for j in range(len(list)):
        if list[i] == list[j]:
            count +=1
    if count == 1:
        list1.append(list[i])
print(list1)