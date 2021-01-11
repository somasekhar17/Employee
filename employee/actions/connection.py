from sqlalchemy.sql import text
import db_connect


class DBAccess:

    def __init__(self):
        self.isConnect = False
        self.db_connection = None

    def login(self, emp_id, password):

        try:
            self.db_connection = db_connect.db_connection
            self.is_connect = True

        # If connection is not successful
        except():
            print("Can't connect to database")
            return 0

        # If Connection Is Successful
        print("Connected")

        # Executing Query
        where_clause1 = "employee_id='" + emp_id + "'"
        where_clause2 = "password='" + password + "'"

        login_check = text("SELECT * from employee where " + where_clause1 + " and " + where_clause2)

        login_check = self.db_connection.execute(login_check).fetchall()
        print("Login Check, Connection: ", login_check)

        # If data exists then login
        return login_check
