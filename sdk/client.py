import requests
from dtos.employee_dto import EmployeeDTO


class EmployeeManagementClient:
    def __init__(self, base_url: str = "http://localhost:8000/api"):
        self.base_url = base_url

    def add_employee(self, emp_id: str, name: str, position: str, salary: float):
        url = f"{self.base_url}/employees"
        payload = {
            "emp_id": emp_id,
            "name": name,
            "position": position,
            "salary": salary
        }
        response = requests.post(url, json=payload)

        if response.status_code == 201 and response.json()["success"]:
            return EmployeeDTO(**response.json()["result"])
        else:
            return response.json()

    def remove_employee(self, emp_id: str):
        url = f"{self.base_url}/employees/{emp_id}"
        response = requests.delete(url)

        if response.status_code == 200 and response.json()["success"]:
            return response.json()["result"]
        else:
            return response.json()

    def promote_employee(self, emp_id: str, new_position: str, new_salary: float):
        url = f"{self.base_url}/employees/{emp_id}/promote"
        payload = {
            "new_position": new_position,
            "new_salary": new_salary
        }
        response = requests.put(url, json=payload)

        if response.status_code == 200 and response.json()["success"]:
            return EmployeeDTO(**response.json()["result"])
        else:
            return response.json()

    def display_employees(self):
        url = f"{self.base_url}/employees"
        response = requests.get(url)

        if response.status_code == 200 and response.json()["success"]:
            return [EmployeeDTO(**emp) for emp in response.json()["result"]]
        else:
            return response.json()
