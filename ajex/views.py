from django.shortcuts import render
from ajex.template.userData import get_dataFrame
from ajex.template.manipulationData import manipulationData
import pandas as pd
from django.http import HttpResponse
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
        sheetManipulation.deletCell()
        return HttpResponse("Sucesso")
       
    return render(request,"index.html")

