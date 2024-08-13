from sqlalchemy.orm import Session
from src.models.employee import Employee
import logging


def add_employee(db: Session, emp_id: str, name: str, position: str, salary: float):
    logging.info("add_employee called")
    db_employee = Employee(emp_id=emp_id, name=name, position=position, salary=salary)
    logging.info(f"Employee created: {db_employee}")
    db.add(db_employee)
    logging.info("Employee added to session")
    db.commit()
    logging.info("Session committed")
    db.refresh(db_employee)
    logging.info("Employee refreshed")
    return db_employee


def remove_employee(db: Session, emp_id: str):
    db_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee


def promote_employee(db: Session, emp_id: str, new_position: str, new_salary: float):
    db_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if db_employee:
        db_employee.position = new_position
        db_employee.salary = new_salary
        db.commit()
        db.refresh(db_employee)
    return db_employee


def display_employees(db: Session):
    return db.query(Employee).all()
