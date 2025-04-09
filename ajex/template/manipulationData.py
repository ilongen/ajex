import pandas as pd

class manipulationData():
    df = pd.DataFrame() 
    n_row, n_columns = df.shape
    dictNA={}
    countPorc_row=0
    porcColumn_min = n_columns*0.60 # %
    def dictIsNA(df,n_row,n_columns):
        for i in range(n_row):
            for j in range(n_columns):
                value=df.iloc[i,j]
                try:
                    if pd.isna(value)==True:
                        dictNA={"row":i,"column":j}
                        if dictNA["row"]==i:
                            countRow_na+=1
                            countPorc_row = countPorc_row + (countRow_na*0.60)
                            dictRemove = {"row":i}
                            return dictRemove
                        else:
                            countRow_na=0
                    else:
                        print("NOT NA")
                except:
                    print("NOT FUNCTION CODE")
    def deletCell(df):
        print("null")