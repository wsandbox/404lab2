import socket, requests

header = b"GET / HTTP/1.1\r\n\r\n"

ip = socket.gethostbyname('www.google.com')
address = ('www.google.com', 80)
#address = (ip, 80)
sock = socket.create_connection(address)
# request a page

msg = sock.sendall(header)
if not msg:
    print("Request sent successfully")
    print(sock.recv(1024))
