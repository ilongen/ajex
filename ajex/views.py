from django.shortcuts import render
from api.user_data.userData import userData
from api.services.manipulationData import manipulationData
import io
from django.http import FileResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

"""
    API: user_data
    modified: 26/04/2025 | 09:42 PM
    describe: This api works on receiving data and preparing for other api/backend services.

"""
def user_data(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        sheetNew = userData(sheet,typeSheet)
        sheetManipulation=manipulation_data_local(param=sheetNew)
        return sheetManipulation
    
def manipulation_data_local(param):
        sheetManipulation = manipulationData(df=param)
        sheetManipulation.valueCell_isna()
        dfOutput = sheetManipulation.deletCell()
        buffer = io.BytesIO()
        dfOutput.to_excel(excel_writer=buffer,index=True)
        buffer.seek(0)
        return FileResponse(buffer,as_attachment=True,filename=f"data.xlsx",content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")