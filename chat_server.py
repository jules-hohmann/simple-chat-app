import socket
import datetime
import client


class Chat_server:
    # creates Chat_server class that retains a list of clients using the server (other variables and functions will be added)    
    def __init__(self, client, client_list: list = []):
        self.client_list = client_list

    def new_client(self, a=client.Client ):
        self.client_list.append(a)

HOST=socket.gethostbyname(socket.gethostname())
PORT = 8005

Dev_client=client.Client("Dev","169.254.34.231", "3476Davinci", 10205,)
Rome_client=client.Client("Rome","169.254.24.19", "RomePassword31415", 10001)
Arthur_client=client.Client("Arthur","169.254.36.171", "SubToMe123", 69696)
AJ_client=client.Client("AJ","169.254.18.213", "ILuvKorea", 54321)



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
                    break
                else:
                    print(data.strip())
