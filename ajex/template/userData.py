import pandas as pd
from django.http import HttpResponse
class userData():
    def dataFrame(args,kwargs):
        try:
            if ".xlsx" in kwargs:
                sheetReceived=pd.read_excel(args)
                print(sheetReceived)
                return HttpResponse(sheetReceived)
            else:
                sheetReceived=pd.read_csv(args)
                print(sheetReceived)
                return HttpResponse(sheetReceived)
        except:
            msg="Spreadsheet was not transformed into a dataframe, check the spreadsheet you sent! Intern Server Erro"
            return HttpResponse(msg)
    def manipulationData(param):
        n_row, n_columns = param.shape()
        qtdNA_row=0
        listIndex = []
        for i in range(n_row):
            for j in range(n_columns):
                value=param.iloc[i,j]
                if pd.isna(value)==True:
                    qtdNA_row+=1
                    listIndex.append(i,j)
                    print(listIndex)

