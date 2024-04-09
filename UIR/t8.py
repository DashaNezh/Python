def proverka(ch):
    if -100 <= ch <= 100:
        return True
    else:
        print("Числа должны лежать в диапазоне [-100; 100]")


X = float(input("Введите количество конфет в кг X: "))
A = float(input("Введите стоимость X кг конфет A: "))
Y = float(input("Введите количество конфет в кг Y: "))


if proverka(X) and proverka(A) and proverka(Y):
    cost_per_kg = A / X  # стоимость 1 кг конфет
    cost_of_Y = cost_per_kg * Y  # стоимость Y кг конфет
    print("Стоимость 1 кг конфет:", round(cost_per_kg, 4))
    print("Стоимость", Y, "кг конфет:", round(cost_of_Y, 4))
else:
    print("Ошибка!")