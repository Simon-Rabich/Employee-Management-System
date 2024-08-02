from sdk.client import EmployeeManagementClient


def main():
    base_url = "http://localhost:8000"
    client = EmployeeManagementClient(base_url)

    # Add an employee
    print("Adding an employee...")
    response = client.add_employee("E001", "John Doe", "Developer", 60000)
    print(response)

    # Display employees
    print("Displaying employees...")
    response = client.display_employees()
    print(response)

    # Promote an employee
    print("Promoting an employee...")
    response = client.promote_employee("E001", "Senior Developer", 70000)
    print(response)

    # Remove an employee
    print("Removing an employee...")
    response = client.remove_employee("E001")
    print(response)


if __name__ == "__main__":
    main()
