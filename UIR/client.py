import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python client.py <server_ip> <port>")
        return

    server_ip = sys.argv[1]
    port = int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        while True:
            data = input("Enter data to send: ")
            s.sendall(data.encode())
            response = s.recv(1024)
            print("Received:", response.decode())

if __name__ == "__main__":
    main()
