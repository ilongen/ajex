from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from api.database.DatabaseController import DatabaseController


class UserSignUp:
    def __init__(self, user_name, user_password, user_email,date_joined):
        self.user_name = user_name.strip() if user_name else None
        self.user_password = user_password.strip() if user_password else None
        self.user_email = user_email.strip() if user_email else None
        self.date_joined = date_joined
       
    def rules(self):
        if not self.user_password or len(self.user_password) < 8:
            return Response({'error': 'Password is too short'}, status=400)
        if not self.user_email or '@' not in self.user_email or len(self.user_email) < 5:
            return Response({'error': 'Invalid email'}, status=400)
        if not self.user_name or len(self.user_name) < 3:
            return Response({'error': 'Username is too short'}, status=400)
        return Response({'success': 'All fields are valid'}, status=200)

    def validation_user_in_db(self):
        select_query = """
            SELECT username,email FROM users.authenticate WHERE username = %s or email = %s
        """
        values = (self.user_name,
                  self.user_email)
        controller = DatabaseController()
        controller.connection_database()
        result_query = controller.exec_select_sql_one_register(sql=select_query,values=values)
        controller.close_connection()
        if result_query is None:
            return Response({'error': 'Not user exists'},status=202)
        else:
            return Response({'sucess': 'Username or email exists'},status=409)


    def insert_data_in_db(self):
        insert_query = """
            INSERT INTO users.authenticate
            (username, password, email, created_at)
            VALUES (%s, %s, %s, %s);
        """
        hashed_password = make_password(self.user_password)

        values = (
            self.user_name,
            hashed_password,
            self.user_email,
            self.date_joined,
        )

        try:
            controller = DatabaseController()
            controller.connection_database()
            controller.exec_insert_sql(sql=insert_query,values=values)
            controller.close_connection()
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'success': 'User created successfully'}, status=201)
