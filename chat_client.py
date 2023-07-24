import socket
import datetime

import server
import client
import message
import chatroom



PORT = 8050
HOST = "0.0.0.0"

#IP: 10.29.48.1

messages = []

def init_connections(HOST, PORT, num_conns):
    address = (HOST, PORT)
    for i in range(1, len(num_conns) + 1):
        connid += 1
        print(f'Connecting ID {connid} to {address}')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect_ex(HOST, PORT)
        server.setblocking(False)
        while True:
            try:
                data = server.recv(1024)
                data.decode("UTF-8")
                messages.append(data)
                for i in range(len(messages)):
                    print(messages[i], "\n")
            except :
                print("Error")
                server.close()
            

            

        
        

