def calculate(a, h):
    area_osnovania = pow(a, 2)

    perimetr_osnovania = 4 * a

    area_poverhnost = area_osnovania + (1/2) * perimetr_osnovania * h

    volume = (1 / 3) * area_osnovania * h

    return area_poverhnost, volume


storona = float(input('Введите сторону квадрата: '))
visota = float(input('Введите высоту пирамиды: '))

x, y = calculate(storona, visota)

print('Площадь поверхности пирамиды:', round(x, 4))
print('Объем пирамиды:', round(y, 4))
