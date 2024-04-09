import socket
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        return

    port = int(sys.argv[1])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                print("Received and sent:", data.decode())


if __name__ == "__main__":
    main()
