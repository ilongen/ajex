import pandas as pd
class manipulationData():
    def deletRow_isNull(param):
        n_row, n_columns = param.shape()
        dictNA={}
        porcColumn_min = n_columns*0.60 # %
        countColumn_NA=0            
        for i in range(n_row):
            for j in range(n_columns):
                value=param.iloc[i,j]
                try:
                    if pd.isna(value)==True:
                        dictNA={"row":i,"column":j,"value":value}
                        if dictNA['row'] == i and dictNA["column"] != 0:
                            countColumn_NA+=1
                        else:
                            return "Error server count(column)"
                    else:
                        return None
                except:
                    print("Value Not  NA")        