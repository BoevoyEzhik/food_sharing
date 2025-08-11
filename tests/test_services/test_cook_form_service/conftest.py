import pytest
from unittest.mock import AsyncMock

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import UpdateCookForm
from app.repo.repo_cook_form import CookFormRepository
from app.services.cook_form_service import CookFormService


@pytest.fixture
def mock_repo():
    return AsyncMock(spec=CookFormRepository)


@pytest.fixture
def cook_form_service(mock_repo):
    return CookFormService(repo=mock_repo)


@pytest.fixture
def sample_cook_form():
    return CookForm(user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
                    title='title',
                    description='description',
                    active=True)


@pytest.fixture
def sample_cook_form2():
    return CookForm(user_id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
                    title='title2',
                    description='description2',
                    active=False)


@pytest.fixture
def test_cook_form_info():
    return UpdateCookForm(user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
                          title='title',
                          description='description',
                          active=False)


@pytest.fixture
def test_cook_form_info2():
    return UpdateCookForm(user_id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
                          title='title2',
                          description='description2',
                          active=False)


