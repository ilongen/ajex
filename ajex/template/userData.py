import pandas as pd
from django.http import HttpResponse
class userData():
    def fileWeb():
        print('Receive the web file')
    def dataFrame(args):
        try:
            if ".xlsx" in args:
                sheetMod=pd.read_excel(args)
                return sheetMod
            else:
                sheetMod=pd.read_csv(args)
                return sheetMod
        except ValueError as vError:
            print(f"Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! {vError}")
 