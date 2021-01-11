from sqlalchemy import text
import db_connect
import db_creation


class EmpChecks:

    def __init__(self):
        self.conn = db_connect.db_connection

    def update_employee(self, emp_id):

        # Fetch Employee Details
        x = self.view_emp(emp_id)

        if len(x) == 0:
            print("Employee doesn't exist")
            return
        check = 'Y'

        while check == 'Y':

            choice = input("Choose the field to be updated:\n"
                           "1. Department\n"
                           "2. Mobile No.\n"
                           "3. Password")

            if choice == '1':
                self.update_emp_dept(emp_id)
            elif choice == '2':
                self.update_emp_mobile_no(emp_id)
            elif choice == '3':
                self.update_emp_pswd(emp_id)
            else:
                print('Wrong choice')

            check = input('Do you wish to update again?(Y/N)')

    def update_emp_pswd(self, emp_id):

        # Check if old password is correct
        old_pswd = input('Enter old password:')

        pswd_attempts = 1
        pswd_check = self.conn.login(emp_id, old_pswd)

        if pswd_check is None:
            print('Password is wrong.')
            while pswd_attempts < 4:
                pswd_check = self.conn.login(emp_id, old_pswd)

                if pswd_check is not None:
                    count = 1
                    while count < 4:
                        new_pswd = input('Enter new password:')
                        renew_pswd = input('Re-enter new password:')
                        if new_pswd == renew_pswd:
                            pswd_update = text("UPDATE EMPLOYEE SET PASSWORD='" + new_pswd +
                                               "' WHERE EMPLOYEE_ID=" + emp_id)
                            self.conn.execute(pswd_update)
                            print("Password Updated Successfully")
                            break
                        else:
                            print("Passwords don't match")

                    if count == 4:
                        print("Limit Reached")

                else:
                    print('Password is wrong.')
                    pswd_attempts += 1

    def update_emp_dept(self, emp_id):

        # View all available Departments
        x = self.view_all_dept()

        # Enter new dept id.
        new_dept_id = int(input('Enter the new Department ID:'))

        # Check if dept exists or not
        flag = 0
        for val in x:
            #print("Val: ", val[0])
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

    def view_emp(self, emp_id):

        # Fetch employee detail
        emp_detail = text("SELECT * FROM EMPLOYEE WHERE EMPLOYEE_ID=" + str(emp_id))
        #print("Employee Detail: ", emp_detail)
        val = self.conn.execute(emp_detail).fetchall()[0]

        print('Employee ID:', str(val[0]))
        print('First Name:', val[2])
        print('Last Name:', val[3])
        dept_details = text("SELECT DEPT_NAME FROM DEPT WHERE DEPT_ID=" + str(val[4]))
        dept_name = self.conn.execute(dept_details).fetchall()[0][0]
        print("Dept Name: ", dept_name)
        print('Gender:', val[5])
        print('Mobile No.:', val[6])

        return val

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

        if x is None:
            print("Department doesn't exist")
            return

        return x
