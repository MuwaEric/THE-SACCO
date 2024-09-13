import mysql.connector
from mysql.connector import errorcode, Error


def connect_to_database():
    mydb = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Htp256@age',
        database = 'sacco3',
        autocommit = True
    )

    mycursor = mydb.cursor()

    try:
        if mydb.is_connected():
            pass
    except:
        try:
            print(f"\nCreating new database connection")
            mydb = mysql.connector.connect()
        except Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print(f'\nIncorrect username or password')
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print(f'\nDatabase does not exist')
                else:
                    print(f'\n{err}')
    return mydb




def close_connection():

    global mydb

    try:
        if mydb.is_connected():
            mydb.close()
    except:
        pass


