import psycopg2
from food_sharing.data_base.db_config import db_name, user, password, host
import datetime


def create_user_table():
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                (id SERIAL PRIMARY KEY,
                                first_name varchar (30) NOT NULL,
                                last_name varchar (30) NOT NULL,
                                age integer NOT NULL,
                                city varchar (80) NOT NULL,
                                sex varchar (1) NOT NULL,
                                email varchar (120) UNIQUE NOT NULL,
                                password_hash varchar (120) NOT NULL,
                                create_date timestamp,
                                update_date timestamp)''')
            db_connect.commit()


def insert_into_users_db(fields):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            values = list(fields.values())
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            values.append(now)
            values.append(now)
            cursor.execute(f'''INSERT INTO users(
                                            first_name,
                                            last_name,
                                            age,
                                            city,
                                            sex,
                                            email,
                                            password_hash,
                                            create_date,
                                            update_date)  
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)''', values)
            db_connect.commit()


def update_user_info_in_db(fields):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            user_id = fields.pop('user_id')
            for key, value in fields.items():
                cursor.execute(f'''UPDATE users set {key} = %s where id=%s''', (value, user_id))
                db_connect.commit()


def select_password_from_users(email):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute(f'''SELECT password_hash FROM users WHERE email = %s''', (email,))
            result = cursor.fetchall()
            return result


def is_user_in_db(email):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''SELECT * FROM users where email=%s''', (email,))
            result = cursor.fetchall()
            return result


def select_id_from_users(email):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            cursor.execute('''SELECT id FROM users where email=%s''', (email,))
            result = cursor.fetchall()
            return result[0][0]
