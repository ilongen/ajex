import pandas as pd

class manipulationData():
    def dictIsNA(param):
        df = pd.DataFrame(param)
        n_row, n_columns = df.shape
        dictNA={}
        porcColumn_min = n_columns*0.60 # %
        for i in range(n_row):
            for j in range(n_columns):
                value=df.iloc[i,j]
                try:
                    if pd.isna(value)==True:
                        dictNA={"row":i,"column":j}
                        if dictNA["row"]==i:
                            countRow_na+=1
                        else:
                            countRow_na=0
                    else:
                        print("NOT NA")
                except:
                    print("NOT FUNCTION CODE")

