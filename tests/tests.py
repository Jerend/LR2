import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.steam_service import SteamDataService

client = TestClient(app)

def test_main_page():
    """Главная страница загружена успешно"""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_steam_service_initialization():
    """Проверить инициализацию службы steam"""
    service = SteamDataService("79DCEEEC80EB29431B88CA479CA11E56")
    assert service is not None
    assert hasattr(service, 'get_featured_games')
    assert hasattr(service, 'search_games')