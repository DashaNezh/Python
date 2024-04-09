while True:
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))

    if 1 <= a <= 100 and 1 <= b <= 100:
        break
    else:
        print("Числа a и b должны быть в диапазоне [1;100]")

S = a * b
P = 2 * (a + b)

print("Площадь =", round(S, 2), ", периметр =", P)

