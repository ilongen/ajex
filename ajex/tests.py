from django.test import TestCase

import pandas as pd


sheet = pd.read_excel(r'/home/iagolongen/Documents/39.268.3960001-98/PLANILHA_ESTOQUE_COMPLETO_LJ.xlsx')
n_row, n_columns = sheet.shape
dictNA={}
porcColumn_min = n_columns*0.60 # %            
for i in range(n_row):
    for j in range(n_columns):
        value=sheet.iloc[i,j]
        if pd.isna(value)==True:
           dictNA={"row":i,"column":j,"value":value}
           if dictNA['row'] == i:
                print(dictNA)