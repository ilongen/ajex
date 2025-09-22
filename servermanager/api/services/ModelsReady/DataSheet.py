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
        check_data = self.data
        check_name = self.name
        try:
            if check_name.endswith('.xlsx'):
                is_sheet = pd.read_excel(check_data)
                self.data = is_sheet
                return self.data
            elif check_name.endswith('.csv'):
                is_sheet = pd.read_csv(check_data,delimiter=",")
                self.data = is_sheet
                return self.data
            else:
                msg="Not type support"
                return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        except:
            msg = "Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return Response({"messageError": msg})
        finally:
            pass

    def set_data(self,data_file,name_file):
        self.data = data_file
        self.name = name_file
        return self.data,self.name_data
    