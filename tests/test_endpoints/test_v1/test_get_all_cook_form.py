import pytest


URL = '/api/v1/get-all-cook-form'


async def test_get_all_cook_form_success(mocker, client, sample_cook_form, sample_cook_form2):
    mock_service = mocker.patch('app.api.v1.get_all_cook_form.CookFormService.get_all_cook_form')
    mock_service.return_value = [sample_cook_form, sample_cook_form2]
    response = client.get(url=URL)
    expected_response_body = {'all_cook_forms': [
        {
            'active': True,
            'description': 'колбаска, сыр, лук, тесто',
            'title': 'pizza',
            'user_id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
        },
        {
            'active': False,
            'description': 'колбаска, сыр, лук, тесто2',
            'title': 'pizza2',
            'user_id': '9fa009ef-c9e8-4f33-a29c-d8879df07106',
        },
    ],
    }

    assert response.status_code == 200
    assert response.json() == expected_response_body

