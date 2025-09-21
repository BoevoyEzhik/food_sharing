from typing import Sequence
from unittest.mock import MagicMock

from app.models.db_models.cook_form import CookForm


async def test_basic_functionality(mock_session, cook_form_repo):
    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [CookForm(), CookForm()]
    mock_result.scalars.return_value = mock_scalars
    mock_session.execute.return_value = mock_result

    result = await cook_form_repo.get_all_cook_form(limit=5, offset=2)

    assert isinstance(result, Sequence)
    assert all(isinstance(item, CookForm) for item in result)
    assert len(result) == 2
    mock_session.execute.assert_awaited_once()

    executed_query = mock_session.execute.call_args[0][0]
    assert executed_query._limit == 5
    assert executed_query._offset == 2
    assert hasattr(executed_query, "whereclause")


async def test_with_default_values(mock_session, cook_form_repo):
    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [CookForm()]
    mock_result.scalars.return_value = mock_scalars
    mock_session.execute.return_value = mock_result

    result = await cook_form_repo.get_all_cook_form()

    assert len(result) == 1
    executed_query = mock_session.execute.call_args[0][0]
    assert executed_query._limit == 1
    assert executed_query._offset == 10
    assert hasattr(executed_query, "whereclause")
