# example: curl https://us-central1-psychic-catwalk-370506.cloudfunctions.net/Twilio-onboard-number?message=+7322774364
from twilio.rest import Client

def onboard(request):
    to_fallback="+17322774364"
    if request.args and 'message' in request.args:
        #send(to,request.args.get('message'))
        to_from_request=request.args.get('message', to_fallback)
        message_1 = "Admin: Hi, this is iMentor. You have signed up for text based communication with your paired Mentor (John Williams)"
        message_2 = "Please save this number in your contacts! For example, you can add it as 'John Williams (iMentor)'"
        send(to=to_from_request, message_body=message_1)
        send(to=to_from_request, message_body=message_2)
        return "Sent onboarding message to: " + to_from_request

def send(to="+17322774364", message_body='test-message'):
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
            body=message_body,
            to=to
        )

    print(message.sid)
    return message.sid

if __name__ == "__main__":
    send(to="+17322774364", message_body="Local Test")