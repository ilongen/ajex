from django.shortcuts import render
from ajex.template.userData import userData
from ajex.template.manipulationData import manipulationData
import json
# Create your views here.

def index(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        print(typeSheet)
        try:
            sheetNew = userData.dataFrame(sheet,typeSheet)
            sheetManipulation = manipulationData.deletRow_isNull(sheetNew)
            #outputFile = outputData.sheet_newOutput(data)
            return sheetManipulation
        except:
            print("Error code")
    return render(request,"index.html")

