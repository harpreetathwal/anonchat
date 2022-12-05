from twilio.rest import Client

def send(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    to = request.args.get("to")
    message_body = request.args.get("message")

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