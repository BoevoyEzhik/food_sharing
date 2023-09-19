from flask import request, Response

from food_sharing.api.cook import cook_app
from food_sharing.data_base.cook_form_db import update_cook_form_info
from food_sharing.data_base.users_db import select_id_from_users

from food_sharing.login_opereations.login_operations import get_email_from_cookie
from food_sharing.middlewares.auth_middleware import auth_middleware


@cook_app.put('/update-cook-form')
@auth_middleware
def update_cook_form():
    body_json_data = request.get_json()
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    body_json_data['user_id'] = select_id_from_users(email)
    update_cook_form_info(body_json_data)
    return Response("Обновил блюдо", status=200)
