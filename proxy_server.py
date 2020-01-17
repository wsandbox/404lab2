import socket, threading

HOST = 'www.google.com'
PORT = 80

HOST2 = 'localhost'
PORT2 = 8001

def handle(client):
    with client, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy:
        proxy.connect((HOST, PORT))
        data = client.recv(4096)
        proxy.sendall(data)
        proxy.shutdown(socket.SHUT_WR)

        resp = proxy.recv(4096)
        end_data = b""
        while resp:
            end_data += resp
            resp = proxy.recv(4096)

        client.sendall(end_data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((HOST2, PORT2))
    listener.listen()
    while True:
        c, a = listener.accept()
        #print(c, a)
        
        stream = threading.Thread(target=handle, args=(c,))
        stream.run()

if __name__=='__main__':
    main()


