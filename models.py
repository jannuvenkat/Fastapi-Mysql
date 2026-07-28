from sqlalchemy import Column, Integer, String, DECIMAL, Date
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(15),nullable=False)
    department = Column(String(50),nullable=False)
    designation = Column(String(50))
    salary = Column(DECIMAL(10,2))
    hire_date = Column(Date)