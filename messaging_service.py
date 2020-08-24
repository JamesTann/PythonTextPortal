import json
from twilio.rest import Client

class MessagingService:

    def __init__(self, path):
        self.path = path
        
        # load existing settings and initiate client
        try:
            with open(self.path) as config_file:
                self.options = json.load(config_file)
                self.client = Client(self.options.get('account_sid'), self.options.get('auth_token'))
        except:
            print("Messaging Service Error: Unable to open config file and initiate client.")

    def send(self, message):

        # try to send a message
        if self.client is not None and self.options is not None:
            try:
                self.client.messages.create(body=message, from_=self.options.get('twilio_phone_number'), to=self.options.get('personal_phone_number'))
            except:
                print("Messaging Service Error: Unable to send message from client.")
        else:
            print("Messaging Service Error: Client or options not initiated.")

    def send_error(self, message):
        self.send("Error: " + message)
