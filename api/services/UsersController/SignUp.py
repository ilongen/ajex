import psycopg2
from rest_framework.response import Response
from decouple import config
from django.contrib.auth.hashers import make_password

class UserSignUp:
    def __init__(self, user_name, user_password, user_email, user_first_name, user_last_name, data_joined):
        self.user_name = user_name.strip() if user_name else None
        self.user_password = user_password.strip() if user_password else None
        self.user_email = user_email.strip() if user_email else None
        self.user_first_name = user_first_name.strip() if user_first_name else ''
        self.user_last_name = user_last_name.strip() if user_last_name else ''
        self.data_joined = data_joined

    def rules(self):
        if not self.user_password or len(self.user_password) < 8:
            return Response({'error': 'Password is too short'}, status=400)
        if not self.user_email or '@' not in self.user_email or len(self.user_email) < 5:
            return Response({'error': 'Invalid email'}, status=400)
        if not self.user_name or len(self.user_name) < 3:
            return Response({'error': 'Username is too short'}, status=400)
        return Response({'success': 'All fields are valid'}, status=200)

    def insert_data_in_db(self):
        sql = """
        INSERT INTO public.auth_user
        (password, username, first_name, last_name, email, date_joined)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        hashed_password = make_password(self.user_password)

        values = (
            hashed_password,
            self.user_name,
            self.user_first_name,
            self.user_last_name,
            self.user_email,
            self.data_joined
        )

        try:
            conn = psycopg2.connect(
                host=config('DB_HOST'),
                user=config('DB_USER'),
                password=config('DB_PASSWORD'),
                database=config('DB_NAME'),
                port=config('DB_PORT')
            )
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'success': 'User inserted successfully'}, status=201)
