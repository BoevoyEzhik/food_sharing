from flask import Response, request

from food_sharing.api.cook import cook_app
from food_sharing.data_base.cook_form_db import get_all_cook_form_from_db
from food_sharing.middlewares.auth_middleware import auth_middleware


@cook_app.get('/get-all-cook-form')
@auth_middleware
def get_all_cook_form():
    body_json_data = request.get_json()
    result = get_all_cook_form_from_db(body_json_data)
    return Response(result, 200)
