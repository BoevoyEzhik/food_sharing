import pytest
from fastapi import HTTPException

from app.models.schemas.cook_form import CookFormCreate


@pytest.fixture
def test_create_cook_form_info():
    return CookFormCreate(
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        title="title",
        description="description",
        active=True,
    )


async def test_create_cook_form_success(
    mock_repo, cook_form_service, test_create_cook_form_info, sample_cook_form
):
    mock_repo.create_cook_form.return_value = sample_cook_form

    result = await cook_form_service.create_cook_form(test_create_cook_form_info)

    assert result == sample_cook_form
    mock_repo.create_cook_form.assert_awaited_once_with(test_create_cook_form_info)


async def test_create_cook_form_failure(
    mock_repo, cook_form_service, test_create_cook_form_info
):
    test_error = Exception("Database error")

    mock_repo.create_cook_form.side_effect = test_error

    with pytest.raises(HTTPException) as exc_info:
        await cook_form_service.create_cook_form(test_create_cook_form_info)

    assert exc_info.value.status_code == 400
    assert str(test_error) in str(exc_info.value.detail)
    mock_repo.create_cook_form.assert_awaited_once_with(test_create_cook_form_info)
