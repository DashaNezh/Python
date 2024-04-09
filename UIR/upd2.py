import socket
import sys

# Получаем IP-адрес и порт из параметров командной строки
ip_address = sys.argv[1]
port = int(sys.argv[2])

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к заданному порту
server_socket.bind((ip_address, port))

while True:
    # Получаем данные
    data, addr = server_socket.recvfrom(1024)

    # Выводим данные на стандартный поток вывода
    print("Получено от {}: {}".format(addr, data.decode()))
