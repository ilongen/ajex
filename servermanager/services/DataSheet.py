import pandas as pd
from django.http import HttpResponse

"""
-> Classe usuário que fará input do seu dado para transformação, aqui pegará o nome e o arquivo para manipular
-> em outro local
"""

class DataSheet:

    def __init__(self, data_input):
        self.data = data_input

    def get_sheet(self):
        data = self.data
        return data
        

    def set_sheet(self,data_file):
        self.data = data_file
        return True
    
    def is_sheet(self):
        try:
            if self.data.name.endswith('.xlsx') or self.data.name.endswith('.xls'):
                return pd.read_excel(self.data)
            elif self.data.name.endswith('.csv'):
                return pd.read_csv(self.data,delimiter=",")
            else:
                msg="Not type support"
                return HttpResponse(msg)
        except:
            msg = "Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return HttpResponse(msg)