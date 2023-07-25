import socket
import threading


##SERVER=socket.gethostbyname(socket.getfqdn(socket.gethostname()))

SERVER="10.29.58.7"
PORT = 8006
HEADER=16
FORMAT="UTF-8"
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))


DISCONNECT_MESSAGE="--Leave"

def handle_client(conn,addr):
    i=0
    print(f"[NEW CONNECTION]{addr}")
    

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            message=conn.recv(msg_length).decode(FORMAT)
            message=message.strip()
            if message==DISCONNECT_MESSAGE:
                connected=False
            if i <= 100:
                print(f"[{addr}][{i}] {message}")
                i+=1
    conn.close()


def start():
    print(f"[LISTENING] Server is listening on: {SERVER}")
    server.listen(5)
    while True:
        conn, addr= server.accept()
        thread= threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


if __name__=="__main__":
    start()
    