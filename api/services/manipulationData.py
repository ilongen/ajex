import pandas as pd

class manipulationData:
    def __init__(self,df):
        self.df = pd.DataFrame(df)  
        self.n_row,self.n_columns = self.df.shape
        self.listDictNA = []
        self.listnotNA=[]
        self.list_rowExcept=[]

    def valueCell_isna(self):
        self.porcColumn_min = self.n_columns * 0.60
        self.n_row,self.n_columns
        for i in range(self.n_row):
            for j in range(self.n_columns):
                value=self.df.iloc[i,j]
                try:
                    if pd.isna(value):
                        self.listDictNA.append({"row": i, "column": j})
                        if i not in self.list_rowExcept:
                            self.list_rowExcept.append(i)
                except:
                    self.listnotNA.append({"row": i,"column": j,"value": value})
        
        return self.listDictNA
    
    def deletCell(self):
        self.porcColumn_min = self.n_columns * 0.02
        countRow=0
        row_now = None
        self.rowDelet = []
        for item in self.listDictNA:
            row=item["row"]
            if row != row_now:
                row_now=row
                countRow=0
            countRow +=1
            if countRow >= self.porcColumn_min and row not in self.rowDelet:
                self.rowDelet.append(row)
        self.df.drop(index=self.rowDelet,inplace=True)
        return self.df
    
    def dataframe_expection(self):
        valid_indice = [i for i in self.list_rowExcept if i < len(self.df)]
        df_backup = self.df.iloc[valid_indice]
        return df_backup