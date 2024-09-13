import getpass, hashlib, os, binascii
from db_connection import connect_to_database, errorcode, Error
from cursor_add_members import store_passwords

mydb = connect_to_database()
cursor = mydb.cursor()

insert_sql = store_passwords()


PEPPER = "PASSWORD_DATABASE"

salt = os.urandom(32)

def create_secure_password(password):
  password_hash = hashlib.sha256(salt + password.encode('utf-8'))  
  return salt + password_hash.digest()



def create_new_user(username, password):

    password_hash = create_secure_password(password)

    salt, key = password_hash[:32], password_hash[32:]

    hash_algo = "PBKDF2"
    
    iterations = 100_000

    try:
        cursor.execute(insert_sql, (
        username,
        key,
        salt,
        hash_algo,
        iterations
        ))
        print("data entered successfully")
    except Exception as e:
        print(f'{e}')

        mydb.commit()


username = input("Please input username: ")

password = getpass.getpass("Please input password: ")
create_new_user(username, password)







# def create_secure_password(password): 
#     iterations = 100_000 
#     hash_value = hashlib.sha256(password.encode('utf-8') + PEPPER.encode('utf-8'), salt, iterations)
#     hashed_password = hashlib.pbkdf2_hmac(hash_value)
#     password_hash =  salt + hashed_password
#     return password_hash

















# def create_secure_password(password): 
#     iterations = 100_000 
#     hash_value = hashlib.pbkdf2_hmac(
#     'sha256',  
#     password.encode('utf-8') + PEPPER.encode('utf-8'), 
#     salt, 
#     iterations
#     )
#     password_hash = hash_value + salt
    
#     return password_hash


# def create_new_user(username, password):

#     password_hash = create_secure_password(password)

#     salt, key = password_hash[:32], password_hash[32:]

#     # password_hash = binascii.unhexlify(password_hash)

#     hash_algo = "PBKDF2"
#     iterations = 100_000

#     try:
#         cursor.execute(insert_sql, (
#         username,
#         key,
#         salt,
#         hash_algo,
#         iterations
#         ))
#         print("data entered successfully")
#     except Exception as e:
#         print(f'{e}')

#         mydb.commit()


# username = input("Please input username: ")

# password = getpass.getpass("Please input password: ")
# create_new_user(username, password)

# print(create_secure_password(password))


























# secure password generate route 2
# def secure_password_route2():
#     salt = os.urandom(32)
#     hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
#     return hashed_password











































# database = {
#     "user1" : "password1",
#     "user2" : "password2"
# }


# username = input("Please input username: ")

# password = getpass.getpass("Please input password: ")

# for i in database.keys():

#     if username in database and database[username] == password:
#         print("Authentication successful")

#     elif password != database.get(i):
#         password = getpass.getpass("incorrect password or username, please input password: ")











































# from datetime import datetime, timedelta

# def loans():
#     memberID = int(input("memberID: "))

#     Fname = input("First name: ")

#     Lname = input("Last name: ")

#     LoanSum = int(input("Sum loaned out: "))

#     LoanDate = datetime.now()

#     SumReturnable = 110*LoanSum
    
#     new_date = LoanDate + timedelta(days=30)

#     ReturnDate = new_date
    
#     return [memberID, Fname, Lname, LoanSum, LoanDate, SumReturnable, ReturnDate]
