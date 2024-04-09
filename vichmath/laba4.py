# численное интегрирование

from math import *
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x)  # интеграл от sin(x)


# метод левых прямоугольников
def left_Rectangle(a, b, n):
    sum = 0
    h = (b - a) / n
    x = a
    for i in range(n - 1):
        sum += h * f(x)
        x += h
    return sum


# метод правых прямоугольников
def right_Rectangle(a, b, n):
    sum = 0
    h = (b - a) / n
    x = b
    for i in range(n):
        sum += h * f(x)
        x -= h
    return sum


# метод средних прямоугольников
def middle_Rectangle(a, b, n):
    sum = 0
    h = (b - a) / n
    x = a
    for i in range(int(n)):
        sum += f(x + 0.5 * h)
        x += h
    return h * sum


# метод трапецией
def trapezoid_Method(a, b, n):
    sum = 0
    h = (b - a) / n
    x = a
    for i in range(n):
        if i == 0 or i == n:
            sum += 0.5 * f(x)
        else:
            sum += f(x)
        x += h
    return h * sum


def simpson_Method(a, b, n):
    h = (b - a) / (2 * n)
    sum = f(a) + f(b)
    for i in range(1, 2 * n):
        if i % 2 != 0:
            sum += 4 * f(a + i * h)
        else:
            sum += 2 * f(a + i * h)
    return sum * h / 3


def main():
    a = 0  # нижний предел интегрирования
    b = pi # верхний предел интегрирования
    n = 1000  # число разбиений
    print(f"Метод левых прямоугольников: {left_Rectangle(a, b, n)}")
    print(f"Метод правых прямоугольников: {right_Rectangle(a, b, n)}")
    print(f"Метод средних прямоугольников: {middle_Rectangle(a, b, n)}")
    print(f"Метод трапецией: {trapezoid_Method(a, b, n)}")
    print(f"Метод симпсона: {simpson_Method(a, b, n)}")


    # Построение графиков погрешности от шага интегрирования
    h = (2 * b - a)/n
    x_values = np.linspace(0, 2 * np.pi, 1000)
    y_values = np.sin(x_values)
    y_values_function = 1 - np.cos(x_values) # Значения от интеграла sin(x)
    t_values = np.linspace(a, 2 * b, 1000)
    difference_values = []
    difference_value = 0
    for t in t_values:
        difference_value += f(t) * h
        difference_values.append(difference_value)
    #Вычисляем накопленную площадь для каждого t
    #integral_values_sum = np.cumsum(f(t_values) * h)
    errors = difference_values - y_values_function

    plt.subplot(121)
    plt.plot(x_values, y_values, label='sin(x)', color='orange')
    plt.xlabel('x')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid()
    plt.title('График sin(x)')

    plt.subplot(122)
    plt.plot(t_values, errors, label='Накопленная площадь')
    plt.xlabel('x')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid()
    plt.title('Накопленная площадь от t')
    plt.show()


if __name__ == "__main__":
    main()