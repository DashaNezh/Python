"""
Разыгрывание случайной величины
Исследование Random-функции, создать большой массив псевдослучайных чисел, узнать сколько ра
повторяются первые 5 чисел в таком же порядке (псевдопериод), посчитать мат.ожидание, дисперсию.
Сформировать Случайную величину с наперед заданными значениями и их вероятностями (задание дискретной СВ)
"""

import random
import numpy as np


def main():
    # Генерация большого массива псевдослучайных чисел
    random.seed(42)  # Установка seed для воспроизводимости результатов
    n = 1000000  # Количество сгенерированных чисел
    random_numbers = [random.random() for _ in range(n)]

    # Поиск повторяющихся последовательностей из первых пяти чисел
    sequence_to_find = random_numbers[:5]
    count = 0
    for i in range(len(random_numbers) - 5):
        if random_numbers[i:i+5] == sequence_to_find:
            count += 1

    print("Количество повторений первых пяти чисел:", count)

    # Вычисление математического ожидания и дисперсии
    mean = np.mean(random_numbers)
    variance = np.var(random_numbers)

    print("Математическое ожидание:", mean)
    print("Дисперсия:", variance)

    # Создание дискретной случайной величины с заданными значениями и вероятностями
    values = [1, 2, 3, 4, 5]
    probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]

    # Генерация случайной величины с использованием заданных значений и вероятностей
    discrete_random_variable = np.random.choice(values, p=probabilities)

    print("Случайная величина с заданными значениями и вероятностями:", discrete_random_variable)

    # Вычисление вероятностей для каждого значения дискретной случайной величины
    num_samples = 10000  # Количество сгенерированных значений для оценки вероятностей
    samples = np.random.choice(values, size=num_samples, p=probabilities)
    unique, counts = np.unique(samples, return_counts=True)
    probability_dict = dict(zip(unique, counts / num_samples))

    print("Вероятности для каждого значения дискретной случайной величины:")
    for value, probability in probability_dict.items():
        print(f"Значение: {value}, Вероятность: {probability}")


if __name__ == "__main__":
    main()