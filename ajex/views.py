from django.shortcuts import render
from api.user_data.userData import userData
from api.manipulation_data.manipulationData import manipulationData
import pandas as pd
import io
import json
from django.http import FileResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

"""
    API: user_data
    modified: 22/04/2025 | 08:07 PM
    describe: This api works on receiving data and preparing for other api/backend services.

"""
def user_data(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        sheetNew = userData(sheet,typeSheet)
        sheetNew.to_json(sheetNew)
        return JsonResponse({"dataFrame":sheetNew})
    
"""
   
    API: manipulation_data
    modified: 22/04/2025 | 08:05 PM
    describe: This api works in the data manipulation photar, it will work with any data that is delivered it, is still being worked and increasing in dimension

"""
def manipulation_data(data_json):
        df = pd.DataFrame(data_json)
        sheetManipulation = manipulationData(df=df)
        sheetManipulation.valueCell_isna()
        dfOutput = sheetManipulation.deletCell()
        buffer = io.BytesIO()
        dfOutput.to_excel(excel_writer=buffer,index=True)
        buffer.seek(0)
        return FileResponse(buffer,as_attachment=True,filename=f"data.xlsx",content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")