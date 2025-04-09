from django.shortcuts import render
from ajex.template.userData import userData
from ajex.template.manipulationData import manipulationData
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        print(typeSheet)
        
        sheetNew = userData.dataFrame(sheet,typeSheet)
        sheetManipulation = manipulationData.dictIsNA()
        print(sheetManipulation)
        return HttpResponse("Sucesso")
       
    return render(request,"index.html")

