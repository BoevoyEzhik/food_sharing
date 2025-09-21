from unittest.mock import AsyncMock

import pytest

from app.models.schemas.tokendto import TokenDTO

URL = "/auth/login"


@pytest.fixture
def sample_token():
    return TokenDTO(token="token")


async def test_login_user_success(mocker, client, sample_token):
    mock_service = mocker.patch(
        "app.api.auth.register.UserService.authenticate_user",
        new_callable=AsyncMock,
        return_value=sample_token,
    )
    json_body = {"email": "example@example.com", "password": "test_password"}
    response = client.post(url=URL, json=json_body)
    mock_service.assert_awaited_once()
    assert response.status_code == 200
    assert response.json() == {"token": "token", "token_type": "Bearer"}


async def test_login_wrong_email(client):
    json_body = {"email": "123.com", "password": "test_password"}
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422


async def test_login_wrong_type_body(client):
    json_body = {"email": "example@example.com", "password": 123}
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422


async def test_login_empty_body(client):
    json_body = {}
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422
