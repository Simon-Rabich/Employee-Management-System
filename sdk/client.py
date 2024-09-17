import requests
from typing import Optional
from datetime import datetime


class EmployeeManagementClient:
    def __init__(self, base_url: str = "http://localhost:8000/api", session: Optional[requests.Session] = None):
        self.base_url = base_url
        self.session = session or requests.Session()

    def add_employee(self, emp_id: str, name: str, position: str, salary: float):
        url = f"{self.base_url}/create_employee"
        payload = {
            "emp_id": emp_id,
            "name": name,
            "position": position,
            "salary": salary
        }
        response = self.session.post(url, json=payload)
        return self._handle_response(response)

    def remove_employee(self, emp_id: str):
        url = f"{self.base_url}/employees/{emp_id}"  # Added /api prefix
        response = self.session.delete(url)
        return self._handle_response(response)

    def promote_employee(self, emp_id: str, new_position: str, new_salary: float):
        url = f"{self.base_url}/employees/{emp_id}/promote"  # Added /api prefix
        payload = {
            "new_position": new_position,
            "new_salary": new_salary
        }
        response = self.session.put(url, json=payload)
        return self._handle_response(response)

    def display_employees(self):
        url = f"{self.base_url}/employees"  # Added /api prefix
        response = self.session.get(url)
        return self._handle_response(response)

    def add_product_version(self, environment: str, version: str, build_time: datetime):
        url = f"{self.base_url}/product_version"  # Added /api prefix
        payload = {
            "environment": environment,
            "version": version,
            "build_time": build_time.isoformat()
        }
        response = self.session.post(url, params=payload)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code in {200, 201}:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
