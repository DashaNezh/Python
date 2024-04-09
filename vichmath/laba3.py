# численное дифференцирование функции тремя аналогами.


from math import *
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

x_0 = 2 * pi # точка,в которой вычисляется приближенное значение производной
n = 100
h = 1e-6 # точность
h_values = np.logspace(-14, -1, n)  # генерация логарифмической последовательности шагов от 1e-14 до 1e-1

#функция
def f(x):
    return sin(x)

# производная функции
def derivative(x):
    return cos(x)

# левая разность
def derivative_a(x, h):
    return (f(x + h) - f(x)) / h

# правая разность
def derivative_b(x, h):
    return (f(x) - f(x - h)) / h

# центральная разность
def derivative_c(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# аналог для второй производной
def second_derivative_h(x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

# вторая производная
def second_derivative(x):
    return (-sin(x))


# Вычисление точной производной в pi/2
exact_derivative = derivative(x_0)

# Создание массивов для хранения значений погрешностей
errors_a = []
errors_b = []
errors_c = []

# Вычисление погрешностей для каждого значения h
for h in h_values:
    approx_derivative_a = derivative_a(x_0, h)
    approx_derivative_b = derivative_b(x_0, h)
    approx_derivative_c = derivative_c(x_0, h)

    error_a = abs(approx_derivative_a - exact_derivative)
    error_b = abs(approx_derivative_b - exact_derivative)
    error_c = abs(approx_derivative_c - exact_derivative)

    errors_a.append(error_a)
    errors_b.append(error_b)
    errors_c.append(error_c)

# Создание таблицы с данными
table_data = list(zip(h_values, errors_a, errors_b, errors_c))
headers = ["Шаг (h)", "Погрешность (Левая разность)", "Погрешность (Правая разность)",
           "Погрешность (Центральная разность)"]

# Вывод таблицы с использованием библиотеки tabulate
print(tabulate(table_data, headers=headers, floatfmt=".10f", tablefmt="pretty"))

print(f"Левая разность для h = {h}: {derivative_a(x_0, h)}")
print(f"Правая разность для h = {h}: {derivative_b(x_0, h)}")
print(f"Центральная разность для h = {h}: {derivative_c(x_0, h)}")
print(f"Значение первой производной в точке x = {x_0}: {exact_derivative}")
print(f"Значение второй производной в точке x = {x_0}: {second_derivative(x_0)}")
print(f"Приближенное значение для h = {h}: {second_derivative_h(x_0, h)}")

# Построение графиков погрешностей
# plt.figure(figsize=(10, 6))
# plt.loglog(h_values, errors_a, label='Левая разность')
# plt.loglog(h_values, errors_b, label='Правая разность')
# plt.loglog(h_values, errors_c, label='Центральная разность')
# plt.xlabel('h')
# plt.ylabel('Погрешность')
# plt.title('Погрешность аппроксимации первой производной')
# plt.legend()
# plt.grid(True)
# plt.show()
# x_values = np.linspace(0, 2 * np.pi, 500)
# y_values = np.cos(x_values)
# plt.figure(figsize=(10, 6))
# plt.plot(x_values, y_values, label='Ошибка')
# plt.xlabel('x')
# plt.ylabel('Ошибка')
# plt.title('Производная f(x) = sin(x)')
# plt.legend()
# plt.grid(True)
# plt.show()


x_values = np.linspace(0, 2 * np.pi, 500)
y_values = np.cos(x_values)
h = 1e-6
mas_y_values = []
for x in x_values:
    a = (f(x + h) - f(x))/h
    mas_y_values.append(a)
error_values = y_values - mas_y_values

plt.figure(figsize=(10, 6))
plt.plot(x_values, error_values, label='Ошибка')
plt.xlabel('x')
plt.ylabel('Ошибка')
plt.title('Приближенная производная f(x) = sin(x)')
plt.legend()
plt.grid(True)
plt.show()

