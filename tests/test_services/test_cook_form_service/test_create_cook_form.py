import pytest
from fastapi import HTTPException

from app.models.schemas.cook_form import CookFormIn


@pytest.fixture
def test_cook_form_info():
    return CookFormIn(title='title',
                      description='description',
                      active=True)


async def test_create_cook_form_success(mock_repo, cook_form_service, test_cook_form_info, sample_cook_form):
    mock_repo.create_cook_form.return_value = sample_cook_form

    result = await cook_form_service.create_cook_form(test_cook_form_info)

    assert result == sample_cook_form
    mock_repo.create_cook_form.assert_awaited_once_with(test_cook_form_info)


async def test_create_cook_form_failure(mock_repo, cook_form_service):
    test_data = {"name": "Invalid Form"}
    test_error = Exception("Database error")

    mock_repo.create_cook_form.side_effect = test_error

    with pytest.raises(HTTPException) as exc_info:
        await cook_form_service.create_cook_form(test_data)

    assert exc_info.value.status_code == 400
    assert str(test_error) in str(exc_info.value.detail)
    mock_repo.create_cook_form.assert_awaited_once_with(test_data)