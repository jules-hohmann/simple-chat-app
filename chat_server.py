import socket
import datetime
import client

HOST=socket.gethostbyname(socket.gethostname())
Port = 8005

Dev_client=client.Client("Dev","169.254.34.231", "3476Davinci", 10205,)
Rome_client=client.Client("Rome","169.254.24.19", "RomePassword31415", 10001)
Arthur_client=client.Client()
Jules_client=client.Client()
AJ_client=client.Client()


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