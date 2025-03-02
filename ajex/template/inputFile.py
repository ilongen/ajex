import pandas as pd
from tkinter import filedialog
from collectData import collectData
def inputFile():
    filename=filedialog.askopenfilename()
    if filename:
        data = collectData(filename)
                                
                    
    