from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from src.database.connection import get_db
from src.services.employee_serivce import promote_employee, add_employee, remove_employee, display_employees
from src.models.employee import Employee
from dtos.employee_dto import EmployeeDTO


class EmployeeCreate(BaseModel):
    emp_id: str
    name: str
    position: str
    salary: float


class EmployeePromote(BaseModel):
    new_position: str
    new_salary: float


router = APIRouter()


@router.post("/employees", response_model=EmployeeDTO)
def add_employee_route(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = add_employee(db, employee.emp_id, employee.name, employee.position, employee.salary)
    return EmployeeDTO.from_orm(db_employee)


@router.delete("/employees/{emp_id}")
def remove_employee_route(emp_id: str, db: Session = Depends(get_db)):
    db_employee = remove_employee(db, emp_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee removed successfully"}


@router.put("/employees/{emp_id}/promote", response_model=EmployeeDTO)
def promote_employee_route(emp_id: str, promotion: EmployeePromote, db: Session = Depends(get_db)):
    db_employee = promote_employee(db, emp_id, promotion.new_position, promotion.new_salary)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return EmployeeDTO.from_orm(db_employee)


@router.get("/employees", response_model=List[EmployeeDTO])
def display_employees_route(db: Session = Depends(get_db)):
    employees = display_employees(db)
    return [EmployeeDTO.from_orm(emp) for emp in employees]
