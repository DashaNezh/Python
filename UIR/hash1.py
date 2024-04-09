book = dict()
dict = {}


def letterIndex(letter):
    letter = letter.lower()
    if ord(letter) - ord('a') != 0:
        return 2 * (ord(letter) - ord('a') + 1) - 1
    else:
        return 2


def hashFunction1(line):
    return 1


def hashFunction2(line):
    return len(line)


def hashFunction3(line):
    letter = line[0].lower()
    return ord(letter) - ord('a') + 1


def hashFunction4(inputValue, lenght):
    sumIndex = 0
    for i in inputValue:
        sumIndex += letterIndex(i)
    return sumIndex % lenght


num_entries = int(input("Введите количество записей: "))

for i in range(num_entries):
    key = input("Введите ключ для записи " + str(i + 1) + ": ")
    value = input("Введите значение для записи " + str(i + 1) + ": ")
    book[key] = value

print("Пример работы первой функции:\n")
for key, value in book.items():
        dict[hashFunction1(key)] = value
print(dict)
dict.clear()

print("Пример работы второй функции:\n")
for key, value in book.items():
        dict[hashFunction2(key)] = value
print(dict)
dict.clear()

print("Пример работы третьей функции:\n")
for key, value in book.items():
        dict[hashFunction3(key)] = value
print(dict)
dict.clear()

print("Пример работы четвертой функции:\n")
for key, value in book.items():
        dict[hashFunction4(key, num_entries)] = value
print(dict)
dict.clear()