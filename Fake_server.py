import socket
import threading
import client


##SERVER=socket.gethostbyname(socket.getfqdn(socket.gethostname()))





SERVER="10.29.58.7"
PORT = 8006
HEADER=16
FORMAT="UTF-8"
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))
DISCONNECT_MESSAGE="--Leave"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    ##Ensuring that the message we send is of the right length
    send_length+=b" "*(HEADER- len(send_length))
    client.send(send_length)
    client.send(message)


def handle_client(conn,addr):


    i=0
    print(f"[NEW CONNECTION]{addr}")
    # client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # client.bind((conn))

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            message=conn.recv(msg_length).decode(FORMAT)
            message=message.strip()
            if message==DISCONNECT_MESSAGE:
                connected=False
            ##this gives message IDs up to 100 for each IP
            if i==0:
                conn.send(f"Welcome to Headspace!\n Your IP and port are:{addr}\n".encode(FORMAT))
                conn.send(f"Please make your first an second messages your IP and Port, respectively.".encode(FORMAT))
            if i <= 100:
                print(f"[{addr}][{i}] {message}")
                i+=1
                conn.send("Message Received".encode(FORMAT))
                conn.send(f"{message}".encode(FORMAT))
                

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
    