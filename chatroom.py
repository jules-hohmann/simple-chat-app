from client import Client
from message import Message

class Chatroom:
    def __init__(self, name, uuid):
        self.name = name
        self.messages = [] #should be empty when constructed
        self.uuid=uuid
        self.users = []

    # def join_chatroom(self, j):
    #     user_id = str(uuid.uuid4())
    #     self.users[name] = user_id
    #     self.messages.append(f"{name} has joined the chatroom.")
    #     return user_id

    def display_messages(self, message):
        if(message.chat_id == self.uuid):
            self.messages.append(message)

    def new_client(self, client):
        self.users.append(client)
    
    def delete_client(self, client):
        if client in self.users: self.users.remove(client)
