import socket

HOST = '127.0.0.1'
PORT = 8001
# source: https://docs.python.org/3.7/library/socket.html

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    connection, address = sock.accept()
    with connection:
        print('Message from', address)
        while True:
            data = connection.recv(4096)
            if not data:
                break
            connection.sendall(data)
