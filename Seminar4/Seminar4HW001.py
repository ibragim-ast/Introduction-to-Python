# Вычислить число Пи c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

p = 3.1415926535897932384626433832795028841971693993751058209749445923078164 
num = int(input('Введите количество знаков после запятой в числе Пи: '))

print(round(p, num))

