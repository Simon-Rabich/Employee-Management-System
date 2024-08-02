import requests


class EmployeeManagementClient:
    def __init__(self, base_url: str):
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
        return response.json()

    def remove_employee(self, emp_id: str):
        url = f"{self.base_url}/employees/{emp_id}"
        response = requests.delete(url)
        return response.json()

    def promote_employee(self, emp_id: str, new_position: str, new_salary: float):
        url = f"{self.base_url}/employees/{emp_id}/promote"
        payload = {
            "new_position": new_position,
            "new_salary": new_salary
        }
        response = requests.put(url, json=payload)
        return response.json()

    def display_employees(self):
        url = f"{self.base_url}/employees"
        response = requests.get(url)
        return response.json()
