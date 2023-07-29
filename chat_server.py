from server import Server
from client import Client
import socket
import _thread

#serverIP = "10.29.61.108"
serverIP = "0.0.0.0"
serverPort = 8008
serverClients = {}

server = Server(serverIP, serverPort) 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reusability
serverSocket.bind((serverIP, serverPort))

def broadcastMessages(message, addr):
    print(message)
    for client in serverClients:
        if(addr[0] != client):
            connection = serverClients[client][0]
            connection.send(message.encode())

def acceptClientsAndMessages(conn, addr):
    while True:
        data = conn.recv(1024)
        msg = data.decode()
        if(msg[0:4] == "INFO"):
            userInformation = msg[6:].split(" ")
            serverClients[addr[0]].append(userInformation[0])
            serverClients[addr[0]].append(userInformation[1])
            print("Welcome " + serverClients[addr[0]][1] + "!")
        else:
            broadcastMessages(msg, addr)

while True:
    serverSocket.listen(5)
    conn, addr = serverSocket.accept()
    serverClients[addr[0]] = [conn]
    conn.send(("Welcome!").encode())
    _thread.start_new_thread(acceptClientsAndMessages, (conn, addr))
