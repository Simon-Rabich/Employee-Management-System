# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from src.main import app  # Update this import based on your actual project structure

@pytest.fixture
def client():
    """Fixture to create a test client for FastAPI app."""
    return TestClient(app)
