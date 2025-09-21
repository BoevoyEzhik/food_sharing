from unittest.mock import AsyncMock, patch

import pytest
from fastapi import HTTPException

from app.models.schemas.login import Login
from app.models.schemas.tokendto import TokenDTO


@pytest.fixture
def sample_login():
    return Login(email="test@example.com", password="password123")


async def test_authenticate_user_success(
    user_service, mock_repo, sample_login, sample_user
):
    mock_repo.get_user_by_email.return_value = sample_user

    with patch(
        "app.services.utils.Password.is_valid_password",
        new_callable=AsyncMock,
        return_value=True,
    ):
        with patch(
            "app.core.jwt_tokens.Token.create_jwt_token",
            new_callable=AsyncMock,
            return_value="generated_token",
        ):

            result = await user_service.authenticate_user(sample_login)

    assert result == TokenDTO(token="generated_token")
    mock_repo.get_user_by_email.assert_awaited_once_with(sample_login.email)


async def test_authenticate_user_not_found(user_service, mock_repo, sample_login):
    mock_repo.get_user_by_email.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await user_service.authenticate_user(sample_login)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "user not registered"


async def test_authenticate_user_wrong_password(
    user_service, mock_repo, sample_login, sample_user
):
    mock_repo.get_user_by_email.return_value = sample_user

    with patch(
        "app.services.utils.Password.is_valid_password",
        new_callable=AsyncMock,
        return_value=False,
    ):
        with pytest.raises(HTTPException) as exc_info:
            await user_service.authenticate_user(sample_login)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "wrong password"
