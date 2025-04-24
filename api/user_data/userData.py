import pandas as pd
from django.http import HttpResponse,JsonResponse

def userData(args,kwargs):
    try:
        if ".xlsx" in kwargs:
            sheetReceived=pd.read_excel(args)
            sheet_json= sheetReceived.to_json(orient='records')
            return JsonResponse(sheet_json,safe=False)
        else:
            sheetReceived=pd.read_csv(args)
            sheet_json = sheetReceived.to_json(orient='records')
            return JsonResponse(sheet_json,safe=False)
    except:
        msg="Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
        return JsonResponse({"messageError":msg})

                    