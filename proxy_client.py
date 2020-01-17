import socket

HOST = 'localhost'
PORT = 8001
header = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(header.encode())
    sock.shutdown(socket.SHUT_WR)
    message = b""
    data = sock.recv(4096)
    while data:
        message += data
        data = sock.recv(4096)
    print(message.decode('ISO-8859-1'))

    
