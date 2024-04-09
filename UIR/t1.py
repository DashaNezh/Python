from math import *
print("Input x:")
x = int(input())
print("Input y:")
y = int(input())
print("Input z:")
z = int(input())
a = (1 + y)*((x + y/(pow(x, 2) + 4))/(exp(2)+1/(pow(x, 2) + 4)))
print("Значение a = ", round(a, 4))
while True:
    if x == 0 and z == 0:
        print("Ошибка: деление на ноль в формуле b!")
        break
    else:
        b = (1 + pow(cos(y - x), 3)) / (pow(x, 2) / 2 + pow(sin(z), 2))
        print("Значение b = ", round(b, 4))


