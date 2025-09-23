import pandas as pd
from rest_framework import status
from rest_framework.response import Response


"""
-> Classe usuário que fará input do seu dado para transformação, aqui pegará o nome e o arquivo para manipular
-> em outro local
"""

class DataSheet:

    def __init__(self, data_file,data_name):
        self.data = data_file
        self.name = data_name

    def get_data(self):
        data = self.data
        name = self.name
        return data,name
        

    def set_data(self,data_file,name_file):
        self.data = data_file
        self.name = name_file
        return True
    
    def is_data(self):
        try:
            if self.name.endswith('.xlsx'):
                return pd.read_excel(self.data)
            elif self.name.endswith('.csv'):
                return pd.read_csv(self.data,delimiter=",")
            else:
                msg="Not type support"
                return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        except:
            msg = "Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return Response({"messageError": msg})