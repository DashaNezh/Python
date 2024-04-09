def proverka(ch):
    if -100 <= ch <= 100:
        return True
    else:
        print("Числа должны лежать в диапазоне [-100; 100]")


a = float(input("Введите координату точки A: "))
b = float(input("Введите координату точки B: "))
c = float(input("Введите координату точки C: "))
if proverka(a) and proverka(b) and proverka(c):
    ac = abs(c - a)
    bc = abs(b - c)
    result = ac * bc
    print("Произведение длин отрезков AC и BC:", result)
else:
    print("Ошибка!")

