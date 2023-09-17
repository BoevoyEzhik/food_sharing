import psycopg2
from data_base.db_config import db_name, user, password, host


def create_cook_form_table():
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS CookForm
                                (id SERIAL PRIMARY KEY,
                                user_id INT NOT NULL,
                                title varchar (120) NOT NULL,
                                description varchar (3000) NOT NULL,
                                active bool NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES users (id)
                                )''')
            db_connect.commit()


def insert_into_cook_form_db(fields):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            values = tuple(fields.values())
            cursor.execute(f'''INSERT INTO CookForm (
                                user_id,
                                title,
                                description,
                                active)  VALUES(%s, %s, %s, %s)''', values)
            db_connect.commit()


def update_cook_form_info(fields):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            user_id = fields.pop('user_id')
            for key, value in fields.items():
                cursor.execute(f'''UPDATE CookForm set {key} = %s where user_id=%s''', (value, user_id))
                db_connect.commit()


def get_my_all_cook_form_from_db(fields):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            user_id = fields['user_id']
            count = fields['count']
            cursor.execute('''SELECT * FROM CookForm WHERE user_id = %s''', user_id)
            select_result = cursor.fatchmany(count)
            names = ['id', 'user_id', 'title', 'description', 'active']
            result = {}
            for args in select_result:
                new_dict = dict(zip(names, args))
                result[new_dict['title']] = new_dict
            return result


def get_all_cook_form_from_db(fields):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            count = fields['count']
            cursor.execute('''SELECT * FROM CookForm LIMIT %s''', (count,))
            result = cursor.fetchall()
            return result
