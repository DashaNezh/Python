import random
while True:
    player = int(input("1 - камень, 2 - ножницы, 3 - бумага\n"))
    if player == 1 or player == 2 or player == 3:
        break
    else:
        print("Вы должны ввести только цифры 1, 2, 3")

if player == 1:
    print("Вы выбрали камень!")
elif player == 2:
    print("Вы выбрали ножницы!")
else:
    print("Вы выбрали бумагу")

comp = random.randint(1, 3)

if comp == 1:
    print("Компьютер выбрал камень!")
elif comp == 2:
    print("Компьютер выбрал ножницы!")
else:
    print("Компьютер выбрал бумагу!")

if player == comp:
    print(f"Ничья! Вы оба выбрали {comp}")
elif player == 1:
    if comp == 2:
        print("Камень бьет ножницы! Вы победили!")
    else:
        print("Бумага обворачивает камень. Вы проиграли!")
elif player == 3:
    if comp == 1:
        print("Бумага оборачивает камень! Вы победили!")
    else:
        print("Ножницы режут бумагу! Вы проиграли.")
elif player == 2:
    if comp == 3:
        print("Ножницы режут бумагу! Вы победили!")
    else:
        print("Камень бьет ножницы! Вы проиграли.")


