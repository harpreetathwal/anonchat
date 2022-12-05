import sqlalchemy
from twilio.rest import Client

connection_name = "psychic-catwalk-370506:us-central1:twilio"
table_name = "Contacts"
db_name = "imentor"
db_user = "root"
db_password = "1234"

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

def insert(request):
    # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.

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

    lname = request.args.get('lname').strip(" +")
    fname = request.args.get('fname').strip(" +")
    phone_number = request.args.get('phone_number').strip(" +")
    if len(phone_number)==10:
        phone_number = "1" + phone_number
    phone_number = '+' + phone_number
    email = request.args.get('email').strip(" +")
    table_fields = "lname, fname, phone_number, email"
    table_field_values = '''"{}", "{}", "{}", "{}"'''.format(lname, fname, phone_number, email)
    stmt = sqlalchemy.text('insert into {} ({}) values ({})'.format(table_name, table_fields, table_field_values))
    
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
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    

    #send(to,request.args.get('message'))
    message_1 = "Admin: Hi, this is iMentor. You have signed up for text based communication with your paired Mentor (John Williams)"
    message_2 = "Please save this number in your contacts! For example, you can add it as 'John Williams (iMentor)'"
    send(to=phone_number, message_body=message_1)
    send(to=phone_number, message_body=message_2)
    
    return ("Success: Sent onboarding message to: " + phone_number, 200, headers)


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
    