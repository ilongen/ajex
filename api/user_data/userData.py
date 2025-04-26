import pandas as pd
from django.http import HttpResponse,JsonResponse

def userData(args,kwargs):
    try:
        if ".xlsx" in kwargs:
            sheetReceived=pd.read_excel(args)
            return sheetReceived
        else:
            sheetReceived=pd.read_csv(args)
            return sheetReceived
    except:
        msg="Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
        return HttpResponse({"messageError":msg})

                    