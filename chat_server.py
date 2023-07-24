import socket
##import datetime
import requirements.txt
from "client.py" import Client

HOST=socket.gethostbyname(socket.gethostname())


PORT=8050

Dev_client
Rome_client
Arthur_client
Client Jules_client()


client_list=[]

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        while True:
            conn, addr= s.accept()
            with conn:

                data = conn.recv(1024, socket.MSG_DONTWAIT)
                data=data.decode("UTF-8")

                if data == None:
                    break
                else:
                    print(data.strip())



##Need function that takes in new client's info and adds them to the system

