import pandas as pd


class userData():
    def convertSheet(args):
        if args is ".xlsx":
            sheetCsv_orXlsx=[]
            sheetCsv = pd.read_excel()

    def optionUserSelected(args,optionUser):
        if any(optionUser) in args:
            sheetRead = pd.read_csv(args)
            return sheetRead
        elif any(optionUser) in args:
            sheetRead = pd.read_excel(args)
            return sheetRead    
