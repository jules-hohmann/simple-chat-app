import socket
import datetime
import uuid
from server import Server
from chatroom import Chatroom
from client import Client
from message import Message
from threading import Thread


server = Server('0.0.0.0', 8001)



if __name__ == "__main__":

    print(HOST)
    print(PORT)
    HOST=(input("GIVE ME YOUR IP!\n"))
    HOST="169.254.24.19"
    PORT=int(input("GIVE ME YOUR PORT!\n"))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        '''sets new variable s as the socket'''
        s.bind((HOST, PORT))
        s.listen(5)
        '''sets number of people who can connect and the Host ip and Port'''
        while True:
            '''creates loop that runs the server'''
            conn, addr= s.accept()
            with conn:
                
                data = conn.recv(1024, socket.MSG_DONTWAIT)
                data = data.decode("UTF-8")

                if data == None:
                    break
                else:
                    print(data.strip())
