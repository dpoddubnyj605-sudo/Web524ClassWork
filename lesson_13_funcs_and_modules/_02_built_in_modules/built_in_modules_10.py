from math import ceil, floor, trunc, factorial, hypot

x = 3.4
y = 5.6

print('Верхнее округление', ceil(x), ceil(y))
print('Верхнее округление', ceil(-x), ceil(-y))
print('Нижнее округление', floor(x), floor(y))
print('Нижнее округление', floor(-x), floor(-y))

print('Усечение до целого числа', trunc(x), trunc(y))
print('Усечение до целого числа', trunc(-x), trunc(-y))

print("Факториал", factorial(5))
print('Гипотенуза', hypot(3, 4))
