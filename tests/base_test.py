import pytest
from unittest.mock import MagicMock
from src.models.employee import Employee


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, mocker):
        # Setup: Run before each test
        self.db = mocker.MagicMock()
        yield
        # Teardown: Run after each test
        self.db.reset_mock()


    def create_employee(self, emp_id, name, position, salary):
        return Employee(emp_id=emp_id, name=name, position=position, salary=salary)
