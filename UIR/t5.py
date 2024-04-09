from math import *


def calculate(a, r):
    length = sqrt(3) * a
    height = a * sqrt(3) / 2

    num_rows = int(height // (2 * r))
    balls_per_row = int(length // (2 * r))

    result = (num_rows * (num_rows + 1)) // 2 * balls_per_row

    return result

x = float(input("Введите сторону треугольника: "))
y = float(input("Введите радиус шара: "))

max_balls = calculate(x, y)
print("Наибольшее количество шаров:", max_balls)