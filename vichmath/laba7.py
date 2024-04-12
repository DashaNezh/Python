"""
Реализовать 3 сортировки: пузырек, реккурентная, сортировка суммированием
"""


def bubble_sort(arr):
    """
    Пузырьковая сортировка массива.

    Аргументы:
    arr: Список, который требуется отсортировать.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge(arr, left, mid, right):
    """
    Вспомогательная функция для сортировки слиянием. Объединяет два подмассива arr[left...mid] и arr[mid+1...right].

    Аргументы:
    arr: Список, который требуется отсортировать.
    left: Индекс начала первого подмассива.
    mid: Индекс конца первого подмассива и начало второго.
    right: Индекс конца второго подмассива.
    """
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    # Заполняем временные массивы
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # Сливаем временные массивы обратно в основной массив
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Дозаполняем оставшиеся элементы, если они есть
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    """
    Рекурсивная сортировка слиянием.

    Аргументы:
    arr: Список, который требуется отсортировать.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Сливаем отсортированные массивы
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Дозаполняем оставшиеся элементы, если они есть
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def sum_sort(arr):
    """
    Сортировка суммированием.

    Аргументы:
    arr: Список, который требуется отсортировать.
    """
    current_size = 1
    while current_size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = min((left + current_size - 1), (len(arr) - 1))
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])
            merge(arr, left, mid, right)
            left = left + current_size * 2
        current_size = 2 * current_size


def main():
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    arr3 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr1)
    merge_sort(arr2)
    sum_sort(arr3)
    print("Пузырьковой сортировкой: ", arr1)
    print("Рекурсивной сортировкой: ", arr2)
    print("Сортировкой суммирования: ", arr3)


if __name__ == "__main__":
    main()
