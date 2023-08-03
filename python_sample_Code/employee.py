# write python program to read sample_employee.json file in current directory and print the employee details in the format given below
# Employee: <employee_name> , Age: <age> , Salary: <salary>

import json

# read json file using os absolute path module


import os

with open((os.path.dirname(os.path.abspath(__file__)) + "/sample_employee.json"), "r") as f:
    employee_data = json.load(f)
   

# read Values of Employees key from employee_data dictionary and print it
for employee in employee_data["Employees"]:
    print("userId: {}, jobTitleName: {}, firstName: {}".format(employee["userId"], employee["jobTitleName"], employee["firstName"]))



# write unit test for the above program

import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_employee(self):
        with patch('employee.Employee') as mocked_employee:
            employee = mocked_employee.return_value
            employee.userId = '12345'
            employee.jobTitleName = 'Software Engineer'
            employee.firstName = 'John'
            employee.lastName = 'Doe'
            employee.preferredFullName = 'John Doe'
            employee.employeeCode = 'E1'
            employee.region = 'CA'
            employee.phoneNumber = '408-1234567'
            employee.emailAddress = '

