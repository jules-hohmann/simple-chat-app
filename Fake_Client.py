import socket
import _thread

HEADER=16
PORT=8008
SERVER="10.29.61.108"
ADDR=(SERVER,PORT)
FORMAT="UTF-8"
DISCONNECT_MESSAGE="--Leave"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.listen(7)

'''
conn, addr = client.accept()
'''
client.connect(ADDR)



def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    ##Ensuring that the message we send is of the right length
    send_length+=b" "*(HEADER- len(send_length))
    client.send(send_length)
    client.send(message)

def listen():
    while True:
        client.send(input())
        if input==DISCONNECT_MESSAGE:
            client.close()
            break

_thread.start_new_thread(listen, ())

while True:
    print(client.recv(1024).decode())



    


