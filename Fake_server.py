import socket
import threading



SERVER=socket.gethostbyname(socket.getfqdn(socket.gethostname()))
PORT = 8005


server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))


DISCONNECT_MESSAGE="--Leave"

def handle_client(conn,addr):
    i=0
    print(f"[NEW CONNECTION]{addr}")
    

    connected=True
    while connected:
        message=conn.recv(1024)
        while i <= 100:
            print(f"[{addr}][{i}] {message}")
            i+=1
    if message==DISCONNECT_MESSAGE:
        connected=False


def start():
    print(f"[LISTENING] Server is listening on: {SERVER}")
    server.listen(5)
    while True:
        conn, addr= server.accept()
        thread= threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")