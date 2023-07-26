import socket
import datetime
import uuid
import _thread
from client import Client
from server import Server
from message import Message
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8005
IP_ADDRESS = '10.29.61.108'

username = input("Enter your username")
password = input("Enter your password")
uuid = uuid.uuid1()

user = Client(username, IP_ADDRESS, password, uuid)
server = Server(IP_ADDRESS, PORT)

s.connect((server.ip_address, server.port))

def listen():
    while True:
        message = input()
        raw_message = Message(user, message)
        print(raw_message.create_message().decode())
        s.send(message.encode())

thread = Thread(target = listen, args = ())
thread.start()
thread.join()

while True:
    msg = s.recv(2048)
    print(msg.decode())

