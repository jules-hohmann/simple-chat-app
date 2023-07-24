import socket
import datetime
import client


class Chat_server:
    def __init__(self, client, client_list: list = []):
        self.client_list = client_list

    def new_client(self, a=client.Client ):
        self.client_list.append(a)

HOST=socket.gethostbyname(socket.getfqdn(socket.gethostname()))

PORT = 8005
print(HOST)
print(PORT)

Dev_client=client.Client("Dev","169.254.34.231", "3476Davinci", 10205,)
Rome_client=client.Client("Rome","169.254.24.19", "RomePassword31415", 10001)
Arthur_client=client.Client("Arthur","169.254.36.171", "SubToMe123", 69696)
AJ_client=client.Client("AJ","169.254.18.213", "ILuvKorea", 54321)



if __name__ == "__main__":

    print(HOST)
    print(PORT)
    HOST=(input("GIVE ME YOUR IP!\n"))
    HOST="10.29.58.7"
    PORT=int(input("GIVE ME YOUR PORT!\n"))
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #Binds this socket to our set host and port to create a socket that listens there
        s.bind((HOST,PORT))
    #s.listen turns our socket on and listens for inputs, the number inside is the number of connections it can listen for
        s.listen(5)

    #If someone tries to make a connection and they have an address then it accepts it into the socket
        while True:
            conn, addr= s.accept()
            conn.send(1024)
            with conn:
                print("Address: ", addr)
                data = conn.recv(1024)
                data=data.decode("UTF-8")
                if data == None:
                    break
                else:
                    print(data.strip())
                    new_data=data[2:-1]
                    print(str(new_data))
                    if (data.strip()) =="Bro":
                        print("300000")
                    # if (data.strip())=="ChaCha":
                    #     Rome_dance(mav_connection)
                    # if (data.strip())=="Straight":
                    #     run_motors_timed(mav_connection, 5, Straight)
                    # if (data.strip())=="Help" or "help" or "h":
                    #     conn.send()
                socket.close()

