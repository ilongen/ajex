import pandas as pd
class manipulationData():
    def deletRow_isNull(param):
        n_row, n_columns = param.shape()
        dictList=[]
        porcColumn = n_columns*0.60 # %            
        for i in range(n_row):
            for j in range(n_columns):
                value=param.iloc[i,j]
                if pd.isna(value)==True:
                    dictData={
                        "row": i,
                        "column": j,
                        "value":value
                    }
                    dictList.append(dictData)
                    for z in range(len(dictList)):
                        print(dictList)
                        # Working for now on the part