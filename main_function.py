from db_connection import connect_to_database
from member import add_member
from cursor_add_members import inserting_data, loan_add, store_passwords
from loan_func import loans

mydb = connect_to_database()

cursor = mydb.cursor()

print("""1. Add member
2. Display member table
3. Disband loan
""")


choice = int(input("Please input your choice here: "))
if choice == 1:

    member = add_member()

    insert = inserting_data()

    try:
        cursor.execute(insert, member)

        
        print(f'Data Successfully inserted to database')

    except Exception as e:
        print(f'{e}')

    
elif choice == 2:
    try:

        cursor.execute("SELECT * FROM members;")

    except Exception as e:
        print(e)



elif choice == 3:

    loan_info = loan_add()

    loan_call = loans()

    try:
        cursor.execute(loan_info, loan_call)


        print("Loan data entered successfully")

    except Exception as e:
        print(e)
