import socket
import datetime

import client
import chat_server
#import client
import message
import chatroom


#Initialize the port and IP address of the client
#When it runs gethostname, it finds the IP of the computer it's running on


#Jules IP: 10.29.48.1
#10.29.61.108


def init_connection():

    PORT=int(input("GIVE ME YOUR PORT!\n"))
    HOST= str(input("GIVE ME YOUR IP\n"))

    address = (HOST, (PORT))
    print(f'Connecting ID {"Jules"} to {address}')


    '''
    Address variable stores IP and PORT, while connection
    ID is initialized to a value as it will be iterated depending on
    number of connections. The server is then initialized and the client 
    is connected using address. Setblocking is set to false prevent waiting.
    Append decoded messages from the chat to display them.
    '''

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

if __name__ == '__main__':
    messages = []
    connid = 0
    IP=input("Give me your IP")
    PORT=input("Give me your port")
    init_connections([1])
            

            

        
        

