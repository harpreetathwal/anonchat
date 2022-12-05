# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['VAR']
# auth_token = os.environ['VAR']
account_sid = 'AC996bb3c3da685a51f2758ddc23b34b5e'
auth_token = 'a4a0da7c754968d88a6f1ec16f437e2e'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         messaging_service_sid='MGffa0074b2cde79bd3c30d0bc5475cd42',
         body='test message',
         to='+17322774364'
     )

print(message.sid)