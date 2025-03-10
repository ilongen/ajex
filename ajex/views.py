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
        try:
            sheet = userData.optionUserSelected(sheet,optionSelect)
            data = manipulationData.dataExtrated(sheet)
            outputFile = outputData.sheet_newOutput(data)
            return outputFile
        except:
            print("Error post not send")
        print(sheet,optionSelect)
    return render(request,"outputFile.html")