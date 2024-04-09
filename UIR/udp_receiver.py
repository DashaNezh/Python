import socket
import sys

def start_receiver(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver_socket:
        receiver_socket.bind(('0.0.0.0', port))
        #Связывает сокет с адресом ('0.0.0.0', порт), где '0.0.0.0' означает, что сокет будет слушать все сетевые интерфейсы на данном устройстве.
        # #Затем используется указанный порт для прослушивания входящих сообщений.


        print(f"Прослушивание порта {port}")

        while True:
            data, addr = receiver_socket.recvfrom(1024)
            print(f"Получено от {addr}: {data.decode()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python udp_receiver.py <порт>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_receiver(port)
