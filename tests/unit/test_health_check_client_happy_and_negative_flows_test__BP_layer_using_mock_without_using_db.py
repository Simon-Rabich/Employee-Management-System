import pytest
from sdk.health_check_sdk import HealthCheckClient
from unittest.mock import patch


@pytest.fixture
def mock_base_url():
    return "http://localhost:8000"


def test_health_check_success(mock_base_url):
    # Mock the requests.post call inside HealthCheckClient
    with patch("requests.post") as mock_post:
        # Mock the response data
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "success": True,
            "result": {
                "status": "healthy",
                "version": "1.0.0",
                "build_time": "16/09/2024 18:47:49"
            }
        }

        client = HealthCheckClient(base_url=mock_base_url)
        response = client.get_health(environment="prod")

        # Assertions
        assert response.success == True
        assert response.result.status == "healthy"
        assert response.result.version == "1.0.0"
        assert response.result.build_time == "16/09/2024 18:47:49"


def test_health_check_failure(mock_base_url):
    # Mock the requests.post call inside HealthCheckClient
    with patch("requests.post") as mock_post:
        # Mock a failure response
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = {
            "success": False,
            "error": "No product version found for the specified environment"
        }

        client = HealthCheckClient(base_url=mock_base_url)
        response = client.get_health(environment="prod")

        # Assertions
        assert response.success == False
        assert response.error == "No product version found for the specified environment"
