import socket, requests

HOST = 'www.google.com'
PORT = 80

sock2 = socket.create_connection((HOST, PORT))
print(sock2)

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
 #   c, a = sock.create_connection((HOST, PORT))
  #  print(c)
    


