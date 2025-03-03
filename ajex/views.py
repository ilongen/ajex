from django.shortcuts import render
from django.shortcuts import redirect
from ajex.template.collectData import collectData
from ajex.template.classData import dataSheet
# Create your views here.

def index(request):
    return render(request,"index.html")
def formPost(request):
    inputFile = request.POST.get("formPost")
    data = collectData(inputFile)
    outputFile = dataSheet(data)
    return outputFile