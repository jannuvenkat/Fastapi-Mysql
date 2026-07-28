from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management System API",
    description="A REST API for managing employee records using FastAPI and MySQL.",
    version="1.0.0"
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home Route
@app.get("/")
def welcome():
    return {"message": "Welcome to Employee Management System API!"}


# Create Employee
@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(db, employee)


# Get All Employees
@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)


# Get Employee By ID
@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# Get Employees By Department
@app.get("/employees/department/{department}", response_model=list[schemas.EmployeeResponse])
def get_department(department: str, db: Session = Depends(get_db)):
    employees = crud.get_by_department(db, department)

    if not employees:
        raise HTTPException(
            status_code=404,
            detail="No employees found in this department"
        )

    return employees


# Update Employee
@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_employee(db, employee_id, employee)

    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")

    return updated


# Delete Employee
@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_employee(db, employee_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}