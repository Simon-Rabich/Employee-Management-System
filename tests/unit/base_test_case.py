import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from src.main import app  # Ensure this matches your project structure

@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI app."""
    return TestClient(app)

@pytest.fixture
def mock_db_session():
    """Fixture to mock the database session."""
    return MagicMock(spec=Session)

@pytest.fixture(autouse=True)
def patch_db(mock_db_session):
    """Fixture to patch the database session globally in tests."""
    with patch('src.database.connection.get_db', return_value=mock_db_session):
        yield
