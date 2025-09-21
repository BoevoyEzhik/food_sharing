from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from app.models.db_models.user import User

URL = "/auth/register"
now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


@pytest.fixture
def sample_user():
    return User(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        email="example@example.com",
        password_hash="hashed_password",
        created_at=now,
        updated_at=now,
    )


async def test_register_user_success(mocker, client, sample_user):
    json_body = {"email": "example@example.com", "password": "test_password"}
    mock_service = mocker.patch(
        "app.api.auth.register.UserService.register_user",
        new_callable=AsyncMock,
        return_value=sample_user,
    )
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 200
    mock_service.assert_awaited_once()
    assert response.json() == {
        "id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "email": "example@example.com",
        "password_hash": "hashed_password",
        "created_at": now,
        "updated_at": now,
    }


async def test_register_invalid_email(client):
    response = client.post(URL, json={"email": "invalid", "password": "123"})
    assert response.status_code == 422


async def test_register_wrong_type_body(client):
    json_body = {"email": "example@example.com", "password": 123}
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422


async def test_register_empty_body(client):
    json_body = {}
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422
