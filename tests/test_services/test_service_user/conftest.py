from unittest.mock import AsyncMock

import pytest

from app.models.db_models.user import User
from app.repo.repo_user import UserRepository
from app.services.service_user import UserService


@pytest.fixture
def mock_repo():
    return AsyncMock(spec=UserRepository)


@pytest.fixture
def user_service(mock_repo):
    return UserService(repo=mock_repo)


@pytest.fixture
def sample_user(date):
    return User(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        email="test@example.com",
        password_hash="hashed_password",
        created_at=date,
        updated_at=date,
    )
