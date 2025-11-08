import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_main_page():
    """Главная страница загружена успешно"""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_search_page():
    """Страница для поиска загружена успешно"""
    response = client.get("/search")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_static_files():
    response = client.get("/static/")
    assert response.status_code != 500