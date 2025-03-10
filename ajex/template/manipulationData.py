from userData import userData


class manipulationData():
    
    """        rules:

        Rule 1: Lack of key information, 
        save backup of that line 
        and delete it in the spreadsheet that will 
        be sent to the end 
        user - Output Spreadsheet (Data Cleared) - Backup Spreadsheet (Missing Data) 
        
        Rule 2: Contain more than 30% NaN information, will be completely deleted line 
        
        Rule 3: Blank rows in the spreadsheet, delete completely.
    """
    def dataExtrated():
        print("test")