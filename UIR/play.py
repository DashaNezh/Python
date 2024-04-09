import random

from enum import IntEnum


class Action(IntEnum):
    stone = 1
    scissors = 2
    paper = 3


def get_user_selection():
    player = input("Сделайте выбор - (камень[1], ножницы[2], бумага[3])\n")
    selection = int(player)
    action = Action(selection)
    if selection == 1:
        print("Вы выбрали камень!")
    elif selection == 2:
        print("Вы выбрали ножницы!")
    else:
        print("Вы выбрали бумагу")
    return action


def get_computer_selection():
    selection = random.randint(1, 3)
    if selection == 1:
        print("Компьютер выбрал камень!")
    elif selection == 2:
        print("Компьютер выбрал ножницы!")
    else:
        print("Компьютер выбрал бумагу!")
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action.name}. Ничья!")
    elif user_action == Action.stone:
        if computer_action == Action.scissors:
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == Action.paper:
        if computer_action == Action.stone:
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == Action.scissors:
        if computer_action == Action.paper:
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")


while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[1, 3]"
        print(f"Некорректный ввод. Введите значение из промежутка {range_str}")
        continue
    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break
