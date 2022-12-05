# webhook_url = "https://us-central1-psychic-catwalk-370506.cloudfunctions.net/Twilio-webhook"

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

def sms(request):
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # message = "Hello <<fname>>, this is your last name: <<lname>>"
    # Add a message
    message = request.values.get('Body', '').lower()
    message = process_templated_message(message)
    message = "Processed Message: " + message + " from " + request.values.get('From', '') 
    resp.message(message)
    
    #Send side-effect message to test forwarding
    send()

    return str(resp)

def process_templated_message(message):
    mapping_table = {"<<fname>>":"Harpreet", "<<lname>>":"Athwal"}
    for key, value in mapping_table.items():
        message = message.replace(key,value)
    return message

def send():
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
            body='sideeffect test message',
            to='+17322774364'
        )

    print(message.sid)
    return message.sid