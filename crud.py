from models import Employee


def create_employee(db, employee):
    new_emp = Employee(**employee.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


def get_employees(db):
    return db.query(Employee).all()


def get_employee(db, emp_id):
    return db.query(Employee).filter(Employee.id == emp_id).first()


def update_employee(db, emp_id, employee):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    emp.name = employee.name
    emp.email = employee.email
    emp.phone = employee.phone
    emp.department = employee.department
    emp.designation = employee.designation
    emp.salary = employee.salary
    emp.hire_date = employee.hire_date

    db.commit()
    db.refresh(emp)
    return emp



def delete_employee(db, emp_id):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    db.delete(emp)
    db.commit()
    
