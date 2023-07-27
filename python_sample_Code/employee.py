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

