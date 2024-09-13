import getpass, hashlib, os
from db_connection import connect_to_database, errorcode, Error
# from cursor_add_members import fetch_user_data

mydb = connect_to_database()
cursor = mydb.cursor()

fetch_sql = "SELECT * FROM admins WHERE username = %s;"

def verify_password(stored_password, provided_password, salt):
    return stored_password == hashlib.sha256(salt + provided_password.encode('utf-8')).digest()

def login_user(username, password):
    try:
        cursor.execute(fetch_sql, (username,))
        result = cursor.fetchone()
        
        if result:
            stored_key, salt, hash_algo, iterations = result[1], result[2], result[3], result[4]
            if verify_password(stored_key, password, salt):
                print("Login successful!")
            else:
                print("Invalid username or password.")
        else:
            print("Invalid username or password.")
    except Exception as e:
        print(f'{e}')

username = input("Please input username: ")
password = getpass.getpass("Please input password: ")
login_user(username, password)






































# from db_connection import connect_to_database, errorcode, Error
# import hashlib, getpass

# mydb = connect_to_database()
# cursor = mydb.cursor()

# print("WELCOME, PLEASE LOG IN")

# username = input("Please enter username: ")

# password = getpass.getpass("Please enter password: ")


# global account
    
# #  Get hash details from database
# select_sql = "SELECT * FROM admins WHERE username = %s;"

# cursor.execute(select_sql, (username,))

# account = cursor.fetchone()

# # key, salt, hash_algo, iterations = account[1:5]  

# salt = account[2]

# def verify_account(username, password):
#     stored_hash = account[1]
#     if stored_hash:
#         # Hash the input password
#         input_hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
#         return stored_hash == input_hashed_password
#     else:
#         return False
    
# if verify_account(username, password):
#     print("Login successful")
# else:
#     print("Incorrect password!")












# select_sql = "SELECT * FROM admins WHERE username = %s;"
# cursor.execute(select_sql, (username,))
# account = cursor.fetchone()

# # if not account:
# #     print("Invalid username")
# #     # return

# key, salt, hash_algo, iterations = account[1:4]

# #Recompute hash from user entered password  
# password_hash = hashlib.pbkdf2_hmac(hash_algo, password.encode('utf-8'),  salt, iterations = 100_000)

# # Compare hashes
# if password_hash == key:
#     print("Login successful")
# else:
#     print("Invalid password")

# # login(username, password)
