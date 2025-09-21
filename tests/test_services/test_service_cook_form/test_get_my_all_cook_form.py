import pytest
from fastapi import HTTPException

from app.models.schemas.cook_form import CookFormResponse


@pytest.mark.asyncio
async def test_get_my_all_cook_form_success(
    mock_repo, cook_form_service, sample_cook_form, sample_cook_form2
):
    test_limit = 10
    test_offset = 0

    mock_repo.get_my_all_cook_form.return_value = [sample_cook_form, sample_cook_form2]

    result = await cook_form_service.get_my_all_cook_form(
        user_id="", limit=test_limit, offset=test_offset
    )

    assert len(result) == 2
    assert all(isinstance(item, CookFormResponse) for item in result)
    mock_repo.get_my_all_cook_form.assert_awaited_once_with(
        user_id="", limit=test_limit, offset=test_offset
    )


async def test_get_my_all_cook_form_failure(mock_repo, cook_form_service):
    test_limit = 10
    test_offset = 0
    test_error = Exception("Database connection error")

    mock_repo.get_my_all_cook_form.side_effect = test_error

    with pytest.raises(HTTPException) as exc_info:
        await cook_form_service.get_my_all_cook_form(
            user_id="", limit=test_limit, offset=test_offset
        )

    assert exc_info.value.status_code == 400
    assert "Database connection error" in str(exc_info.value.detail)


async def test_get_all_my_cook_form_empty(mock_repo, cook_form_service):
    mock_repo.get_my_all_cook_form.return_value = []

    result = await cook_form_service.get_my_all_cook_form(
        user_id="", limit=10, offset=20
    )

    assert result == []
    mock_repo.get_my_all_cook_form.assert_awaited_once_with(
        user_id="", limit=10, offset=20
    )
