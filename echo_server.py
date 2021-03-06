import socket, multiprocessing as m

HOST = '127.0.0.1'
PORT = 8001
# source: https://docs.python.org/3.7/library/socket.html

def echo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('localhost', PORT))
        sock.listen()
        connection, address = sock.accept()
# print local socket info         
#        print("Local socket info:", sock)
        with connection:
            while True:
                data = connection.recv(4096)
                if not data:
                    break
                connection.sendall(data)
# print statements to view data received as well as information about the connected client                
#                print("Received", data)
#                print('Connection:', connection, "type:", type(connection))
#                print('Address:', address, "type:", type(address))

if __name__ == '__main__':
    m.set_start_method('spawn')
    p = m.Process(target=echo)
    p.start()

