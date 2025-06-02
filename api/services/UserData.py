import pandas as pd
from django.http import JsonResponse
from jinja2.utils import Joiner


class UserData:
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
                return JsonResponse(msg, status=404)
        except:
            msg = "Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return JsonResponse({"messageError": msg})
        finally:
            print("Success read file")
            pass
