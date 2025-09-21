from unittest.mock import MagicMock
from uuid import uuid4

from app.models.db_models.cook_form import CookForm


async def test_get_my_all_cook_form_all_parameters(mock_session, cook_form_repo):
    user_id = uuid4()
    limit = 15
    offset = 25

    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [CookForm()]

    mock_result = MagicMock()
    mock_result.scalars.return_value = mock_scalars

    mock_session.execute.return_value = mock_result

    result = await cook_form_repo.get_my_all_cook_form(
        user_id=user_id, limit=limit, offset=offset
    )

    assert len(result) == 1
    mock_session.execute.assert_awaited_once()

    executed_query = mock_session.execute.call_args[0][0]
    assert executed_query._limit == limit
    assert executed_query._offset == offset
    assert hasattr(executed_query, "whereclause")


async def test_get_my_all_cook_form_empty_for_user(mock_session, cook_form_repo):
    user_id = uuid4()

    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = []
    mock_result.scalars.return_value = mock_scalars
    mock_session.execute.return_value = mock_result

    result = await cook_form_repo.get_my_all_cook_form(user_id=user_id)

    assert result == []
    assert len(result) == 0
    mock_session.execute.assert_awaited_once()

    executed_query = mock_session.execute.call_args[0][0]
    assert hasattr(executed_query, "whereclause")


async def test_get_my_all_cook_form_default_parameters(mock_session, cook_form_repo):
    user_id = uuid4()

    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [CookForm()]

    mock_result = MagicMock()
    mock_result.scalars.return_value = mock_scalars

    mock_session.execute.return_value = mock_result

    result = await cook_form_repo.get_my_all_cook_form(user_id=user_id)

    assert len(result) == 1
    mock_session.execute.assert_awaited_once()

    executed_query = mock_session.execute.call_args[0][0]
    assert executed_query._limit == 1
    assert executed_query._offset == 10
    assert hasattr(executed_query, "whereclause")
