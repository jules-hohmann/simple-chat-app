import socket
import datetime

PORT = 8050
HOST = "0.0.0.0"

#IP: 10.29.48.1

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.connect_ex(HOST, PORT)

def init_connections(HOST, PORT, num_conns):
    pass

