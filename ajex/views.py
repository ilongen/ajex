from django.shortcuts import render
from django.shortcuts import redirect
<<<<<<< HEAD
from ajex.template.classData import dataSheet
=======
from ajex.template.inputData import inputData
>>>>>>> db3cde2 (msg: continue class and creating methods)
# Create your views here.

def index(request):
    return render(request,"index.html")
def formPost(request):
<<<<<<< HEAD
    data = request.POST.get("formPost")
=======
    data = inputData
>>>>>>> db3cde2 (msg: continue class and creating methods)
    outputFile = data
    return outputFile