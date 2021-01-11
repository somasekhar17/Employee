import random
from datetime import datetime
from sqlalchemy import text
import db_creation
import db_connect


class AdminChecks:

    def __init__(self):
        self.conn = db_connect.db_connection

    def close_admin_conn(self):
        db_connect.database_connection.close_connection()

    def add_emp(self, emp_id, first_name, last_name, dept_name, gender, mobile_no, dob):

        # Fetch if the employee details already exist
        x = self.view_emp(emp_id)

        dob = datetime.strptime(dob, "%Y-%m-%d").date()

        # If Employee already exists
        if x:
            print('Employee already exists')
            return x

        dept_details = self.view_dept(dept_name)

        if dept_details is None:
            self.add_dept(dept_name)
            dept_details = self.view_dept(dept_name)

        dept_id = dept_details[0]

        # Generate random password
        password = random.choice("[a-z]") + random.choice("[A-Z]") + random.choice("[0-9]") \
                   + random.choice("[!-*&@#$()]")

        for i in range(4):
            password += random.choice("[a-zA-Z0-9!-*&@#$()]")

        # Insert Employee Details
        add_emp = text("INSERT INTO EMPLOYEE VALUES(" + str(emp_id) + ", '" + password + "', '" + first_name + "', '"
                       + last_name + "', " + dept_id + ", '" + gender + "'," + mobile_no + " , " + str(dob) + ")")
        self.conn.execute(add_emp)

        print('Employee Added Successfully')

    def add_dept(self, dept_name):

        # Fetch if the department already exists
        x = self.view_dept(dept_name)

        # If Department already exists
        if len(x) != 0:
            print('Department already exists')
            return x

        # Fetch the highest Dept ID
        dept_id_check = text("SELECT MAX(DEPT_ID) FROM DEPT")

        max_dept_id = int(self.conn.execute(dept_id_check).fetchall()[0][0])
        #print("Max Dept ID:", max_dept_id)

        # Insert Dept Details
        add_dept = text("INSERT INTO DEPT VALUES(" + str(max_dept_id+1) + ", " + dept_name + ")")
        self.conn.execute(add_dept)

        print('Department Added Successfully')

    def update_emp(self, emp_id):

        # Fetch Employee Details
        x = self.view_emp(emp_id)

        if not x:
            print("Employee ID is incorrect")
            return
        check = 'Y'

        while check == 'Y':

            choice = input("Choose the field to be updated:\n"
                           "1. Department\n"
                           "2. Mobile No.")

            if choice == '1':
                self.update_emp_dept(emp_id)
            elif choice == '2':
                self.update_emp_mobile_no(emp_id)
            else:
                print('Wrong choice')

            check = input('Do you wish to update again?(Y/N)')

    def update_emp_dept(self, emp_id):

        # View all available Departments
        x = self.view_all_dept()

        # Enter new dept id.
        new_dept_id = int(input('Enter the new Department ID:'))

        # Check if dept exists or not
        flag = 0
        for val in x:
            if new_dept_id == val[0]:
                flag = 1
                break

        if flag == 0:
            print('Incorrect Department Details!')
            return

        # Update Dept
        dept_update = text("UPDATE EMPLOYEE SET DEPT_ID='" + str(new_dept_id) + "' WHERE EMPLOYEE_ID=" + str(emp_id))
        self.conn.execute(dept_update)
        print("Department Updated Successfully")

    def update_emp_mobile_no(self, emp_id):

        # Enter new mobile no.
        new_mobile_no = input('Enter the new mobile no.:')

        # Check if mobile no. is valid
        if len(new_mobile_no) == 10 and new_mobile_no.isdigit():
            mobile_update = text("UPDATE EMPLOYEE SET MOBILE_NO='" + str(new_mobile_no) + "' WHERE EMPLOYEE_ID="
                                 + str(emp_id))
            self.conn.execute(mobile_update)
            print('Mobile No. Updated Successfully')
        else:
            print("Mobile no. is not Valid")

    def update_dept(self, dept_name):

        # Check if dept exists
        x = self.view_dept(dept_name)

        new_dept_name = input("Enter new department name:")

        # Update Dept Details
        dept_update = text("UPDATE DEPT SET DEPT_NAME='" + str(new_dept_name) + "' WHERE DEPT_ID=" + str(x[0]))
        self.conn.execute(dept_update)
        print("Department Updated Successfully")

    def del_emp(self, emp_id):

        # Fetch if employee exists
        x = self.view_emp(emp_id)

        if len(x) == 0:
            print("Employee doesn't exist")
            return

        del_emp = text("DELETE FROM EMPLOYEE WHERE EMP_ID=" + str(emp_id))
        self.conn.execute(del_emp)
        print("Employee Deleted Successfully")

    def view_all_emp(self):

        # Fetch all employee details
        all_emp = text("SELECT * FROM EMPLOYEE")
        print("Query:", all_emp)
        x = self.conn.execute(all_emp).fetchall()

        for val in x:
            print('Employee ID:', val[0])
            print('First Name:', val[2])
            print('Last Name:', val[3])
            dept_details = text("SELECT DEPT_NAME FROM DEPT WHERE DEPT_ID=" + str(val[4]))
            dept_name = self.conn.execute(dept_details).fetchall()[0][0]
            print('Department', dept_name)
            print('Gender:', val[5])
            print('Mobile No.:', val[6])

    def view_emp(self, emp_id):

        # Fetch employee detail
        emp_detail = text("SELECT * FROM EMPLOYEE WHERE EMPLOYEE_ID=" + str(emp_id))
        #print("Query:", emp_detail)
        emp_detail = self.conn.execute(emp_detail).fetchall()
        print("emp_detail:", emp_detail)

        if not emp_detail:
            return

        #print("Value:", emp_detail)

        for val in emp_detail:
            print('Employee ID:', val[0])
            print('First Name:', val[2])
            print('Last Name:', val[3])
            dept_details = text("SELECT DEPT_NAME FROM DEPT WHERE DEPT_ID=" + str(val[4]))
            dept_name = self.conn.execute(dept_details).fetchall()[0][0]
            print('Department:', dept_name)
            print('Gender:', val[5])
            print('Mobile No.:', val[6])

        return emp_detail[0]

    def view_all_dept(self):

        # Fetch all dept details
        all_dept = text("SELECT * FROM DEPT")
        dept_details = self.conn.execute(all_dept).fetchall()

        print("List of Available Departments")
        for dept in dept_details:
            print('Dept ID:', dept[0], ' Dept Name:', dept[1])

        return dept_details

    def view_dept(self, dept_name):

        # Fetch the dept details
        dept_details = text("SELECT * FROM DEPT WHERE DEPT_NAME='" + dept_name + "'")
        x = self.conn.execute(dept_details).fetchall()

        if len(x) == 0:
            print("Department doesn't exist")
            return

        print("Dept ID: ", x[0][0])
        print("Dept Name: ", x[0][1])

        return x
