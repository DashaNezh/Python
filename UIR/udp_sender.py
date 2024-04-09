import socket
import sys

def start_sender(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender_socket:
        sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #Устанавливает опцию сокета SO_BROADCAST, которая разрешает использование широковещательных сообщений.
        # #Это позволяет отправлять сообщения широковещательно на все узлы в локальной сети.

        while True:
            message = input("Введите сообщение (или 'exit' для завершения): ")
            if message.lower() == 'exit':
                break

            sender_socket.sendto(message.encode(), ('<broadcast>', port))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python udp_sender.py <порт>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_sender(port)
