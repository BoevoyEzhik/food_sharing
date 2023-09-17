from flask import Flask, request, make_response, Response
from data_base.users_db import *
from data_base.cook_form_db import *
from login_opereations.login_operations import generating_hash, check_password, is_valid_email, get_email_from_cookie
from login_opereations.cookie import create_login_cookie
from middlewares.auth_middleware import auth_middleware


app = Flask(__name__)


@app.route('/register')
def register():
    body_json_data = request.get_json()
    if not is_valid_email(body_json_data['email']):
        return Response(status='403', response='Incorrect email format')
    if not 18 < body_json_data['age'] < 120:
        return Response(status='403', response='Age error')
    body_json_data['password_hash'] = generating_hash(body_json_data['password_hash'])
    insert_into_users_db(body_json_data)
    return Response(status=200, response='Successfully registration')


@app.route('/login')
def login():
    body_json_data = request.get_json()
    if not is_user_in_db(body_json_data['email']):
        return Response(status=403, response='User not found')
    if check_password(body_json_data['email'], body_json_data['password']):
        login_cookie = create_login_cookie(body_json_data['email'])
        res = make_response('setting cookies')
        res.set_cookie('name', login_cookie, max_age=60 * 60 * 24 * 365 * 2)
        return res
    return Response(status=403, response='Incorrect email or password')


@app.route('/logout')
def logout():
    resp = make_response()
    cookies = request.cookies
    for cookie in cookies:
        resp.delete_cookie(cookie)
    return resp


@app.route('/api/v1/update-user-info')
@auth_middleware
def update_user_info():
    body_json_data = request.get_json()
    my_dict = {"user_id": ''}
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    my_dict['user_id'] = select_id_from_users(email)
    my_dict.update(body_json_data)
    update_user_info_in_db(my_dict)
    return Response('Обновил табличку юзерс', status=200)


@app.route('/api/v1/create-cook-form')
@auth_middleware
def create_cook_form():
    body_json_data = request.get_json()
    my_dict = {"user_id": ''}
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    my_dict['user_id'] = select_id_from_users(email)
    my_dict.update(body_json_data)
    insert_into_cook_form_db(my_dict)
    return Response("Вставил блюдо", status=200)


@app.route('/api/v1/update-cook-form')
@auth_middleware
def update_cook_form():
    body_json_data = request.get_json()
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    body_json_data['user_id'] = select_id_from_users(email)
    update_cook_form_info(body_json_data)
    return Response("Обновил блюдо", status=200)


@app.route('/api/v1/get-my-all-cook-form')
@auth_middleware
def get_my_all_cook_form():
    body_json_data = request.get_json()
    my_dict = {"user_id": ''}
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    my_dict['user_id'] = select_id_from_users(email)
    my_dict.update(body_json_data)
    result = get_my_all_cook_form_from_db(my_dict)
    return Response(status=200, response=result)


@app.route('/api/v1/get-all-cook-form')
@auth_middleware
def get_all_cook_form():
    body_json_data = request.get_json()
    result = get_all_cook_form_from_db(body_json_data)
    return Response(result, 200)


if __name__ == '__main__':
    create_user_table()
    create_cook_form_table()
    app.run(port=5001)

