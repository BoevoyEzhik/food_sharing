from unittest.mock import patch, AsyncMock

import pytest
from datetime import date

from app.models.schemas.profile import UpdatedProfile


@pytest.fixture
def sample_profile_info():
    return UpdatedProfile(id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
                          firstname='firstname',
                          lastname='lastname',
                          birthday=date.today().isoformat(),
                          city='city',
                          sex='sex')


async def test_update_user_info(user_service, sample_profile_info, sample_user, mock_repo):
    expected_user_dict = sample_profile_info.dict()
    test_user_id = expected_user_dict.pop("id")
    mock_repo.update_user_info.return_value = sample_user

    result = await user_service.update_user_info(sample_profile_info)

    assert result == sample_user
    mock_repo.update_user_info.assert_awaited_once_with(
        test_user_id, expected_user_dict
    )
