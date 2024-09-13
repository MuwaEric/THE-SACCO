import datetime
def add_member():

    print("Please add member info")

    memberID = int(input("Member ID: "))

    Fname = input("First name: ")

    LName = input("Last name: ")

    DOB = input(f'Date of birth(yyyy-mm-dd): ')
    # date_object = datetime.strptime(DOB, f'%Y-%m-%d').date()

    PhoneNo = int(input("Phone number: "))

    email = input("e-mail: ")

    return [memberID, Fname, LName, DOB, PhoneNo, email]

print(type(add_member()))



    

