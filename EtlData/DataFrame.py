import pandas as pd
import numpy as np
from io import StringIO,BytesIO
class DataFrame:
    def __init__(self, dataframe,opt_download):
        self.dataframe = dataframe
        self.opt_download = opt_download

    def convert_to_long_text(self):
        df = self.dataframe

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