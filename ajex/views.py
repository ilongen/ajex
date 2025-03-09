from django.shortcuts import render
from ajex.template.inputData import inputData
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    return render(request,"index.html")

def fileOutput(request):
    if request.method == "POST":
        sheet = request.POST.get("fileSheet")
        optionSelect = request.POST.get("optionSelect")
        try:
            sheetValidated = inputData.validationInput(sheet)
            analData = inputData.optionUserSelected(optionSelect,sheetValidated)
        except:
            print("Error post not send")
        print(sheet,optionSelect)
    return render(request,"outputFile.html")