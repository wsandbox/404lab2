import socket, requests

ip = socket.gethostbyname('www.google.com')
address = (ip, 80)
sock = socket.create_connection(address)
#print(sock)
