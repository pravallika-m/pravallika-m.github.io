# write rest api to perform crud operations on employee data
# use flask framework
# use flask_restful extension
# use sqlalchemy extension
# use sqlite database
# use marshmallow extension for serialization and deserialization

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError



app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(80), unique=True, nullable=False)
    jobTitleName = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(80), unique=True, nullable=False)
    lastName = db.Column(db.String(80), unique=True, nullable=False)
    preferredFullName = db.Column(db.String(80), unique=True, nullable=False)
    employeeCode = db.Column(db.String(80), unique=True, nullable=False)
    region = db.Column(db.String(80), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(80), unique=True, nullable=False)
    emailAddress = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Employee %r>' % self.userId
    
    def __init__(self, userId, jobTitleName, firstName, lastName, preferredFullName, employeeCode, region, phoneNumber, emailAddress):
        self.userId = userId
        self.jobTitleName = jobTitleName
        self.firstName = firstName
        self.lastName = lastName
        self.preferredFullName = preferredFullName
        self.employeeCode = employeeCode
        self.region = region
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

class EmployeeSchema(Schema):
    userId = fields.Str()
    jobTitleName = fields.Str()
    firstName = fields.Str()
    lastName = fields.Str()
    preferredFullName = fields.Str()
    employeeCode = fields.Str()
    region = fields.Str()
    phoneNumber = fields.Str()
    emailAddress = fields.Str()

@app.route('/employee', methods=['POST'])
def add_employee():
    employee_schema = EmployeeSchema()
    try:
        employee = employee_schema.load(request.json)
        result = employee_schema.dump(employee.create())
        return jsonify(result), 201
    except ValidationError as err:
        return jsonify(err.messages), 422
    
@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    return jsonify(employee)

@app.route('/employee/<id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    employee_schema = EmployeeSchema()
    try:
        employee = employee_schema.load(request.json, instance=employee)
        result = employee_schema.dump(employee.update())
        return jsonify(result), 200
    except ValidationError as err:
        return jsonify(err.messages), 422
    
@app.route('/employee/<id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify(employee), 200
    else:
        return jsonify({"employee": "Not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)


# create Dockerfile to build docker image
# create docker-compose.yml file to run docker container

# Path: python_sample_Code/Dockerfile
# FROM python:3.7
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE 5000
# CMD python employee_rest.py

# Path: python_sample_Code/docker-compose.yml
# version: '3'
# services:
#   web:
#     build: .
#     ports:

# create helmchart 




