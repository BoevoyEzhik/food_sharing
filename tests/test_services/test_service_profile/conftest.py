from datetime import date as d
from unittest.mock import AsyncMock

import pytest

from app.models.db_models.profile import Profile
from app.models.schemas.profile import ProfileDTO
from app.repo.repo_profile import ProfileRepository
from app.services.service_profile import ProfileService


@pytest.fixture
def mock_repo():
    return AsyncMock(spec=ProfileRepository)


@pytest.fixture
def profile_service(mock_repo):
    return ProfileService(repo=mock_repo)


@pytest.fixture
def sample_profile(date):
    return Profile(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
        firstname="firstname",
        lastname="lastname",
        birthday=d.today().isoformat(),
        city="city",
        sex="sex",
        created_at=date,
        updated_at=date,
    )


@pytest.fixture
def profile_dto(date):
    return ProfileDTO(
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname",
        lastname="lastname",
        birthday=d(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
    )
