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

def delete(request):
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


    result = None
    stmt = sqlalchemy.text('delete from Contacts order by person_id desc limit 1;')
    
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

    return ("Success, deleted latest user", 200, headers)
