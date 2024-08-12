import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from src.controllers.employee_api import (
    add_employee_route,
    remove_employee_route,
    promote_employee_route,
    display_employees_route,
    EmployeeCreate,
    EmployeePromote,
)
from src.models.employee import Employee
from dtos.employee_dto import EmployeeDTO


@pytest.fixture
def mock_db_session():
    return MagicMock()


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, mock_db_session):
        self.db = mock_db_session

    def create_employee(self, emp_id, name, position, salary):
        return Employee(emp_id=emp_id, name=name, position=position, salary=salary)


class TestEmployeeAPI(BaseTest):
    @patch('src.services.employee_serivce.add_employee')
    def test_add_employee_route(self, mock_add_employee):
        # Arrange
        employee_data = {
            "emp_id": "1",
            "name": "John Doe",
            "position": "Developer",
            "salary": 60000.0,
        }
        employee_create = EmployeeCreate(**employee_data)
        mock_employee = self.create_employee(**employee_data)
        mock_add_employee.return_value = mock_employee

        # Act
        response = add_employee_route(employee_create, self.db)

        # Assert
        assert response == EmployeeDTO.from_orm(mock_employee)
        mock_add_employee.assert_called_once_with(
            self.db,
            employee_data["emp_id"],
            employee_data["name"],
            employee_data["position"],
            employee_data["salary"],
        )

    @patch('src.services.employee_serivce.remove_employee')
    def test_remove_employee_route(self, mock_remove_employee):
        # Arrange
        emp_id = "1"
        mock_employee = self.create_employee(emp_id, "John Doe", "Developer", 60000.0)
        mock_remove_employee.return_value = mock_employee

        # Act
        response = remove_employee_route(emp_id, self.db)

        # Assert
        assert response == {"message": "Employee removed successfully"}
        mock_remove_employee.assert_called_once_with(self.db, emp_id)

    @patch('src.services.employee_serivce.remove_employee')
    def test_remove_employee_route_not_found(self, mock_remove_employee):
        # Arrange
        emp_id = "1"
        mock_remove_employee.return_value = None

        # Act & Assert
        with pytest.raises(HTTPException) as exc_info:
            remove_employee_route(emp_id, self.db)
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Employee not found"

    @patch('src.services.employee_serivce.promote_employee')
    def test_promote_employee_route(self, mock_promote_employee):
        # Arrange
        emp_id = "1"
        promotion_data = {"new_position": "Senior Developer", "new_salary": 80000.0}
        promotion_create = EmployeePromote(**promotion_data)
        mock_employee = self.create_employee(
            emp_id, "John Doe", promotion_data["new_position"], promotion_data["new_salary"]
        )
        mock_promote_employee.return_value = mock_employee

        # Act
        response = promote_employee_route(emp_id, promotion_create, self.db)

        # Assert
        assert response == EmployeeDTO.from_orm(mock_employee)
        mock_promote_employee.assert_called_once_with(
            self.db, emp_id, promotion_data["new_position"], promotion_data["new_salary"]
        )

    @patch('src.services.employee_serivce.promote_employee')
    def test_promote_employee_route_not_found(self, mock_promote_employee):
        # Arrange
        emp_id = "1"
        promotion_data = {"new_position": "Senior Developer", "new_salary": 80000.0}
        promotion_create = EmployeePromote(**promotion_data)
        mock_promote_employee.return_value = None

        # Act & Assert
        with pytest.raises(HTTPException) as exc_info:
            promote_employee_route(emp_id, promotion_create, self.db)
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Employee not found"

    @patch('src.services.employee_serivce.display_employees')
    def test_display_employees_route(self, mock_display_employees):
        # Arrange
        mock_employee_1 = self.create_employee("1", "John Doe", "Developer", 60000.0)
        mock_employee_2 = self.create_employee("2", "Jane Doe", "Manager", 80000.0)
        mock_display_employees.return_value = [mock_employee_1, mock_employee_2]

        # Act
        response = display_employees_route(self.db)

        # Assert
        assert response == [
            EmployeeDTO.from_orm(mock_employee_1),
            EmployeeDTO.from_orm(mock_employee_2),
        ]
        mock_display_employees.assert_called_once_with(self.db)


if __name__ == "__main__":
    pytest.main()
