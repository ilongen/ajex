from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from api.database.DatabaseController import DatabaseController
from datetime import datetime


class UserSignUp:
    def __init__(self, user_name, user_password, user_email, user_first_name='', user_last_name='', date_joined=None):
        self.user_name = user_name.strip() if user_name else None
        self.user_password = user_password.strip() if user_password else None
        self.user_email = user_email.strip() if user_email else None
        self.user_first_name = user_first_name.strip() if user_first_name else ''
        self.user_last_name = user_last_name.strip() if user_last_name else ''
        self.date_joined = datetime.now()
        self.updated_at = datetime.now()
        self.last_login = None
        self.is_active = True
        self.is_verified = False

    def rules(self):
        if not self.user_password or len(self.user_password) < 8:
            return Response({'error': 'Password is too short'}, status=400)
        if not self.user_email or '@' not in self.user_email or len(self.user_email) < 5:
            return Response({'error': 'Invalid email'}, status=400)
        if not self.user_name or len(self.user_name) < 3:
            return Response({'error': 'Username is too short'}, status=400)
        return Response({'success': 'All fields are valid'}, status=200)

    def insert_data_in_db(self):
        insert_query = """
            INSERT INTO users.authenticate
            (username, "password", email, is_active, is_verified, created_at, updated_at, last_login)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        hashed_password = make_password(self.user_password)

        values = (
            self.user_name,
            hashed_password,
            self.user_email,
            self.is_active,
            self.is_verified,
            self.date_joined,
            self.updated_at,
            self.last_login
        )

        try:
            controller = DatabaseController()
            controller.connection_database()
            controller.exec_insert_sql(sql=insert_query,values=values)
            controller.close_connection()
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'success': 'User created successfully'}, status=201)
