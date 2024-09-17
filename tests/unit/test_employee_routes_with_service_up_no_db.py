
from unittest.mock import MagicMock, patch
from dtos.employee_dto import EmployeeDTO


def test_add_employee_success(client):
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



