from rest_framework.response import Response
import psycopg2
from decouple import config

class DatabaseController:
    def __init__(self):
        self.connection_params = {
            "host": config('DB_HOST'),
            "user": config('DB_USER'),
            "password": config('DB_PASSWORD'),
            "dbname": config('DB_NAME'), 
            "port": config('DB_PORT')
        }
        self.conn = None

    def connection_database(self):
        try:
            self.conn = psycopg2.connect(**self.connection_params)
        except psycopg2.Error as e:
            return Response({'message': f'error: {e}'})

    def exec_select_sql_one_register(self, sql, values):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            return cursor.fetchone()
        except psycopg2.Error as e:
            return Response({'message': f'error: {e}'})
    def exec_insert_sql(self,sql,values):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql,values)
            self.conn.commit()
            return Response({'message': True})
        except psycopg2.Error as e:
            return Response({'message': f'error: {e}'})

    def close_connection(self):
        if self.conn:
            try:
                self.conn.close()
            except psycopg2.Error as error:
                return Response({'message': f'error: {error}'})
