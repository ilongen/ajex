import pandas as pd
import numpy as np
from io import BytesIO

class DataFrame:
    def __init__(self, dataframe, opt_download):
        self.dataframe = dataframe
        self.opt_download = opt_download

    def convert_to_list(self):

        # TODO
        # VALIDAR SE ESSE ESTILO DE AGRUPAMENTO É IDEAL
        # POIS ELE ESTÁ AGRUPANDO DE LINHA PARA COLUNA, ESTÁ VALIDANDO A LINHA ATÉ A ULTIMA COLUNA
        # E AGRUPANDO A INFORMAÇÃO.

        n_row,n_column = self.dataframe.shape
        data_sequence:list[str] = []
        data_groups:list[list[str]] = []

        try:
            for i in range(n_row):
                for j in range(n_column):

                    # PEGO O VALOR DA LINHA
                    value:str = self.dataframe.iloc[i,j]

                    # ADICIONO ESSE VALOR NUMA LISTA PARA SEQUÊNCIA
                    data_sequence.append(value)

                    # APÓS ISTO, VALIDO SE A POSIÇÃO FOR IGUAL O NUMERO DA COLUNA
                    # IDEIA É SE A LISTA CONTER O NUMERO IGUAL DA COLUNA, COLOQUE EM UMA LISTA SEPARADA E ADICIONE -
                    # PARA FAZER SEPARAÇÃO

                    if len(data_sequence) == n_column:
                        data_groups.append(data_sequence)
                        data_groups.append(['-'])
                        data_sequence = []
                    else:
                        pass
                return print(data_groups)

        except Exception as e:
            return print(f'Erro devido à {e}')


    # TODO
    # Executado no final depois de converter todos os dados estruturados e remapear
    def transform_to_download(self):
        try:
            if self.opt_download.endswith('.csv'):
                return BytesIO(self.dataframe.to_csv(index=False).encode('utf-8'))
            elif self.opt_download.endswith('.xlsx'):
                return BytesIO(self.dataframe.to_excel(index=False).encode('utf-8'))
            elif self.opt_download.endswith('.json'):
                return BytesIO(self.dataframe.to_json(orient='records').encode('utf-8'))
            else:
                return BytesIO('Tipo de arquivo não suportado'.encode('utf-8'))
        except Exception as e:
            print(f'Erro devido {e}')


df = pd.DataFrame(np.random.rand(100, 5), columns=['A', 'B', 'C', 'D', 'E'])
dados=DataFrame(df,opt_download='.xslx')
dados.convert_to_list()
print(df)