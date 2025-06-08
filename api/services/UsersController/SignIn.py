from multiprocessing import connection

import psycopg2
from django.contrib import postgres
from rest_framework.response import Response
from decouple import config

class UserSignIn:
    def __init__(self, user_name, user_password, user_email):
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email

    def rules(self):
        if len(self.user_password) < 8:
            return Response({'error': 'Password is too short'}, status=400)
        elif '@' not in self.user_email or len(self.user_email) < 5:
            return Response({'error': 'Invalid email'}, status=400)
        elif len(self.user_name) < 3:
            return Response({'error': 'Username is too short'}, status=400)
        else:
            return Response({'success': 'All fields are valid'}, status=200)
    def insert_data_in_db(self):
        sql="INSERT INTO users (user_name, user_password, user_email) VALUES (%s, %s, %s)"
        conn = psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_NAME'),
            port=config('DB_PORT')
        )
        cursor = conn.cursor()
        cursor.execute(sql, (self.user_name, self.user_password, self.user_email))
        cursor.close()
