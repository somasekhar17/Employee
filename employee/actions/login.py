from employee.actions import connection
from getpass import getpass
conn = connection.DBAccess()


def emp_login():

    login_attempts = 1
    print('Enter Employee Credentials:')
    emp_id = input('Enter employee id:')
    password = getpass('Enter password:')
    login_check = conn.login(emp_id, password)
    print("Login Check, Login: ", login_check)

    if len(login_check) == 0:
        while login_attempts < 4:
            print('Enter Employee Credentials:')
            emp_id = input('Enter employee id:')
            password = input('Enter password:')
            login_check = conn.login(emp_id, password)
            print("Login Check, Login: ", login_check)

            if login_check is not None:
                print("Welcome Employee")
                break

            else:
                print("Incorrect employee id/password")
                login_attempts += 1

    if login_attempts == 4:
        return

    return login_check
