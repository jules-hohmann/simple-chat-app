import socket
import datetime

PORT = 8050
HOST = "0.0.0.0"

#IP: 10.29.48.1


def init_connections(HOST, PORT, num_conns):
    address = (HOST, PORT)
    for i in range(1, len(num_conns) + 1):
        connid += 1
        print(f'Connecting ID {connid} to {address}')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setblocking(False)
        server.connect_ex(HOST, PORT)
        while True:
            data = server.recv(1024)
            server.sendall()
        

