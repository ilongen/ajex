import pandas as pd
import numpy as py
import time
from django.http import HttpResponse
from django.http import request

class inputData():
    def validationInput(args):
        if type(args) == ".xlsx" or type(args) == ".csv":
            return args
        else:
            return HttpResponse("File not supported, try again!")

    def optionUserSelected(optionUser,sheetValidated):
        if optionUser is not None:
            if optionUser == ".csv":
                sheetNew = "converting"
            elif optionUser == ".xlsx":
                sheetNew = "converting"
                return sheetNew    
        else:
            msg="Error option is null"
            return HttpResponse(msg)
        
    sheet = "test"
    sheetValidated = validationInput(args=sheet)
    #nextStep = optionUserSelected(optionUser,sheetValidated)
