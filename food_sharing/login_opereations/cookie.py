import hmac
import hashlib
import base64

from food_sharing.config import config


def sign_data(data: str) -> str:
    return hmac.new(config.session_secret_key.encode(),
                    msg=data.encode(),
                    digestmod=hashlib.sha256
                    ).hexdigest().upper()


def create_login_cookie(email: str):
    email_signed = base64.b64encode(email.encode()).decode() + "." + sign_data(email)
    return email_signed


def is_valid_cookie(cookie):
    try:
        email_base64, sign = cookie.split('.')
        email = base64.b64decode(email_base64.encode()).decode()
        valid_sign = sign_data(email)
        result = hmac.compare_digest(valid_sign, sign)
    except:
        return False
    return result
