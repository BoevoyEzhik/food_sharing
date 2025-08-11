import pytest
from unittest.mock import AsyncMock

from app.repo.repo_user import UserRepository
from app.services.user_service import UserService
from app.models.db_models.user import User


@pytest.fixture
def mock_repo():
    return AsyncMock(spec=UserRepository)


@pytest.fixture
def user_service(mock_repo):
    return UserService(repo=mock_repo)


@pytest.fixture
def sample_user():
    return User(id='9fa009ef-c9e8-4f33-a29c-d8879df07107',
                email="test@example.com",
                password_hash='hashed_password')