from admin import admin_tasks
from employee import tasks
from employee.actions import connection
from admin.action import admin_connector


def test_admin_view_dept():
    dept_id = 101
    dept = admin_tasks.AdminChecks()
    assert dept.view_dept(dept_id) == [(101, 'Development')]


def test_admin_view_emp():
    emp_id = 123
    emp_detail = admin_tasks.AdminChecks()
    assert emp_detail.view_emp(emp_id) == [('123', 'Raghu1', 'Raghu', 'Ramaiah',
                                            101, 'Male', 9642692820, '1998-06-01')]


def test_emp_view_dept():
    dept_id = 102
    dept = tasks.EmpChecks()
    assert dept.view_dept(dept_id) == [(102, 'Support')]


def test_emp_view_emp():
    emp_id = 124
    emp_detail = tasks.EmpChecks()
    assert emp_detail.view_emp(emp_id) == [('124', 'rana2', 'Rana', 'Bhagathi',
                                            102, 'Male', 8639886712, '1996-11-08')]


test_admin_view_emp()
test_emp_view_emp()
test_admin_view_dept()
test_emp_view_dept()
