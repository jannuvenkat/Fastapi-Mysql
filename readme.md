Employee Management System API

Overview

This is a simple Employee Management System built using FastAPI, MySQL, and SQLAlchemy. The project provides REST APIs to perform CRUD (Create, Read, Update, Delete) operations on employee records.

Features

- Add a new employee
- View all employees
- View employee by ID
- Update employee details
- Delete an employee
- Search employees by department
- Interactive API documentation using Swagger UI

Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- Uvicorn

Project Structure

employee_management/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
└── README.md

Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required packages:

pip install -r requirements.txt

4. Configure your MySQL database in "database.py".
5. Start the application:

uvicorn main:app --reload

API Endpoints

Method| Endpoint| Description
GET| "/"| Welcome message
POST| "/employees"| Create a new employee
GET| "/employees"| Get all employees
GET| "/employees/{id}"| Get employee by ID
GET| "/employees/department/{department}"| Get employees by department
PUT| "/employees/{id}"| Update an employee
DELETE| "/employees/{id}"| Delete an employee

Future Improvements

- JWT Authentication
- Role-Based Access Control
- Pagination
- Search and Filtering
- Employee Dashboard
- Docker Deployment

Author

Venkata Ayyappa Jannu