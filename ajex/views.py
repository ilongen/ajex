from django.shortcuts import render
from ajex.template.userData import userData
import json
# Create your views here.

def index(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=".xlsx"
        try:
            sheetNew = userData.dataFrame(sheet,typeSheet)
            #data = manipulationData.dataExtrated(sheet)
            #outputFile = outputData.sheet_newOutput(data)
            return sheetNew
        except:
            print("Error code")
    return render(request,"index.html")

