URL = "/api/v1/get-all-cook-form"


async def test_get_all_cook_form_success(
    mocker, client, cook_form_response, all_cook_forms, cook_form_response_list
):
    mock_service = mocker.patch(
        "app.api.v1.get_all_cook_form.CookFormService.get_all_cook_form"
    )
    mock_service.return_value = cook_form_response_list
    response = client.get(url=URL)

    cook_form_response.model_dump(mode="json")

    assert response.status_code == 200
    assert response.json() == all_cook_forms
