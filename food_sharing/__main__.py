from flask import Flask, Blueprint

from food_sharing.api.auth import auth_app
from food_sharing.api.cook import cook_app
from food_sharing.api.user import user_app
from food_sharing.data_base.users_db import create_user_table
from food_sharing.data_base.cook_form_db import create_cook_form_table

v1 = Blueprint('v1', __name__)
v1.register_blueprint(user_app, url_prefix='/user')
v1.register_blueprint(cook_app, url_prefix='/cook')

api_app = Blueprint('api', __name__)
api_app.register_blueprint(v1, url_prefix='/v1')

main_app = Flask(__name__)
main_app.register_blueprint(auth_app, url_prefix='/')
main_app.register_blueprint(api_app, url_prefix='/api')

if __name__ == '__main__':
    create_user_table()
    create_cook_form_table()
    main_app.run(port=5001)
