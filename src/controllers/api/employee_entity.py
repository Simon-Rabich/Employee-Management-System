from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.services.employee_service import add_employee, promote_employee, display_employees, remove_employee
from dtos.employee_dto import EmployeeDTO, EmployeeCreate, EmployeePromote
from dtos.response_dto import ResponseDTO
from common.decorators.decorator_logs_the_date_and_time import log_datetime
from utils.format_response import format_response

router = APIRouter()


@router.post("/create_employee", response_model=ResponseDTO)
@log_datetime
def add_employee_route(employee: EmployeeCreate, db: Session = Depends(get_db)) -> ResponseDTO:
    try:
        db_employee = add_employee(db, employee.emp_id, employee.name, employee.position, employee.salary)
        return format_response(success=True, result=EmployeeDTO.from_orm(db_employee))
    except Exception as e:
        return format_response(success=False, error=str(e))


@router.delete("/employees/{emp_id}", response_model=ResponseDTO)
@log_datetime
def remove_employee_route(emp_id: str, db: Session = Depends(get_db)) -> ResponseDTO:
    db_employee = remove_employee(db, emp_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return format_response(success=True, result={"message": "Employee removed successfully"})


@router.put("/employees/{emp_id}/promote", response_model=ResponseDTO)
@log_datetime
def promote_employee_route(emp_id: str, promotion: EmployeePromote, db: Session = Depends(get_db)) -> ResponseDTO:
    db_employee = promote_employee(db, emp_id, promotion.new_position, promotion.new_salary)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return format_response(success=True, result=EmployeeDTO.from_orm(db_employee))


@router.get("/employees", response_model=ResponseDTO)
@log_datetime
def display_employees_route(db: Session = Depends(get_db)) -> ResponseDTO:
    # Now, the correct db session should be passed here
    employees = display_employees(db)
    return format_response(success=True, result=[EmployeeDTO.from_orm(emp) for emp in employees])
