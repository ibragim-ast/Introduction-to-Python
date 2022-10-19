# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности

data = list(map(int, input().split()))
list = list(filter(lambda i: data.count(i)==1, data))
print(list)