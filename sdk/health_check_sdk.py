import requests
from dtos.health_check_dto import HealthCheckDTO  # Import from your dtos folder
from dtos.response_dto import ResponseDTO  # Import from your dtos folder


class HealthCheckClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_health(self, environment: str) -> ResponseDTO:
        try:
            # Use POST request with the environment as a parameter in the body
            response = requests.post(f"{self.base_url}/health", json={"environment": environment})
            response.raise_for_status()
            response_data = response.json()

            print(response_data)  # For debugging purposes

            if response_data.get("success"):
                result_data = HealthCheckDTO(**response_data.get("result", {}))
                return ResponseDTO(success=True, result=result_data)
            else:
                return ResponseDTO(success=False, error=response_data.get("error"))
        except requests.RequestException as req_error:
            return ResponseDTO(success=False, error=str(req_error))
        except Exception as e:
            return ResponseDTO(success=False, error=str(e))


# Example usage
if __name__ == "__main__":
    base_url = "http://localhost:8000"  # Adjust to your FastAPI URL
    client = HealthCheckClient(base_url=base_url)

    # Provide an environment for the health check (e.g., "prod", "dev", "stg")
    environment = "prod"
    health_response = client.get_health(environment=environment)

    if health_response.success:
        print(f"Service is {health_response.result.status}")
        print(f"Version: {health_response.result.version}")
        if health_response.result.build_time:
            print(f"Build Time: {health_response.result.build_time}")
        else:
            print("Build Time: Not available")
    else:
        print(f"Error: {health_response.error}")
