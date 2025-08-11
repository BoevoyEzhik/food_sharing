import pytest

from fastapi import HTTPException


async def test_update_cook_form_success(cook_form_service, mock_repo, test_cook_form_info):
    test_form = test_cook_form_info
    expected_result = test_cook_form_info
    mock_repo.update_cook_form.return_value = expected_result

    result = await cook_form_service.update_cook_form(test_form)

    assert result == expected_result
    mock_repo.update_cook_form.assert_awaited_once_with(
        test_cook_form_info.user_id,
        {"title": "title", "description": "description", "active": False}
    )


async def test_update_cook_form_failure(cook_form_service, mock_repo, test_cook_form_info):
    test_error = Exception("Database error")
    mock_repo.update_cook_form.side_effect = test_error

    with pytest.raises(HTTPException) as exc_info:
        await cook_form_service.update_cook_form(test_cook_form_info)

    assert exc_info.value.status_code == 400
    assert "Database error" in str(exc_info.value.detail)