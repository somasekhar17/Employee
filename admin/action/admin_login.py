from admin.action import admin_connector
from getpass import getpass
conn = admin_connector.DBAccess()


def admin_login():

    login_attempts = 1
    print('Enter Admin Credentials:')
    username = input('Enter username:')
    password = getpass('Enter password:')
    login_check = conn.login(username, password)
    #print("Admin Login, Login Check: ", login_check)

    if len(login_check) == 0:
        while login_attempts < 4:
            print('Enter Admin Credentials:')
            username = input('Enter username:')
            password = input('Enter password:')
            login_check = conn.login(username, password)
            #print("Admin Login, Login Check: ", login_check)

            if login_check is not None:
                print("Welcome Admin")
                break

            else:
                print("Incorrect username/password")
                login_attempts += 1

    if login_attempts == 4:
        return

    return login_check
