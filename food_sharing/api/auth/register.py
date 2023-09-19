from flask import request, Response

from food_sharing.api.auth import auth_app
from food_sharing.data_base.users_db import *
from food_sharing.login_opereations.login_operations import generating_hash, is_valid_email


@auth_app.post('/register')
def register():
    body_json_data = request.get_json()
    if not is_valid_email(body_json_data['email']):
        return Response(status='403', response='Incorrect email format')
    if not 18 < body_json_data['age'] < 120:
        return Response(status='403', response='Age error')
    body_json_data['password_hash'] = generating_hash(body_json_data['password_hash'])
    insert_into_users_db(body_json_data)
    return Response(status=200, response='Successfully registration')