from sqlalchemy import update

from app.models.db_models.user import User


async def test_update_user_info_with_mocks(mock_session, user_repo):

    user_info = {"email": "new@example.com", 'password_hash': 'password_hash'}
    await user_repo.update_user_info('user_id', user_info)

    mock_session.execute.assert_awaited_once()

    executed_stmt = mock_session.execute.call_args[0][0]
    expected_stmt = update(User).where(id == 'user_id').values(**user_info)

    assert str(executed_stmt) == str(expected_stmt)
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()
