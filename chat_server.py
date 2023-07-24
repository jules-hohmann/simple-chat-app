import socket
##import datetime
import requirements.txt

HOST=socket.gethostbyname(socket.gethostname())


PORT=8050


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