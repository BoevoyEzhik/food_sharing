from flask import request, make_response, Response
from food_sharing.login_opereations.cookie import is_valid_cookie


def auth_middleware(func):
    def wrapper():
        cookie = request.cookies.get('name')
        if not cookie:
            return Response(status=401, response='Cookie not found, login please')
        if not is_valid_cookie(cookie):
            resp = make_response("удалил куки")
            resp.delete_cookie('name')
            return resp
        return func()
    wrapper.__name__ = func.__name__
    return wrapper
