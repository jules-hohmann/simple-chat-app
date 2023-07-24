import socket
import datetime
from "client.py" import Client

HOST="0.0.0.0"
PORT=8050

class Chat_server:
    client_list = []

    def new_client(Client a)





if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        while True:
            conn, addr= s.accept()
            with conn:
                
                data = conn.recv(1024, socket.MSG_DONTWAIT)
                data = data.decode("UTF-8")

                if data == None:
                    s.close()
                else:
                    print(data.strip())