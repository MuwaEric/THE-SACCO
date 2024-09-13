def inserting_data():
    query = '''
        INSERT INTO members
            (memberID, Fname, LName, DOB, PhoneNo, email)
        VALUES
            (%s, %s, %s, %s, %s, %s)
    '''
    return query


def loan_add():
    loan_info = '''
            INSERT INTO loans
                (memberID, Fname, Lname, LoanSum, LoanDate, SumReturnable, ReturnDate)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s);
    '''
    return loan_info


def store_passwords():
    password_info= """
    INSERT INTO admins
            (username, password_hash, salt, hash_algo, iterations) 
    VALUES 
            (%s, %s, %s, %s, %s);
    """
    return password_info
    