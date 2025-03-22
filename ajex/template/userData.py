import pandas as pd
from django.http import HttpResponse
class userData():
    def dataFrame(args,kwargs):
        try:
            if kwargs == ".xlsx":
                sheetMod=pd.read_excel(args)
                print(sheetMod)
                msg="Sucess"
                return HttpResponse(msg)
            else:
                sheetMod=pd.read_csv(args)
                print(sheetMod)
                msg="Sucess"
                return HttpResponse(msg)
        except:
            msg="Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return HttpResponse(msg)