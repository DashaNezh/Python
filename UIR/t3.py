from math import *


def f(start, end, step):
    x = start
    while x <= end + step:
        result = sin(sqrt(x)) + cos(sqrt(x))
        print(f"f({round(x, 1)}) = {round(result, 4)}")
        x += step


f(1, 3, 0.1)
