import pandas as pd
import numpy as np
from io import BytesIO

class DataFrame:
    def __init__(self, dataframe, opt_download):
        self.dataframe = dataframe
        self.opt_download = opt_download

    #TODO
    #tentando adicionar lógica de grupos de dados, a quantidade de coluna irá fazer o grupo de dados para salvar separado
    #e long text
    def convert_to_long_text(self):
        n_row,n_column = self.dataframe.shape

        lista_one=[]
        lista_two = []
        for i in range(n_column):
            for j in range(n_row):
                value = self.dataframe.iloc[j,i]
                lista_one.append(value)
                #if i <= n_column:
                #    lista_two.append(lista_one)
                #    lista_two.append("-")
                #else:
                #    lista_one.clear()
            return print(lista_one)
        return print("deu algum bug")


    # TODO
    # Executado no final depois de converter todos os dados estruturados e remapear
    def transform_to_download(self):
        if self.opt_download.endswith('.csv'):
            return BytesIO(self.dataframe.to_csv(index=False).encode('utf-8'))
        elif self.opt_download.endswith('.xlsx'):
            return BytesIO(self.dataframe.to_excel(index=False).encode('utf-8'))
        elif self.opt_download.endswith('.json'):
            return BytesIO(self.dataframe.to_json(orient='records').encode('utf-8'))
        else:
            return BytesIO('Tipo de arquivo não suportado'.encode('utf-8'))


df = pd.DataFrame(np.random.rand(100, 5), columns=['A', 'B', 'C', 'D', 'E'])
dados=DataFrame(df,opt_download='.xslx')
dados.convert_to_long_text()
