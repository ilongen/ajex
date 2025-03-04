from libs import *
<<<<<<< HEAD
class analystData():
=======
from inputData import inputData
class analystData():
    data:pd.DataFrame
>>>>>>> db3cde2 (msg: continue class and creating methods)
    """        rules:

        Rule 1: Lack of key information, 
        save backup of that line 
        and delete it in the spreadsheet that will 
        be sent to the end 
        user - Output Spreadsheet (Data Cleared) - Backup Spreadsheet (Missing Data) 
        
        Rule 2: Contain more than 30% NaN information, will be completely deleted line 
        
        Rule 3: Blank rows in the spreadsheet, delete completely.
    """

    def isFirstColumnNull(data):
        if data == "NaN":
            print("Test")
    def isContainMoreNan(data):
        print("Null")
    def BlankRows(data):
        print("YEs")