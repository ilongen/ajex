from django.db import connection
from django.http import JsonResponse

"""
    TODO:
    
    Testar insert totalmente funcionando via API
"""
class DBSQL:
    def sql_insert_data(email,password,username):
        sql = """INSERT INTO users (user_email,user_name,user_password) VALUES (?,?,?)"""
        values = (email,password,username)
        cursor = connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        JsonResponse({"status": "success", "message": "Data Inserted", "data": None})