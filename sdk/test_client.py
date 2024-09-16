# from sdk.client import EmployeeManagementClient
# from datetime import datetime
#
# def main():
#     base_url = "http://localhost:8000"
#     client = EmployeeManagementClient(base_url)
#
#     # # Add an employee
#     # print("Adding an employee...")
#     # response = client.add_employee("E001", "John Doe", "Developer", 60000)
#     # print(response)
#
#     # Display employees
#     print("Displaying employees...")
#     response = client.display_employees()
#     print(response)
#
#     # Promote an employee
#     # print("Promoting an employee...")
#     # response = client.promote_employee("E001", "Senior Developer", 70000)
#     # print(response)
#     #
#     # # Remove an employee
#     # print("Removing an employee...")
#     # response = client.remove_employee("E001")
#     # print(response)
#     #
#     # # Add a product version
#     # print("Adding a product version...")
#     # response = client.add_product_version("dev", "v1.0", datetime.now())
#     # print(response)
#     #
#
# if __name__ == "__main__":
#     main()
import pytest
from sdk.client import EmployeeManagementClient
from datetime import datetime

@pytest.fixture(scope="module")
def client():
    return EmployeeManagementClient(base_url="http://localhost:8000/api")


def test_add_employee(client):
    # Test adding an employee
    response = client.add_employee("E001", "John Doe", "Developer", 60000)
    assert response["success"] is True
    assert response["result"]["emp_id"] == "E001"
    assert response["result"]["name"] == "John Doe"
    assert response["result"]["position"] == "Developer"
    assert response["result"]["salary"] == 60000.0


def test_display_employees(client):
    # Test fetching employees
    response = client.display_employees()
    assert response["success"] is True
    assert len(response["result"]) > 0
    # Check the first employee returned
    employee = response["result"][0]
    assert employee["emp_id"] is not None
    assert employee["name"] is not None
    assert employee["position"] is not None


def test_promote_employee(client):
    # Test promoting an employee
    response = client.promote_employee("E001", "Senior Developer", 70000)
    assert response["success"] is True
    assert response["result"]["position"] == "Senior Developer"
    assert response["result"]["salary"] == 70000.0


def test_remove_employee(client):
    # Test removing an employee
    response = client.remove_employee("E001")
    assert response["success"] is True
    assert response["result"]["message"] == "Employee removed successfully"


def test_add_product_version(client):
    # Test adding a product version
    response = client.add_product_version("dev", "v1.0", datetime.now())
    assert response["success"] is True
    assert response["result"]["environment"] == "dev"
    assert response["result"]["version"] == "v1.0"
