import psycopg2
from rest_framework import status
from rest_framework.response import Response
from decouple import config
import re
from django.contrib.auth.hashers import check_password
from api.database.DatabaseController import DatabaseController


class UserSignIn:
    def __init__(self,username,password):

        self.username_or_email = username
        self.password = password

    def exists_user(self):

        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        email = email_pattern.match(self.username_or_email)

        if email:
            sql_password = "select password from users.authenticate where email = %s;"
        else:
            sql_password = "select password from users.authenticate where username = %s;"
        try:
            with DatabaseController as db:
                db_password = db.exec_select_sql_one_register(
                    sql=sql_password,
                    values=(self.username_or_email))
                
                if db_password is None:
                    return Response({'message': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    if check_password(self.password, db_password[0]):
                        return Response({'message': 'login successful'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'message': 'user,email or password invalid'}, status=status.HTTP_404_NOT_FOUND)
                    
        except psycopg2.errors as error:
            return Response({'message':f'{error}'})
            
