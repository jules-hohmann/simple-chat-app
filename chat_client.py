import socket
import datetime

import server
import chat_server
import client
import message
import uuid
import chatroom
import sys


#Initialize the port and IP address of the server
#When it runs gethostname, it finds the IP of the computer it's running on
PORT = 8005
#SERVERIP = '10.29.61.108'
CLIENTS = []


#Jules IP: 10.29.48.1
#Jules IP: 10.29.61.108

def broadcast():
    pass


def init_connection():
    username = input("Username: ")
    password = input("Password: ")
    personal_ip = input("Personal IP: ")
    client_uuid = uuid.uuid4()

    cl = client.Client(username, personal_ip, password, uuid)
    se = server.Server(SERVERIP, PORT)

    address = (se.ip, se.port)
    #where server ip is HOST and PORT is PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(address)
            print("yay")
        except:
            print("bad")
        print(address)
        chat_uuid = uuid.uuid3() #will contain network address
        #conn, addr = s.accept()
        while True:
            message_input = s.recv(1024).decode("utf-8")
            print(message_input)
            print("Enter Message: ")
            message = input()

            if message == "LEAVE":
                s.close()
                sys.exit(cl.username)
                return
            else:
                s.send("<" + cl.username + " " + cl.uuid + " >",{message.encode("utf-8")})

                

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


if __name__ == '__main__':
    SERVERIP = input("Enter HOST/Server IP Adress: ")
    init_connection()

            

            

        
        

