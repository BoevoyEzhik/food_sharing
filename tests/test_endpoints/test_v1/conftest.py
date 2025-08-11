import pytest

from app.models.db_models.cook_form import CookForm


@pytest.fixture
def sample_cook_form():
    return CookForm(user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
                    title='pizza',
                    description='колбаска, сыр, лук, тесто',
                    active=True)


@pytest.fixture
def sample_cook_form2():
    return CookForm(user_id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
                    title='pizza2',
                    description='колбаска, сыр, лук, тесто2',
                    active=False)
