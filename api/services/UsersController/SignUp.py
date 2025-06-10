import psycopg2
from rest_framework.response import Response
from decouple import config
from django.contrib.auth.hashers import make_password


class UserSignUp:
    def __init__(self,username,password):
        self.user = username
        self.password = password
    def validated_user(self):
        sql = "SELECT password FROM users WHERE username='{}'".format(self.user)
        values = (self.password,)
        conn = psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_NAME'),
            port=config('DB_PORT')
        )
        cursor = conn.cursor()
        cursor.execute(sql, values)