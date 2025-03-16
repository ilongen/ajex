import pandas as pd


class userData():
    def  saveWebFile(args):
        print("save file from web")


    def optionUserSelected(args,optionUser):
        print("debug one - ",args,optionUser)
        try:
            if optionUser is ".xlsx":
                sheetMod=pd.read_excel('')
            else:
                sheetMod=pd.read_csv('')
            return sheetMod
        except ValueError as vError:
            print(f"Is error: {vError}")
 