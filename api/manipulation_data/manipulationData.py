import pandas as pd
from django.http import FileResponse
import io

class manipulationData:
    def __init__(self,df):
        self.df = pd.DataFrame(df)  
        self.n_row,self.n_columns = df.shape
        self.listDictNA = []
        self.listnotNA=[]
    
    def insight_dataframe(self):
        self.df
    
    def valueCell_isna(self):
        self.porcColumn_min = self.n_columns * 0.60
        self.n_row,self.n_columns
        print(self.df[:0])
        print(self.n_columns,self.n_row)
        for i in range(self.n_row):
            for j in range(self.n_columns):
                value=self.df.iloc[i,j]
                try:
                    if pd.isna(value):
                        self.listDictNA.append({"row": i, "column": j})
                except:
                    self.listnotNA.append({"row": i,"column": j,"value": value})
        return self.listDictNA
    def deletCell(self):
        self.porcColumn_min = self.n_columns * 0.95
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
