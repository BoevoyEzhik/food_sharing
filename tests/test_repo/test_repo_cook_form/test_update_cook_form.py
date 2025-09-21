import pytest
from fastapi import HTTPException

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormUpdate

cook_form_update = CookFormUpdate(
    id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
    title="string",
    description="string",
    active=True,
)


async def test_update_cook_form_success(mock_session, cook_form_repo, sample_cook_form):
    mock_session.get.return_value = sample_cook_form

    result = await cook_form_repo.update_cook_form(cook_form_update)

    assert result == sample_cook_form

    mock_session.get.assert_awaited_once_with(CookForm, cook_form_update.id)
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once_with(sample_cook_form)


async def test_update_cook_form_not_found(mock_session, cook_form_repo):

    mock_session.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await cook_form_repo.update_cook_form(cook_form_update)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "cook not created"

    mock_session.commit.assert_not_awaited()
    mock_session.refresh.assert_not_awaited()
