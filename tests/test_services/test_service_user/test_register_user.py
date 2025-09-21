import pytest
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.schemas.register import Register, RegisterRequest


@pytest.fixture
def sample_user_info():
    return RegisterRequest(email="test@example.com", password="password123")


async def test_register_user_success(
    user_service, mock_repo, sample_user_info, sample_user
):
    mock_repo.register_user.return_value = sample_user
    result = await user_service.register_user(sample_user_info)
    assert result == sample_user

    mock_repo.register_user.assert_awaited_once()
    called_with = mock_repo.register_user.call_args[0][0]
    assert isinstance(called_with, Register)
    assert called_with.email == sample_user_info.email
    assert called_with.password_hash is not None


async def test_register_user_already_exists(user_service, mock_repo, sample_user_info):
    mock_repo.register_user.side_effect = IntegrityError("", "", "")

    with pytest.raises(HTTPException) as exc_info:
        await user_service.register_user(sample_user_info)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "user already exist"


async def test_register_user_other_error(user_service, mock_repo, sample_user_info):
    error_message = "Database connection failed"
    mock_repo.register_user.side_effect = Exception(error_message)

    with pytest.raises(HTTPException) as exc_info:
        await user_service.register_user(sample_user_info)

    assert exc_info.value.status_code == 405
    assert exc_info.value.detail == error_message
