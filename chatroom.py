

class Chatroom:
    def __init__(self, name, uuid, messages, users):
        self.name = name
        self.messages = messages
        self.uuid=uuid
        self.users=users

    # def join_chatroom(self, j):
    #     user_id = str(uuid.uuid4())
    #     self.users[name] = user_id
    #     self.messages.append(f"{name} has joined the chatroom.")
    #     return user_id

    def display_messages(self):
        for message in self.messages:
            print(message)
