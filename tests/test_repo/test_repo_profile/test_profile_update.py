from datetime import date as d

import pytest
from fastapi import HTTPException

from app.models.db_models.profile import Profile
from app.models.schemas.profile import ProfileUpdate


@pytest.fixture
def sample_profile_update_data():
    return ProfileUpdate(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname2",
        lastname="lastname2",
        birthday=d(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
    )


@pytest.fixture
def sample_profile(date):
    return Profile(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname",
        lastname="lastname",
        birthday=d(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
        created_at=date,
        updated_at=date,
    )


async def test_profile_update_success(
    profile_repo, mock_session, sample_profile, sample_profile_update_data
):

    mock_session.get.return_value = sample_profile
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None

    result = await profile_repo.profile_update(sample_profile_update_data)

    assert result is sample_profile

    assert str(result.user_id) == str(sample_profile.user_id)

    assert result.firstname == "firstname2"
    assert result.lastname == "lastname2"

    mock_session.get.assert_awaited_once_with(Profile, sample_profile_update_data.id)
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once_with(sample_profile)


async def test_profile_update_not_found(
    profile_repo, mock_session, sample_profile_update_data
):

    mock_session.get.return_value = None
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await profile_repo.profile_update(sample_profile_update_data)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "profile not created"

    mock_session.get.assert_awaited_once_with(Profile, sample_profile_update_data.id)
    mock_session.commit.assert_not_awaited()
    mock_session.refresh.assert_not_awaited()
