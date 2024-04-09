import random

from enum import IntEnum


class Action(IntEnum):
    stone = 1
    scissors = 2
    paper = 3


def get_user_selection():
    player = int(input("Сделайте выбор - (камень[1], ножницы[2], бумага[3])\n"))
    computer_action = random.randint(1,3)
    action = Action(player)
    if player == 1:
        print("Вы выбрали камень!")
    elif player == 2:
        print("Вы выбрали ножницы!")
    else:
        print("Вы выбрали бумагу")

    if computer_action == 1:
        print("Компьютер выбрал камень!")
    elif computer_action == 2:
        print("Компьютер выбрал ножницы!")
    else:
        print("Компьютер выбрал бумагу!")

    if player == computer_action:
        print(f"Оба пользователя выбрали {action}. Ничья!")
    elif player == Action.stone:
        if computer_action == Action.scissors:
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif player == Action.paper:
        if computer_action == Action.stone:
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif player == Action.scissors:
        if computer_action == Action.paper:
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
while True:
    try:
        get_user_selection()
    except ValueError as e:
        range_str = f"[1, 3]"
        print(f"Некорректный ввод. Введите значение из промежутка {range_str}")
        continue
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break