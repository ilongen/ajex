import pandas as pd

class manipulationData:
    def __init__(self,df):
        self.df = pd.DataFrame(df)  
        self.n_row,self.n_columns = df.shape
        self.listDictNA = []
    
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
                    print("NOT IS NA")
        return self.listDictNA
    def deletCell(self):
        self.porcColumn_min = self.n_columns * 0.60
        range_list = self.listDictNA
        for z in range(len(range_list)):
            print(range_list)
