import json
from twilio.rest import Client

class MessagingService:

    def __init__(self, path):
        self.path = path
        with open(self.path) as config_file:
            self.options = json.load(config_file)
            self.client = Client(self.options.get('account_sid'), self.options.get('auth_token'))

    def send(self, message):
        if self.client is not None and self.options is not None:
            self.client.messages.create(body=message, from_=self.options.get('twilio_phone_number'), to=self.options.get('personal_phone_number'))
        else:
            print("Messaging Service Error: Client or options not initiated.")

