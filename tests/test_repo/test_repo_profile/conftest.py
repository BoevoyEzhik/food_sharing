from datetime import date
from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.profile import ProfileDTO
from app.repo.repo_profile import ProfileRepository


@pytest.fixture
def mock_session():
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def profile_repo(mock_session):
    return ProfileRepository(mock_session)


@pytest.fixture
def sample_profile_data():
    return ProfileDTO(
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname",
        lastname="lastname",
        birthday=date(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
    )
