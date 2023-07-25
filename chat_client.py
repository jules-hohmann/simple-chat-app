import socket
import datetime

import server
import chat_server
import client
import message
import chatroom


#Initialize the port and IP address of the server
#When it runs gethostname, it finds the IP of the computer it's running on


#Jules IP: 10.29.48.1
#10.29.61.108


def init_connection():

    PORT=int(input("GIVE ME YOUR PORT!\n"))
    HOST= str(input("GIVE ME YOUR IP\n"))

    address = (HOST, (PORT))
    print(f'Connecting ID {"Jules"} to {address}')


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
    
        with conn:
            while True:
                data = conn.recv(1024)
                data = data.decode("UTF-8")
                if data == None:
                    break
                else:
                    print(data.strip())
                    new_data=data[2:-1]
                    print(str(new_data))

                    socket.close


if __name__ == '__main__':
    messages = []
    connid = 0
    init_connection()


            

            

        
        

