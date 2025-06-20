import psycopg2
from rest_framework import status
from rest_framework.response import Response
from decouple import config
import re
from django.contrib.auth.hashers import check_password


class UserSignIn:
    def __init__(self,username,password):
        self.username_or_email = username
        self.password = password
    def exists_user(self):
        conn = psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_NAME'),
            port=config('DB_PORT')
        )
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        email = email_pattern.match(self.username_or_email)
        if email:
            sql_password = "select password from public.auth_user where email = %s;"
        else:
            sql_password = "select password from public.auth_user where username = %s;"
        cursor = conn.cursor()
        cursor.execute(sql_password, (self.username_or_email,))
        db_password = cursor.fetchone()
        if db_password is None:
            return Response({'message': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            if check_password(self.password, db_password[0]):
                return Response({'message': 'login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'user,email or password invalid'}, status=status.HTTP_404_NOT_FOUND)
