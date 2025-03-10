import pandas as pd

class userData():

    def optionUserSelected(args,optionUser):
        if optionUser == ".csv":
            sheetNew = pd.read_csv(args)
            return sheetNew
        elif optionUser == ".xlsx":
            sheetNew = pd.read_excel(args)
            return sheetNew    
