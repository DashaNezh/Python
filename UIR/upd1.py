import socket
import sys

# Получаем IP-адрес и порт из параметров командной строки
ip_address = sys.argv[1]
port = int(sys.argv[2])

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Запрашиваем данные с клавиатуры
    data = input("Введите данные для отправки: ")

    # Отправляем данные на заданный адрес и порт
    client_socket.sendto(data.encode(), (ip_address, port))
