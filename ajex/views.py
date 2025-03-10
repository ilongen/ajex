from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from ajex.template.outputData import outputData
from ajex.template.userData import userData
from ajex.template.manipulationData import manipulationData

# Create your views here.

def index(request):
    
    return render(request,"index.html")

def fileOutput(request):
    if request.method == "POST":
        sheet = request.POST.get("fileSheet")
        optionSelect = request.POST.get("optionSelect")
        print(sheet,optionSelect,"- Debug one")
        try:
            print(sheet,optionSelect,"- Debug two")
            sheetNew = userData.optionUserSelected(args=sheet,optionUser=optionSelect)
            #data = manipulationData.dataExtrated(sheet)
            #outputFile = outputData.sheet_newOutput(data)
            print(sheetNew,"- Debug three")
            return sheetNew
        except:
            print("Error code")
    return render(request,"outputFile.html")