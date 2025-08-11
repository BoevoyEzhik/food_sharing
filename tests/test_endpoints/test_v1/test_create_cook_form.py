import pytest


URL = 'api/v1/create-cook-form'


async def test_create_cook_form_success(mocker, client, sample_cook_form):
    mock_service = mocker.patch('app.api.v1.create_cook_form.CookFormService.create_cook_form')
    mock_service.return_value = sample_cook_form
    json_body = {'title': 'pizza',
                 'description': 'колбаска, сыр, лук, тесто',
                 'active': True}
    response = client.post(url=URL,
                           json=json_body)
    assert response.status_code == 200
    assert response.json() == {'user_id': "9fa009ef-c9e8-4f33-a29c-d8879df07107",
                               'title': 'pizza',
                               'description': 'колбаска, сыр, лук, тесто',
                               'active': True}


async def test_create_cook_form_wrong_type_body(client):
    json_body = {'title': 123,
                 'description': 'колбаска, сыр, лук, тесто',
                 'active': True}
    response = client.post(url=URL,
                           json=json_body)
    assert response.status_code == 422


async def test_create_cook_form_empty_body(client):
    json_body = {}
    response = client.post(url=URL,
                           json=json_body)
    assert response.status_code == 422


