import socket
import datetime
import uuid
from server import Server
from chatroom import Chatroom
from client import Client
from message import Message
from threading import Thread


server = Server('0.0.0.0', 8001)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server.ip, server.port))


CLIENTS = []
chatroom = Chatroom("Headspace", uuid.uuid1())

def broadcast(data, addr):
    for client in CLIENTS:
        if client.ip_address != addr[0]:
            print(f"{client.username} received message.")
            mess = Message(CLIENTS[client][1], data)
            CLIENTS[client][0].send(mess.format_message())
            chatroom.send(mess)

def server(conn, addr):
    while True:
        data = (conn.recv(1024).decode().strip()).split()
        print(data)
        client = Client(data[0], addr[0])
        #CLIENTS[addr[0]].append(client)
        CLIENTS.append(client)
        chatroom.new_client(client)

        message = f"{client.username} joined the chat"
        broadcast(message, addr)

        if data == "--Leave":
            chatroom.delete_client(client)
            CLIENTS[client][0].close()
            
            try:
                CLIENTS.pop(client)
            except:
                print("Client not found")

            message = f"{client.username} left the chat"
            broadcast(message, addr)
        elif data:
            broadcast(data, addr)


while True:
    s.listen(6)
    conn, addr = s.accept()
    #CLIENTS[addr[0]] = [conn]

    #could be an issue
    thread = Thread(target = server, args = (conn, addr))
    thread.start()
    thread.join()



 



