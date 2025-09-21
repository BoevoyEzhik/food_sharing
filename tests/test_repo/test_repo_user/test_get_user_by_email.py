from unittest.mock import AsyncMock, Mock

from sqlalchemy import select

from app.models.db_models.user import User


async def test_get_user_by_email_exist_user(mock_session, user_repo):
    test_email = "test@example.com"
    test_user = User(email=test_email)

    mock_result = AsyncMock()
    mock_result.scalar_one_or_none = Mock(return_value=test_user)
    mock_session.execute.return_value = mock_result

    result = await user_repo.get_user_by_email(test_email)

    assert result == test_user

    args, _ = mock_session.execute.call_args
    executed_query = args[0]

    expected_query = select(User).where(User.email == test_email)

    assert str(executed_query) == str(expected_query)


async def test_get_user_by_email_none(mock_session, user_repo):
    test_email = ""

    mock_result = AsyncMock()
    mock_result.scalar_one_or_none = Mock(return_value=None)
    mock_session.execute.return_value = mock_result

    result = await user_repo.get_user_by_email(test_email)

    assert result is None

    args, _ = mock_session.execute.call_args
    executed_query = args[0]

    expected_query = select(User).where(User.email == test_email)

    assert str(executed_query) == str(expected_query)
