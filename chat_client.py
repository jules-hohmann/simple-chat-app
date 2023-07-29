import socket
import datetime

import server
import chat_server
import client
import message
import uuid
import chatroom
import sys

import _thread


#Initialize the port and IP address of the server
#When it runs gethostname, it finds the IP of the computer it's running on
PORT = 8008
#SERVERIP = '10.29.61.108'
SERVERIP = '0.0.0.0'
CLIENTS = []

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




#Jules IP: 10.29.48.1
#Jules IP: 10.29.61.108
username = ''
password = ''

while len(username) == 0:
    username = input("Username: ")
while len(password) == 0:
    password = input("Password: ")
personal_ip = socket.gethostbyname(socket.gethostname())
client_uuid = uuid.uuid1()




cl = client.Client(username, personal_ip, password, uuid)
se = server.Server(SERVERIP, PORT)

address = (se.ip, se.port)
#where server ip is HOST and PORT is PORT

try:
    clientSocket.connect(address)
except:
    print("Connection Failed")


#will contain network address
#conn, addr = s.accept()
clientInfo = "INFO: " + cl.username + " " + cl.uuid
clientSocket.send(clientInfo.encode())

def listen():
    while True:
        message_input = clientSocket.recv(1024).decode("utf-8")
        print(message_input)

_thread.start_new_thread(listen(), ())

while True:
    message = input(cl.username + ": ")
    message = cl.username + ": " + message
    if message == "LEAVE":
        clientSocket.close()
        sys.exit(cl.username)
    else:
        clientSocket.send("<" + cl.username + " " + cl.uuid + " >",{message.encode("utf-8")}) 

'''
    Address variable stores IP and PORT, while connection
    ID is initialized to a value as it will be iterated depending on
    number of connections. The server is then initialized and the client 
    is connected using address. Setblocking is set to false prevent waiting.
    Append decoded messages from the chat to display them.
    

    address = (IP, PORT)
    connid = 0
    for i in range(1, len(num_conns) + 1):
        connid = connid + 1
        print(f'Connecting ID {connid} to {address}')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect_ex(address)
        server.setblocking(False)
        try:
            while True:
                try:
                    data = server.recv(1024)
                    data.decode("UTF-8")
                    messages.append(data)
                    for i in range(len(messages)):
                        print(messages[i], "\n")
                except:
                    #print(address)
                    pass
        except KeyboardInterrupt:
            print(f'Client with ID {connid} leaves the chat')
        '''


            

            

        
        

