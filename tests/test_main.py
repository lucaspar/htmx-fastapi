"""Tests for the main route."""

from fastapi import status
from fastapi.testclient import TestClient

from src.config import settings
from src.main import app

client = TestClient(
    app,
    base_url=settings.url_base,
)


def test_read_main() -> None:
    """Tests the main route."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "HTMX" in response.text
