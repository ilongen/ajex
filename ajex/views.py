from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from ajex.template.userData import userData
# Create your views here.

def index(request):
    if request.method == "POST":
        sheet = request.POST.get("fileSheet")
        optionSelect = request.POST.get("optionSelect")
        try:
            sheetUpdateUserHair = userData.saveWebFile(sheet)
            sheetNew = userData.optionUserSelected(args=sheetUpdateUserHair,optionUser=optionSelect)
            #data = manipulationData.dataExtrated(sheet)
            #outputFile = outputData.sheet_newOutput(data)

            return sheetNew
        except:
            print("Error code")
    return render(request,"index.html")

def fileOutput(request):
    return render(request,"outputFile.html")