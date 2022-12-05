# Example: curl https://us-central1-psychic-catwalk-370506.cloudfunctions.net/updatedb?lname=curltest&fname=ftest&phone_number=+7322774364&email=ha22@cornell.edu

import sqlalchemy
connection_name = "psychic-catwalk-370506:us-central1:twilio"
table_name = "Contacts"
db_name = "imentor"
db_user = "root"
db_password = "1234"

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

def insert(request):
    lname = request.args.get('lname').strip(" +")
    fname = request.args.get('fname').strip(" +")
    phone_number = '+' + request.args.get('phone_number').strip(" +")
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
    return 'ok'