from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: str
    phone: str
    department: str
    designation: str
    salary: float
    hire_date: date

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True