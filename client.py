import socket, requests

ip = socket.gethostbyname('www.google.com')
address = ('www.google.com', 80)
sock = socket.create_connection(address)
#print(requests.get('www.google.com'))
#print(sock)
