from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormCreate


async def test_create_cook_form(mock_session, cook_form_repo):
    cook_form_data = CookFormCreate(
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        title="string",
        description="string",
        active=True,
    )

    result = await cook_form_repo.create_cook_form(cook_form_data)

    assert isinstance(result, CookForm)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once_with(result)
