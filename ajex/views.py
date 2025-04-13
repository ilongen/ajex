from django.shortcuts import render
from ajex.template.userData import get_dataFrame
from ajex.template.manipulationData import manipulationData
import pandas as pd
from django.http import HttpResponse
import io
from django.http import FileResponse
import json
# Create your views here.

def index(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        print(typeSheet)
        
        sheetNew = get_dataFrame(sheet,typeSheet)
        df = pd.DataFrame(sheetNew)
        sheetManipulation = manipulationData(df=df)
        sheetManipulation.valueCell_isna()
        dfOutput = sheetManipulation.deletCell()
        buffer = io.BytesIO()
        dfOutput.to_excel(excel_writer=buffer,index=False,sheet_name="sheetNew")
        buffer.seek(0)
        return FileResponse(buffer,as_attachment=True,filename="data.xlsx",content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    return render(request,"index.html")

