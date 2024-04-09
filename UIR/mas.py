import random

def mirror(array):
    mirrored = []
    for row in array:
        mirrored.append(row[::-1])
    return mirrored

def rotate_right(array):
    rotated = []
    n = len(array)
    for i in range(n):
        row = []
        for j in range(n-1, -1, -1):
            row.append(array[j][i])
        rotated.append(row)
    return rotated

n = int(input("Введите размерность массива: "))

array = [[0] * n for _ in range(n)]

num = 1
for i in range(n // 2 + 1):
    for j in range(i, n - i):
        array[i][j] = num
        array[j][i] = num
        array[n - i - 1][j] = num
        array[j][n - i - 1] = num
        num += 1

# Заполнение исходного массива случайными числами
for i in range(n):
    for j in range(n):
        array[i][j] = random.randint(1, 100)

print("Исходный массив:")
for row in array:
    print(row)

mirrored = mirror(array)

rotated = rotate_right(mirrored)
print("Готовый массив:")
for row in rotated:
    print(row)