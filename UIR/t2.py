from math import *


def f(start, end, step):
    a = 5
    b = 2
    x = start
    while x <= end:
        if x + a >= 0:
            result = sqrt(x + a) + (pow(x, 2) + b) / x
            print(f"f({round(x, 1)}) = {round(result, 4)}")
        else:
            print(f"Ошибка: квадратный корень из отрицательного числа при x = {round(x, 1)}")
        x += step


f(-5, -4, 0.1)
