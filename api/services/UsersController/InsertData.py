from django.db import connection
from django.http import JsonResponse

class InsertData:
    """
        TODO:

        Tester insert entailment functional via API
    """
    def sql_insert_data(email,password,username):
        sql = """INSERT INTO users (user_email,user_name,user_password) VALUES (?,?,?)"""
        values = (email,password,username)
        cursor = connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        JsonResponse({"status": "success", "message": "Data Inserted", "data": None})