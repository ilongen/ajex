import pandas as pd
def collectData(file):
    data = pd.read_excel(file)
    return data
