from libs import *
from django.http import request
from django.http import HttpResponse

class inputData():
    def validationInput(sheet:pd.DataFrame):
        if type(sheet) == ".xlsx" or type(sheet) == ".csv":
            return sheet
        else:
            return HttpResponse("File not supported, try again!")
    def convertInput(sheet:pd.DataFrame):
        print("Create options .csv or .xlsx")
    def optionUserSelected(optionUser,sheetValidated):
        usingFunction=inputData
        if optionUser is not None:
            if optionUser is ".csv":
                sheetNew = usingFunction.convertInput(sheetValidated)
            elif optionUser is ".xlsx":
                sheetNew = usingFunction.convertInput(sheetValidated)
                return sheetNew    

    sheet = request.POST.get("formPost")
    date:time
    optionUser:str
    sheetValidated = validationInput(sheet)
    nextStep = optionUserSelected(optionUser,sheetValidated)
