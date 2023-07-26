import socket
import datetime
import uuid
from server import Server
from chatroom import Chatroom
from client import Client
from message import Message
from threading import Thread


server = Server("10.29.60.96", 8001)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server.ip_address, server.port))


CLIENTS = []
chatroom = Chatroom("Headspace", uuid.uuid1())

def broadcast_message(data, addr):
    for client in CLIENTS:
        if client.ip_address != addr[0]:
            print(f"{client.username} received message.")
            mess = Message(CLIENTS[client][1], data)
            CLIENTS[client][0].send(mess.create_message())
            chatroom.send(mess)

def server(conn, addr):
    while True:
        data = (conn.recv(1024).decode().strip()).split()
        client = Client(data[0], addr[0], data[1], data[2])
        CLIENTS[addr[0]].append(client)
        chatroom.add_client(client)
        message = f"{client.username} joined the chat"
        broadcast_message(message, addr)
        if data == "EXIT":
            chatroom.delete_client(client)
            CLIENTS[client][0].close()
            
            try:
                CLIENTS.pop(client)
            except KeyError:
                print("Client does not exist.")

            message = f"{client.username} just left."
            broadcast_message(message, addr)
        elif data:
            broadcast_message(data, addr)

while True:
    s.listen(6)
    conn, addr = s.accept()
    CLIENTS[addr[0]] = [conn]

    #could be an issue
    thread = Thread(target = server, args = (conn, addr))
    thread.start()
    thread.join()



