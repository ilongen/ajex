import pandas as pd

class userData():

    def optionUserSelected(optionUser,sheetValidated):
        if optionUser == ".csv":
            sheetNew = pd.read_csv(sheetValidated)
            return sheetNew
        elif optionUser == ".xlsx":
            sheetNew = pd.read_excel(sheetValidated)
            return sheetNew    
