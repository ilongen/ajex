from django.shortcuts import render
from ajex.template.userData import userData
# Create your views here.

def index(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        try:
            sheetNew = userData.dataFrame(sheet)
            #data = manipulationData.dataExtrated(sheet)
            #outputFile = outputData.sheet_newOutput(data)
            print(sheetNew)
            return sheetNew
        except:
            print("Error code")
    return render(request,"index.html")

def fileOutput(request):
    return render(request,"outputFile.html")