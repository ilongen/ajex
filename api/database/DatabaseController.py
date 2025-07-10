import psycopg2
from decouple import config

class DatabaseController:
    def __init__(self):
        self.connection_params = psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_NAME'),
            port=config('DB_PORT')
        )
        self.cursor = self.connection_params.cursor()  
        
    
    def exec_select_sql_all_register(self,sql,values):
        try:
            self.cursor.execute(sql, values)
            return self.cursor.fetchall()  
        except psycopg2.Error as e:        
            print(e)
            return None

    def exec_select_sql_one_register(self,sql,values):
        try:
            self.cursor.execute(sql, values)
            return self.cursor.fetchone()  
        except psycopg2.Error as e:        
            print(e)
            return None
    
    def close_conn_and_cursor(self):
        try:
            self.cursor.close()           
            self.connection_params.close() 
        except psycopg2.Error as error:    
            print(error)