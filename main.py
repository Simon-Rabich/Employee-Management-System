from src.database.connection import engine, Base, get_db
from src.controllers.cli.employee import handle_add_employee, handle_remove_employee, handle_promote_employee, handle_display_employees
from src.exceptions.input_salary_exception import InputError
from termcolor import colored


def init_db():
    Base.metadata.create_all(bind=engine)


def main():
    init_db()
    db = next(get_db())

    while True:
        print("\n1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Display Employees")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            try:
                handle_add_employee(db)
            except InputError as e:
                print(colored(e.message, 'red'))
        elif choice == '2':
            handle_remove_employee(db)
        elif choice == '3':
            try:
                handle_promote_employee(db)
            except InputError as e:
                print(colored(e.message, 'red'))
        elif choice == '4':
            handle_display_employees(db)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()