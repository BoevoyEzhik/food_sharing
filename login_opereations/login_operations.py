import hashlib
import os
import re
from data_base.users_db import select_password_from_users
from flask import request
import base64


def generating_hash(password):
    salt = os.urandom(16).hex()
    key = hashlib.sha512(password.encode() + salt.encode()).hexdigest()
    result = (key + salt)[80:]
    return result


def check_password(email, password):
    hashed = select_password_from_users(email)[0][0]
    salt = hashed[48:]
    key = hashlib.sha512(password.encode() + salt.encode()).hexdigest()
    result = (key + salt)[80:]
    if hashed == result:
        return True
    return False


def is_valid_email(email):
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    return bool(re.fullmatch(regex, email))


def get_email_from_cookie(cookie):
    email_base64, sign = cookie.split('.')
    email = base64.b64decode(email_base64.encode()).decode()
    return email

