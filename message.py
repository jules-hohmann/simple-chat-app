class Message:
    def __init__(self, sender, payload, timestamp, chatroom_id, uuid):
        self.sender = sender
        self.payload = payload
        self.timestamp = timestamp
        self.chatroom_id = chatroom_id
        self.uuid = uuid
