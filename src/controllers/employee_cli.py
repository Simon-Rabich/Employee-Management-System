from sqlalchemy.orm import Session

from src.exceptions.input_salary_exception import InputError
from src.services.employee_serivce import add_employee, remove_employee, promote_employee, display_employees
from tabulate import tabulate
from termcolor import colored


def handle_add_employee(db: Session):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        raise InputError("Invalid input. Please enter a valid number for salary.")

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


def format_employee_table(employees):
    table = []
    for i, emp in enumerate(employees):
        color = 'green' if i % 2 == 0 else 'yellow'
        row = [colored(emp.emp_id, color), colored(emp.name, color), colored(emp.position, color),
               colored(emp.salary, color)]
        table.append(row)

    # Color headers
    headers = [colored('ID', 'cyan'), colored('Name', 'cyan'), colored('Position', 'cyan'), colored('Salary', 'cyan')]

    return tabulate(table, headers=headers, tablefmt="grid")


def handle_display_employees(db: Session):
    employees = display_employees(db)
    print(format_employee_table(employees))

