import pandas as pd

class userData():

    def optionUserSelected(args,optionUser):
        if optionUser in args:
            sheetNew = pd.read_csv(args)
            return sheetNew
        elif optionUser in args:
            sheetNew = pd.read_excel(args)
            return sheetNew    
