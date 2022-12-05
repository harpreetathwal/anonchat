# webhook_url = "https://us-central1-psychic-catwalk-370506.cloudfunctions.net/Twilio-webhook"

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import sqlalchemy
import json

connection_name = "psychic-catwalk-370506:us-central1:twilio"
table_name = "Persons"
db_name = "imentor"
db_user = "root"
db_password = "1234"

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})


def webhook(request):
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

    sender_phone_number = request.values.get('From', '')
    sender_name = None
    message_body = None
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    # try:
    print("Connecting to DB...")
    with db.connect() as conn:
        stmt = sqlalchemy.text('SELECT concat(fname, " ", lname) FROM Contacts WHERE phone_number LIKE "%{}%";'.format(sender_phone_number))
        print(stmt)
        result = conn.execute(stmt)
        print(result)
        result = [x for x in result]
        print(result)
        sender_name = result[0][0]
        print("sender: {}".format(sender_name))
        print(sender_name)

        stmt = sqlalchemy.text('SELECT fname, lname, phone_number FROM Contacts WHERE phone_number NOT LIKE "%{}%";'.format(sender_phone_number))
        print(stmt)
        result = conn.execute(stmt)
        print(result)
        outbound_contacts = [list(x) for x in result]
        print(outbound_contacts)
        outbound_names = [[x[0], x[1]] for x in outbound_contacts]
        outbound_numbers = [x[2] for x in outbound_contacts]
        print(outbound_names)
        print(outbound_numbers)

        message_body = request.values.get('Body', '').lower()
        print("Updating Messaages in CloudSQL")
        stmt = sqlalchemy.text('INSERT INTO Messages ( from_phone_number, message) VALUES ("{}","{}");'.format(sender_phone_number, message_body))
        print(stmt)
        result = conn.execute(stmt)
        print(result)
        print("Updated Messaages in CloudSQL")

    # except Exception as e:
    #     return 'Error: {}'.format(str(e))
    
    print("Forwarding messages...")
    for i,number in enumerate(outbound_numbers):
        print(number)
        print("outbound_names{}".format(outbound_names[i][1]))
        message_body = sender_name + ": " + process_templated_message(message_body, outbound_names[i][0], outbound_names[i][1])
        send(to=number, message_body=message_body)
    print("Forwarded!")

    print("Replying...")
    resp = MessagingResponse()
    resp.message("Your message was forwarded to: {}".format(json.dumps(outbound_names)))
    return str(resp)
    # return ("Sent to: "+json.dumps(outbound_numbers), 200, headers)


def process_templated_message(message, fname, lname):
    mapping_table = {"<<fname>>":fname, "<<lname>>":lname}
    for key, value in mapping_table.items():
        message = message.replace(key,value)
    return message


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
    