import pytest
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.schemas.profile import ProfileDTO


async def test_profile_create(profile_service, mock_repo, sample_profile, profile_dto):
    mock_repo.profile_create.return_value = sample_profile

    result = await profile_service.profile_create(profile_dto)

    assert result == sample_profile
    mock_repo.profile_create.assert_awaited_once_with(profile_dto)
    called_with = mock_repo.profile_create.call_args[0][0]
    assert isinstance(called_with, ProfileDTO)


async def test_profile_already_exists(profile_service, mock_repo, profile_dto):
    mock_repo.profile_create.side_effect = IntegrityError("", "", "")

    with pytest.raises(HTTPException) as exc_info:
        await profile_service.profile_create(profile_dto)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "profile already exist"


async def test_profile_create_other_error(profile_service, mock_repo, profile_dto):
    error_message = "Database connection failed"
    mock_repo.profile_create.side_effect = Exception(error_message)

    with pytest.raises(HTTPException) as exc_info:
        await profile_service.profile_create(profile_dto)

    assert exc_info.value.status_code == 405
    assert exc_info.value.detail == error_message
