from datetime import datetime, timedelta

def loans():
    memberID = int(input("memberID: "))

    FName = input("First name: ")

    LName = input("Last name: ")

    LoanSum = int(input("Sum loaned out: "))

    Date = datetime.now()

    LoanDate = Date.date()

    SumReturnable = 1.1*LoanSum
    
    ReturnDate = LoanDate + timedelta(days=30)
    
    return [memberID, FName, LName, LoanSum, LoanDate, SumReturnable, ReturnDate]













































# def loans():
#     memberID = int(input("memberID: "))

#     Fname = input("First name: ")

#     Lname = input("Last name: ")

#     LoanSum = int(input("Sum loaned out: "))

#     date_obj = input("Input date(yyyy-mm-dd): ")
#     LoanDate = datetime.strptime(date_obj, f'%Y-%m-%d').date()


#     SumReturnable = 110*LoanSum

#     days_to_add = 30
#     new_date = date_obj + timedelta(days=days_to_add)

#     ReturnDate = new_date
    
#     return [memberID, Fname, Lname, LoanSum, LoanDate, SumReturnable, ReturnDate]
