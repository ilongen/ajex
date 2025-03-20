import pandas as pd
from django.http import HttpResponse
class userData():
    def fileWeb():
        print('Receive the web file')
    def dataFrame(args):
        try:
            if ".xlsx" in args:
                sheetMod=pd.read_excel(args)
                print(sheetMod)
                msg="Spreadsheet Sucess"
                return HttpResponse(msg)
            else:
                print(args)
                sheetMod=pd.read_csv(args)
                print(sheetMod)
                msg="Spreadsheet Sucess"
                return HttpResponse(msg)
        except:
            msg="Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent!"
            return HttpResponse(msg)