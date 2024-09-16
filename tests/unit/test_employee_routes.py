# tests/unit/test_employee_routes.py

from unittest.mock import MagicMock, patch
from dtos.employee_dto import EmployeeDTO, EmployeePromote  # Ensure this matches your project structure

def test_add_employee_success(client):
    # Create a MagicMock instance for the EmployeeDTO
    mock_employee = MagicMock(spec=EmployeeDTO)
    mock_employee.emp_id = "E123"
    mock_employee.name = "John Doe"
    mock_employee.position = "Developer"
    mock_employee.salary = 50000

    # Patch the add_employee service to return the mock employee
    with patch('src.services.employee_service.add_employee', return_value=mock_employee):
        response = client.post("/api/create_employee", json={
            "emp_id": "E123",
            "name": "John Doe",
            "position": "Developer",
            "salary": 50000
        })

    # Assert the response
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["result"]["emp_id"] == "E123"
    assert data["result"]["name"] == "John Doe"



