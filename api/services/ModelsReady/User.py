import pandas as pd
from rest_framework import status
from rest_framework.response import Response


"""
-> Classe usuário que fará input do seu dado para transformação, aqui pegará o nome e o arquivo para manipular
-> em outro local
"""

class User:


    def __init__(self, user_data_file,user_data_name):
        self.user_file = user_data_file
        self.name_file = user_data_name


    def get_data(self):
        file = self.user_file
        name_file = self.name_file
        try:
            if name_file.endswith('.xlsx'):
                sheet_received = pd.read_excel(file)
                return sheet_received
            elif name_file.endswith('.csv'):
                sheet_received = pd.read_csv(file,delimiter=",")
                return sheet_received
            else:
                msg="Not type support"
                return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        except:
            msg = "Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return Response({"messageError": msg})
        finally:
            pass
