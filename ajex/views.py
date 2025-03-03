from django.shortcuts import render
from django.shortcuts import redirect
from template.collectData import collectData
from template.manipulationData import dataSheet
# Create your views here.

def index(request):
    return render(request,"index.html")
def formPost(request):
    inputFile = request.POST.get("formPost")
    data = collectData(inputFile)
    outputFile = dataSheet(data)
    return outputFile