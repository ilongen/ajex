import unittest
import pandas as pd
from EtlData.DataFrame import DataFrame

df = pd.read_excel(r'..\data_examples\data.xlsx')

test = DataFrame(
    df,
    opt_download='.json'
)
test.convert_to_long_text()

print(test)

