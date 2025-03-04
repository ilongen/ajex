from django.shortcuts import render
from django.shortcuts import redirect
from ajex.template.classData import dataSheet
# Create your views here.

def index(request):
    return render(request,"index.html")
def formPost(request):
    data = request.POST.get("formPost")
    outputFile = data
    return outputFile