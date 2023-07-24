import socket
import datetime

import server
import chat_server
import client
import message
import chatroom



PORT = 8050
HOST = "0.0.0.0"

#IP: 10.29.48.1

messages = []


def init_connections(num_conns):
    address = (HOST, PORT)
    connid = 0
    for i in range(1, len(num_conns) + 1):
        connid = connid + 1
        print(f'Connecting ID {connid} to {address}')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect_ex(address)
        server.setblocking(False)
        while True:
            try:
                data = server.recv(1024)
                data.decode("UTF-8")
                messages.append(data)
                for i in range(len(messages)):
                    print(messages[i], "\n")
            except KeyboardInterrupt:
                print("Error")
                server.close()

if __name__ == '__main__':
    messages = []
    connid = 0
    init_connections([1])
            

            

        
        

