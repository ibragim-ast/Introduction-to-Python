# Цифровой корень - это рекурсивная сумма всех цифр числа
# Учитывая n, возьмите сумму цифр n.
# Если это значение имеет более одной цифры,
# продолжайте уменьшать таким образом, пока не будет получено однозначное число.
# Ввод будет неотрицательным целым числом.
# 16 => 7
# 942 => 6
# 132189 => 6
# 493193 => 2


a = int(input('Введите число: '))


def summ(a):
    if a < 10:
        return (a)
    else:
        return summ(sum(map(int, list(str(a)))))


print(f'Цифровой корень числа {a} = {summ(a)}')
