def generate_custom_matrix(rows, cols):
    # Создаём матрицу размером rows х cols и заполняем её нулями.
    custom_matrix = [[0] * cols for _ in range(rows)]
    count = 1  # Начинаем счётчик для подсчёта значений матрицы.
    for i in range(cols - 1, -1, -1):  # Проходим столбцы от последнего к первому.
        if i % 2 == 0:  # Если номер столбца чётный (считая с 0), идём снизу вверх.
            for j in range(rows - 1, -1, -1):
                custom_matrix[j][i] = count
                count += 1
        else:  # Если номер столбца нечётный, идём сверху вниз.
            for j in range(rows):
                custom_matrix[j][i] = count
                count += 1
    return custom_matrix

def create_mirror_bottom_left(original_matrix):
    # Создаём отражение оригинальной матрицы по горизонтальной оси.
    mirror_bottom_left_array = original_matrix[::-1]
    # обозначает срез массива, который разворачивает порядок элементов по первой оси.
    # #Это означает, что новый массив будет иметь элементы,
    # #перевернутые вверх ногами, что позволяет отразить исходный массив вдоль нижнего и левого края.
    return mirror_bottom_left_array

def create_mirror_bottom_right(mirror_bottom_left_array):
    # Создаём отражение матрицы по вертикальной оси (зеркально относительно центральной вертикали).
    mirror_bottom_right_array = [row[::-1] for row in mirror_bottom_left_array]
    # обозначает срез массива, который разворачивает порядок элементов по первой оси.
    # #Это означает, что новый массив будет иметь элементы,
    # #перевернутые вверх ногами, что позволяет отразить исходный массив вдоль нижнего и левого края.
    return mirror_bottom_right_array

def create_mirror_upper_right(mirror_bottom_right_array):
    n = len(mirror_bottom_right_array)
    mirror_upper_right_array = []
    for i in range(n-1, -1, -1):
        mirror_upper_right_array.append(mirror_bottom_right_array[i])
    return mirror_upper_right_array


def build_and_display_matrix(rows, cols):
    # Генерация всех частей для формирования большой матрицы из отражений.
    # Получаем первоначальную и все отражённые матрицы.
    custom_matrix = generate_custom_matrix(rows, cols)
    mirror_bottom_left = create_mirror_bottom_left(custom_matrix)
    mirror_bottom_right = create_mirror_bottom_right(mirror_bottom_left)
    mirror_upper_right = create_mirror_upper_right(mirror_bottom_right)

    # Создаём верхнюю и нижнюю части большой матрицы путём соединения генерированных ранее матриц.
    top_half = [custom_matrix[i] + mirror_upper_right[i] for i in range(rows)]
    bottom_half = [mirror_bottom_left[i] + mirror_bottom_right[i] for i in range(rows)]
    big_matrix = top_half + bottom_half  # Объединяем верхнюю и нижнюю части в одну большую матрицу.

    # Выводим большую матрицу в консоль, отформатировав элементы матрицы для удобства чтения.
    print("Большая матрица:")
    for row in big_matrix:
        print(' '.join(map(str, row)))

def main():
    # Запрашиваем у пользователя количество строк и столбцов,
    # проверяем ввод на корректность и вызываем функцию для вывода матрицы.
    rows = int(input("Введите количество строк матрицы:\n"))
    while rows < 1:  # Проверяем, что количество строк больше 0.
        print("Вы допустили ошибку, повторите ввод")
        rows = int(input())

    cols = int(input("Введите количество столбцов матрицы:\n"))
    while cols < 1:  # Проверяем, что количество столбцов больше 0.
        print("Вы допустили ошибку, повторите ввод")
        cols = int(input())

    build_and_display_matrix(rows, cols)  # Построение и вывод большой матрицы.

# Входная точка скрипта, если имя модуля __name__ установлено в "__main__", то вызываем функцию main().
if __name__ == "__main__":
    main()
