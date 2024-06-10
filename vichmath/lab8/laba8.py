"""
Генерация псевдослучайных чисел, подсчет псевдопериода, расчет математического ожидания и дисперсии,
создание дискретной случайной величины.

Переменные:
- random_numbers: список, содержащий сгенерированные псевдослучайные числа
- pseudo_period_count: количество повторений первых пяти чисел в том же порядке (псевдопериод)
- mean: математическое ожидание псевдослучайных чисел
- variance: дисперсия псевдослучайных чисел
- values: значения дискретной случайной величины
- probabilities: вероятности соответствующих значений дискретной случайной величины
- random_value: случайное число от 0 до 1, используемое для создания дискретной случайной величины
- discrete_random_variable: значение дискретной случайной величины, сгенерированное на основе вероятностей
"""

from lab8.Random import CustomRandom


def main():
    # Генерация большого массива псевдослучайных чисел
    custom_random = CustomRandom()  # Используем генерируемое начальное зерно
    n = 100000  # Количество сгенерированных чисел
    random_numbers = [custom_random.my_random() for _ in range(n)]

    # Подсчет псевдопериода - сколько раз повторяются первые 5 чисел в таком же порядке
    first_five = random_numbers[:5]
    pseudo_period_count = 0
    for i in range(len(random_numbers) - 5):
        if random_numbers[i:i + 5] == first_five:
            pseudo_period_count += 1

    print("Псевдопериод:", pseudo_period_count)

    # Расчет математического ожидания и дисперсии
    mean = sum(random_numbers) / len(random_numbers)
    variance = sum([(x - mean) ** 2 for x in random_numbers]) / len(random_numbers)

    print("Математическое ожидание:", mean)
    print("Дисперсия:", variance)

    # Создание дискретной случайной величины с заданными значениями и вероятностями
    values = [1, 2, 3, 4, 5]
    probabilities = [0.05, 0.2, 0.3, 0.4, 0.05]

    random_value = custom_random.my_random() / 100  # Случайное число от 0 до 1
    discrete_random_variable = None
    cumulative_prob = 0
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if random_value <= cumulative_prob:
            discrete_random_variable = values[i]
            break

    print("Дискретная случайная величина с заданными значениями и вероятностями:", discrete_random_variable)


if __name__ == "__main__":
    main()
