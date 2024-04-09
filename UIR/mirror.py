def mirror_array(arr):
    n = len(arr)
    mirrored_arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            mirrored_arr[n - i - 1][n - j - 1] = arr[i][j]

    print("Зеркально отображенный массив:")
    for row in mirrored_arr:
        print(' '.join(map(str, row)))


def snake_array(arr):
    n = len(arr)
    snake_arr = [[0 for _ in range(n)] for _ in range(n)]
    value = 1
    for i in range(n - 1, -1, -1):
        if (n - 1 - i) % 2 == 0:  # если четная строка, двигаемся вниз
            for j in range(n - 1, -1, -1):
                snake_arr[j][i] = value
                value += 1
        else:  # если нечетная строка, двигаемся вверх
            for j in range(n):
                snake_arr[j][i] = value
                value += 1

    print("\nМассив с заполнением змейкой:")
    for row in snake_arr:
        print(' '.join(map(str, row)))



array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print("Исходный массив:")
for row in array:
    print(' '.join(map(str, row)))

mirror_array(array)
snake_array(array)