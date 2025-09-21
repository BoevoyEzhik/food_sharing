from datetime import date as d

import pytest

from app.models.schemas.profile import ProfileUpdate


@pytest.fixture
def profile_update(date):
    return ProfileUpdate(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname",
        lastname="lastname",
        birthday=d(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
    )


async def test_profile_update(
    profile_service, mock_repo, sample_profile, profile_update
):
    mock_repo.profile_update.return_value = sample_profile

    result = await profile_service.profile_update(profile_update)

    assert result == sample_profile
    mock_repo.profile_update.assert_awaited_once_with(profile_update)
