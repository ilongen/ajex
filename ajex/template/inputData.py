from libs import *
class inputData():
    sheet = pd.DataFrame()
    date:time
    optionUser:str

    def validationInput(sheet:pd.DataFrame):
        print("Test")

    def convertInput(sheet:pd.DataFrame):
        print("Create options .csv or .xlsx")

    #sheet = requests.POST.get("formPost")
    date:time
    optionUser:str


    def validationInput(sheet:pd.DataFrame):
        print("Test")
        return sheet

    def convertInput(sheet:pd.DataFrame):
        print("Create options .csv or .xlsx")
        return sheet
    sheet = validationInput(sheet)
    sheetNew = convertInput(sheet)
