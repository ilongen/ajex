from django.shortcuts import render
from ajex.template.inputData import inputData
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")
def formPost():
    data = inputData.sheet
    outputFile = data
    return HttpResponse("File: ",outputFile)