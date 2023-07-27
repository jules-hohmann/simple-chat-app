from client import Client
from datetime import datetime, date


class Message:
    '''
    Constructor for each message that is either sent or received.

    Sender: Client that sent the message
    Payload: Content of the message
    '''
    def __init__(self, sender: Client, payload):
        self.sender = sender
        self.payload = payload
        self.timestamp = datetime.now()
    
    def format_message(self):
        '''
        Formats the attributes of a message into text that looks organized
        '''
        return(str(self.timestamp) + " | " + str(self.sender.username) + ": " + str(self.payload)).encode("utf-8")

