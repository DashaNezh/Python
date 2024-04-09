def generate_custom_matrix(rows, cols):
    custom_matrix = [[0] * cols for _ in range(rows)]
    count = 1
    for i in range(cols - 1, -1, -1):
        if i % 2 == 0:
            for j in range(rows - 1, -1, -1):
                custom_matrix[j][i] = count
                count += 1
        else:
            for j in range(rows):
                custom_matrix[j][i] = count
                count += 1
    return custom_matrix

1
def create_mirror_bottom_left(original_matrix):
    mirror_bottom_left_array = original_matrix[::-1]
    return mirror_bottom_left_array


def create_mirror_bottom_right(mirror_bottom_left_array):
    mirror_bottom_right_array = [row[::-1] for row in mirror_bottom_left_array]
    return mirror_bottom_right_array


def create_mirror_upper_right(mirror_bottom_right_array):
    mirror_upper_right_array = mirror_bottom_right_array[::-1]
    return mirror_upper_right_array


def build_and_display_matrix(rows, cols):
    # Генерация матриц
    custom_matrix = generate_custom_matrix(rows, cols)
    mirror_bottom_left = create_mirror_bottom_left(custom_matrix)
    mirror_bottom_right = create_mirror_bottom_right(mirror_bottom_left)
    mirror_upper_right = create_mirror_upper_right(mirror_bottom_right)

    # Создание большой матрицы
    top_half = [custom_matrix[i] + mirror_upper_right[i] for i in range(rows)]
    bottom_half = [mirror_bottom_left[i] + mirror_bottom_right[i] for i in range(rows)]
    big_matrix = top_half + bottom_half

    # Вывод большой матрицы
    print("Большая матрица:")
    for row in big_matrix:
        print(' '.join(map(str, row)))

def main():
    rows = int(input("Введите количество строк матрицы:\n"))
    while rows < 1:
        print("Вы допустили ошибку, повторите ввод")
        rows = int(input())

    cols = int(input("Введите количество столбцов матрицы:\n"))
    while cols < 1:
        print("Вы допустили ошибку, повторите ввод")
        cols = int(input())

    build_and_display_matrix(rows, cols)


if __name__ == "__main__":
    main()