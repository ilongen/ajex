import pandas as pd

class manipulationData:
    def __init__(self,df):
        self.df = pd.DataFrame(df) 
        self.n_row,self.n_columns = df.shape
        self.dictRemove=None
        self.countPorc_row=0
        self.porcColumn_min = self.n_columns*0.60 # %
    
    def dictIsNA(self):
        self.porcColumn_min
        self.n_row,self.n_columns
        for i in range(self.n_row):
            for j in range(self.n_columns):
                value=self.df.iloc[i,j]
                try:
                    if pd.isna(value)==True:
                        dictNA={"row":i,"column":j}
                        if dictNA["row"]==i:
                            countRow_na+=1
                            countPorc_row = countPorc_row + (countRow_na*0.60)
                            self.dictRemove=dictRemove = {"row":i}
                            return self.dictRemove
                        else:
                            countRow_na=0
                    else:
                        print("NOT NA")
                except:
                    print("NOT FUNCTION CODE")
    def deletCell(self,df):
        print(self.df)