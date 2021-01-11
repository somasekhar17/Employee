from admin.action import admin_login
from admin.admin_tasks import AdminChecks
from employee.actions import login
from employee.tasks import EmpChecks

while True:

    choice = input("Welcome!\n"
                   "1. Admin Login\n"
                   "2. Employee Login\n"
                   "3. Exit\n")

    if choice == '1':
        admin = admin_login.admin_login()
        admin_class = AdminChecks()

        ADMIN_CHECK = 'Y'

        while ADMIN_CHECK == 'Y':

            admin_choice = input("Choose action to perform\n"
                                 "1. View All Employees\n"
                                 "2. View Employee\n"
                                 "3. Add Employee\n"
                                 "4. Update Employee\n"
                                 "5. Delete Employee\n"
                                 "6. View All Departments\n"
                                 "7. View Department\n"
                                 "8. Add Department\n"
                                 "9. Update Department\n"
                                 "10. Exit\n")

            if admin_choice == '1':
                admin_class.view_all_emp()
            elif admin_choice == '2':
                emp_id = int(input("Enter Employee ID:"))
                admin_class.view_emp(emp_id)
            elif admin_choice == '3':
                emp_id = int(input("Enter Employee ID:"))
                first_name = input("Enter First Name:")
                last_name = input("Enter Last Name:")
                dept_name = input("Enter Department Name:")
                gender = input("Enter Gender:")
                mobile_no = int(input("Enter Mobile No.:"))
                dob = input("Enter Date of Birth(YYYY-MM-DD)")
                # dob = date(int(dob[6:]), int(dob[3:5]), int(dob[:3]))
                admin_class.add_emp(emp_id, first_name, last_name, dept_name, gender,
                                    mobile_no, dob)
            elif admin_choice == '4':
                emp_id = int(input("Enter Employee ID:"))
                admin_class.update_emp(emp_id)
            elif admin_choice == '5':
                emp_id = int(input("Enter Employee ID:"))
                admin_class.del_emp(emp_id)
            elif admin_choice == '6':
                admin.Admin_Checks().view_all_dept()
            elif admin_choice == '7':
                dept_name = input("Enter Department Name")
                admin_class.view_dept(dept_name)
            elif admin_choice == '8':
                dept_name = input("Enter Department Name")
                admin_class.add_dept(dept_name)
            elif admin_choice == '9':
                dept_name = input("Enter Existing Department Name")
                admin_class.update_dept(dept_name)
            elif admin_choice == '10':
                print("Bye Admin")
                break
            else:
                print('Invalid Choice')

            ADMIN_CHECK = input("Do you wish to continue accessing admin details?(Y/N)")
            '''if ADMIN_CHECK == 'N':
                admin_class.close_admin_conn()'''

    elif choice == '2':
        emp = login.emp_login()
        emp_class = EmpChecks()
        EMP_CHECK = 'Y'

        while EMP_CHECK == 'Y':
            emp_id = emp[0]
            emp_choice = input("Choose action to perform\n"
                               "1. View Employee\n"
                               "2. Update Employee\n"
                               "3. View All Departments\n"
                               "4. View Department\n"
                               "5. Exit\n")

            if emp_choice == '1':
                emp_class.view_emp(emp_id[0])
            elif emp_choice == '2':
                emp_class.update_employee(emp_id[0])
            elif emp_choice == '3':
                emp.Emp_Checks.view_all_dept()
            elif emp_choice == '4':
                dept_name = input("Enter department name:")
                emp_class.view_dept(dept_name)
            elif emp_choice == '5':
                print("Bye Employee")
                break
            else:
                print('Invalid Choice')

            EMP_CHECK = input("Do you wish to continue accessing employee details?(Y/N)")
            '''if EMP_CHECK == 'N':
                emp_class.close_emp_conn()'''

    elif choice == '3':
        print("Bye Bye")
        break

    else:

        print("Wrong Choice")

    x = input("Do you wish to continue?(Y/N)")
    if x == 'N':
        print("Bye Bye")
        break
