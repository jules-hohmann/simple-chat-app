import socket

HEADER=16
PORT=8006
SERVER="10.29.58.7"
ADDR=(SERVER,PORT)
FORMAT="UTF-8"
DISCONNECT_MESSAGE="--Leave"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    ##Ensuring that the message we send is of the right length
    send_length+=b" "*(HEADER- len(send_length))
    client.send(send_length)
    client.send(message)

conn=True

while conn==True:
    send(input())
    if input==DISCONNECT_MESSAGE:
        conn.close()
        conn=False