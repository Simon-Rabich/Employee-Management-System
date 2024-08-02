from sqlalchemy.orm import Session
from src.services.employee_serivce import add_employee, remove_employee, promote_employee, display_employees

def handle_add_employee(db: Session):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = float(input("Enter Salary: "))
    add_employee(db, emp_id, name, position, salary)
    print("Employee added successfully.")


def handle_remove_employee(db: Session):
    emp_id = input("Enter Employee ID to remove: ")
    remove_employee(db, emp_id)
    print("Employee removed successfully.")


def handle_promote_employee(db: Session):
    emp_id = input("Enter Employee ID to promote: ")
    new_position = input("Enter new position: ")
    new_salary = float(input("Enter new salary: "))
    promote_employee(db, emp_id, new_position, new_salary)
    print("Employee promoted successfully.")


def handle_display_employees(db: Session):
    employees = display_employees(db)
    for emp in employees:
        print(f"ID: {emp.emp_id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}")
