import socket
import datetime
import uuid
from client import Client
from server import Server
from message import Message
from threading import Thread
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8001
IP_ADDRESS = '0.0.0.0'

username = input("Username: ")
password = input("Password: ")
uuid = uuid.uuid4()
se = Server(IP_ADDRESS, PORT)
cl = Client(username, IP_ADDRESS, password, uuid)


s.connect((se.ip, se.port))

def receive():
    while True:
        message = input("Enter a message (First: username ip )> ")
        if message == "--Leave":
            s.close()
            os._exit(1)
        unformatted_message = Message(cl, message)
        print(unformatted_message.format_message().decode())
        s.send(message.encode("utf-8"))

thread = Thread(target = receive, args = ())
thread.start()
thread.join()

while True:
    msg = s.recv(2048)
    print(msg.decode())

